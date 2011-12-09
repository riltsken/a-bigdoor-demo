function multiform(){
    this.total_forms = parseInt($('#id_form-TOTAL_FORMS').val());
    this.initial_forms = parseInt($('#id_form-INITIAL_FORMS').val());
	this.addAnother = function(formName,addButtonId){
		$(addButtonId).click(function(){
			var zero_based_total = total_forms - 1;
			var last_added_form = "#" + formName + "-form-" + zero_based_total;
			
			// copy the html and increment all id's
			form = $("fieldset div:contains(Activity)").first().html(); // grab the first form
			form = "<div id='" + formName + "-form-" + (zero_based_total + 1) + "'>" + form + "</div>";
			form = form.replace(RegExp("form-" + "0", "g"), "form-" + (zero_based_total + 1))
			
			// increment the forms
			total_forms += 1;
			$("#id_form-TOTAL_FORMS").val(total_forms);
		
			$(last_added_form).after(form);

			// clear any data on the new form
			$("#" + formName + "-form-" + (zero_based_total + 1) + " :input").each(function(){
				$(this).val("");
			})
		});
	}
}

