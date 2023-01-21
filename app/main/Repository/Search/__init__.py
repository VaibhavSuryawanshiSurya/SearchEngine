try:
	from app.main.Repository.Search.SearchDbOperation import *
except Exception as e:
    print(e,'\n')


DB = DbOperation()

DB.createTable()