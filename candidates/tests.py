from django.test import TestCase
import json

# Create your tests here.


class UrlTest(TestCase):
    def test_endpoit_get_request(self):
        response = self.client.get("/candidates")
        self.assertEqual(response.status_code, 200)

    def test_endpoit_post_request(self):
        data = {
            "name": "Txip",
            "workExperience": [
                {"start": "Jan 1998", "end": "Apr 2005"},
                {"start": "Jan 2005", "end": "Apr 2013"},
                {"start": "Feb 2015", "end": "May 2016"},
            ],
        }
        response = self.client.post(
            "/candidates", json.dumps(data), content_type="aplication/json"
        )
        self.assertEqual(response.status_code, 200)
