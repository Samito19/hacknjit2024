from openai import OpenAI
import os

client = OpenAI()

def generate_ai_response(summary):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You are an agent that reads receipts produced by a business like a restaurant, and gives excellent business insights."},
            {
                "role": "user",
                "content": "Give me a summary of this in JSON, and generate a csv file that can be displayed in to a relevant graph\n" + summary        }
        ]
    )

    print(completion.choices[0].message.content)
    

keywords = ["Total Price", "Date/Time", "// VAT"]
summary = ""
for filename in os.listdir("sorted_data/6352/receipts"):
    with open("sorted_data/6352/receipts/" + filename, 'r') as f:
        for line in f:
            for keyword in keywords:
                if keyword in line:
                    summary += line + "\n"
    summary += "-----------------------------------------\n"

