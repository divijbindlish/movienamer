import os.path as path
import re

from .tmdb import search
from .distance import compute_distance


def _query(guess):
    '''
    Take guess dictionary (guessit) and query TMDb using movienamer.tmdb and
    return query string and list (possibly empty) of results.
    '''
    if 'title' not in guess:
        raise Exception

    name = guess['title']
    if 'alternative_title' in guess:
        name = name + ' ' + guess['alternative_title']

    year = None
    if 'year' in guess:
        year = guess['year']

    return name, tmdb.search('movie', name, year)


class Identifier:
    '''
    Class for identifying a movie based on it's filename.

    Provided methods:
    next(): Continue (or start) identification process in case the user does
            not accept any of the matched movies. Returns a list of results.
    '''

    def __init__(filename):
        self.full_path = path.abspath(filename)
        self._state = 0
        self.query = ''
        self.results = []

    def next():
        if self._state == 0:
            # Beginning of identification, show zero distance results
            filename = path.basename(path.splitext(self.full_path)[0])
            guess = guessit(filename)

            self.query, self.results = _query(guess)
            if len(self.results) == 0:
                self._state = 2
                return self.next()

            zero_distance_results = filter(
                lambda result: compute_distance(query, result['title']) == 0,
                results
            )

            if len(zero_distance_results) == 0:
                self._state = 1
                return self.next()

            self._state += 1
            return zero_distance_results

        if self._state == 1:
            # Zero distance results weren't enough
            self._state += 1
            return self.results

        if self._state == 2:
            # No identification from filename guess, show results from parent
            parent_directory = path.basename(path.dirname(self.full_path))
            if parent_directory == '':
                self._state = 4
                return self.next()

            parent_guess = guessit(parent_directory)

            self.query, self.results = _query(self.parent_guess)
            if len(self.results) == 0:
                self._state = 4
                return self.next()

            zero_distance_results = filter(
                lambda result: compute_distance(query, result['title']) == 0,
                results
            )

            if len(zero_distance_results) == 0:
                self._state = 3
                return self.next()

            self._state += 1
            return zero_distance_results

        if self._state == 3:
            # Return all results for parent
            self._state += 1
            return self.results

        if self._state == 4:
            # We didn't find anything
            return []
