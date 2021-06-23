# -*- iso-8859-1 -*-

"""Modulo Leito	

"""

import wx
import paciente


"""Class Leito
"""
class LeitoPanel(wx.Panel):
    def __init__(self, parent, id, posxy, sizexy, color): #parametrized constructor
    	self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_SIMPLE)
	self.SetBackgroundColour(color)

	"""atributos publicos(+)
	"""


	"""atributos privados(-)
	"""
	self.child_paciente = paciente.Paciente(self, id, (2,2), (100,135), 'GRAY')


	"""metodos
	"""
    def return_nr_dispositivos(self, id):
	self.devices = 0
	return self.devices


    def aloca_dispositivo(self, nr_serie_dispositivo):
	self.devices = 0


    def desaloca_dispositivo(self, nr_serie_dispositivo):
	self.devices = 0

# Codigo de inicializacao
print "Inicializando modulo Leito..."
