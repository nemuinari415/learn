from flask import Flask

app = Flask(__name__)
app.secret_key = "your_secret_key"

import myapp_001.main

from myapp_001 import db

db.create_profile_table()
