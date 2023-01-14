from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from secret import *

app = Flask(__name__)

# this is where we connect to the database

app.config['SQLALCHEMY_DATABASE_URI'] = SECRET_STRING
app.config["SQLALCHEMY_ECHO"] = True
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app)
db.create_all()

<<<<<<< HEAD
# import flight_data #updated this
# from models import * # and this

from scraper import plotting
# from views import *


=======
from scraper import plotting
>>>>>>> 644adc22a5c52624585f4cdec05ba1efbe31d664
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger

<<<<<<< HEAD
trigger = CronTrigger(minute='*/1')
=======
trigger = CronTrigger(hour='*/5')
>>>>>>> 644adc22a5c52624585f4cdec05ba1efbe31d664

sched = BackgroundScheduler()
# sched.add_job(update_flight_data, trigger)
# sched.add_job(cut_off_delay, trigger)
sched.add_job(plotting, trigger)

sched.start()

if __name__ == "__main__":

    app.run()



    


