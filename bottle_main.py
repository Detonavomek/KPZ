from jinja2 import Template
from bottle import route, run, request
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
import orm_functions as Controler

@route('/add')
def addPeople():
	passToFile = os.path.dirname(os.path.realpath(__file__))+'/site/registerAdd.htm'
	t = Template(open(passToFile, 'r').read())
	return t.render(peoples=Controler.GetPeople())

@route('/court')
def courtMeetingWork():
	passToFile = os.path.dirname(os.path.realpath(__file__))+'/site/courtMeeting.htm'
	t = Template(open(passToFile, 'r').read())
	return t.render(courts=Controler.GetCourts(), removals=Controler.GetRemovals(), court_meeting=Controler.GetCourtMeeting())

@route('/court', method='POST')
def postCourtMeetingWork():
	if request.forms.get('checkForm') == 'addCourtMeeting':
		Controler.AllAddCourtMeeting(request.forms.get('number_case'), request.forms.get('date_meeting'), request.forms.get('punishment'),
	 							request.forms.get('isNewCourt'), request.forms.get('courtId'), request.forms.get('name'),
	 							request.forms.get('isNewRemoval'), request.forms.get('removalId'), request.forms.get('reason'))
	else:
		for l in request.body:
			Controler.DeleteCourtMeeting(l.split('&')[1].split('=')[0])
	run(reloader=True)

run(host='localhost', port=8082, debug=True)