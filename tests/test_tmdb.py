import unittest

import movienamer.tmdb as tmdb


class TMDbTest(unittest.TestCase):

    def test_search(self):
        movies = tmdb.search('inception')
        self.assertIsInstance(movies, list)
        self.assertGreater(len(movies), 0)

        movie = movies[0]
        self.assertIsInstance(movie, dict)
        self.assertTrue('title' in movie)
        self.assertTrue('original_language' in movie)
        self.assertTrue('release_date' in movie)
        self.assertTrue('popularity' in movie)

        empty_list = tmdb.search('!@#$%^&*()')
        self.assertIsInstance(empty_list, list)
        self.assertEqual(len(empty_list), 0)
