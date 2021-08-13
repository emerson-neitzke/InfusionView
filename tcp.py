# -*- iso-8859-1 -*-

"""Modulo servidor TCP

"""

from datetime import datetime
import wx
import socket, ssl, pprint
import re
import threading
import sys, time

recv = ""
recv2 = ""
medicine1 = ""
medicine2 = ""
fluxo1 = ""
fluxo2 = ""
status_bar = ""
pan1_color = ""
pan2_color = ""
datalog_canal1 = ""
datalog_canal2 = ""
stat_equipament1 = "Equipamento Desconectado"
stat_equipament2 = "Equipamento Desconectado"
unidade1 = ""
unidade2 = ""
local_host = "127.0.0.1"
power = ""
infusion_mod = ""
tipo_de_paciente = "Adulto"
ttconnect = ""
thoras = 0
tmin = 0
tsec = 0
ttsec = 0

gleito_atual = 1

'Datalogger status Required'
status_dl_1 = 0x00
status_dl_2 = 0x00
reg_number_dl_1 = 0xE4
reg_number_dl_2 = 0xF0

"""Classe TCP
"""

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

    """ Thread inconnection
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

                self.th_client = threading.Thread(target=self.thread_client,args=("thread client " + ip_addr + " sendo executada:",connstream, self.id, 0))
                self.th_client.start()

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


    """ Thread client
    """

    def thread_client(self, arg1, conn, cid, init):
        global recv, recv2, medicine1, medicine2, fluxo1, fluxo2, status_bar, pan1_color, pan2_color
        global datalog_canal1, datalog_canal2, unidade1, unidade2, power, infusion_mod, tipo_de_paciente
        self.estado = init
        self.s = bytearray(368)
        self.ack = bytearray(8)
        self.s = "";

        print arg1, cid

        """ Send auth request
        """
        self.envia_auth_required(conn)

        while self.threadClientConnected:
            try:
                self.data = conn.read()
            except:
                print "Read Error..."

            self.watchdog_timeout = 0

            if self.estado == 0:              
               """ Todo: tratar resposta do desafio aqui
               """

               """ AUTH_RESPONSE
               """
               auth_response = bytearray(2)
               auth_response[0] = 03
               auth_response[1] = 01     #ACCEPTED
               conn.write(auth_response)
               time.sleep(1)

               """ SYNCHRONIZE date/time
               """
               sync_response = bytearray(8)
               now = datetime.now()
               sync_response[0] = 04
               sync_response[1] = now.hour
               sync_response[2] = now.minute
               sync_response[3] = now.second
               sync_response[4] = now.day
               sync_response[5] = now.month
               sync_response[6] = (now.year / 256)
               sync_response[7] = (now.year % 256)
               conn.write(sync_response)
               self.estado +=1
               
            elif self.estado == 1:
               #check PING/disconnecting
               if len(self.data) == 1:
                   if self.data == chr(0x05):
                       print "Rx PING:", "%02X" % ord(self.data)
                       conn.write(chr(0x0C))  #PONG
                   elif self.data == chr(0x06):
                       print "Cliente desconectado pelo usuario"
                       self.threadClientConnected = False               



    def envia_auth_required(self, connstream):
        desafio = bytearray(6)
        desafio[0] = 01
        desafio[1] = 04
        desafio[2] = 12
        desafio[3] = 34
        desafio[4] = 56
        desafio[5] = 78
        connstream.write(desafio)

    def envia_ack(self, connstream, data):
        ack = bytearray(8)
    
        if len(data) == 1:
            return False
        else:
          ack[0] = 0xAA
          ack[1] = 0x55
          ack[2] = 0xF0
          ack[3] = ord(data[5])
          ack[4] = ord(data[6])
          ack[5] = ord(data[7])
          ack[6] = ord(data[8])
          ack[7] = 0xFF

          connstream.write(ack)

    def envia_ackex_status_troca_alocacao(self, connstream, data):
           temp = bytearray(17)
           BsdBuf = bytearray(17)

           BsdBuf[0]= 0xaa
           BsdBuf[1]= 0x55
           BsdBuf[2]= 0xfd
           BsdBuf[3]= 0x0b
           BsdBuf[4]= 0x00
           BsdBuf[5]= data[5]
           BsdBuf[6]= data[6]
           BsdBuf[7]= data[7]
           BsdBuf[8]= data[8]
           BsdBuf[9]= data[17]
           BsdBuf[10]= data[18]
           BsdBuf[11]= data[19]
           BsdBuf[12]= data[20]
           BsdBuf[13]= 0x00
           BsdBuf[14]= 0x00
           BsdBuf[15]= 0x00
           BsdBuf[16]= 0xff

           size = (BsdBuf[4] * 256) + BsdBuf[3]

           for x in range(size):
                temp[x] = BsdBuf[x + 3]

           crc_16b = self.calcula_crc16(temp, size)

           BsdBuf[14]= crc_16b % 256
           BsdBuf[15]= crc_16b / 256

           connstream.write(BsdBuf)



# Codigo de inicializacao
print "Inicializando modulo tcp_server..."
