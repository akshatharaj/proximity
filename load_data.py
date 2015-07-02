import logging
import httplib2
import json
import pymysql
from settings import DATABASE
from generate_data import generate_datum

logger = logging.getLogger()

# third party api url to get zip code for given lat, lng
ZIP_API_URL = 'http://ws.geonames.org/findNearbyPostalCodesJSON?formatted=true&lat=%s&lng=%s&maxRows=1&username=akshatharaj'

def get_zip_for_lat_lng(lat, lng):
    http = httplib2.Http()
    return json.loads((http.request(ZIP_API_URL % (lat, lng))[-1].decode('utf-8'))).get('postalCodes')[0].get('postalCode')

def get_mysql_connection():
	conn = pymysql.connect(**DATABASE)
	conn.autocommit(1)
	return conn

def load_listings():
	for i in range (0, 1):
		l = generate_datum()
		listing = l._asdict()
		cur = get_mysql_connection().cursor()
		listing['zip'] = get_zip_for_lat_lng(listing.get('lat'), listing.get('lon'))
		import pdb; pdb.set_trace()
		cur.execute("""insert into listing (num_bedrooms, num_bathrooms, living_area, lat, lon, 
			exterior_stories, pool, dwelling_type,	list_date, list_price, close_date, close_price, zip) 
		values (%(num_bedrooms)s, %(num_bathrooms)s, %(living_area)s, %(lat)s, %(lon)s, %(exterior_stories)s, 
			'%(pool)s', '%(dwelling_type)s', '%(list_date)s', %(list_price)s, '%(close_date)s', %(close_price)s, '%(zip)s' )""" % listing)

if __name__ == __main__:
	logger.info('Loading 10000 listings into database. Please wait...')
	load_listings()
	logging.info('Successfully loaded data into database!')
