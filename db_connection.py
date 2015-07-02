import pymysql

DATABASE = {
        'db': 'proximity',
        'user': 'tuto_user',
        'passwd': 'password',
        'host': 'localhost',
        'port': 3306
    }


def get_mysql_connection():
	conn = pymysql.connect(**DATABASE)
	conn.autocommit(1)
	return conn