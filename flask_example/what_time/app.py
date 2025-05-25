from flask import Flask, request, render_template
from datetime import datetime
from my_time import MyTimeZone

app = Flask(__name__)

@app.route('/')
@app.route('/time_zone')
class MyTimeZone():
    
    user_time_zone = request.args.get('time_zone')

    def user_zone (self):
        user_tz = self.user_time_zone()
        return user_tz

    def what_time_in_zone(self, user_zone, user_time_now):
        if self.tz(user_zone) == True:
            user_tz = user_time_now(user_tz)
            return render_template('time.html', user_tz=user_tz)
        return "Error: invalid ISCA time zone!"
#   if user_tz == None:
#user_tz  = time_zones['Warsaw']
#    elif time_zones[user_tz] == True:
#        my_time_now = my_time_now(user_tz)
#    else:
#        return 'Please provide time zone in ISKA'
#render_template('time.html', time_zone=time_zone())
    

if __name__ == '__main__':
    app.run(debug = True)