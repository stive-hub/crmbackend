console.log("Hello World");


function reAssign(lead) {
    console.log(`Reassign function working ${lead.id}`)
}

// function to display lead information in a modal
$(document).ready(function () {
    $('#example').DataTable();
    $(".lead-detail").click(function () {
        fetch(`/leads/${this.id}`)
            .then((response) => {
                return response.json();
            })
            .then((leadjson) => {
                var leadData = `<p>: <strong>${leadjson.first_name}</strong></p>
                <p>: <strong>${leadjson.last_name}</strong></p> <p> : <strong>${leadjson.type_of_enquiry}</strong></p><p> : <strong>${leadjson.company}</strong></p><p>: <strong>${leadjson.email}</strong></p><p> : <strong>${leadjson.phone}</strong></p><p>: <strong>${leadjson.positions_to_fill}</strong></p><p>: <strong>${leadjson.service_requirements}</strong></p><p>: <strong>${leadjson.loc_of_hire}</strong></p><p>: <strong>${leadjson.industry}</strong></p><p>: <strong>${leadjson.comp_emp_strength}</strong></p><p>: <strong>${leadjson.form_submission_time}</strong></p><p>: <strong>${leadjson.form_type }</strong></p>`
                $(".lead-data").html(leadData)
                var leadStatus = leadjson.status.name
                $('#leadStatus').text(leadStatus)
                $('#currentStatus').text(leadStatus)
                $('#changeStatusForm').attr('action', `leads/${this.id}`);


                console.log($('#status').val())
                // const data = { status: `${$('#status').val()}` };

                fetch(`/leads/${this.id}`, {
                    method: 'PATCH', // or 'PUT'
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data),
                })
                    .then((response) => response.json())
                    .then((data) => {
                        console.log('Success:', data);
                    })
                    .catch((error) => {
                        console.error('Error:', error);
                    });
            });
        
        $("#myModal").modal();
    });
    $(".lead-reassign").click(function () {
        console.log(`reassign : ${this.id}`)
    })
});
