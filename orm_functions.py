#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
import orm_db_struct as DB

def GetCourts():
	return DB.session.query(DB.Court).filter().all()
def GetRemovals():
	return DB.session.query(DB.Removal).filter().all()
def GetCourtMeeting():
	return DB.session.query(DB.CourtMeeting, DB.Court, DB.Removal).join(DB.Court).join(DB.Removal).order_by(DB.CourtMeeting.court_meeting_id.asc()).filter().all()

def AddCourt(courtName):
	DB.session.add(DB.Court(name = courtName))
	DB.session_commit()
	res = DB.session.query(DB.Court).order_by(DB.Court.court_id.desc()).filter().all()
	return res[0].court_id
def AddRemoval(removalReason):
	DB.session.add(DB.Removal(reason = removalReason))
	DB.session_commit()
	res = DB.session.query(DB.Removal).order_by(DB.Removal.removal_id.desc()).filter().all()
	return res[0].removal_id
def AddCourtMeeting(gcourt_id,gremoval_id,gnumber_case,gdate_meeting,gpunishment):
	DB.session.add(DB.CourtMeeting(court_id=gcourt_id,removal_id=gremoval_id,number_case=gnumber_case,date_meeting=gdate_meeting,punishment=gpunishment))
	DB.session_commit()

def DeleteCourtMeeting(cm_id):
	DB.session.query(DB.CourtMeeting).filter(DB.CourtMeeting.court_meeting_id == cm_id).delete()
	DB.session_commit()

def AllAddCourtMeeting(number_case, date_meeting, punishment, isNewCourt, courtId, name, isNewRemoval, removalId, reason):
	gcourt_id = '0'
	gremoval_id = '0'
	if '0' in isNewCourt:
		gcourt_id = courtId
	else:
		gcourt_id = AddCourt(name)
	if '0' in isNewRemoval:
		gremoval_id = removalId
	else:
		gremoval_id = AddRemoval(reason)
	AddCourtMeeting(gcourt_id,gremoval_id,number_case,date_meeting,punishment)

# r = GetCourtMeeting()
# for rs in r:
# 	print rs.CourtMeeting.court_meeting_id,' - ',rs.CourtMeeting.date_meeting
# def GetPeople():
	# return DB.session.query(DB.People).filter().all()
# def AddPeople(gname,gsurname,gsecond_name,gbirthday,gbirth_place,gpassport_series,gpassport_number,ginn_code,gwork_place):
# 	DB.session.add(DB.People(name=gname,surname=gsurname,second_name=gsecond_name,birthday=gbirthday,birth_place=gbirth_place,passport_series=gpassport_series,passport_number=gpassport_number,inn_code=ginn_code,work_place=gwork_place))
# 	DB.session_commit()
# def AddViolance(gdate_do,gconstitution_alticle,gstruct,gcharact,gdate_start):
# 	DB.session.add(DB.Violance(date_do=gdate_do,constitution_alticle=gconstitution_alticle,struct=gstruct,charact=gcharact,date_start=gdate_start))
# 	DB.session_commit()
# def AddDisciplinaryAction(gstage_property,gway,gtype,greason,gdate,gnote):
# 	DB.session.add(DB.DisciplinaryAction(stage_property=gstage_property,way=gway,type=gtype,reason=greason,date=gdate,note=gnote))
# 	DB.session_commit()
# def AddRegister(people_id,violation_id,court_meeting_id,disciplinary_action_id,registrator_id):
# 	DB.session.add(DB.Register(people_id=people_id,violation_id=violation_id,court_meeting_id=court_meeting_id,disciplinary_action_id=disciplinary_action_id,registrator_id=registrator_id))
# 	DB.session_commit()
# def AddRegistrator(gname):
# 	DB.session.add(DB.Registrator(name=gname))
# 	DB.session_commit()
# def AddStatements(gstatements_types_id,gregistrator_id,gregister_id,gfullname_plaintiff,gdate,gnote):
# 	DB.session.add(DB.Statements(statements_types_id=gstatements_types_id,registrator_id=gregistrator_id,register_id=gregister_id,fullname_plaintiff=gfullname_plaintiff,date=gdate,note=gnote))
# 	DB.session_commit()
# def AddStatementsTypes(gname):
# 	DB.session.add(DB.StatementsTypes(name=gname))
# 	DB.session_commit()

# def GetPeopleForViolanceStruct(violanceStruct):
# 	rs = DB.session.query(DB.People).join(DB.Register).join(DB.Violance).filter(DB.Violance.struct == violanceStruct).all()
# 	for row in rs:
# 		print row.name, ' - ', row.surname

# def GetConstitutionArticleForStatementType(statementType):
# 	rs = DB.session.query(DB.Violance).join(DB.Register).join(DB.Statements).join(DB.StatementsTypes).filter(DB.StatementsTypes.name==statementType).all()
# 	for row in rs:
# 		print row.constitution_article

#GetConstitutionArticleForStatementType('Statement type 3')
#AddCourt('court begin')
#GetCourts()
#AddRemoval('ORM Removal Back Up') 
#AddCourtMeeting(23, 3,'number case test', '2010-10-10 21:38:11', 'test punishment wow')
#GetPeopleForViolanceStruct('Struct 2')