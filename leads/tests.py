from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from leads.models import Lead
from salespersons.models import SalesPersonUser

# # Create your tests here.
class TestLeadModel(object):

    def setUp(self):
        self.client = Client()

        self.user = SalesPersonUser.objects.create(
            username='johnLead', email='johnLead@example.com', role="ADMIN")
        self.user.set_password('password')
        self.user.save()

        self.user1 = SalesPersonUser.objects.create(
            first_name="janeLead1",
            username='janeLead1',
            email='janeLead1@example.com',
            role="USER")
        self.user1.set_password('password')
        self.user1.save()

        self.lead = Lead.objects.create(first_name="jane doe",
                                        last_name="doe",
                                        email="janeDoe@example.com",
                                        source="call",
                                        message="lead description",
                                        phone="1234567890")
        self.lead.assigned_to.add(self.user)


        self.lead1 = Lead.objects.create(first_name="testing",
                                        last_name="app",
                                        email="testingapp@testing.com",
                                        source="campaign",
                                        message="testing description",
                                        phone="1234567890")
        self.lead.assigned_to.add(self.user)



class LeadsGetrequestTestCase(TestLeadModel, TestCase):

    def test_getrequest(self):
        res = self.client.get('http://localhost:8000/leads/')
        self.assertEqual(res.status_code, 200)


class LeadsPostrequestTestCase(TestLeadModel, TestCase):

    def test_postrequest(self):
        data = {'first_name': "user",
                'last_name': "test", 
                'email': "testuser@testing.com",
                "source": "call",
                'phone': "1234567890",
                'type_of_enquiry':'Sales Enquiry',
                'company': "testing company",
                'service_requirements': "Media testing",
                'loc_of_hire': 'intern',
                'message': "this message of lead",
                'status': 'BD call'
                }
        res = self.client.post('http://localhost:8000/leads', data)
        self.assertEqual(res.status_code, 301)


class  LeadsPutrequestTestCase(TestLeadModel, TestCase):
    def test_putrequest(self):
        url = 'http://localhost:8000/leads/' + str(self.lead.id)
        data = {'first_name': "user1",
                'last_name': "test1", 
                'email': "testuser1@testing.com",
                "source": "campaign",
                'phone': "1234567891",
                'type_of_enquiry':'Job Seeker',
                'company': "company",
                'service_requirements': "application testing",
                'loc_of_hire': 'application tester',
                'message': "this message is from employee"
                }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, 301)


class LeadsPatchrequestTestCase(TestLeadModel, TestCase):
        def test_patchrequest(self):
            url = 'http://localhost:8000/leads/' + str(self.lead.id)
            data = {
            'first_name': "update first", 'last_name': "update last name",
            'email': "testingLead@example.com",
            'phone': "1234567890",
            }
            response = self.client.patch(url, data)
            self.assertEqual(response.status_code, 301)


class LeadsDeleterequestTestCase(TestLeadModel, TestCase):

    def test_deleterequest(self):
        res = self.client.delete('http://localhost:8000/leads/' + str(self.lead1.id))
