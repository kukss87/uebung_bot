from pprint import pprint

'''Заполните пропуски, используя правильную форму Perfekt:
Beispiel: Ich __________ (gehen) gestern ins Kino.
Antwort: Ich bin gestern ins Kino gegangen.'''


def process_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        split_text = text.split('\n\n')
        replaced_text = [item.replace('Antwort: ', '') for item in split_text]
        fin = [tuple(item.split('\n')) for item in replaced_text]
    return fin


# print(process_data('perfekt.txt'))
# create_new_file('perfekt2.txt')
