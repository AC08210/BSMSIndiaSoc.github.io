from datetime import datetime
from app import db

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    year = db.Column(db.String(20))
    role = db.Column(db.String(64))
    motivation = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<Application {self.name} - {self.role}>'

class RSVP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(140), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<RSVP {self.name} for {self.event_name}>'

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(140))
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<Contact {self.email} - {self.subject}>'

# Dummy fixture helper (not used by app directly but helpful for initial data)
def load_dummy_data():
    if not Application.query.first():
        a = Application(name='Riya Patel', email='riya@example.com', year='2', role='Events Officer', motivation='Love organising events')
        db.session.add(a)
    if not RSVP.query.first():
        r = RSVP(event_name='Diwali Night 2024', name='Aman Singh', email='aman@example.com')
        db.session.add(r)
    db.session.commit()
