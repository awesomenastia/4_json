import json


def load_data(filepath):
    with open(filepath, "r") as file_json:
        return json.load(file_json)


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4))


if __name__ == '__main__':
    json_content = load_data(filepath=input('Enter filepath: '))
    pretty_print_json(json_content)
