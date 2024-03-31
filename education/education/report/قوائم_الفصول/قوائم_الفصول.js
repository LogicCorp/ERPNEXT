// Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["قوائم الفصول"] = {
	"filters": [
		{
			fieldname: "program",
			label: __("Program"),
			fieldtype: "Link",
			options: "Program",
			
		  },
		  {
			fieldname: "academic_year",
			label: __("Academic Year"),
			fieldtype: "Link",
			options: "Academic Year",
		  },
		  {
			fieldname: "actual_academic_year",
			label: __("Actual Academic Year"),
			fieldtype: "Link",
			options: "Actual Academic Year",
		  },
		
		
		{
		  fieldname: "based_on",
		  label: __("Arrange Names Based On"),
		  fieldtype: "Select",
		  options: ["Alphabet","Female","Male"],
		  default:"Alphabet"
		},
		{
			fieldname: "name_lang",
			label: __("Arrange Names Alphabet  Based On"),
			fieldtype: "Select",
			options: ["Name In Arabic","Name In English"],
			default:"Name In Arabic"
		  },
		  {
			fieldname: "show_all",
			label: __("Show All"),
			fieldtype: "Check",
			default:0
		  },
  ],
  tree: true,

  initial_depth: 3,
  formatter: function (value, row, column, data, default_formatter) {
	  value = default_formatter(value, row, column, data);
	  return value;
  },
};