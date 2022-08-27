import requests
import itertools


def decoder():
    response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt')
    text = response.content.decode('cp1251')
    with open('russian_decoding.txt', 'wb') as ru:
        ru.write(text.encode('utf-8'))


def search_words(list_letters=["а", "в", "т", "а"]):
    words_number = 0
    possible_words_list = []
    search_words_list = []

    for item in list(itertools.permutations(list_letters)):
        possible_words_list.append(''.join(item))
        possible_words_list = list(set(possible_words_list))

    print(possible_words_list)

    for word in possible_words_list:
        print(f'//////    word:  {word}    searching  ///////')
        with open('russian_decoding.txt', 'r', encoding='utf-8') as file:
            rus_words = file.readlines()
            if word in [item.strip() for item in rus_words]:
                words_number += 1
                print(f'---- Word {word} - success! Number: {words_number} ---------')
                if word not in search_words_list:
                    search_words_list.append(word)

    if search_words_list == []:
        print('The result of the search is negative! There is no one word!')
    else:
        print(f'The result of the search is positive! The list of searching words is:\n{search_words_list}.')


if __name__ == '__main__':
    # decoder()
    search_words()