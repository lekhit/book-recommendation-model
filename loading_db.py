import json
def load(name):
	with open(name,'r') as f:
		js=json.load(f)	
	return js
from replit import db
def to_db():
	js=load('my_data')
	

