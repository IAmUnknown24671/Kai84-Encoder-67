#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 5145714881
    OWNER = config("OWNER", default="5145714881")
    FFMPEG = config(
        "FFMPEG", default='ffmpeg -i "{}"-c:v libx265 -preset veryfast -crf 28 -vf "drawtext=fontfile=AvengeroRegular-zvgl.ttf:text='Jarvis':fontcolor=white:x=w-tw:y=0:fontsize=30:box=1:boxcolor=black@0.5" -pix_fmt yuv420p -s 1280x720 -c:a libfdk_aac -b:a 60k -map 0"{}"',
    )
    THUMB = config(
        "THUMBNAIL", default="https://telegra.ph/file/6d122eb240c33b6c10180.jpg"
    )
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
