import requests
import json

url = 'https://raw.githubusercontent.com/Botspot/pi-apps-analytics/main/clicklist'

response = requests.get(url)
data = response.text.splitlines()

parsed_data = {}
for line in data:
    parts = line.split(' ', 1)
    if len(parts) == 2:
        number, name = parts
        name = name.strip()
        if name.lower() == 'template':
            continue
        parsed_data[name] = int(number)

# Sort the parsed data by the number values in descending order
sorted_data = {k: v for k, v in sorted(parsed_data.items(), key=lambda item: item[1], reverse=True)}

# Convert the sorted data to JSON
json_data = json.dumps(sorted_data, indent=2)
print(json_data)
