import re

case_sensitive_keywords = [
    'LIMITED', 'EXTENDED', 'PROPER', 'xRG', 'E-SuB', 'LiNE', 'DTS', 'ADTRG',
    'HD', 'UNRATED'
]

print_keywords = [
    '720p', '1080p', '480p', 'bdrip', 'bd rip', 'bd.rip', 'brrip', 'br rip',
    'br.rip', 'webscr', 'web scr', 'web.scr', 'dvdrip', 'dvd rip', 'dvd.rip',
    'camrip', 'cam rip', 'cam.rip', 'dvdscr', 'dvd scr', 'dvd.scr', 'hdrip',
    'hd rip', 'hd.rip', 'hdcam', 'hd cam', 'hd.cam', 'hddvd', 'hd dvd',
    'hd.dvd', 'bluray', 'blu ray', 'blu.ray', 'hdts', 'hd ts', 'hd.ts',
    'telesync', 'hdtv', 'hd tv', 'hd.tv', 'ts ', 'ts.', ' ts', '.ts', 'tvrip',
    'tv rip', 'tv.rip', 'web-dl', 'r4', 'r5', 'r6',
]

case_insensitive_keywords = [
    'cd1', 'cd 1', 'cd.1', 'cd2', 'cd 2', 'cd.2', 'disc1', 'disc 1', 'disc.1',
    'disc2', 'disc 2', 'disc.2', 'glowgaze com', 'glowgaze.com', 'glowgaze',
    'g2g fm', 'g2g.fm', 'g2g', 'subbed', 'dubbed', 'unrated', 'subs ', 'subs.',
    ' subs', '.subs', 'sub ', 'sub.', ' sub', '.sub', 'ntsc', 'axxo', 'fxm',
    'ntsc', 'yify', 'dd5.1', '5.1ch'
]

regex_keywords = [
    'xvid[ \.\-_]?[a-zA-Z0-9\-]*', 'x264[ \-_]?[a-zA-Z0-9\-]*',
    'ac3[ \-_]?[a-zA-Z0-9\-]*', '\[ ?[^\/\]]*\.com ?\]'
]

roman_numerals = [
    'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'xi', 'xii',
    'xiii', 'xiv', 'xv', 'xvi', 'xvii', 'xviii', 'xix', 'xx'
]

year_extract_patterns = [re.compile(pattern) for pattern in [
    '^(?P<name>.+?) ?(?P<year>[0-9]{4}?)[^\\/]*$',
    '^(?P<year>[0-9]{4}?) ?(?P<name>.+?)$'
]]

video_extensions = [
    '.mkv', '.mp4', '.avi', '.flv', '.rmvb', '.wmv', '.mpeg'
]

subtitle_extensions = [
    '.srt', '.sub'
]
