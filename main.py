import requests
import itertools


def decoder():
    response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt')
    text = response.content.decode('cp1251')
    with open('russian_decoding.txt', 'wb') as ru:
        ru.write(text.encode('utf-8'))


def search_words(list_letters=["а", "с", "п", "у", "р"]):
    words_number = 0
    possible_words_list = []
    search_words_list = []
    for item in list(itertools.permutations(list_letters)):
        possible_words_list.append(''.join(item))
    print(possible_words_list)


if __name__ == '__main__':
    # decoder()
    search_words()