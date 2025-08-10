import sqlite3
from pathlib import Path
from datetime import datetime, timedelta

DB = Path(__file__).resolve().parent / 'bsms.db'

schema = '''
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    date TEXT,
    img TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS gallery (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    img TEXT,
    caption TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS committee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    role TEXT,
    img TEXT
);
CREATE TABLE IF NOT EXISTS mailing (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    created_at TEXT
);
CREATE TABLE IF NOT EXISTS suggestions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    suggestion TEXT,
    created_at TEXT
);
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    message TEXT,
    created_at TEXT
);
'''

conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.executescript(schema)

# sample events
events = [
    ('Curry Social — Welcome Back','Casual evening of homemade curries, music and board games.','2025-09-20','https://images.unsplash.com/photo-1524499982521-1ffd58dd89ea?auto=format&fit=crop&w=1000&q=60'),
    ('Bollywood Dance Workshop','Learn a group routine. No experience required.','2025-10-10','https://images.unsplash.com/photo-1514512364185-6d8f1dfc5be7?auto=format&fit=crop&w=1000&q=60'),
    ('Diwali Celebration','Lights, sweets, performances & community dinner.','2025-11-12','https://images.unsplash.com/photo-1542736667-069246bdbc93?auto=format&fit=crop&w=1000&q=60'),
]

for e in events:
    cur.execute('INSERT INTO events (title,description,date,img) VALUES (?,?,?,?)', e)

# sample gallery
gallery = [
    ('https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1000&q=60','Culture Night'),
    ('https://images.unsplash.com/photo-1533777324565-a040eb52fac2?auto=format&fit=crop&w=1000&q=60','Curry Social'),
    ('https://images.unsplash.com/photo-1506368249639-73a05d6f6488?auto=format&fit=crop&w=1000&q=60','Bollywood Night'),
    ('https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=1000&q=60','Students performing'),
]

for g in gallery:
    cur.execute('INSERT INTO gallery (img,caption) VALUES (?,?)', g)

# sample committee (14)
committee = [
    ('Aisha Khan','President','https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=400&q=60'),
    ('Rahul Patel','Events Lead','https://images.unsplash.com/photo-1545996124-1b4b0b9ccf4b?auto=format&fit=crop&w=400&q=60'),
    ('Priya Sharma','Welfare Officer','https://images.unsplash.com/photo-1531123414780-f9a6b8c8a6f2?auto=format&fit=crop&w=400&q=60'),
    ('Imran Ali','Treasurer','https://images.unsplash.com/photo-1547425260-76bcadfb4f2c?auto=format&fit=crop&w=400&q=60'),
    ('Sara Begum','Secretary','https://images.unsplash.com/photo-1544006659-f0b21884ce1d?auto=format&fit=crop&w=400&q=60'),
    ('Karan Mehta','Media Lead','https://images.unsplash.com/photo-1531123414780-f9a6b8c8a6f2?auto=format&fit=crop&w=400&q=60'),
    ('Nadia Khan','Socials','https://images.unsplash.com/photo-1545996124-1b4b0b9ccf4b?auto=format&fit=crop&w=400&q=60'),
    ('Arjun Singh','Performances','https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=400&q=60'),
    ('Leela Rao','Outreach','https://images.unsplash.com/photo-1544006659-f0b21884ce1d?auto=format&fit=crop&w=400&q=60'),
    ('Mohammed Yusuf','Welfare Rep','https://images.unsplash.com/photo-1547425260-76bcadfb4f2c?auto=format&fit=crop&w=400&q=60'),
    ('Sana Khan','Logistics','https://images.unsplash.com/photo-1531123414780-f9a6b8c8a6f2?auto=format&fit=crop&w=400&q=60'),
    ('Dev Sharma','Sponsorships','https://images.unsplash.com/photo-1545996124-1b4b0b9ccf4b?auto=format&fit=crop&w=400&q=60'),
    ('Rina Patel','Accessibility','https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=400&q=60'),
    ('Omar Ahmed','Web & Tech','https://images.unsplash.com/photo-1547425260-76bcadfb4f2c?auto=format&fit=crop&w=400&q=60'),
]

for c in committee:
    cur.execute('INSERT INTO committee (name,role,img) VALUES (?,?,?)', c)

conn.commit()
conn.close()
print('Database created at', DB)
