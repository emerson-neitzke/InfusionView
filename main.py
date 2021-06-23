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


class LeitoPanel(wx.Panel):
    def __init__(self, parent, id, posxy, sizexy, color):
    	self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_SIMPLE)
	self.SetBackgroundColour(color)
	self.child = paciente.Paciente(self, id, (2,2), (120,216), "",123456789, 'GRAY')


class MyForm(wx.Frame):
	def	__init__(self):
		window = wx.Frame.__init__(self, None, wx.ID_ANY, "", style = wx.MINIMIZE_BOX | wx.CLOSE_BOX)
		self.Centre()
		self.SetBackgroundColour('GRAY')
		self.Show()
		self.Maximize(True)

		#modulos.display()
		self.panel = wx.Panel(self)
		self.leito1 = LeitoPanel(self, 1, (2,2), (960,216), 'BLACK')
		self.leito2 = LeitoPanel(self, 2, (2,218), (960,216), 'BLACK')
		#self.paciente1 = paciente.Paciente(self, -1, (2,2), (120,250), 'GRAY')
		#self.leito1 = LeitoPanel(self, -1, (2,216+3), (960,216), 'BLACK')
		#self.leito1 = LeitoPanel(self, -1, (2,216*2+4), (960,216), 'BLACK')




if __name__ == "__main__":
	main()
	app = wx.App()
	frame = MyForm().Show()
	app.MainLoop()

