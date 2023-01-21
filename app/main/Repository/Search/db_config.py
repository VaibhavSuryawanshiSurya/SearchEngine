try:
	import psycopg2
	from app.main.Utils.Logger.logging import *

except Exception as e:
    print(e,'\n')

db = {
	'host' : 'localhost',
	'user' : 'postgres',
	'password' : 'root@123',
	'database' : 'SearchHistory'
}


def dbConnection():

	conn = None
	try:
		conn = psycopg2.connect(**db)
		return conn
	except (Exception, psycopg2.DatabaseError) as e:
		print(e)


def close_conn(conn, cur):
	cur.close()
	conn.close()


def main():
	create_table()
	pass

if __name__ == '__main__':
	main()