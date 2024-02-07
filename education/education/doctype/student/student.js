// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student', {
	refresh: function(frm) {
	
	   
		frm.set_query("user", function (doc) {
			return {
				filters: {
					ignore_user_type: 1,
				},
			};
		});

		if(!frm.is_new()) {
			frm.add_custom_button(__('Accounting Ledger'), function() {
				frappe.set_route('query-report', 'General Ledger',
					{party_type:'Student', party:frm.doc.name});
			});
		}

		frappe.db.get_single_value('Education Settings', 'user_creation_skip')
			.then((r) => {
				if (cint(r) !== 1) {
					frm.set_df_property('student_email_id', 'reqd', 1);
			}
		});
	},
	date_of_birth:function(frm){
		if (frm.doc.date_of_birth){
		frappe.call({
			method:"age_in_detail_on_last_october_date",
			doc:frm.doc,
			args:{"birthday_date":frm.doc.date_of_birth},
			callback:function(r){
				
				if (r.message){
				frm.set_value("number_of_years_october",r.message)}
			}
		})}
	}
});

frappe.ui.form.on('Student Guardian', {
	guardians_add: function(frm){
		frm.fields_dict['guardians'].grid.get_field('guardian').get_query = function(doc){
			let guardian_list = [];
			if(!doc.__islocal) guardian_list.push(doc.guardian);
			$.each(doc.guardians, function(idx, val){
				if (val.guardian) guardian_list.push(val.guardian);
			});
			return { filters: [['Guardian', 'name', 'not in', guardian_list]] };
		};
	}
});
frappe.ui.form.on('Student Sibling', {
	student:(frm,cdt,cdn)=>{
		let row=locals[cdt][cdn]
		
		frappe.call({
			method: "education.education.doctype.student.student.get_student_data",
			args: {
			  student: row.student,
			
			},
		
			callback: function (r) {
				
				if (r.message[0]){

					row.custom_actual_academic_year=r.message[0]
					
				}
				if (r.message[1]){
					row.program=r.message[1]
					
				}
				
			}})
			frappe.db.get_value('Student', row.student, 'date_of_birth')
			.then(r => {
				row.date_of_birth=r.message.date_of_birth // Open
			})
			frm.refresh()
	}
});
cur_frm.set_query('program', 'siblings',  function(frm, cdt, cdn) {
	var d = locals[cdt][cdn];
    return {
      query:
        'education.education.doctype.student.student.program',
		filters:{"parent":d.custom_actual_academic_year}
    };
    
  
    
 

});
