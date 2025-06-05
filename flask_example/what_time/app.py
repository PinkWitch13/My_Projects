from flask import Flask, request, render_template
from datetime import datetime
from zoneinfo import ZoneInfo


app = Flask(__name__)

@app.route('/')
@app.route('/time_zone')
class MyTimeZone():
    
    time_zones =  list(ZoneInfo.zoneinfo.available_timezones())
    user_time_zone = request.args.get('time_zone')

    def user_zone (self):
        user_tz = self.user_time_zone()
        return user_tz

    def what_time_in_zone(self, user_zone, time_zones):
        for zone in time_zones:
            if self.user_zone() == zone:
                ut = user_time_now(user_zone)
                return render_template('time.html', what_time_in_zone=what_time_in_zone())
        return "Error: invalid ISCA time zone!"

from my_time import user_time_now
#   if user_tz == None:
#user_tz  = time_zones['Warsaw']
#    elif time_zones[user_tz] == True:
#        my_time_now = my_time_now(user_tz)
#    else:
#        return 'Please provide time zone in ISKA'
#render_template('time.html', time_zone=time_zone())
    

if __name__ == '__main__':
    app.run(debug = True)