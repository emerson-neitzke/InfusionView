# -*- iso-8859-1 -*-

"""Modulo Paciente
"""

import wx

class Paciente(wx.Panel):
    def __init__(self, parent, id, posxy, sizexy, nome, prontuario, color):
    	self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_SIMPLE)
	self.SetBackgroundColour(color)
        self.device = wx.StaticText(self, -1, str(id), (15, 63))
        self.font = wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.device.SetFont(self.font)
	self.nome = nome
	self.prontuario = prontuario
		



# Codigo de inicializacao
print "Inicializando modulo paciente..."
