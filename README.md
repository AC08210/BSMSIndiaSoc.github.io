BSMS IndiaSoc - Full Flask site (sample)
=======================================

What's included
- Flask app (app.py)
- Templates for Home, About, Events, Gallery, Join, Suggestions, Contact
- Static CSS/JS (single stylesheet matching the tricolor theme)
- SQLite database bootstrap script (run_db.py)
- Sample data: events, gallery images, committee of 14 members
- Contact form that stores messages and attempts sending via SMTP (configure in .env)

Quick start (Linux / macOS)
1. Copy config.example.env -> .env and fill values (SECRET_KEY, MAIL_*, etc.)
2. Create virtualenv: python -m venv venv; source venv/bin/activate
3. Install: pip install -r requirements.txt
4. Initialize DB: python run_db.py
5. Run: flask run (or python app.py)

Notes
- For production, use a WSGI server (gunicorn) and set proper env vars.
- Instagram widget: replace placeholder in templates/contact.html with your widget embed or IG Graph API integration.
