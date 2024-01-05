# Copyright (c) 2023, ahmed ramzi and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    columns, data = [], []
    columns = get_columns(filters)
    data = get_data(filters)
    return columns, data

def get_columns(filters):

	columns = [
		
		{
		   "fieldname": "program",
			"label":_("المرحله"),
			"fieldtype": "Link",
			"options":"Program",
			 "width": 200
	
		},
		
		
		{
			"label": _("بنين"),
			"fieldname": "male",
			"fieldtype": "Int",
			
			 "width": 100
		
		
		},
		{
			"label": _("بنات"),
			"fieldname": "female",
			"fieldtype": "Int",
			 "width": 100
		
		
		},{
			"label": _("جمله"),
			"fieldname": "total",
			"fieldtype": "Int",
			 "width": 100
		
		
		},
		{
			"label": _("مسلم"),
			"fieldname": "muslim",
			"fieldtype": "Int",
			 "width": 100
		
		
		},
		{
			"label": _("مسيحي"),
			"fieldname": "christian",
			"fieldtype": "Int",
		 "width": 100
		
		},
		{
			"label": _("دمج"),
			"fieldname": "mirge",
			"fieldtype": "Int", 
			"width": 100
		
		
		},
		{
			"label": _("ابناء شهيد او مصاب"),
			"fieldname": "shahid",
			"fieldtype": "Int",
			 "width": 200
		
		
		},
	
		

	]

	return columns

def get_data(filters):
		data = []
		
	
		filter=set_program_filters(filters)
	

		programs = frappe.db.get_all("Program",filters=filter, pluck="name")
	
		if len(programs):
			for program in programs:
				program_data={}
				program_data["program"]=program
				male_count=get_gender_count(program,"Male")
				program_data["male"]=male_count
				female_count=get_gender_count(program,"Female")
				program_data["female"]=female_count
				program_data["total"]=male_count+female_count
				muslim=get_religion_count(program,"مسلم")
				program_data["muslim"]=muslim
				christian=get_religion_count(program,"مسيحي")
				program_data["christian"]=christian

				mirge=get_status_count(program,"دمج")
				program_data["mirge"]=mirge
				shahid=get_status_count(program,"أبناء شهيد")
				program_data["shahid"]=shahid

				data.append(program_data)
				
			

		return data




def get_gender_count (program,gender):
	gender_count=0
	students=frappe.db.get_all("Program Enrollment",filters={"program":program},pluck="student")
	
	for student in students:
		student_gender= frappe.db.get_value("Student",{"name":student},"gender")
		
		if student_gender == gender:
			gender_count+=1
	return gender_count


def get_religion_count (program,religion):
	religion_count=0
	students=frappe.db.get_all("Program Enrollment",filters={"program":program},pluck="student")
	
	for student in students:
		student_religion= frappe.db.get_value("Student",{"name":student},"religion")
		
		if student_religion == religion:
			religion_count+=1
	return religion_count

def get_status_count (program,student_status):
	status_count=0
	students=frappe.db.get_all("Program Enrollment",filters={"program":program},pluck="student")
	
	for student in students:
		student_status_= frappe.db.get_value("Student",{"name":student},"student_status")
	

		if student_status_ == student_status:
			status_count+=1
	return status_count

def arrange_students_by_gender(students, gender_first):
   
    students_sorted = sorted(students, key=lambda x: x['gender'] != gender_first)

    return students_sorted

def set_program_filters(filters):
    program_filters = {}

    if filters.get("program"):
        program_filters["name"] = ["in", filters.get("program")]



    return program_filters