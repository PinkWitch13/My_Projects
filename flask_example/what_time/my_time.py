import datetime
import zoneinfo
from My_Projects.flask_example.what_time.u_time import MyTimeZone

time_zones = zoneinfo.available_timezones()


def user_time_now():
    ut_now = str(datetime.datetime.utcnow(tz = zoneinfo.ZoneInfo(time_zones)))
    return ut_now

tz = MyTimeZone(time_zones)

#Find out what IANA time zones are
#Check zoneinfo.available_timezones() function - how it wor

