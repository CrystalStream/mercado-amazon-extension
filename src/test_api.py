import unittest
from api import best_offer_app

class ApiTest(unittest.TestCase):
    def setUp(self):
        bo = best_offer_app()
        self.client = bo.test_client()
    
    def test_not_found_for_all_routes(self):
        req = self.client.get('/')
        self.assertDictEqual(req.get_json(), {'data': '404 not found'})
    
    def test_search(self):
        req = self.client.get('/api/search?q={}'.format())
        self.assertEqual(req.get_json(), {'status': '200'})

if __name__ == '__main__':
    unittest.main()
