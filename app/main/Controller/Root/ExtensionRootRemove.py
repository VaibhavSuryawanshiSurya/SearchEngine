try:
	import re
	from app.main.Business.Root.RootExtensionRemove import *
	from app.main.Utils.Logger.logging import *
	
except Exception as e:
    print(e,'\n')

class ExtensionRemove:

	def inputFileNameExtensionRemove(self, filename):
		filename = filename[::-1]
		# print(filename)

		if '.' in filename:

			for i in range(len(filename)):
				if '.' == filename[i]:
					filename = filename[i+1:]
					# print("fileExceptionRemove")
					return filename[::-1]

		# print("No need of fileExceptionRemove")
		return filename[::-1]

	def selectFileNameFromPath(self, path):
		path = str(path[::-1])
		p = re.compile(r'[\w ._-]+/')
		result = list(p.findall(path))
		filename = result[0][-2::-1]
		# return inputFileNameExtensionRemove(filename)
		return filename


def main():
	# filename = 'DSC03384'
	# filename = inputFileNameExtensionRemove(filename)
	# print(filename)
	ER = ExtentionRemove()
	path = "D:My Project/BE Final Year Project/LiFi Project/TxRx.pdsprj.DESKTOP-KKP8PPD.Vaibhav.pdf"
	filename = ER.selectFileNameFromPath(path)
	print(filename)


if __name__ == '__main__':
	main()