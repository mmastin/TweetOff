''' Main application for routing logic for TweetOff'''
from flask import Flask

def create_app():
	'''Create and configure an instance of the Flask application'''
	app = Flask(__name__)
	
	@app.route('/')
	def root():
		return 'Welcome to TweetOff!'	

	return app
