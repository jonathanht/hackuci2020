import json
import requests

x = 33.640495 # latitude
y = -117.844296 # longitude

coords = x, y

class RestaurantLocator:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._BaseURL = "https://api.yelp.com/v3/businesses/search"
        self._ID = "1Vp1MSf8DUcnw-OjS41qzQ" # Client ID
        self._API = "ljefBWbwtGtW4FYiVXEFj5qMXQMBaL08TR1mU6uCa421ZpT7ABj060EfqL7cJQTPRpek-P6-GtmiskfuwihuduS88ie0KDa7dIt2nFDLnQCjWni0aDkcdghjW0M1XnYx" # API Key
        self.headers = {'Authorization': 'Bearer %s' % self._API}
        self.param = {'term': 'food', 'location': 'Irvine'}
        self.filters = ['fast food', 'burgers']
        self.radius = 3000


    def constructURL(self):
        retList = []
        req = requests.get(self._BaseURL, params=self.param, headers=self.headers)
        print('The status code is {}'.format(req.status_code))
        data = json.loads(req.text)
        for item in data['businesses']:
            if item['distance'] < self.radius:
                innerList = []
                filtered = False
                for cdicts in item['categories']:
                    innerList.append(cdicts['alias'])
                for filter in innerList:
                    if filter in self.filters:
                        filtered = True
                if filtered:
                    pass
                else:
                    retList.append(item['name'])

        return retList



        #print json.dumps(data, indent=2, sort_keys=True) # prints all data about each business


if __name__ == "__main__":
    tester = RestaurantLocator(x, y)
    m = tester.constructURL()
    for item in m:
        print(item)
