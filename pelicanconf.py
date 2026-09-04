from minchin.pelican.plugins import post_stats


AUTHOR = "Alan"
SITENAME = "medioalanum"
SITESUBTITLE = "Notes on Python, APIs, and Software Engineering"
SITEURL = ""

PATH = "content"
OUTPUT_PATH = "output/"
STATIC_PATHS = ["theme"]

TIMEZONE = "Europe/Rome"
DEFAULT_LANG = "en"

THEME = "themes/elegant"

DEFAULT_PAGINATION = 10
RELATIVE_URLS = True

# Elegant home page and article metadata.
RECENT_ARTICLES_COUNT = 10
RECENT_ARTICLE_SUMMARY = True
SUMMARY_MAX_LENGTH = 50

# Elegant displays article.stats["read_mins"] when post_stats is enabled.
PLUGINS = [post_stats]
READING_TIME_LOWER_LIMIT = 1

SOCIAL_PROFILE_LABEL = "Find me online"
SOCIAL = (
    ("Github", "https://github.com/medioalanum", "Alan Viana on GitHub"),
    (
        "LinkedIn",
        "https://www.linkedin.com/in/alanviana/",
        "Alan Viana on LinkedIn",
    ),
)

DIRECT_TEMPLATES = ["index", "tags", "categories", "archives"]
TAGS_URL = "tags.html"
CATEGORIES_URL = "categories.html"
ARCHIVES_URL = "archives.html"

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
