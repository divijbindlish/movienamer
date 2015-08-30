import os.path as path
import re

import Levenshtein

from .sanitize import sanitize
from .tmdb import search


def _gather(filename, directory=None, titles={}):
    # Sanitize the input filename
    name, year = sanitize(filename)

    # Start with a basic search
    results = search(name, year)

    if year is not None and len(results) == 0:
        # If no results are found when year is present,
        # allow a tolerance of 1 in the year
        results = search(name, year + 1)
        results = results + search(name, year - 1)

    # Try to find a result with zero error and return
    zero_distance_results = []
    for i, result in enumerate(results):
        distance = Levenshtein.distance(
            unicode(re.sub('[^a-zA-Z0-9]', '', name.lower())),
            unicode(re.sub('[^a-zA-Z0-9]', '', result['title'].lower()))
        )

        # Update the results with the distance
        result['distance'] = distance
        results[i]['distance'] = distance

        # Update the results with year
        result['with_year'] = (year is not None)
        results[i]['with_year'] = (year is not None)

        # Add count field to the result
        result['count'] = 1
        results[i]['count'] = 1

        if distance == 0:
            zero_distance_results.append(result)

    if len(zero_distance_results) > 0:
        # Directly return results with zero error
        return zero_distance_results

    if year is not None and len(results) > 0:
        # Directly return results which were queried with year
        return results

    # If neither zero distance results are present nor is the year,
    # accumulate results from directory one level up
    if directory is not None:
        dirname = directory.split('/')[-1]
        results_from_directory = _gather(dirname)

        results_to_be_removed = []

        # Increment count for all duplicate results
        for i, r1 in enumerate(results):
            for r2 in results_from_directory:
                if r1['popularity'] == r2['popularity']:
                    # Check with popularity since title can be duplicate
                    results[i]['count'] += r2['count']
                    results_from_directory.remove(r2)
                    break

        results = results + results_from_directory

    return results


def identify(filename, directory=None):
    if directory == '' or directory == '.' or directory == '..':
        directory = None

    results = _gather(filename, directory)
    for i, result in enumerate(results):
        # Add year to all the results
        try:
            results[i]['year'] = re.findall(
                '[0-9]{4}', result['release_date'])[0]
        except TypeError:
            results[i]['year'] = None

    if len(results) == 0:
        return []

    max_distance = 1 + max([result['distance'] for result in results])
    return sorted(
        results,
        key=lambda r: ((r['count'] ** 1.1) *
                       ((max_distance - r['distance'])) *
                       ((1 + r['with_year'])) *
                       ((r['popularity']))),
        reverse=True
    )
