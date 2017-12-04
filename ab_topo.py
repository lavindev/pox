from mininet.topo import Topo

class ABTopo(Topo):
	def __init__(self):
		Topo.__init__(self)
		
		aHosts = [self.addHost('a%d' % i) for i in range(1, 3+1)]
		bHosts = [self.addHost('b%d' % i) for i in range(1, 3+1)]
		switch = self.addSwitch('s0', flow_limit=100)
		
		for a in aHosts:
			self.addLink(a, switch)
		for b in bHosts:
			self.addLink(b, switch)

topos = { 'abtopo': ( lambda: ABTopo()  )}
