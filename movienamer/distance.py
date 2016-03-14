import re


def _levenshtein(s1, s2):
    '''Compute and levenshtein distance between two strings.'''
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def compute_distance(query, result):
    '''
    Compute and return levenshtein distance between query or target movie
    and fetched result.
    '''
    query = re.sub('[^a-z0-9]', '', query.lower())
    result = re.sub('[^a-z0-9]', '', result.lower())

    return levenshtein(query, result)
