import argparse
import json

from sys import argv

def main(argv):
    if "--" not in argv:
        argv = [] # as if no args are passed
    else:
        argv = argv[argv.index("--") + 1:]

    parser = argparse.ArgumentParser(description='Simple tool to parse user JSON to list of user emails')
    parser.add_argument('-i', '--input', required=True, help='user JSON file')
    parser.add_argument('-o', '--output', required=True, help='TXT file listing user emails')
    args = parser.parse_args(argv)

    # read file
    data = json.load(open(args.input))
    users = data['users']
    emails = [user['text'] for user in users]
    with open(args.output, "w") as txt_file:
        for user in data['users']:
            user_text = user['text']

            if '(' in user_text and ')' in user_text:
                # Name (email)
                name = user_text.rpartition('(')[0].strip()
                email = user_text.rpartition('(')[-1].strip(')')
                line = f'{email} {name}'
            else:
                # Email
                line = user_text

            txt_file.write(line + "\n")

if __name__ == '__main__':
    main(argv)