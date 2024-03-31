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
            "label": _("Name In Arabic"),
            "fieldname": "name_arabic",
            "fieldtype": "Data",
        
            "width": 400,
        },
    
        {
           "fieldname": "name",
            "label":_("Name"),
            "fieldtype": "Data",
            "width": 400,
        }
        
        
    
        

    ]

    return columns

def get_data(filters):
    data = []

    # Constructing the SQL query based on filters
    sql_query = """
        SELECT s.full_name_in_arabic, s.student_name, s.name
        FROM `tabStudent` s
        """
    if filters.get("name_lang") == "Name In Arabic":
        if  filters.get("actual_academic_year"):
            sql_query += "WHERE s.actual_academic_year = %(actual_academic_year)s ORDER BY s.full_name_in_arabic"
        else:
            sql_query += "ORDER BY s.full_name_in_arabic"    
    else:
        if  filters.get("actual_academic_year"):
            sql_query += "WHERE s.actual_academic_year = %(actual_academic_year)s ORDER BY s.student_name"
        else:
            sql_query += "ORDER BY s.student_name"

    # Executing the SQL query
    students = frappe.db.sql(sql_query, {"actual_academic_year": filters.get("actual_academic_year")}, as_dict=True)

    if students:
        for student in students:
            student_data = {
                "name": student["student_name"],
                "name_arabic": student["full_name_in_arabic"]
            }

            # Fetching program enrollment data once for each student
            program_enrollment = frappe.db.sql("""
                SELECT name
                FROM `tabProgram Enrollment`
                WHERE student = %(student_name)s
                AND program = %(program)s
                AND academic_year = %(academic_year)s
                """,
                {"student_name": student["name"], "program": filters.get("program"), "academic_year": filters.get("academic_year")},
                as_dict=True
            )

            if filters.get("show_all") or program_enrollment:
                if not filters.get("program") or not filters.get("academic_year") or program_enrollment:
                    data.append(student_data)

    return data




def arrange_students_by_gender(students, gender_first):
   
    students_sorted = sorted(students, key=lambda x: x['gender'] != gender_first)

    return students_sorted
