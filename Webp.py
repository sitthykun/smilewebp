"""
Author: masakokh
Version: 1.0.0
Note:
"""
import os
from typing import Any
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
		self.__webpSDKPath	= webpPath
		# public
		self.error			= Error()

	def __foundSDKPath(self) -> bool:
		"""

		:return:
		"""
		# the default path in ubuntu
		defaultPath = '/usr/local/bin/pngquant'

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
			self.error.setError('The pngquant sdk path\'s not found.')
			return False

	def setWebp(self, path: str = '') -> None:
		"""

		:param path:
		:return:
		"""
		self.__webpSDKPath	= path
