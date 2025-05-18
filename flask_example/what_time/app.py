from flask import Flask, request, render_template
from datetime import datetime
from my_time import my_time_now, time_zones

app = Flask(__name__)

@app.route('/')
@app.route('/time_zone')
def what_time():
    time_zone = request.args.get('time_zone')
#    if time_zone != None:
#        time_zone = str(time_zone)
    return "Ta da! {}".format(time_zone)
#   if user_tz == None:
#user_tz  = time_zones['Warsaw']
#    elif time_zones[user_tz] == True:
#        my_time_now = my_time_now(user_tz)
#    else:
#        return 'Please provide time zone in ISKA'
#return render_template('time.html', time_zone=time_zone())
    

if __name__ == '__main__':
    app.run(debug = True)