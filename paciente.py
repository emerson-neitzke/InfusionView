# -*- iso-8859-1 -*-

"""Modulo Paciente
"""

import wx
import cadastro

"""Classe Paciente
"""
class Paciente(wx.Panel):	#classe herdada da classe "Panel"
    def __init__(self, parent, id, posxy, sizexy, color): #parametrized constructor
    	self.paciente = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_NONE)
	self.SetBackgroundColour(color)
	self.Bind(wx.EVT_LEFT_UP, self.onMouseLeftClicked)

	"""class variable shared by all instances
	"""
	tipo = "humano"

	"""instance variable unique to each instance
	"""
	self.leito = id
	self.nome = ''
	self.prontuario = 0
	self.data_entrada = ''
	self.data_saida = ''
	self.idade = 0
	self.genero = ''
	self.tipo_sanguineo = ''

	self.id = wx.StaticText(self, -1, "%02d" % id, (33, 16))
	self.id.SetForegroundColour('WHITE')
	self.font = wx.Font(12, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
	self.id.SetFont(self.font)

	"""metodos
	"""
    def onMouseLeftClicked(self, event):
        print("Left button of the mouse was clicked\n", self.leito)
        self.cadastro = cadastro.Cadastro(self.leito, 1, 1, '#3C4043')



# Codigo de inicializacao
print "Inicializando modulo paciente..."
