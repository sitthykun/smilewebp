"""
Author: masakokh
Version: 1.0.1
Note:
"""
import os
# internal
from Error import Error


class Webp:
	"""

	"""

	def __int__(self, webpPath: str = ''):
		"""

		:param webpPath:
		:return:
		"""
		# private
		self.__extension	= 'webp'
		self.__filename		= ''
		self.__quality		= 0
		self.__webpSDKPath	= webpPath
		# public
		self.error			= Error()

	def __foundSDKPath(self) -> bool:
		"""

		:return:
		"""
		# the default path in ubuntu
		defaultPath = '/usr/bin/cwebp'

		#
		if self.__webpSDKPath and os.path.isfile(self.__webpSDKPath):
			return True

		elif os.path.isfile(defaultPath):
			# set default
			# but nonsense to set here, but, it saves some process
			self.setWebp(path=	defaultPath)
			return True

		else:
			# set error
			self.error.setError('The cwebp sdk path\'s not found.')
			return False

	def convert(self, filename: str, quality: int= 100, newFilename: str= '', newDirname: str= '') -> None:
		"""

		:param filename:
		:param quality:
		:param newFilename:
		:param newDirname:
		:return:
		"""
		# verify sdk path
		if self.__foundSDKPath():
			# todo
			# put in try catch
			try:
				# if no newFilename and newDirname
				needRemove		= False
				tempFileMove	= ''

				# validate extension first
				if not os.path.exists(filename):
					# error
					self.error.setError(f'File not found: {filename}')

				# double-check
				elif (os.path.basename(filename).split('.', 1)[1]).lower() != self.__extension:
					#
					self.error.setError('Wrong extension')

				# found file
				else:
					# set default
					self.error.setErrorNo()
					self.__quality	= quality

					# need removing
					if newFilename and newDirname:
						# make sure no backslash at the end
						self.__filename	= f'{os.path.dirname(newDirname)}/{newFilename}.{self.__extension}'

					elif newFilename:
						# set new filename and keep it
						self.__filename	= f'{os.path.dirname(filename)}/{newFilename}.{self.__extension}'

					elif newDirname:
						# the same directory
						if os.path.dirname(newDirname) == os.path.dirname(filename):
							# name with extension
							self.__filename = f'{os.path.dirname(newDirname)}/{os.path.basename(filename)}_new.{self.__extension}'
							# remove the exists
							needRemove = True
							# move the exist file
							if os.path.exists(self.__filename):
								# move to temp
								tempFileMove	= f'/tmp/{os.path.basename(self.__filename)}'
								#
								os.rename(
									self.__filename
									, tempFileMove
								)

						else:
							# name with extension
							self.__filename	= f'{os.path.dirname(newDirname)}/{os.path.basename(filename)}'

					else:
						# override current file
						needRemove		= True
						self.__filename	= f'/tmp/123456ABCDEF789_ukLepAeSeceSe3fsaEF_HnesieceS2_seq.{self.__extension}'

					# validate and set default
					# maximum
					if self.__quality > 100:
						self.__quality	= 100

					# minimum is 10
					elif self.__quality < 10:
						self.__quality	= 10

					# command
					# you have to install pngquant first
					cmd = [
						# that is the default location
						self.__webpSDKPath
						# it's able to set in range 60 to 80
						# but below, it sets fix
						, f'-q {self.__quality}'
						, filename
						, '-o'
						, self.__filename
					]

					# run a process
					process = subprocess.run(
						cmd
						, stdout	= subprocess.PIPE
						, stderr	= subprocess.PIPE
					)

					# no error
					if process.returncode == 0:
						# remove old if it's true
						if needRemove:
							# remove the old and rename new file to old name
							os.remove(filename)

							# rename
							os.rename(
								self.__filename
								, filename
							)

							# name the filename to the file
							self.__filename = filename

					else:
						# file has been moving to tmp for a while
						if tempFileMove:
							# move back the file
							os.rename(
								tempFileMove
								, f'{os.path.dirname(self.__filename)}/{os.path.basename(tempFileMove)}'
							)
						# got the new error message
						self.error.setError(str(process.stderr))

			except Exception as e:
				self.error.setError(str(e))
				print(str(e))

	def setWebp(self, path: str = '') -> None:
		"""

		:param path:
		:return:
		"""
		self.__webpSDKPath	= path
