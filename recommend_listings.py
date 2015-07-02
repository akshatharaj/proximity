import logging
from collections import namedtuple
from geopy.distance import vincenty

from db_connection import get_mysql_connection
from load_data import get_nearest_zips_for_lat_lon

logger = logging.getLogger(__name__)

def get_nearest_zips_codes(home):
	nearest_zips = get_nearest_zips_for_lat_lon(home.lat, home.lon, nearest=4)
	retval = ""
	for zipcode in nearest_zips:
		retval += "'%s', " % zipcode['postalCode']
	retval = retval.rstrip(', ')
	return retval

def find_similar_listings(home): 
	cur = get_mysql_connection().cursor()

	cur.execute("""select * from listing where (abs(num_bedrooms - %d) <= 1 or 
		abs(num_bathrooms - %d) <= 1) and zip in (%s) """ % (home.num_bedrooms, home.num_bathrooms, 
		get_nearest_zips_codes(home)))

	similar_listings = cur.fetchall()

	print_listings(similar_listings)

def print_listings(listings):
	print('================= Listings you might like ======================\n\n')
	for listing in listings:
		print('Lat: %s' % listing[4])
		print('Lon: %s' % listing[5])
		print('# bedrooms: %s' % listing[1])
		print('# bathrooms: %s' % listing[2])
		print('Dwelling type: %s' % listing[8])
		print('List price: %s' % listing[10])
		print('----------------------------------------------------------------\n')


Home = namedtuple('Home', 
	['num_bedrooms', 'num_bathrooms', 'living_area', 'lat', 'lon', 'exterior_stories', 'pool', 'dwelling_type'])


if __name__ == '__main__':
	# to provide a different home that you want to see similar listings for, please edit object below
	home = Home(3, 4, 3453, 33.200, -112.110, 1, 'private', 'loft')
	logger.info('Trying to find closest match for the home you provided...')
	find_similar_listings(home)