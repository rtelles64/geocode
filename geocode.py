#!/usr/bin/env python3

# Here we demonstrate the code-based version of http requests and responses for
# geolocating

import httplib2
import json

GOOGLE_API_KEY = 'YOUR KEY HERE!'
CLIENT_ID = 'FOURSQUARE CLIENT ID HERE'
CLIENT_SECRET = 'FOURSQUARE CLIENT SECRET HERE'


def getGeocodeLocation(input_string):
    '''
        Gets geocode location from input_string.

        Params:
            input_string (str): String to retrieve geolocation from
                (e.g. "Dallas, Texas")

        Returns:
            results (tup): A tuple containing latitude and longitude of input
    '''
    google_api_key = GOOGLE_API_KEY

    # NOTE: having api keys viewable in live code isn't safe, but is fine for
    #       this demonstration

    # Replace spaces with '+' to avoid breaks in the url code for the server to
    # read correctly
    location_string = input_string.replace(" ", "+")

    # Build the url
    url = ('https://maps.googleapis.com/maps/api/geocode/json?'
           'address=%s&key=%s' % (location_string, google_api_key))

    # Create an instance of the http class
    h1 = httplib2.Http()

    # Create a GET request with the request() method
    # This request returns an array with two values, the http response and
    # the content
    response, content = h1.request(url, 'GET')

    # Use json.loads() on content to format it in a way that is easier to read,
    # in proper JSON format
    # NOTE: decode('utf-8') necessary for json.loads() as it is a 'bytes' class
    result = json.loads(content.decode('utf-8'))

    # print response to the terminal to see what it looks like
    # print("response header: %s \n\n" % response)

    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']

    return (latitude, longitude)


"""
print("response header: ...") prints out:

response header: {
    'access-control-allow-origin': '*',
    'content-type': 'application/json; charset=UTF-8',
    'content-location': 'https://maps.googleapis.com/maps/api/geocode/json?
        address=Dallas,+Texas&key=AIzaSyDckUaUMhwJ5nSW4iJgvqQlHIrts4DLuZ4',
    'cache-control': 'public, max-age=86400',
    '-content-encoding': 'gzip',
    'x-xss-protection': '0',
    'expires': 'Sat, 25 May 2019 00:12:39 GMT',
    'content-length': '1725',
    'date': 'Fri, 24 May 2019 00:12:39 GMT',
    'server': 'mafe',
    'server-timing': 'gfet4t7; dur=685',
    'alt-svc': 'quic=":443"; ma=2592000; v="46,44,43,39"',
    'vary': 'Accept-Language',
    'x-frame-options': 'SAMEORIGIN',
    'status': '200'}

result returns:

{
    'results': [
        {'types': ['locality', 'political'],
         'place_id': 'ChIJS5dFe_cZTIYRj2dH9qSb7Lk',
         'formatted_address': 'Dallas, TX, USA',
         'geometry': {
            'bounds': {
                'northeast': {
                    'lat': 33.0237921,
                    'lng': -96.4637379
                },
                'southwest': {
                    'lat': 32.617537,
                    'lng': -96.999347
                }
            },
            'location': {
                'lat': 32.7766642,
                'lng': -96.79698789999999
            },
            'location_type': 'APPROXIMATE',
            'viewport': {
                'northeast': {
                    'lat': 33.0237921,
                    'lng': -96.4637379
                },
                'southwest': {
                    'lat': 32.617537,
                    'lng': -96.999347
                }
            }
         },
         'address_components': [
            {'short_name': 'Dallas',
             'long_name': 'Dallas',
             'types': ['locality', 'political']
            },
            {'short_name': 'Dallas County',
             'long_name': 'Dallas County',
             'types': ['administrative_area_level_2', 'political']
            },
            {'short_name': 'TX',
             'long_name': 'Texas',
             'types': ['administrative_area_level_1', 'political']
            },
            {'short_name': 'US',
             'long_name': 'United States',
             'types': ['country', 'political']
            }
         ]}
    ],
    'status': 'OK'
}
"""

