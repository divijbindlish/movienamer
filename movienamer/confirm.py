import os

# The number of results to display at one time
N = 5


def _confirmation_text_single(result, filename, extension):
    prompt = ['Processing file: %s' % (filename + extension)]

    if result['year'] is not None:
        prompt.append('Detected movie: %s [%s]'
                      % (result['title'], result['year']))
    else:
        prompt.append('Detected movie: %s' % result['title'])

    prompt = prompt + ['', 'Rename?', '([y]/n/q)', '']

    return '\n'.join(prompt)


def _confirm_single(result, filename, extension):
    input_to_action_map = {'y': 'YES', 'n': 'SKIP', 'q': 'QUIT'}

    text = _confirmation_text_single(result, filename, extension)
    confirmation = raw_input(text.encode('utf-8'))
    if confirmation == '':
        confirmation = 'y'

    while confirmation not in input_to_action_map.keys():
        confirmation = raw_input(
            '\n'.join(['Rename?', '([y]/n/q)', '']).encode('utf-8')).lower()
        if confirmation == '':
            confirmation = 'y'

    action = input_to_action_map[confirmation]
    return action


def _final_line_multiple(length, start):
    final_line = 'Enter option (return for default, '
    if length - start > N:
        final_line += '\'m\' for more, '
    final_line += '\'s\' to skip, \'q\' to quit):\n'

    return final_line


def _combine_multiple_options(results, start):
    prompt = []

    if results[start]['year'] is not None:
        prompt.append('%d: %s [%s] (default)'
                      % (start+1, results[start]['title'],
                         results[start]['year']))
    else:
        prompt.append('%d: %s (default)' % (start+1, results[start]['title']))

    for i, result in enumerate(results[start+1:start+N]):
        if result['year'] is None:
            prompt.append('%d: %s' % (start+i+2, result['title']))
            continue

        prompt.append('%d: %s [%s]'
                      % (start+i+2, result['title'], result['year']))

    prompt += [
        '',
        _final_line_multiple(len(results), start)
    ]

    return prompt


def _confirmation_text_multiple(results, filename, extension):
    prompt = [
        'Processing file: %s' % (filename + extension),
        'Detected multiple movies:',
        ''
    ]

    prompt += _combine_multiple_options(results, 0)
    return '\n'.join(prompt)


def _confirm_multiple(results, start, filename, extension):
    if len(results) - start > N:
        actions = [str(i) for i in range(1, start+N+1)] + ['s', 'q', 'm']
    else:
        actions = [str(i) for i in range(1, len(results)+1)] + ['s', 'q']

    if start == 0:
        text = '\n'.join(
            [
                'Processing file: %s' % (filename + extension),
                'Detected multiple movies:',
                ''
            ] + _combine_multiple_options(results, 0)
        )
    else:
        text = '\n'.join(_combine_multiple_options(results, start))

    confirmation = raw_input(text.encode('utf-8')).lower()
    if confirmation == '':
        confirmation = str(start+1)

    if confirmation == 'm' and 'm' in actions:
        return _confirm_multiple(results, start+N, filename, extension)

    while confirmation not in actions:
        confirmation = raw_input(
            _final_line_multiple(len(results), start).encode('utf-8'))
        if confirmation == '':
            confirmation = str(start+1)

        if confirmation == 'm' and 'm' in actions:
            return _confirm_multiple(results, start+N, filename, extension)

    if confirmation.isdigit():
        return confirmation
    elif confirmation == 's':
        return 'SKIP'
    elif confirmation == 'q':
        return 'QUIT'
    else:
        raise Exception


def confirm(results, filename, extension):
    if len(results) == 1:
        action = _confirm_single(results[0], filename, extension)
        if action == 'YES':
            return '0'
        return action

    else:
        return _confirm_multiple(results, 0, filename, extension)
