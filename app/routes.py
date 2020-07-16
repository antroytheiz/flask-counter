from app import app, ipinfo, db
from datetime import datetime
from flask import render_template, request, redirect, session, url_for
import os
from .models import PageCounter
import mysql.connector



@app.route('/')
def index():
    return render_template('index.html',  data=PageCounter.query.all())

@app.route('/add2', methods=['POST'])
def add_two():
    # session['count'] += 1
    if not session.get('count'):
        session['count'] = 0
    session['count'] += 1
    ipadd = ipinfo.ipaddress
    data = PageCounter(ipaddress=ipadd)
    db.session.add(data)
    db.session.commit()
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session['count'] = 0
    data = PageCounter.query.first()
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('index'))



