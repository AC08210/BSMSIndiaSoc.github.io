from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.forms import ApplicationForm, RSVPForm, ContactForm
from app import db
from app.models import Application, RSVP, ContactMessage
from app.email_utils import send_contact_email

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    # Sample images and blurbs shown on home
    featured = [
        {'src': url_for('static', filename='images/placeholder1.jpg'), 'alt': 'Festival'},
        {'src': url_for('static', filename='images/placeholder2.jpg'), 'alt': 'Event'},
        {'src': url_for('static', filename='images/committee_sample.jpg'), 'alt': 'Committee'}
    ]
    return render_template('index.html', featured=featured)

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/events', methods=['GET', 'POST'])
def events():
    form = RSVPForm()
    if form.validate_on_submit():
        r = RSVP(event_name=form.event_name.data, name=form.name.data, email=form.email.data)
        db.session.add(r)
        db.session.commit()
        flash('Thanks — you are RSVP’d!', 'success')
        return redirect(url_for('main.events'))

    # Dummy list of events for display
    events_list = [
        {'title':'Diwali Night 2024', 'date':'2024-11-10', 'desc':'A sparkling celebration of lights.'},
        {'title':'Holi Colour Run', 'date':'2025-03-22', 'desc':'An outdoor splash of colours and fun.'}
    ]
    # Google Calendar embed (replace with your calendar ID in production)
    calendar_embed_src = 'https://calendar.google.com/calendar/embed?src=en.uk%23holiday%40group.v.calendar.google.com&ctz=Europe%2FLondon'

    return render_template('events.html', events=events_list, calendar_embed_src=calendar_embed_src, form=form)

@bp.route('/committee')
def committee():
    # Dummy committee
    committee_members = [
        {'name':'Ananya Rao','role':'President','bio':'Third-year student passionate about culture & events.','photo': url_for('static', filename='images/committee_sample.jpg')},
        {'name':'Karan Mehta','role':'Events Officer','bio':'Loves organizing big bashes and workshops.','photo': url_for('static', filename='images/committee_sample.jpg')},
        {'name':'Priya Singh','role':'Treasurer','bio':'Keeps the finances and sponsors happy.','photo': url_for('static', filename='images/committee_sample.jpg')}
    ]
    return render_template('committee.html', committee=committee_members)

@bp.route('/sponsors')
def sponsors():
    sponsors = [
        {'name':'Local Restaurant','logo': url_for('static', filename='images/placeholder1.jpg'), 'link':'https://example.com'},
        {'name':'Campus Cafe','logo': url_for('static', filename='images/placeholder2.jpg'), 'link':'https://example.org'}
    ]
    return render_template('sponsors.html', sponsors=sponsors)

@bp.route('/merch')
def merch():
    featured_products = [
        {'name':'IndiaSoc T‑shirt','image': url_for('static', filename='images/placeholder1.jpg'), 'link':'https://merch.example.com/product/1'},
        {'name':'IndiaSoc Hoodie','image': url_for('static', filename='images/placeholder2.jpg'), 'link':'https://merch.example.com/product/2'}
    ]
    merch_link = 'https://merch.example.com'
    return render_template('merch.html', products=featured_products, merch_link=merch_link)

@bp.route('/applications', methods=['GET', 'POST'])
def applications():
    form = ApplicationForm()
    if form.validate_on_submit():
        a = Application(name=form.name.data, email=form.email.data, year=form.year.data, role=form.role.data, motivation=form.motivation.data)
        db.session.add(a)
        db.session.commit()
        flash('Application submitted — thank you!', 'success')
        
