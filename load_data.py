import logging
import httplib2
import json
from db_connection import get_mysql_connection
from generate_data import generate_datum

logger = logging.getLogger()

# third party api url to get zip code for given lat, lng
ZIP_API_URL = 'http://ws.geonames.org/findNearbyPostalCodesJSON?formatted=true&lat=%s&lng=%s&maxRows=%s&username=akshatharaj'
# how many listings do you want to see in the database?
DATA_SAMPLE_SIZE = 10000

def get_nearest_zips_for_lat_lon(lat, lon, nearest=1):
    """
    Talks to a third-party API and gets the nearest zip codes
    """
    http = httplib2.Http()
    return json.loads((http.request(ZIP_API_URL % (lat, lon, nearest))[-1].decode('utf-8'))).get('postalCodes')

def load_listings():
    """
    gets random listings and inserts into database
    """
    for i in range (0, DATA_SAMPLE_SIZE):
	    l = generate_datum()
	    listing = l._asdict()
	    cur = get_mysql_connection().cursor()
	    listing['zip'] = get_nearest_zips_for_lat_lon(listing.get('lat'), listing.get('lon'))[0].get('postalCode')
	    cur.execute("""insert into listing (num_bedrooms, num_bathrooms, living_area, lat, lon, 
	    	exterior_stories, pool, dwelling_type,	list_date, list_price, close_date, close_price, zip) 
	    values (%(num_bedrooms)s, %(num_bathrooms)s, %(living_area)s, %(lat)s, %(lon)s, %(exterior_stories)s, 
	    	'%(pool)s', '%(dwelling_type)s', '%(list_date)s', %(list_price)s, '%(close_date)s', %(close_price)s, '%(zip)s' )""" % listing)

if __name__ == '__main__':
	logger.info('Loading 10000 listings into database. Please wait...')
	load_listings()
	logging.info('Successfully loaded data into database!')
