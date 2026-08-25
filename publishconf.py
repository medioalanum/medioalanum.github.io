import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from pelicanconf import *  # noqa: E402,F403

SITEURL = "https://medioalanum.github.io"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
