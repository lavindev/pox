
import SocketServer
import sys


SUBSTATIONS = {
	1: "10.0.0.2",
	2: "10.0.0.3",
	3: "10.0.0.4",
	4: "10.0.0.5",
	5: "10.0.0.6",
	6: "10.0.0.7",
	7: "10.0.0.8",
	8: "10.0.0.9",
	9: "10.0.0.10",
	10: "10.0.0.11",
	11: "10.0.0.12",
	12: "10.0.0.13",
	13: "10.0.0.14",
	14: "10.0.0.15",
	15: "10.0.0.16",
	16: "10.0.0.17",
	17: "10.0.0.18",
	18: "10.0.0.19",
	19: "10.0.0.20",
	20: "10.0.0.21"
}


class SubstationHandler(SocketServer.BaseRequestHandler):

	def handle(self):
		self.data = self.request.recv(1024).strip()
		print "{} wrote:".format(self.client_address[0])
		print self.data

		req_num = int(self.data.replace('REQUEST', ''))
		response = "RESPONSE%d" % req_num
		self.request.sendall(response)
	



if __name__ == '__main__':

	try:
		sub = int(sys.argv[1])
		ip = SUBSTATIONS[sub]
	except:
		print 'Argument out of range'
		sys.exit(1)

	server = SocketServer.TCPServer((ip, 7788), SubstationHandler)
	server.serve_forever()