from rest_framework import serializers
from leads.models import Lead
from leads.utils import assign_salesperson

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = [
            'first_name', 'last_name', 'type_of_enquiry',
            'company', 'email', 'phone', 'role', 'message',
            'positions_to_fill', 'service_requirements', 
            'loc_of_hire', 'industry', 'comp_emp_strength',
            'form_submission_time', 'form_type', 'status',
            'source'     
        ]
    
    def create(self, validated_data):
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        type_of_enquiry = self.validated_data['type_of_enquiry']
        company = self.validated_data['company']
        email = self.validated_data['email']
        phone = self.validated_data['phone']
        role = self.validated_data['role']
        message = self.validated_data['message']
        positions_to_fill = self.validated_data['positions_to_fill']
        service_requirements = self.validated_data['service_requirements']
        loc_of_hire = self.validated_data['loc_of_hire']
        industry = self.validated_data['industry']
        comp_emp_strength = self.validated_data['comp_emp_strength']
        form_submission_time = self.validated_data['form_submission_time']
        form_type = self.validated_data['form_type']
        status = self.validated_data['status']
        source = self.validated_data['source']
        # assigned_to = assign_salesperson()
        lead_object = Lead(first_name=first_name, last_name=last_name , type_of_enquiry=type_of_enquiry, company=company, email=email, phone=phone, role=role, message=message, positions_to_fill=positions_to_fill, service_requirements=service_requirements, loc_of_hire=loc_of_hire, industry=industry, comp_emp_strength=comp_emp_strength, form_submission_time=form_submission_time, form_type=form_type, status=status, source=source)
        lead_object.save()
        lead_object.assigned_to.set([assign_salesperson()])
        return lead_object




    
