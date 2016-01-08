from unittest import TestCase
from gateway import Gateway


class TestFetch_data(TestCase):
    def test_fetch_data(self):
        input = {"coord":{"lon":-0.13,"lat":51.51},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"base":"cmc stations","main":{"temp":279.68,"pressure":998,"humidity":87,"temp_min":278.15,"temp_max":281.15},"wind":{"speed":3.1,"deg":200},"rain":{"1h":0.25},"clouds":{"all":75},"dt":1452282912,"sys":{"type":1,"id":5091,"message":0.0111,"country":"GB","sunrise":1452240240,"sunset":1452269460},"id":2643743,"name":"London","cod":200}
        expected_output = {'name': 'London', 'weather_type': 'light rain', 'temp': 279.68}

        gateway = Gateway()
        output = gateway.fetch_data(input)
        self.assertEqual(expected_output, output)
