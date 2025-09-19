from flask import Flask, request, render_template, url_for
from datetime import datetime
from what_time import exercise_zoneinfo

app = Flask(__name__)

# @app.index('/')
# def user_zone_input():
    
#     return user_zone

@app.route('/user_zone', methods=['POST','GET'])
def user_zone():
    user_zone = None
    ez = None
    if request.method == 'POST':
        user_zone = request.args.get('user_zone')
        ez = exercise_zoneinfo()
    return render_template('time.html', ez = ez )

if __name__ == '__main__':
    app.run(debug = True)