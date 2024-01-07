// Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["الميزانية"] = {
	"filters": [
	
		
		{
		  fieldname: "stage",
		  label: __("المرحله"),
		  fieldtype: "Select",
      options: ["KINDERGARTEN","SECONDARY","PREPARATORY",""]
     
		},
		

  ],
  tree: true,

  initial_depth: 3,
  formatter: function (value, row, column, data, default_formatter) {
	  value = default_formatter(value, row, column, data);
	  return value;
  },
};
