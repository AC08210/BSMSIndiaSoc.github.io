import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mail import Mail, Message
from dotenv import load_dotenv
import sqlite3
from werkzeug.utils import secure_filename
from pathlib import Path
from datetime import datetime

# Load env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / 'bsms.db'

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret')
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 25))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'False').lower() in ('1','true','yes')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER', 'indiasoc@bsmsmedsoc.co.uk')

mail = Mail(app)

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    db = get_db()
    events = db.execute('SELECT * FROM events ORDER BY date DESC').fetchall()
    gallery = db.execute('SELECT * FROM gallery ORDER BY id DESC').fetchall()
    committee = db.execute('SELECT * FROM committee ORDER BY id').fetchall()
    return render_template('index.html', events=events, gallery=gallery, committee=committee)

@app.route('/about')
def about():
    db = get_db()
    committee = db.execute('SELECT * FROM committee ORDER BY id').fetchall()
    return render_template('about.html', committee=committee)

@app.route('/events')
def events_page():
    db = get_db()
    events = db.execute('SELECT * FROM events ORDER BY date DESC').fetchall()
    return render_template('events.html', events=events)

@app.route('/gallery')
def gallery_page():
    db = get_db()
    gallery = db.execute('SELECT * FROM gallery ORDER BY id DESC').fetchall()
    return render_template('gallery.html', gallery=gallery)

@app.route('/join', methods=['GET','POST'])
def join():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        db = get_db()
        db.execute('INSERT INTO mailing (name,email,created_at) VALUES (?,?,?)', (name,email, datetime.utcnow()))
        db.commit()
        flash('Thanks! You are on the mailing list.')
        return redirect(url_for('join'))
    return render_template('join.html')

@app.route('/suggestions', methods=['GET','POST'])
def suggestions():
    if request.method == 'POST':
        name = request.form.get('name') or 'Anonymous'
        suggestion = request.form.get('suggestion')
        db = get_db()
        db.execute('INSERT INTO suggestions (name,suggestion,created_at) VALUES (?,?,?)', (name,suggestion, datetime.utcnow()))
        db.commit()
        flash('Suggestion received — thank you!')
        return redirect(url_for('suggestions'))
    return render_template('suggestions.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        db = get_db()
        db.execute('INSERT INTO contacts (name,email,message,created_at) VALUES (?,?,?,?)', (name,email,message, datetime.utcnow()))
        db.commit()

        # try send email via SMTP if configured
        try:
            msg = Message(f"Website contact: {name}", recipients=[app.config.get('MAIL_DEFAULT_SENDER')])
            msg.body = f"From: {name} <{email}>\n\n{message}"
            mail.send(msg)
            flash('Message sent — thank you!')
        except Exception as e:
            print('Mail send failed:', e)
            flash('Message saved. We could not send email right now; we will check the site inbox.')

        return redirect(url_for('contact'))

    return render_template('contact.html')

@app.route('/api/events')
def api_events():
    db = get_db()
    events = db.execute('SELECT * FROM events ORDER BY date DESC').fetchall()
    return jsonify([dict(r) for r in events])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
