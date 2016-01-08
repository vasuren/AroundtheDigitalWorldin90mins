import requests


class Gateway:

    def get_data(self, url):
        response = requests.get(url)
        data = response.json()

        info = self.fetch_data(data)

        return info

    def fetch_data(self, data):
        temp = int(data['main']['temp'])
        name = data['name']
        weather_type = data['weather'][0]['description']

        informations = { 'temp': temp, 'name': name, 'weather_type': weather_type }

        return informations
