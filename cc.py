"""
Client that sends out REQUEST messages
"""

import socket
import sys
import time

SUBSTATIONS = [
	"10.0.0.2",
	"10.0.0.3",
	"10.0.0.4",
	"10.0.0.5",
	"10.0.0.6",
	"10.0.0.7",
	"10.0.0.8",
	"10.0.0.9",
	"10.0.0.10",
	"10.0.0.11",
	"10.0.0.12",
	"10.0.0.13",
	"10.0.0.14",
	"10.0.0.15",
	"10.0.0.16",
	"10.0.0.17",
	"10.0.0.18",
	"10.0.0.19",
	"10.0.0.20",
	"10.0.0.21"
]

class ControlCenter(object):

	def __init__(self):
		pass
		


	def launch(self, period=10, print_response=False):

		req_counter = 1

		while True:
			data = "REQUEST%d\n" % req_counter
			open_sockets = []
			responses = []
			for sub_ip in SUBSTATIONS:
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock.connect((sub_ip, 7788))
				sock.sendall(data)
				open_sockets.append(sock)
			for sock in open_sockets:
				r = sock.recv(1024)
				responses.append(r)
				sock.close()
			print 'Got %d responses' % len(responses)
			time.sleep(period)
			req_counter += 1


if __name__ == '__main__':
	cc = ControlCenter()
	cc.launch(period=10, print_response=True)






