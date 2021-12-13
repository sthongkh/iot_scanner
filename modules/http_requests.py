import requests
from exception import exception, debug
from logger import logger
from configuration_file import Config


class HtttpRequests:
	"""
		This is class build for the http requests to access server.
	"""
	def __init__(
		self, host, port, path_name, method, data, timeout=5, **kwargs):
		"""
			host is the ip address of the http requests server.
			port is port of the http requests server.
			part_name is the path of data operations.
		"""
		self.url = "http://{}:{}/{}".format(host, port, path_name)
		self.status_code = -1
		self.response_text = ""
		self.method = method
		self.data = data
		self.timeout = timeout
		super().__init__(**kwargs)

	
	@exception(logger)
	@debug(logger)
	def send(self):
		"""
			data is the object of Json format example {"model": "Mustang"}.
			method is the select between GET method and POST method of http
				requests and default with the GET method.
			time_out is the time out of http requests and default setting with
				2 seconds.
		"""
		if self.method == "GET":
			x = requests.get(
				self.url, params = self.data, timeout=self.timeout)
			self.status_code = x.status_code
			self.response_text = x.text
			logger.info(self.response_text)

		elif self.method == "POST":
			x = requests.post(self.url, data = self.data, timeout=self.timeout)
			self.status_code = x.status_code
			self.response_text = x.text

		return self.status_code, self.response_text


class TestSend(HtttpRequests):
	def __init__(self, data, **kwargs):
		self.data = data
		host="192.9.150.101"
		port="1880"
		path_name="hello"
		method="GET"
		super().__init__(
			host=host, port=port, path_name=path_name, method=method, 
			data=self.data, **kwargs)

	@exception(logger)
	def excecute(self):
		http_ret = super().send()
		return http_ret


class DataSend(HtttpRequests):
	def __init__(self, data, retry=0, **kwargs):
		self.data = data
		self.retry = retry
		config_file = "config.ini"
		config_name = "SERVER"
		config = Config(file_path=config_file, item_name=config_name).read()
		host = str(config["host"])
		port = int(config["port"])
		path_name = str(config["path_name"])
		method = str(config["method"])
		super().__init__(
			host=host, port=port, path_name=path_name, method=method, 
			data=self.data, **kwargs)

	@exception(logger)
	def excecute(self):
		cnt = 0
		while True:
			http_ret = super().send()
			if http_ret[0] != 200:
				cnt += 1
				print("Retry : {}".format(cnt))

			elif cnt == self.retry:
				cnt = 0
				break

			else:
				cnt = 0
				break

		return http_ret


if __name__ == "__main__":
	data={"user": "Mustang"}
	update = DataSend(data=data)
	ret = update.excecute()
	print(ret)
	"""
	http = HtttpRequests(
		host="192.9.150.101", port="1880", path_name="hello", method="GET",
		data=data)
	ret = http.send()
	print(ret)
	"""

