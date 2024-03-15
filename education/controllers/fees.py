import frappe
from frappe.utils import money_in_words

def get_student_dicount(doc,event):
    sql_query = """
            SELECT SUM(discount_percent) as total_discount
            FROM `tabStudents Discount` 
            WHERE parent = %s
        """
    total_discount = frappe.db.sql(sql_query, (doc.student,), as_dict=True)
    total_discount =total_discount[0].get('total_discount', 0)
    if not total_discount:
        total_discount = 0.0
    doc.student_discount = total_discount

    doc.actual_total = doc.grand_total - ( doc.grand_total * ((float(total_discount) / 100)))
    doc.grand_total_in_words = money_in_words(doc.actual_total)

    doc.outstanding_amount = doc.actual_total
    
 