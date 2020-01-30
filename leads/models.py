from django.db import models
from salespersons.models import SalesPersonUser

LEAD_SOURCE = (
    ('call', 'Call'),
    ('website', 'Website'),
    ('email', 'Email'),
    ('existing customer', 'Existing Customer'),
    ('partner', 'Partner'),
    ('public relations', 'Public Relations'),
    ('compaign', 'Campaign'),
    ('other', 'Other'),
)

LEAD_STATUS = (
    ('not updated', 'Not Updated'),
    ('BD call', 'BD Call'),
    ('meeting', 'Meeting'),
    ('proposal', 'Proposal')
)

ROLE = (
    ('Business Owner/Leader', 'Business Owner/Leader'),
    ('Media', 'Media'),
    ('Director HR/Talent Acquisition', 'Director HR/Talent Acquisition'),
    ('Job Seeker', 'Job Seeker'),
    ('Recruiter/Sourcer', 'Recruiter/Sourcer')
)

ENQUIRY_TYPE = (
    ('Sales Enquiry', 'Sales Enquiry'),
    ('Job Seeker', 'Job Seeker'),
    ('Media','Media')
)


class Lead(models.Model):
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    type_of_enquiry = models.CharField("Type of Enquiry", max_length=255, choices=ENQUIRY_TYPE, default='Sales Enquiry', null=True)
    company = models.CharField("Company", max_length=255, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True)
    role = models.CharField("Role", max_length=60, choices=ROLE, default='Business Owner/Leader')
    message = models.TextField(null=True)
    positions_to_fill = models.BigIntegerField(default=10)
    service_requirements = models.CharField(max_length=100000, null=True)
    loc_of_hire = models.CharField(max_length=100000, null=True)
    industry = models.CharField(max_length=100000, null=True)
    comp_emp_strength = models.BigIntegerField(default=1)
    form_submission_time = models.CharField(max_length=100000, null=True)
    form_type = models.CharField(max_length=100000, null=True)
    status = models.CharField("Status of Lead", max_length=255,
                              blank=True, null=True, choices=LEAD_STATUS, default="not updated")
    source = models.CharField("Source of Lead", max_length=255,
                              blank=True, null=True, choices=LEAD_SOURCE, default="website")
    assigned_to = models.ManyToManyField(
        SalesPersonUser, related_name='lead_assigned_salespersonusers', default=1)
    createdOn = models.DateTimeField("Created on", auto_now_add=True)

    def __str__(self):
        return f"{self.email} with {self.first_name} {self.last_name}"
