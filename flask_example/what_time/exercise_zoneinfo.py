import datetime
import zoneinfo

def user_time_now():
    now = datetime.datetime.utcnow()
    zone = list(zoneinfo.available_timezones())
    for i in range(len(zone)):
        print("Number: %d" % i)
        z = zone[i]
        dt = now.astimezone(tz=zoneinfo.ZoneInfo(z))
        print("Kubas time: %s" % dt)

user_time_now()

