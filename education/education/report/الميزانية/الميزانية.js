// Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["الميزانية"] = {
	"filters": [
	
		
		{
		  fieldname: "program",
		  label: __("Program"),
			
		  fieldtype: "MultiSelectList",
      options: "Program",
      get_data: function (txt) {
        return frappe.db.get_link_options("Program", txt);
      },
		  
		},
		

  ],
  tree: true,

  initial_depth: 3,
  formatter: function (value, row, column, data, default_formatter) {
	  value = default_formatter(value, row, column, data);
	  return value;
  },
};
