from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length

class ApplicationForm(FlaskForm):
    name = StringField('Full name', validators=[DataRequired(), Length(max=128)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    year = SelectField('Year of study', choices=[('1','1'),('2','2'),('3','3'),('4+','4+')])
    role = StringField('Role applying for', validators=[DataRequired(), Length(max=64)])
    motivation = TextAreaField('Why do you want this role?', validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField('Submit application')

class RSVPForm(FlaskForm):
    name = StringField('Full name', validators=[DataRequired(), Length(max=128)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    event_name = StringField('Event name', validators=[DataRequired(), Length(max=140)])
    submit = SubmitField('RSVP')

class ContactForm(FlaskForm):
    name = StringField('Your name', validators=[DataRequired(), Length(max=128)])
    email = StringField('Your email', validators=[DataRequired(), Email(), Length(max=120)])
    subject = StringField('Subject', validators=[Length(max=140)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(max=2000)])
    submit = SubmitField('Send message')
