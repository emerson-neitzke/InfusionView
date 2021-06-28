# -*- iso-8859-1 -*-

"""Modulo Paciente
"""

import wx

"""Classe Paciente
"""
class Paciente(wx.Panel):	#classe herdada da classe "Panel"
    def __init__(self, parent, id, posxy, sizexy, color):
    	self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_SIMPLE)
	self.SetBackgroundColour(color)

	"""class variable shared by all instances
	"""
	tipo = "humano"

	"""instance variable unique to each instance
	"""
	self.nome = ''
	self.prontuario = 0
	self.data_entrada = ''
	self.data_saida = ''
	self.idade = 0
	self.genero = ''
	self.tipo_sanguineo = ''

	self.id = wx.StaticText(self, -1, "%02d" % id, (33, 16))
	self.id.SetForegroundColour('WHITE')
	self.font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
	self.id.SetFont(self.font)

	"""metodos
	"""



# Codigo de inicializacao
print "Inicializando modulo paciente..."
