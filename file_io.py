import json
import csv


def read_csv(file):
    with open(file, "r") as f:
        reader = csv.reader(f)
        data = [line for line in reader]
    return data


def read_json(file):
    with open(file, "r") as f:
        data = json.load(f)
        data = json.dumps(data, indent=2)
    return data


def read_txt(file):
    with open(file, "r") as f:
        data = f.read()
    return data


csv_path = "./static/booklist.csv"
print(read_csv(csv_path))

json_path = "./static/data.json"
print(read_json(json_path))

txt_path = "./static/text.txt"
print(read_txt(txt_path))
