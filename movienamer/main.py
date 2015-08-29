import argparse
import os

from identify import identify
from confirm import confirm


def movienamer(movie, options=dict()):
    directory = '/'.join(movie.split('/')[:-1])
    filename, extension = os.path.splitext(os.path.basename(movie))

    results = identify(filename, directory)
    if len(results) == 0:
        raise Exception

    action = confirm(results, filename, extension)

    if action == 'SKIP':
        print 'Skipping movie file\n'
    elif action == 'QUIT':
        print 'Exiting movienamer'
    else:
        i = int(action)
        result = results[i-1]

        if directory == '':
            directory = '.'

        dest = (directory + '/' +
                result['title'] +
                ' [' + result['year'] + ']' +
                extension)
        # os.rename(movie, dest)


def main():
    parser = argparse.ArgumentParser(
        description='Command-line utlity to properly organize movies.'
    )

    parser.add_argument('movies', nargs='+', help='movie files to rename')

    args = vars(parser.parse_args())

    if len(args) == 0:
        raise Exception

    for movie in args['movies']:
        movienamer(movie)
