from ARYAN.core.bot import ARYAN
from ARYAN.core.dir import dirr
from ARYAN.core.git import git
from ARYAN.core.userbot import Userbot
from ARYAN.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ARYAN()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
