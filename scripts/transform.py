# scripts/transform.py

import json

def transform(data):
    # Simplify the data structure
    transformed_data = []
    for entry in data['entries']:
        transformed_data.append({
            'API': entry['API'],
            'Description': entry['Description'],
            'Link': entry['Link'],
            'Category': entry['Category']
        })
    return transformed_data

if __name__ == "__main__":
    with open("../data/raw_data.json", "r") as f:
        data = json.load(f)
    transformed_data = transform(data)
    with open("../data/transformed_data.json", "w") as f:
        json.dump(transformed_data, f)
    print("Data transformed successfully.")
