try:
	from app.main.UI.SearchForm import *
	from app.main.Repository.Search.SearchDbOperation import *
	from app.main.Utils.Logger.logging import *
except Exception as e:
    print(e,'\n')


class UserLogin:

	def __init__(self):
		self.user_name = None
		self.password = None

	
	def checkLogiInfo(self, user_name, password):

		DB = DbOperation()

		result = DB.searchUserInfo(user_name, password)
		for r in result:
			if user_name == r[0] and password == r[1]:
				return True

		return False


def main():
	pass

if __name__ == '__main__':
	main()