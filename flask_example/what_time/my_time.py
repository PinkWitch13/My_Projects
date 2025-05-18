import datetime
import zoneinfo
import time

time_zones = zoneinfo.available_timezones()

import app

def my_time_now(user_tz):
    time_now = datetime.now(tz = ZoneInfo(user_tz))
    return time_now

#Find out what IANA time zones are
#Check zoneinfo.available_timezones() function - how it works?
