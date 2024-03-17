import frappe 
def get_student_actual_academic_year(doc,event):
    actual_academic_year = frappe.get_all("Academic Year Program", 
                                         fields = ["parent","program"])
    
    for  year in actual_academic_year:
        if year.get("program") == doc.program:
            frappe.db.set_value("Student",doc.student,"actual_academic_year",year.get("parent"))