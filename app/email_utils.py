from flask import current_app
from app import mail
from flask_mail import Message


def send_contact_email(subject, sender, recipients, body):
    """Try to send an email via Flask-Mail; if mail is not configured, return False so caller can log/store the message."""
    try:
        if not current_app.config.get('MAIL_SERVER'):
            return False
        msg = Message(subject=subject, sender=sender, recipients=recipients, body=body)
        mail.send(msg)
        return True
    except Exception as e:
        current_app.logger.exception('Failed to send mail: %s', e)
        return False
