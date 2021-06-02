from app import app, db
from flask import render_template, request, redirect, url_for, flash, json, jsonify
from app.models import Ride
from flask_login import login_user, logout_user, current_user
import requests as r
import joblib
import traceback
import pandas as pd
import numpy as np
from datetime import datetime
import statistics

# Testing - 
# Development - 
# Production - 

# file-watcher

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['GET'])
def calculate():
    startdate = request.args.get('start')
    enddate = request.args.get('end')
    fromid = request.args.get('from_station_id')
    if fromid is None:
        answer = Ride.query.filter(Ride.starttime > startdate, Ride.stoptime < enddate).all()
        triptotal = 0
        for a in answer:
            triptotal += a.trip_duration
        avgtrip = triptotal / len(answer)
        out = {
            "averageDuration": avgtrip
        }
        return out
    else:
        answer = Ride.query.filter(Ride.starttime > startdate, Ride.stoptime < enddate, Ride.from_station_id == fromid).all()
        stationNamequery = Ride.query.filter(Ride.from_station_id == fromid).first()
        stationName = stationNamequery.from_station_name
        triptotal = 0
        for a in answer:
            triptotal += a.trip_duration
        avgtrip = triptotal / len(answer)
        out = {
            "averageDuration": avgtrip,
            "fromStationId": fromid,
            "fromStationName": stationName
        }
        return out