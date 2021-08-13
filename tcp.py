# -*- iso-8859-1 -*-

"""Modulo servidor TCP

"""
import wx
import socket, ssl, pprint
import threading



class Tcp(wx.Panel):
    def __init__(self, id, tcp_port):  #parametrized constructor
        self.panel = wx.Panel.__init__(self)

        self.tcp_port = tcp_port
        self.id = id

        """ TCP server
        """
        self.socket_tcp = socket.socket()
        self.socket_tcp.bind(('', self.tcp_port))
        self.socket_tcp.listen(1)

        self.threadStopped = False
        self.threadClientConnected = False
        self.watchdog_timeout = 0
        self.th1 = threading.Thread(target = self.thread_inconnection, args=("thread inconnection sendo executada", self.id, self.tcp_port))
        self.th1.start()

    """metodos
    """
    def thread_inconnection(self, arg1, arg2, arg3):
        self.id = 0
        self.error = False
        self.init = True

        print arg1
        print arg2
        print arg3        

        while not self.threadStopped:
            try:
                newsocket, fromaddr = self.socket_tcp.accept()
                print "Bind Socket"
            except:
                self.error = True
                print "Bind exception..."

            try:
                connstream = ssl.wrap_socket(newsocket, certfile = "server.cert", keyfile = "server.key",server_side=True)
            except:
                self.error = True
                print "Socket exception..."

            self.watchdog_timeout = 0

            print "Client connected,", fromaddr
            ip_addr = ""
            temp = ""
            ip_addr = str(fromaddr)
            ip_addr = re.sub(r'[(|)|,]',r'', ip_addr)
            ip_addr = re.sub(r'[\']',r'', ip_addr)

            self.id += 1

            try:
                self.cyph = (connstream.cipher())
                #self.cert = (pprint.pformat(connstream.getpeercert()))
            except:
                self.error = True
                print "Cipher Error..."

            try:
                self.cert = connstream.getpeercert()
            except:
                self.error = True
                print "Cert Error..."

            if not self.error:
                print "cypher: ", self.cyph
                print "cert: ", self.cert

                #self.th_client = threading.Thread(target=self.thread_client,args=("thread client " + str(sys.argv[1]) + " sendo executada:",connstream, self.id, 0))
                #self.th_client.start()

                self.threadClientConnected = True

                #print "\n"
                #print "Client " + str(sys.argv[1]) + " Connected...", ip_addr
                #print "\n"

                #time.sleep(1)
                #self.envia_auth_required(connstream)

                #stat_equipament1 = ""
                #stat_equipament2 = ""

                #ttsec = 0
                #self.tmr_ttconnect.Start(1000)

                while self.threadClientConnected:
                    time.sleep(1)

                #print "Client " + str(sys.argv[1]) + " disconnected...", ip_addr
            else:
                self.error = False
                time.sleep(1)

    def thread_client(self, arg1, arg2, arg3):
        self.estado = init
        self.s = bytearray(368)
        self.ack = bytearray(8)
        self.s = "";

        print arg1, arg2, arg3


# Codigo de inicializacao
print "Inicializando modulo tcp_server..."
