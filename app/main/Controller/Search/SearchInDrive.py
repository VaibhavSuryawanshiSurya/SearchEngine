try:
	import os
	from app.main.Utils.Logger.logging import *
	from app.main.Controller.Root.ActiveRootFinder import *
	from app.main.Business.Search.SearchInDriveAbstract import *

except Exception as e:
    print(e,'\n')


class Search(SearchAbstract):

	def __init__(self):
		self.file_index=[]
		self.results=[]
		self.matches=0
		self.records=0
    
	def createNewIindex(self,root_path):
	    self.file_index=[(root,files) for root,dirs,files in os.walk(root_path) if files]
    

	def search(self,term,search_type='contains'):
	    self.results.clear()
	    self.matches=0
	    self.records=0
	    
	    #perform search

	    for path,files in self.file_index:
		    for file in files:
		        self.records +=1
		        if(  term.lower() in file.lower() or
		             file.lower().startswith(term.lower()) or
		             file.lower().endswith(term.lower())):

		                result=path.replace('\\','/') + '/' + file
		                self.results.append(result)
		                self.matches +=1


def findFiles(filename, SystemDrive):

    s=Search()
    s.createNewIindex(SystemDrive)
    s.search(filename)
    path = list(s.results)
    # print(path)
    return '\n'.join(path)

def main():
    s=Search()
    s.createNewIindex('D:')
    s.search('DSC03384')
    print()
    print('>> There were {:,d} matches out of {:d} records searched.'.format(s.matches,s.records))
    # print(s.results)
    for match in s.results:
        print(match)
    
    
if __name__ == '__main__':
    main()
