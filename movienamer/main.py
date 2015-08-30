import argparse
import fnmatch
import os
import sys

from identify import identify
from confirm import confirm
from keywords import subtitle_extensions, video_extensions

def movienamer(movie):
    directory = '/'.join(movie.split('/')[:-1])
    filename, extension = os.path.splitext(os.path.basename(movie))

    results = identify(filename, directory)
    if len(results) == 0:
        print 'No results found. Skipping movie file\n'
        return False

    action = confirm(results, filename, extension)

    if action == 'SKIP':
        print 'Skipping movie file\n'
        return False
    elif action == 'QUIT':
        print 'Exiting movienamer'
        sys.exit()
    else:
        i = int(action)
        result = results[i-1]

        if directory == '':
            directory = '.'

        dest = (directory + '/' +
                result['title'] +
                ' [' + result['year'] + ']' +
                extension)

        if os.path.isfile(dest):
            print 'File already exists: ' + dest
            print 'Overwrite?'
            final_confirmation = raw_input('([y]/n/q)'.encode('utf-8')).lower()
            if final_confirmation == '':
                final_confirmation = 'y'

            if final_confirmation not in ['y', 'n', 'q']:
                final_confirmation = raw_input(
                    '([y]/n/q)'.encode('utf-8')).lower()
                if final_confirmation == '':
                    final_confirmation = 'y'

            if final_confirmation == 'n':
                print 'Skipping movie file\n'
                return False
            elif final_confirmation == 'q':
                print 'Exiting movienamer'
                sys.exit()

        return movie, dest


def main():
    parser = argparse.ArgumentParser(
        description='Command-line utlity to organize movies.'
    )

    parser.add_argument('movie', nargs='+', help='movie files to rename')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='recursively rename movies in deirectories')

    args = vars(parser.parse_args())

    if len(args) == 0:
        raise Exception

    movies = []
    errors = []

    if args['recursive']:
        for movie in args['movie']:
            if os.path.isfile(movie):
                movies.append(movie)
                continue
            elif not os.path.isdir(movie):
                errors.append(movie)
                continue

            for root, dirnames, files in os.walk(movie):
                for filename in files:
                    _, extension = os.path.splitext(filename)
                    if extension in video_extensions:
                        movies.append(root + '/' + filename)

    else:
        for filename in args['movie']:
            _, extension = os.path.splitext(filename)
            if extension in video_extensions:
                movies.append(filename)
            else:
                errors.append(filename)

    for i, movie in enumerate(movies):
        result = movienamer(movie)
        if result == False:
            errors.append(movie)
        else:
            os.rename(*result)
            print 'Movie succesfully renamed'
            if i + 1 < len(movies):
                print ''

    if len(errors) > 0:
        print 'Unable to rename the following movie files:'
        for i, filename in enumerate(errors):
            print '%d: %s' % (i+1, filename)
