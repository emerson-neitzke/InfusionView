# -*- iso-8859-1 -*-

"""Modulo Paciente
"""

import wx

class Paciente(wx.Panel):
    def __init__(self, parent, id, posxy, sizexy, nome, prontuario, color):
    	self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_SIMPLE)
	self.SetBackgroundColour(color)
	self.nome = nome
	self.prontuario = prontuario
	self.device = wx.StaticText(self, -1, "%02d" % id, (40, 16))
	self.device.SetForegroundColour('WHITE')
        self.font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.device.SetFont(self.font)



# Codigo de inicializacao
print "Inicializando modulo paciente..."
