

'''Antonymize transforms all words of a text into their antonysms.
May not work in English'''

import requests
from bs4 import BeautifulSoup

def antonymize_text(text):
    antonymized_text = []
    list_of_words = text.split()
    for index, elem in enumerate(list_of_words):
        if ',' in elem or '.' in elem or '!' in elem or '?' in elem:
            list_of_words[index] = elem[-1]
        list_of_words[index] = elem.lower()
    for word in list_of_words:
        antonymized_text.append(parser_wiktionary(word))
    return antonymized_text


def parser_wiktionary(word):
    url = "https://ru.wiktionary.org/wiki/" + word
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, features="html.parser")
    antonyms = (soup.find(id='Антонимы'))
    try:
        if (
            antonyms is None
            or antonyms.parent.find_next_sibling('ol').contents[0].contents == []
            or antonyms.parent.find_next_sibling('ol').contents[0].contents[0] in ('?', '—', '-')
        ):
            return word
        return antonyms.parent.find_next_sibling('ol').contents[0].contents[0].contents[0]
    except AttributeError:
        pass
    var_to_short_the_line = antonyms.parent.find_next_sibling('div').contents[0].contents[0]
    if (
        antonyms is None
        or var_to_short_the_line.find_next_sibling('li').contents[2].contents == []
        or var_to_short_the_line.find_next_sibling('li').contents[2].contents[0] in {'?', '—', '-'}
    ):
        return word

    return var_to_short_the_line.find_next_sibling('li').contents[2].contents[0].contents[0]

