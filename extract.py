import os, json

def extract_receipts_data():
    keywords = ["Total Price", "Date/Time", "// VAT"]
    receipt_num = 0
    receipt = {"receipt_number": receipt_num, "total_price": 0.0, "date_time": "", "orders": []}
    receipts = []
    for filename in os.listdir("sorted_data/6352/receipts"):
        with open("sorted_data/6352/receipts/" + filename, 'r') as f:
            for line in f:
                if keywords[0] in line:
                    tokens = line.split(" ")
                    receipt["total_price"] = float(tokens[2])
                elif keywords[1] in line:
                    tokens = line.split(" ")
                    date = tokens[2].replace("(", "")
                    date = date.replace(")", "")
                    receipt["date_time"] = date
                elif keywords[2] in line:
                    tokens = line.split("//") 
                    product = tokens[0].split("-")
                    order = {"quantity": int(product[0].replace(" ", "")), "name": product[1]}
                    receipt["orders"].append(order)
        receipts.append(receipt)
        receipt_num += 1

    return json.dumps(receipts)

