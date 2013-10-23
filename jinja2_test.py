from jinja2 import Template
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
import orm_functions as Controler

passToFile = os.path.realpath(__file__)+'/site/registerAdd.htm'
t = Template(open(passToFile, 'r').read())
print t.render(peoples=Controler.GetPeople())