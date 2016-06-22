"""Custom topology DASH project

Two hosts connected trough 1 switch but 3 times (ethernet,wifi,3G):

        --- switch ---
       -              -
   host --- switch --- host
       -              -
        --- switch ---

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo 3links' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        wifiSwitch = self.addSwitch( 's1' )
        ethernetSwitch = self.addSwitch( 's2' )
        hspaSwitch = self.addSwitch( 's3' )
        
        # Add links
        self.addLink( leftHost, wifiSwitch,     bw=5.5,  delay='50ms', loss=1 )
        self.addLink( leftHost, ethernetSwitch, bw=1.5, loss=1)
        self.addLink( leftHost, hspaSwitch,     bw=1.5)
        
        self.addLink( wifiSwitch,     rightHost, bw=5.5)
        self.addLink( ethernetSwitch, rightHost, bw=1.5)
        self.addLink( hspaSwitch,     rightHost, bw=1.5)

topos = { '3links': ( lambda: MyTopo() ) }
