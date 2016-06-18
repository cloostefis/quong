import socket

QUONG_PORT = 6968

class Client:


	def __init__(self, ipAddress):

		self._ipAddress = ipAddress

		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._socket.connect((ipAddress, QUONG_PORT))

		print("Connected")


	def send(self, key):

		self._socket.send(key.to_bytes(1, byteorder='big'))


	def receive(self):

		pass