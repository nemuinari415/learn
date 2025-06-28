from flask import Flask

app = Flask(__name__)
import myapp_001.main

from myapp_001 import db

db.create_profile_table()
