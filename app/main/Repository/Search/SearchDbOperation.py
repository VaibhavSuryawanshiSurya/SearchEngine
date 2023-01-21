try:
	from app.main.Utils.Logger.logging import *
	from app.main.Repository.Search.db_config import *
	from app.main.Controller.Root.ExtensionRootRemove import *
	from app.main.Business.Search.SearchDbOperationAbstract import *

except Exception as e:
    print(e,'\n')


class DbOperation(Database):

	def createTable(self):
		query_result_table = """CREATE TABLE resulthistory(filename TEXT NOT NULL, url TEXT NOT NULL)"""
		query_userInfo_table = """CREATE TABLE userinfo(id serial primary key, username TEXT NOT NULL, password TEXT NOT NULL)"""
		query_transaction_table = """CREATE TABLE transaction(id serial primary key, transactionsdate DATE  NOT NULL, operation TEXT NOT NULL, filename TEXT NOT NULL)"""
		
		conn = dbConnection()
		cur = conn.cursor()
		try:
			cur.execute(query_userInfo_table);
			print(f"userinfo table created")

		except:
			print(f"resulthistory table already exists")
			pass

		try:
			cur.execute(query_result_table);
			print(f"resulthistory table created")
		except:
			print(f"resulthistory table already exists")
			pass
		
		try:
			cur.execute(query_transaction_table);
			print(f"Transaction table created")
		except:
			print(f"resulthistory table already exists")
			pass
		

		conn.commit()
		close_conn(conn, cur)


	def insertInputPath(self, filename,path):

		query = """ INSERT INTO public.resulthistory(filename,url) VALUES('{}','{}') """

		conn = dbConnection()
		cur = conn.cursor()
		cur.execute(query.format(filename,path));
		conn.commit()
		close_conn(conn, cur)


	def deleteDuplicateRow(self):

		query = ''' WITH ResultCTE AS 
		( 
			SELECT *, 
	        ROW_NUMBER() OVER (PARTITION BY url ORDER BY url ) 
	        as row_num
	     	FROM public.resulthistory 
	     )
		DELETE FROM ResultCTE
		WHERE row_num > 1;'''

		
		conn = dbConnection()
		cur = conn.cursor()

		cur.execute(query)

		conn.commit()
		close_conn(conn, cur)


	def searchResultPath(self, filename, drive):
		result_list = []

		# deleteDuplicateRow()

		query = "SELECT filename, url from public.resulthistory"

		conn = dbConnection()
		cur = conn.cursor()

		cur.execute(query)
		result = cur.fetchall()

		conn.commit()
		close_conn(conn, cur)

		ER = ExtensionRemove()

		for r in result:
			FileNameWithoutExtension = ER.inputFileNameExtensionRemove(r[0])

			if filename.lower() == FileNameWithoutExtension.lower() and r[1][0:2] in drive:
				result_list.append(r[1])
		
		return result_list


	def deletePath(self, filename):

		query = "DELETE FROM public.resulthistory WHERE resulthistory.filename = '{}'"

		conn = dbConnection()
		cur = conn.cursor()

		cur.execute(query.format(filename))

		conn.commit()
		close_conn(conn, cur)


	def insertUserInfo(self, user_name, password):

		query = """ INSERT INTO public.userinfo(username,password) VALUES('{}','{}') """

		conn = dbConnection()
		cur = conn.cursor()
		cur.execute(query.format(user_name,password));
		conn.commit()
		close_conn(conn, cur)


	def searchUserInfo(self, user_name, password):
		result_list = []

		# deleteDuplicateRow()

		query = "SELECT username, password from public.userinfo WHERE userinfo.username = '{}'"

		conn = dbConnection()
		cur = conn.cursor()

		cur.execute(query.format(user_name))
		result = cur.fetchall()

		conn.commit()
		close_conn(conn, cur)

		return result


def main():
	# create_table()
	# insert_input('vai','D:javvj')
	result_list = searchResult('vai')
	print(result_list)
	pass


if __name__ == '__main__':
	main()