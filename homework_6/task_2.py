"""2. У додатку є json файл. Написати програму, яка прочитає його та
порахує загальну тривалість всіх треків в альбомі.
  Базовий кейс - поверне кількість секунд.
  * Дод. ускладнення повернути у вигляді рядка години:хвилини:секунди, прик. 0:41:39"""

import json
import time
import datetime


def count_duration() -> int:
    """Return duration in seconds"""
    with open('acdc.json') as f:
        data_json = json.loads(f.read())
        duration = 0
        for track in data_json["album"]["tracks"]["track"]:
            duration += int(track['duration'])
    return duration


def convert_seconds(secs):
    convert = str(datetime.timedelta(seconds=secs))
    return convert


seconds = count_duration()
result = convert_seconds(seconds)
print(f"Total duration: {result}")
