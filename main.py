# -*- iso-8859-1 -*-

"""Modulo main

"""

import wx
import struct
import modulos
import tcp_server
import udp_server
import leito
import paciente
import dispositivo
import cadastro
import password
import dbase
import udp_server
import tcp_server

UDP_PORT = 4434
ip_addr = "127.0.0.1"
tcp_port = 8192

def main():
    print "Inicializando modulo principal..."

class MyPanel(wx.Panel):    #classe herdada da classe "Panel"
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        self.Bind(wx.EVT_KEY_DOWN, self.onKey)

    """ Verifica se a tecla ESC foi pressionada
    """
    def onKey(self, event):
        key_code = event.GetKeyCode()
        if key_code == wx.WXK_ESCAPE:
            self.GetParent().Close()
        else:
            event.Skip()


class MyForm(wx.Frame): #classe herdada da classe "Frame"
    def __init__(self):
        window = wx.Frame.__init__(self, None, title="Full screen")
        self.SetBackgroundColour('GRAY')
        self.ShowFullScreen(True)

        self.panel = MyPanel(self)

        self.broadcom = udp_server.Udp(ip_addr, UDP_PORT, tcp_port)
        
        print self.broadcom.test

        self.leito1 = leito.Leito(self, 1, (1,1), (960,135), '#232728')
        
        print self.leito1.teste
        print self.leito1.child_paciente.leito

        self.leito1.child_paciente.lbl_nome.SetLabel("Fulano")
        
        self.leito2 = leito.Leito(self, 2, (1,135), (960,135), '#232728')
        
        print self.leito2.child_paciente.leito        
        
        
        self.leito3 = leito.Leito(self, 3, (1,2*135), (960,135), '#232728')
        self.leito4 = leito.Leito(self, 4, (1,3*135), (960,135), '#232728')
        self.leito5 = leito.Leito(self, 5, (1,4*135), (960,135), '#232728')
        self.leito6 = leito.Leito(self, 6, (1,5*135), (960,135), '#232728')
        self.leito7 = leito.Leito(self, 7, (1,6*135), (960,135), '#232728')
        self.leito8 = leito.Leito(self, 8, (1,7*135), (960,135), '#232728')
        self.leito9 = leito.Leito(self, 9, (960,1), (960,135), '#232728')
        self.leito10 = leito.Leito(self, 10, (960,135), (960,135), '#232728')
        self.leito11 = leito.Leito(self, 11, (960,2*135), (960,135), '#232728')
        self.leito12 = leito.Leito(self, 12, (960,3*135), (960,135), '#232728')
        self.leito13 = leito.Leito(self, 13, (960,4*135), (960,135), '#232728')
        self.leito14 = leito.Leito(self, 14, (960,5*135), (960,135), '#232728')
        self.leito15 = leito.Leito(self, 15, (960,6*135), (960,135), '#232728')
        self.leito16 = leito.Leito(self, 16, (960,7*135), (960,135), '#232728')

        #self.child_canal_11 = dispositivo.Canal(self, -1, (94, 3), (280, 131), '#2A6DF7')
        #self.child_canal_12 = dispositivo.Canal(self, -1, (94+280+1, 3), (280, 131), '#2A6DF7')


if __name__ == "__main__":
    main()
    app = wx.App()
    frame = MyForm().Show()
    app.MainLoop()

