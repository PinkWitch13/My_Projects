import datetime
import zoneinfo

def user_time_zone():
    user_zone = input("Please write your time_zone(ISKA format): \n")
    uz = str(user_zone)
    tz = zoneinfo.available_timezones()
    for zone in tz:
        if uz == zone:
           return uz

def user_time_now():
    utz = user_time_zone()  
    now = datetime.datetime.utcnow()
    dt = now.astimezone(tz=zoneinfo.ZoneInfo(utz))
    print("Your time: %s" % dt)

user_time_now()




