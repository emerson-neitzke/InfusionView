# -*- iso-8859-1 -*-

"""Modulo main

"""
import wx
import modulos
import tcp_server
import udp_server
import leito
import paciente
 

def main():
	print "Inicializando modulo principal..."

class MyPanel(wx.Panel):
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


class MyForm(wx.Frame):
	def __init__(self):
		window = wx.Frame.__init__(self, None, title="Full screen")
		self.SetBackgroundColour('GRAY')
		self.ShowFullScreen(True)

		self.panel = MyPanel(self)

		self.leito1 = leito.LeitoPanel(self, 1, (1,1), (960,135), 'BLACK')
		self.leito2 = leito.LeitoPanel(self, 2, (1,135), (960,135), 'BLACK')
		self.leito3 = leito.LeitoPanel(self, 3, (1,2*135), (960,135), 'BLACK')
		self.leito4 = leito.LeitoPanel(self, 4, (1,3*135), (960,135), 'BLACK')
		self.leito5 = leito.LeitoPanel(self, 5, (1,4*135), (960,135), 'BLACK')
		self.leito6 = leito.LeitoPanel(self, 6, (1,5*135), (960,135), 'BLACK')
		self.leito7 = leito.LeitoPanel(self, 7, (1,6*135), (960,135), 'BLACK')
		self.leito8 = leito.LeitoPanel(self, 8, (1,7*135), (960,135), 'BLACK')
		self.leito9 = leito.LeitoPanel(self, 9, (960,1), (960,135), 'BLACK')
		self.leito10 = leito.LeitoPanel(self, 10, (960,135), (960,135), 'BLACK')
		self.leito11 = leito.LeitoPanel(self, 11, (960,2*135), (960,135), 'BLACK')
		self.leito12 = leito.LeitoPanel(self, 12, (960,3*135), (960,135), 'BLACK')
		self.leito13 = leito.LeitoPanel(self, 13, (960,4*135), (960,135), 'BLACK')
		self.leito14 = leito.LeitoPanel(self, 14, (960,5*135), (960,135), 'BLACK')
		self.leito15 = leito.LeitoPanel(self, 15, (960,6*135), (960,135), 'BLACK')
		self.leito16 = leito.LeitoPanel(self, 16, (960,7*135), (960,135), 'BLACK')



if __name__ == "__main__":
	main()
	app = wx.App()
	frame = MyForm().Show()
	app.MainLoop()

