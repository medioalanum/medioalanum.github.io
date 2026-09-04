AUTHOR = "Alan"
SITENAME = "medioalanum"
SITESUBTITLE = "Notes on Python, APIs, and Software Engineering"
SITEURL = ""

PATH = "content"
OUTPUT_PATH = "output/"

TIMEZONE = "Europe/Rome"
DEFAULT_LANG = "en"

THEME = "themes/mnmlist"
CSS_FILE = "main.css"
HIDE_DATE = False

DEFAULT_PAGINATION = 10
RELATIVE_URLS = True

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
    },
    "output_format": "html5",
}

ARTICLE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{slug}/index.html"
PAGE_URL = "pages/{slug}/"
PAGE_SAVE_AS = "pages/{slug}/index.html"

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