# Mashup:
# Now include the foursquare api


def findRestaurant(meal_type, location):
    '''
        Gets a restaurant from given meal_type query and location (lat, lng).

        Params:
            meal_type (str): Meal to search for
            location (str): Latitude and longitude to search for meal

        Returns:
            restaurants (lst): A list containing dictionaries with restaurant
                names, addresses, and images
    '''
    # Use the keys from postman
    foursquare_client_id = CLIENT_ID
    foursqr_client_secret = CLIENT_SECRET
    version = '20190523' # This is just a date
    query = meal_type.lower()
    limit = '1'  # just return one restaurant

    # 1. Geocode the location
    latitude, longitude = getGeocodeLocation(location)

    # 2. Search for restaurants
    # HINT: format for url should be something like:
    #   https://api.foursquare.com/v2/venues/search?
    #   client_id=CLIENT_ID&client_secret=CLIENT_SECRET
    #   &v=20130815&ll=40.7,-74&query=sushi
    url = (
        'https://api.foursquare.com/v2/venues/search?'
        'client_id=%s&client_secret=%s'
        '&v=%s&ll=%s,%s&query=%s&limit=%s' %
        (foursquare_client_id,
         foursqr_client_secret,
         version,
         latitude,
         longitude,
         query,
         limit)
    )

    h2 = httplib2.Http()
    response, content = h2.request(url, 'GET')
    result = json.loads(content.decode('utf-8'))

    if result['response']['venues']:
        # 3. Parse response and return one restaurant
        restaurant = result['response']['venues'][0]
        venue_id = restaurant['id']
        restaurant_name = restaurant['name']
        restaurant_address = ', '.join(
            restaurant['location']['formattedAddress']
        )

        # 4. Get a 300x300 picture of the restaurant using venue_id (you can
        #    change this by altering the 300x300 value in the URL or replacing
        #    it with 'orginal' to get the original picture)
        #
        # Image address prefix
        url = (
            'https://api.foursquare.com/v2/venues/%s/photos?client_id=%s'
            '&v=20150603&client_secret=%s' %
            (venue_id, foursquare_client_id, foursqr_client_secret)
        )

        # 5. Grab first image
        # 6. If no image, insert a default image url
        result = json.loads(h2.request(url, 'GET')[1])

        if result['response']['photos']['items']:
            firstpic = result['response']['photos']['items'][0]
            prefix = firstpic['prefix']
            suffix = firstpic['suffix']
            imageURL = prefix + '300x300' + suffix
        else:
            imageURL = ('http://pixabay.com/get/8926af5eb597ca51ca4c'
                        '/1433440765/cheeseburger-34314_1280.png?direct')

        # 7. Return a dictionary containing the restaurant name, address, and
        #    image url
        restaurantInfo = {
            'name': restaurant_name,
            'address': restaurant_address,
            'image': imageURL
        }

        print("Restaurant Name: %s" % restaurantInfo['name'])
        print("Restaurant Address: %s" % restaurantInfo['address'])
        print("Image: %s \n" % restaurantInfo['image'])

        return restaurantInfo
    else:
        print("No Restaurants Found for %s" % location)
        return "No Restaurants Found"


if __name__ == '__main__':
    findRestaurant("Pizza", "Tokyo, Japan")
    findRestaurant("Tacos", "Jakarta, Indonesia")
    findRestaurant("Tapas", "Maputo, Mozambique")
    findRestaurant("Falafel", "Cairo, Egypt")
    findRestaurant("Spaghetti", "New Delhi, India")
    findRestaurant("Cappuccino", "Geneva, Switzerland")
    findRestaurant("Sushi", "Los Angeles, California")
    findRestaurant("Steak", "La Paz, Bolivia")
    findRestaurant("Gyros", "Sydney, Australia")
