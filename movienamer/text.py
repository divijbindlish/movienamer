'''
movienamer.text

Generate different text for CLI.
'''

import os
import dateutil.parser as dup


def user_options():
    return ('Enter option: Return for default, \'s\' to skip, \'q\' to quit%s'
            % (os.linesep))


def init_text(filename):
    return 'Processing file: %s%s' % (filename, os.linesep)


def confirmation_text(results):
    prompt = ['Found following results:']

    for i, result in enumerate(results):
        prompt.append(('%d: %s [%d]'
                       % (i+1, result['title'],
                          dup.parse(result['release_date']))))

    return os.linesep.join(prompt)


def wrong_input():
    prompt = ['', 'Sorry, I couldn\'t understand what you meant.']
    prompt.append(user_options())

    return os.linesep.join(prompt)

