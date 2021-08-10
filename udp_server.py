# -*- iso-8859-1 -*-

"""Modulo servidor UDP
"""
import wx
import socket, ssl, pprint
import struct

"""Classe Udp
"""
class Udp(wx.Panel):
    def __init__(self, ip, udp_port, tcp_port):  #parametrized constructor
        self.panel = wx.Panel.__init__(self)

        self.ip = ip
        self.udp_port = udp_port
        self.tcp_port = tcp_port        

        self.test = "udp test"

        """ Timers
        """
        self.tmr_broadcast = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.tmr_broadcast_handler, self.tmr_broadcast)
        self.tmr_broadcast.Start(1000)

        """ UDP server
        """
        self.sock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock_udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock_udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sock_udp.bind((self.ip, self.udp_port))

    """metodos
    """
    def tmr_broadcast_handler(self, event):
        ip  = bytearray(4)
        msg = bytearray(14)

        ip = [int(x) for x in self.ip.split('.')]

        msg[0] = 0
        msg[1] = ord('L')
        msg[2] = ord('I')
        msg[3] = ord('F')
        msg[4] = ord('E')
        msg[5] = ord('S')
        msg[6] = ord('M')
        msg[7] = ord('T')
        msg[8] = ord('V')
        msg[9] = ord('X')
        msg[10:13] = ip
        msg[14:15] = struct.pack('>H', self.tcp_port)

        try:
            #self.sock_udp.sendto(msg, ('<broadcast>', UDP_PORT))
            print msg
        except:
            print "Socekt Error...broadcast"


# Codigo de inicializacao
print "Inicializando modulo udp_server..."
