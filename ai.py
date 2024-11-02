from openai import OpenAI
from openai import OpenAI
from pathlib import Path
from openai import OpenAI
from recorder import record_audio
from player import play_ai_response
import os, json, subprocess

client = OpenAI()

record_audio()

audio_file= open("output.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)

transcibed_prompt = transcription.text

print("You asked: " + transcibed_prompt)

def generate_ai_response(summary):
    completion = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": """You are an agent that reads receipts produced by a business like a restaurant, 
            and gives excellent business insights. Don't be general, give thorough responses with actionable suggestions and metrics of sales. 
            You also make sure you give back a JSON object in this form: 
            Anytime you see a line in this format "x - Product Name", remember that x is the quantity.
            {"text_summary": "a text to be read through speaker", "streamlit_code": "here you will generate python code using the streamlit library to show relevant graphs and charts. Use any extra libraries you may need. Make sure you add the text_summary transcribed at the top of the streamlit app. Please write python code that will be saved to a file! no \\n characters"} 
            """},
            {
                "role": "user",
                "content": transcibed_prompt + summary        }
        ]
    )
    
    ai_response = completion.choices[0].message.content
    if ai_response:
        ai_response_json = json.loads(ai_response)
        text_summary = ai_response_json["text_summary"]
        streamlit_response = ai_response_json["streamlit_code"]
        with open("streamlit_response.py", "w") as text_file:
            text_file.write(streamlit_response)
        print(json.dumps(ai_response_json, indent=4))
        speech_file_path = Path(__file__).parent / "speech.mp3"
        response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text_summary
        )

        response.stream_to_file(speech_file_path)
        play_ai_response()
        

keywords = ["Total Price", "Date/Time", "// VAT"]
summary = ""
receipt_num = 0 
for filename in os.listdir("sorted_data/6352/receipts"):
    with open("sorted_data/6352/receipts/" + filename, 'r') as f:
        summary += f"Receipt number {receipt_num}\n"
        for line in f:
            for keyword in keywords:
                if keyword in line:
                    summary += line + "\n"
    summary += "-----------------------------------------\n"
    receipt_num += 1

generate_ai_response(summary)
