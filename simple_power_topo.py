"""
Simple Power Topology
				_________
sub1 ---------- |		|
				|		|
sub2 ---------- |		|
				|		|
sub3 ---------- |	s0	|----------cc (command center)
   .			|		|
   .			|		|
   .			|		|
sub20 --------- |_______|
				
"""
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.cli import CLI
import pdb

NUM_SUBSTATIONS = 20

class SimplePowerTopo(Topo):

	def __init__(self):
		Topo.__init__(self)

		substations = [self.addHost('sub%d' % i) for i in range(1, NUM_SUBSTATIONS+1)]
		cc = self.addHost('cc')
		switch = self.addSwitch('s0')

		self.addLink(cc, switch)
		for sub in substations:
			self.addLink(sub, switch)


def launch():
	simple_power_topo = SimplePowerTopo()
	net = Mininet(topo=simple_power_topo)
	net.start()
	
	cc = net.hosts[0]
	for i in range(1, NUM_SUBSTATIONS + 1):
		sub = net.hosts[i]
		sub_no = sub.name.replace('sub', '')
		print 'Launching substation %s' % sub_no
		sub.cmd("python substation.py %s &" % sub_no)
	print 'Launching command center'
	cc.cmd('python cc.py & ')
	CLI(net)
	net.stop()

if __name__ == '__main__':
	launch()
