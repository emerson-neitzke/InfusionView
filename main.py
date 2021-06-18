# -*- iso-8859-1 -*-

"""Modulo main

"""
import wx
import modulos
import mod_tcp_server
import mod_udp_server
import mod_leito
 

def main():
	print "Inicializando modulo principal..."


class MyForm(wx.Frame):
	def	__init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, "", style = wx.MINIMIZE_BOX | wx.CLOSE_BOX)
		self.Centre()
		self.SetBackgroundColour('BLACK')
		self.Show()
		self.Maximize(True)

		modulos.display()
		self.canal1 = CanalPanel(self, -1, (50,20), (264,67), '#3c60f2')



if __name__ == "__main__":
	main()
	app = wx.App()
	frame = MyForm().Show()
	app.MainLoop()

