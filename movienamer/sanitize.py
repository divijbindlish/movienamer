import re

from .keywords import *


def _replace_roman_numerals(name):
    if name is None or name == '':
        raise Exception

    words = name.split(' ')
    for i, word in enumerate(words):
        if i == 0:
            continue

        if i == len(words) - 1 and word == 'i':
            words[i] = str(1)
            return ' '.join(words)

        if word in roman_numerals:
            words[i] = str(roman_numerals.index(word) + 2)
            return ' '.join(words)

    return name


def _get_year(name):
    if name is None or name == '':
        raise Exception

    if len(name.split(' ')) == 1:
        return (name, None)

    for pattern in year_extract_patterns:
        match = re.match(pattern, name)
        if match is not None:
            year = match.group('year')
            if int(year) >= 1900:
                return (str(match.group('name')), int(year))

    return (name, None)


def sanitize(name):
    if name is None or name == '':
        raise Exception

    for keyword in case_sensitive_keywords:
        if keyword in name:
            name = name.replace(keyword, '')

    name = name.lower()
    for keyword in regex_keywords:
        name = re.sub(keyword, '', name)

    for keyword in print_keywords:
        if keyword in name:
            name = name.replace(keyword, '')

    for keyword in case_insensitive_keywords:
        if keyword in name:
            name = name.replace(keyword, '')

    name = _replace_roman_numerals(name.strip())
    name = re.sub('[\.\-_\[\(\)\]]', ' ', name)
    name = re.sub(' +', ' ', name)
    name = name.strip()

    return _get_year(name)
