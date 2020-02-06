console.log("Hello World");


function reAssign(lead) {
    console.log(`Reassign function working ${lead.id}`)
}

// function to display lead information in a modal
$(document).ready(function () {
    $(".lead-detail").click(function () {
        console.log(` ${this.id}`)
        fetch(`/leads/${this.id}`)
            .then((response) => {
                return response.json();
            })
            .then((leadjson) => {
                var leadData = `<p>First Name : <strong>${leadjson.first_name}</strong></p>
                <p>Last Name : <strong>${leadjson.last_name}</strong></p> <p>Type of Enquiry : <strong>${leadjson.type_of_enquiry}</strong></p><p> Company : <strong>${leadjson.company}</strong></p><p> Email : <strong>${leadjson.email}</strong></p><p> Phone : <strong>${leadjson.phone}</strong></p><p> Number of Positions to fill : <strong>${leadjson.positions_to_fill}</strong></p><p>Service Requirements : <strong>${leadjson.service_requirements}</strong></p><p> Location of Hire : <strong>${leadjson.loc_of_hire}</strong></p><p> Industry : <strong>${leadjson.industry}</strong></p><p> Company Employee Strength : <strong>${leadjson.comp_emp_strength}</strong></p><p> Form Submission Time : <strong>${leadjson.form_submission_time}</strong></p><p> Form Type : <strong>${leadjson.form_type }</strong></p>`
                $(".lead-data").html(leadData)

                var leadForm = `<form><label>Current Lead Status :</label>
                <select class="form-control" id="leadstatus">
                  <option>${leadjson.status.name}</option>
                  <option>Not Updated</option>
                  <option>Meeting</option>
                  <option>Proposal</option>
                </select></form>`
                $(".lead-form").html(leadForm)
            });
        
        $("#myModal").modal();
    });
});
$(document).ready(function() {
    $('#example').DataTable();
} );