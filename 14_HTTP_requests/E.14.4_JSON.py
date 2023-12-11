import json

def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def process_colors(colors):
    processed_colors = []
    for color in colors:
        processed_color = {
            "color": color["color"],
            "rgb": ", ".join(str(value) for value in color["code"]["rgba"][:3]),
            "hex": color["code"]["hex"]
        }
        processed_colors.append(processed_color)
    return processed_colors

filename = "failo_pavadinimas.json"

try:
    data = read_json_file(filename)
    processed_data = process_colors(data["colors"])
    output = {
        "colors": processed_data
    }

    output_filename = "rezultatas.json"
    with open(output_filename, 'w') as output_file:
        json.dump(output, output_file, indent=2)
    print(f"Saved in '{output_filename}'.")
except FileNotFoundError:
    print(f"File '{filename}' not found.")
except json.JSONDecodeError:
    print(f"File format '{filename}' not JSON.")

