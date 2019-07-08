import unittest
from unittest import mock
from api import best_offer_app
import config
import fixtures

DATA_TEST = {
    'test_one': {
        'query': 'asdfqwer'
    },
    'test_two': {
        'query': 'Bicicletas',
        'results': fixtures.ML_TEST_1,
    },
    'test_three': {
        'query': 'Relojes',
        'results': fixtures.AMZN_TEST_1,
    },
    'test_four': {
        'query': 'Tablas de surf',
    }
}

def best_offer_mock_request(query):
    switcher = {
        config.get_ml_url_for(DATA_TEST['test_one']['query']): '',
        config.get_ml_url_for(DATA_TEST['test_two']['query']): DATA_TEST['test_two']['results'],
        config.get_amazon_url_for(DATA_TEST['test_three']['query']): DATA_TEST['test_three']['results'],
        config.get_ml_url_for(DATA_TEST['test_four']['query']): fixtures.ML_TEST_1,
        config.get_amazon_url_for(DATA_TEST['test_four']['query']): fixtures.AMZN_TEST_1,
    }
    return switcher.get(query, '')


class ApiTest(unittest.TestCase):
    def setUp(self):
        bo = best_offer_app()
        self.client = bo.test_client()
    
    def test_not_found_for_all_routes(self):
        req = self.client.get('/')
        self.assertDictEqual(req.get_json(), {'results': 'not found', 'status_code':  404})

    @mock.patch('api.urlopen', side_effect=best_offer_mock_request)
    def test_search_no_result(self, mock_get):
        query = DATA_TEST['test_one']['query']
        req = self.client.get('/api/search?q={}'.format(query)).get_json()
        code = req['status_code']
        data = req['results']

        self.assertEqual(code, 200)
        self.assertEqual(len(data), 2)
        self.assertEqual(len(data[0]), 0)
        self.assertEqual(len(data[1]), 0)

    @mock.patch('api.urlopen', side_effect=best_offer_mock_request)
    def test_search_result_ml(self, mock_get):
        query = DATA_TEST['test_two']['query']
        req = self.client.get('/api/search?q={}'.format(query)).get_json()
        code = req['status_code']
        data = req['results']

        self.assertEqual(code, 200)
        self.assertEqual(len(data), 2)
        self.assertEqual(len(data[0]), 3)
        self.assertEqual(len(data[1]), 0)

    @mock.patch('api.urlopen', side_effect=best_offer_mock_request)
    def test_search_result_amzn(self, mock_get):
        query = DATA_TEST['test_three']['query']
        req = self.client.get('/api/search?q={}'.format(query)).get_json()
        code = req['status_code']
        data = req['results']
        
        self.assertEqual(code, 200)
        self.assertEqual(len(data), 2)
        self.assertEqual(len(data[0]), 0)
        self.assertEqual(len(data[1]), 1)
    
    @mock.patch('api.urlopen', side_effect=best_offer_mock_request)
    def test_search_result_both(self, mock_get):
        query = DATA_TEST['test_four']['query']
        req = self.client.get('/api/search?q={}'.format(query)).get_json()
        code = req['status_code']
        data = req['results']
        
        self.assertEqual(code, 200)
        self.assertEqual(len(data), 2)
        self.assertEqual(len(data[0]), 3)
        self.assertEqual(len(data[1]), 1)

if __name__ == '__main__':
    unittest.main()
