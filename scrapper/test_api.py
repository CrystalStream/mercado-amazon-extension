import unittest
from unittest import mock
from app import app
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
    },
    'test_five': {
        'query': 'Playstation',
    },
    'test_six': {
        'query': 'Xbox',
    },
}

def best_offer_mock_request(query, headers):
    class MockResponse():
        def __init__(self, results):
            self.text = results

    switcher = {
        config.get_ml_url_for(DATA_TEST['test_one']['query']): MockResponse(''),
        config.get_ml_url_for(DATA_TEST['test_two']['query']): MockResponse(DATA_TEST['test_two']['results']),
        config.get_amazon_url_for(DATA_TEST['test_three']['query']): MockResponse(DATA_TEST['test_three']['results']),
        config.get_ml_url_for(DATA_TEST['test_four']['query']): MockResponse(fixtures.ML_TEST_1),
        config.get_amazon_url_for(DATA_TEST['test_four']['query']): MockResponse(fixtures.AMZN_TEST_1),
        config.get_ml_url_for(DATA_TEST['test_five']['query']): MockResponse(fixtures.ML_TEST_2),
        config.get_amazon_url_for(DATA_TEST['test_six']['query']): MockResponse(fixtures.AMZN_TEST_2),
    }
    return switcher.get(query, MockResponse(''))


class AppTest(unittest.TestCase):
    def setUp(self):
        bo = app
        self.client = bo.test_client()
    
    def test_not_found_for_all_routes(self):
        req = self.client.get('/')
        self.assertDictEqual(req.get_json(), {'results': 'not found', 'status_code':  404})

    @mock.patch('app.requests.get', side_effect=best_offer_mock_request)
    def test_search_no_result(self, mock_get):
        query = DATA_TEST['test_one']['query']
        req = self.client.get('/api/search?q={}'.format(query)).get_json()
        code = req['status_code']
        data = req['results']

        self.assertEqual(code, 200)
        self.assertEqual(len(data), 2)
        self.assertEqual(len(data[0]), 0)
        self.assertEqual(len(data[1]), 0)

    @mock.patch('app.requests.get', side_effect=best_offer_mock_request)
    def test_search_result_ml(self, mock_get):
        query = DATA_TEST['test_two']['query']
        req = self.client.get('/api/search?q={}'.format(query)).get_json()
        code = req['status_code']
        data = req['results']

        self.assertEqual(code, 200)
        self.assertEqual(len(data), 2)
        self.assertEqual(len(data[0]), 3)
        self.assertEqual(len(data[1]), 0)

    @mock.patch('app.requests.get', side_effect=best_offer_mock_request)
    def test_search_result_ml_second_layout(self, mock_get):
        query = DATA_TEST['test_five']['query']
        req = self.client.get('/api/search?q={}'.format(query)).get_json()
        code = req['status_code']
        data = req['results']

        self.assertEqual(code, 200)
        self.assertEqual(len(data), 2)
        self.assertEqual(len(data[0]), 3)
        self.assertEqual(len(data[1]), 0)

    @mock.patch('app.requests.get', side_effect=best_offer_mock_request)
    def test_search_result_amzn(self, mock_get):
        query = DATA_TEST['test_three']['query']
        req = self.client.get('/api/search?q={}'.format(query)).get_json()
        code = req['status_code']
        data = req['results']
        
        self.assertEqual(code, 200)
        self.assertEqual(len(data), 2)
        self.assertEqual(len(data[0]), 0)
        self.assertEqual(len(data[1]), 1)

    @mock.patch('app.requests.get', side_effect=best_offer_mock_request)
    def test_search_result_amzn_second_layout(self, mock_get):
        query = DATA_TEST['test_six']['query']
        req = self.client.get('/api/search?q={}'.format(query)).get_json()
        code = req['status_code']
        data = req['results']

        self.assertEqual(code, 200)
        self.assertEqual(len(data), 2)
        self.assertEqual(len(data[0]), 0)
        self.assertEqual(len(data[1]), 5)
    
    @mock.patch('app.requests.get', side_effect=best_offer_mock_request)
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
