import os

# bot name
bot_name = "PLAGGYt"
bot_username = "@planetshnaggybot"

# message for /start command
welcome_message_template = "Hi {username}, welcome to the bot!Please **don't share this Bot with anyone!**"


# message for /info command
info_message = '''This Powered by [Python](https://www.python.org/) Telegram Bot is Private and only didicated to My Spotify tracker telegram channel.

**Developer's Contact:**
[https://t.me/auraatic](https://t.me/auuratic)
'''

# errors and wrong link patterns from user
deezer_link_message = '''This bot is created to download from spotify but you sent a deezer link.
Send the link of your track/album/playlist from spotify'''
soundcloud_link_message = '''This bot is created to download from spotify but you sent a soundcloud link.
Send the link of your track/album/playlist from spotify'''
youtube_link_message = '''This bot is created to download from spotify but you sent a youtube link.
Send the link of your track/album/playlist from spotify'''
spotify_episode_link_message = '''You can't send podcast episode links.
Send the link of your track/album/playlist from spotify'''
spotify_artist_link_message = '''You can't send artist links.
Send the link of your track/album/playlist from spotify'''
spotify_user_link_message = '''You can't send user links.
Send the link of your track/album/playlist from spotify'''

# end_message = '''end.

# motivate me to buy more servers for faster download by:
# • Giving a star in [github](https://github.com/arashnm80/spot-seek-bot)⭐🙂
# • Or subscribing to [my youtube](https://www.youtube.com/@Arashnm80)🔥❤️'''

end_message = '''end.

You can use me anytime latter but quick reminder to not share this robot to anyone else'''

sth_to_download_message = '''`You already have some link to download, wait for it to finish.`'''

wrong_link_message = '''This is not a correct spotify link.'''

# download directory
directory = "./output/"

# paths
# db_csv_path = "./csv_files/db.csv" # old method
db_by_letter_folder_path = "./csv_files/db_by_letter"
users_csv_path = "./csv_files/users.csv"
received_links_folder_path = "./received_links"

# env variables
bot_api = os.environ["SPOT_SEEK_BOT_API"]
database_channel = os.environ["MUSIC_DATABASE_ID"]

# spotify regex patterns
spotify_shortened_link_pattern = r'https?:\/\/spotify\.link\/[A-Za-z0-9]+'
spotify_track_link_pattern = r'https?:\/\/open\.spotify\.com\/(intl-[a-zA-Z]{2}\/)?track\/[a-zA-Z0-9]+'
spotify_album_link_pattern = r'https?:\/\/open\.spotify\.com\/(intl-[a-zA-Z]{2}\/)?album\/[a-zA-Z0-9]+'
spotify_playlist_link_pattern = r'https?:\/\/open\.spotify\.com\/(intl-[a-zA-Z]{2}\/)?playlist\/[a-zA-Z0-9]+'
spotify_correct_link_pattern = spotify_track_link_pattern + "|" + spotify_album_link_pattern + "|" + spotify_playlist_link_pattern + "|" + spotify_shortened_link_pattern
deezer_link_pattern = r'https?:\/\/(?:www\.)?deezer\.com\/(?:\w{2}\/)?(?:\w+\/)?(?:track|album|artist|playlist)\/\d+'
soundcloud_link_pattern = r"(?:https?://)?(?:www\.)?soundcloud\.com/([a-zA-Z0-9-_]+)/([a-zA-Z0-9-_]+)"
youtube_link_pattern = r"(?:(?:https?:)?//)?(?:www\.)?(?:(?:youtube\.com/(?:watch\?.*v=|embed/|v/)|youtu.be/))([\w-]{11})"
spotify_episode_link_pattern = r'https?:\/\/open\.spotify\.com\/(intl-[a-zA-Z]{2}\/)?episode\/[a-zA-Z0-9]+'
spotify_artist_link_pattern = r'https?:\/\/open\.spotify\.com\/(intl-[a-zA-Z]{2}\/)?artist\/[a-zA-Z0-9]+'
spotify_user_link_pattern = r'https?:\/\/open\.spotify\.com\/(intl-[a-zA-Z]{2}\/)?user\/[a-zA-Z0-9]+'

# log chanel
log_bot_url = "https://api.telegram.org/bot" + bot_api + "/"
log_channel_id = os.environ['-1002405407964']

# specify to use warp or not
warp_mode = True

# promote channel
promote_channel_username = "@SHLSAL"
promote_channel_link = "https://t.me/SHLSAL"
not_subscribed_to_channel_message = '''Your link is correct✅.
Join to get access to database, then send your link again.'''

# spotify
spotify_client_id = os.environ["SPOTIFY_APP_CLIENT_ID"]
spotify_client_secret = os.environ["SPOTIFY_APP_CLIENT_SECRET"]

# database csv columns
db_time_column = 0
db_sp_track_column = 1
db_tl_audio_column = 2

# users csv columns
ucsv_user_id_column = 0
ucsv_last_time_column = 1

# data and time format in csv files
datetime_format = "%Y/%m/%d-%H:%M:%S"

# necessary time in seconds for user to wait between 2 requests
user_request_wait = 30

unsuccessful_process_message = '''Sorry, process wasn't sucessful :(

But you can try another link or use the bot again after some time, it might help.'''

abnormal_behavior_message = " log:\nNo matches found.\
this line should not happen in normal behavior\
becuase it is already checked with regex, if happens is a bug."

more_than_1000_tracks_message = "Bot can't download playlists more than 1000 tracks at the moment.\
This feature will be added later."
