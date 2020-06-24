import argparse
import json


def cleanup(text):
    text_parts = text.replace('(forces new resource)', '').replace('\\"', '"').replace('\n', '').split('=>')
    return (part.lstrip('  "').rstrip(' "') for part in text_parts)


def extract_key(obj):
    return obj['name']


if __name__ == '__main__':
    ALLOWED_KEYS = {'environment', 'secrets'}
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()

    with open(args.file, 'r') as file:
        cleaned_parts = cleanup(''.join(file.readlines()))

    parts = [json.loads(cleaned_part)[0] for cleaned_part in cleaned_parts]

    for part in parts:
        del_keys = [key for key in part.keys() if key not in ALLOWED_KEYS]
        for key in del_keys:
            del part[key]
        part['environment'].sort(key=extract_key)
        part['secrets'].sort(key=extract_key)

    with open(f'{args.file}_old.json', 'w') as file:
        file.write(json.dumps(parts[0], indent='\t'))

    with open(f'{args.file}_new.json', 'w') as file:
        file.write(json.dumps(parts[1], indent='\t'))
