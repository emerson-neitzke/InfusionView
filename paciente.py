# -*- iso-8859-1 -*-

"""Modulo Paciente
"""

import wx

"""Classe Paciente
"""
class Paciente(wx.Panel):
    def __init__(self, parent, id, posxy, sizexy, color):
    	self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_SIMPLE)
	self.SetBackgroundColour(color)

	"""atributos publicos(+)
	"""
	tipo = "humano"

	"""atributos privados(-)
	"""
	self.nome = ''
	self.prontuario = 0
	self.data_entrada = ''
	self.data_saida = ''
	self.idade = 0
	self.genero = ''

	self.device = wx.StaticText(self, -1, "%02d" % id, (40, 16))
	self.device.SetForegroundColour('WHITE')
        self.font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.device.SetFont(self.font)

	"""metodos
	"""
    def set_nome_paciente(self, nome):
	self.nome = nome


    def set_prontuario(self, prontuario):
	self.prontuario = prontuario


    def dar_alta(self, prontuario):
	self.data_saida = 0



# Codigo de inicializacao
print "Inicializando modulo paciente..."
