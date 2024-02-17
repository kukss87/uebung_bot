from pprint import pprint


def process_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        split_text = text.split('\n\n')
        replaced_text = [item.replace('Antwort: ', '') for item in split_text]
        clean_data = [tuple(item.split('\n')) for item in replaced_text]
    return clean_data


# pprint(process_data('perfekt.txt'))
spisok = process_data('perfekt.txt')

for i in spisok:
    print(len(i))


