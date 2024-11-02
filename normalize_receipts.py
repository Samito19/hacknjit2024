import os


keywords = ["Total Price", "Date/Time", "// VAT"]
for filename in os.listdir("sorted_data/6352/receipts"):
    with open("sorted_data/6352/receipts/" + filename, 'r') as f:
        i = 0
        for line in f:
            for keyword in keywords:
                if keyword in line:
                    print(line)
    print("-------------------------")
