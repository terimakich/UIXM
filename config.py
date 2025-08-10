import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

# Vars For API End Pont.
API_URL = getenv("API_URL", 'https://api.thequickearn.xyz') #youtube song url
API_KEY = getenv("API_KEY", '30DxNexGenBots6d066c') # youtube song api ke

#API_URL = getenv("API_URL", 'https://api.thequickearn.xyz') #youtube song url
#API_KEY = getenv("API_KEY", 'NxGBNexGenBots41dd4c') # 

DURATION_LIMIT = int(getenv("DURATION_LIMIT", 14400)) # 5 hours
VIDEO_DURATION_LIMIT = int(getenv("VIDEO_DURATION_LIMIT", 14400)) # 5 hours

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002046320443))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7650291301))

SUDO_USERS = list(map(int, getenv("SUDO_USERS", str(OWNER_ID)).split()))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/terimakich/UIXM",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/THE_INCRICIBLE")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TEAMINCRICIBLE")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
ASSISTANT_LEAVE_TIME = int(getenv("ASSISTANT_LEAVE_TIME",  6400))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 52428800))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2097152099999))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

PRIVATE_BOT_MODE_MEM = int(getenv("PRIVATE_BOT_MODE_MEM", 5))

# Broadcast system temp values
CACHE_DURATION = 3600  # 1 hour in seconds
CACHE_SLEEP = 600      # check every 10 mins
file_cache = {}
autoclean = []


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = ["https://graph.org/file/eaa3a2602e43844a488a5.jpg",
                 "https://graph.org/file/b129e98b6e5c4db81c15f.jpg",
                 "https://graph.org/file/826485f2d7db6f09db8ed.jpg",]
    
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/2e3cf4327b169b981055e.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/uxcm48.jpg"
STATS_IMG_URL = "https://graph.org/file/9e23720fedc47259b6195.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/timwpo.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/timwpo.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/timwpo.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/c95a687e777b55be1c792.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/e8730fdece86a1166f608.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://strad-dev131.github.io/TeamXsrc/img/sp_artist.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://strad-dev131.github.io/TeamXsrc/img/sp_album.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://strad-dev131.github.io/TeamXsrc/img/sp_playlist.jpg"

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
