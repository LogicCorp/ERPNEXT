import frappe 
def get_student_actual_academic_year(doc,event):
    actual_academic_year = frappe.get_all("Academic Year Program", 
                                         fields = ["parent","program"])
    
    for  year in actual_academic_year:
        if year.get("program") == doc.program:
            frappe.db.set_value("Student",doc.student,"actual_academic_year",year.get("parent"))

    siblings = frappe.get_all("Student Sibling",
				   filters={"student":doc.student},
				   pluck='name')
    frappe.db.set_value("Student",doc.student,"program_enrollment",doc.name)
    
    
				
    for seb in siblings:
        frappe.db.set_value("Student Sibling",seb,"program",doc.program)
        actual_academic_year = frappe.db.get_value("Student",doc.student,"actual_academic_year")
        gender = frappe.db.get_value("Student",doc.student,"gender")
        date_of_birth = frappe.db.get_value("Student",doc.student,"date_of_birth")
        student_name= frappe.db.get_value("Student",doc.student,"student_name")
        frappe.db.set_value("Student Sibling",seb,"custom_actual_academic_year",actual_academic_year)
        frappe.db.set_value("Student Sibling",seb,"full_name",student_name)
        frappe.db.set_value("Student Sibling",seb,"gender",gender)
        frappe.db.set_value("Student Sibling",seb,"date_of_birth",date_of_birth)
