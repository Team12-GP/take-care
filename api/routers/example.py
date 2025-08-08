from flask import Blueprint, redirect

home_hr = Blueprint('home', __name__)

@home_hr.route('/')
def index():
	return redirect("https://www.facebook.com/md.hr.o.o.2024", code = 301)

@home_hr.route('/about')
def about():
    return "This is the About Page."