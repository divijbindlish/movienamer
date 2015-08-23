import unittest

import movienamer.sanitize as sanitize


class SanitizeTest(unittest.TestCase):

    def test_sanitizer(self):
        items = [
            ('2001 - A Beautiful Mind', ('a beautiful mind', 2001)),
            ('Inception', ('inception', None)),
            ('Closer.2004.brrip.Xvid-VLiS', ('closer', 2004)),
            ('Dead.Man.Down.2013.720p.BluRay.x264.YIFY',
             ('dead man down', 2013)),
            ('Death.Sentence.2007.BluRay.720p.DTS.x264-WiKi',
             ('death sentence', 2007)),
            ('Heat [1995]-720p-BRRip-x264-StyLishSaLH',
             ('heat', 1995))
        ]

        for value, output in items:
            self.assertEqual(sanitize.sanitize(value), output)
