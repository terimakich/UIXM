import re
from os import getenv, environ

from pyrogram import filters  # ✅ This is required

# Load .env only if not in environment
if not environ.get("API_ID"):
    from dotenv import load_dotenv
    load_dotenv()

API_ID_RAW = getenv("API_ID")
if not API_ID_RAW or not API_ID_RAW.isdigit():
    raise SystemExit("[ERROR] - API_ID is missing or invalid in your .env file!")

API_ID = int(API_ID_RAW)
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

# continue with rest...

# ========= Optional MongoDB & API Integrations =========
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
YTPROXY_URL = getenv("YTPROXY_URL", "https://tgapi.xbitcode.com")
YT_API_KEY = getenv("YT_API_KEY", None)

# ========= Duration & File Size Limits =========
DURATION_LIMIT = int(getenv("DURATION_LIMIT", 14400))  # 4 hrs
VIDEO_DURATION_LIMIT = int(getenv("VIDEO_DURATION_LIMIT", 14400))  # 4 hrs
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 52428800))  # 50MB
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2147483648))  # 2GB

# ========= Bot Ownership & Logs =========
OWNER_ID = int(getenv("OWNER_ID", 6221699441))
SUDO_USERS_RAW = getenv("SUDO_USERS", str(OWNER_ID))
SUDO_USERS = list(map(int, SUDO_USERS_RAW.split()))
LOGGER_ID = int(getenv("LOGGER_ID", -1002715747653))

# ========= Heroku Configuration =========
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# ========= Git & Upstream Repo =========
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/strad-dev131/TeamXmusic2.0")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# ========= Support & Channels =========
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TeamXUpdate")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TeamsXchat")

# ========= Assistant Behavior Settings =========
AUTO_LEAVING_ASSISTANT = bool(int(getenv("AUTO_LEAVING_ASSISTANT", 0)))
ASSISTANT_LEAVE_TIME = int(getenv("ASSISTANT_LEAVE_TIME", 6400))

# ========= Spotify Credentials =========
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

# ========= Playlist Fetch Limit =========
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# ========= Pyrogram String Sessions =========
STRING_SESSIONS = [
    getenv("STRING_SESSION", None),
    getenv("STRING_SESSION2", None),
    getenv("STRING_SESSION3", None),
    getenv("STRING_SESSION4", None),
    getenv("STRING_SESSION5", None),
]

# ========= System Constants =========
PRIVATE_BOT_MODE_MEM = int(getenv("PRIVATE_BOT_MODE_MEM", 5))
CACHE_DURATION = 3600  # 1 hour
CACHE_SLEEP = 600      # 10 minutes

# ========= Image URLs =========
START_IMG_URL = [
    "https://files.catbox.moe/uxcm48.jpg",
    "https://files.catbox.moe/uxcm48.jpg",
    "https://files.catbox.moe/uxcm48.jpg",
]
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/uxcm48.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/uxcm48.jpg"
STATS_IMG_URL = "https://files.catbox.moe/pguloz.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/timwpo.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/timwpo.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/timwpo.jpg"
SOUNDCLOUD_IMG_URL = "https://graph.org/file/c95a687e777b55be1c792.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/e8730fdece86a1166f608.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://strad-dev131.github.io/TeamXsrc/img/sp_artist.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://strad-dev131.github.io/TeamXsrc/img/sp_album.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://strad-dev131.github.io/TeamXsrc/img/sp_playlist.jpg"

# ========= In-Memory Data Stores =========
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
file_cache = {}

# ========= Validate URLs =========
URL_PATTERN = re.compile(r"^(?:http|https)://")

if SUPPORT_CHANNEL and not URL_PATTERN.match(SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL URL is invalid. Must start with https://")

if SUPPORT_CHAT and not URL_PATTERN.match(SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Your SUPPORT_CHAT URL is invalid. Must start with https://")
