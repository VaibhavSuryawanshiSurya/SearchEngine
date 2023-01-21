try:
	from app.main.Repository.Search.db_config import *
	from app.main.Business.Analytics.TransactionModuleAbstract import *

except Exception as e:
    print(e,'\n')


class DbTransaction(Transaction):

	def insertTransactions(self,operation ,filename):

		query = """ INSERT INTO public.transaction(transactionsdate, operation, filename) VALUES(CURRENT_DATE ,'{}','{}') """

		conn = dbConnection()
		cur = conn.cursor()
		
		cur.execute(query.format(operation, filename));
		
		conn.commit()
		close_conn(conn, cur)


	def getAllTransactions(self):

		query = "SELECT transactionsdate, operation, filename from public.transaction"

		conn = dbConnection()
		cur = conn.cursor()

		cur.execute(query);
		result = cur.fetchall()

		conn.commit()
		close_conn(conn, cur)

		print('All Transactions:')
		
		for r in result:
			print(f'Date : {r[0]}\t Opeation : {r[1]}\t FileName : {r[2]}')


	def getTransactionBetweenDates(self, start_date, end_date):
		
		query = "SELECT transactionsdate, operation, filename from public.transaction WHERE transactionsdate BETWEEN '{}' AND '{}'"

		conn = dbConnection()
		cur = conn.cursor()

		cur.execute(query.format(start_date, end_date));
		result = cur.fetchall()

		conn.commit()
		close_conn(conn, cur)

		print('All Transactions:')
		
		for r in result:
			print(f'Date : {r[0]}\t Opeation : {r[1]}\t FileName : {r[2]}')
