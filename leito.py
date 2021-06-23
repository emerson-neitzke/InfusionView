# -*- iso-8859-1 -*-

"""Modulo Leito	

"""

import wx
import paciente
import dispositivo


"""Class Leito
"""
class Leito(wx.Panel):
    def __init__(self, parent, id, posxy, sizexy, color): #parametrized constructor
    	self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_SIMPLE)
	self.SetBackgroundColour(color)

	"""atributos publicos(+)
	"""


	"""atributos privados(-)
	"""
	self.child_paciente = paciente.Paciente(self, id, (2,2), (100,135), 'GRAY')
	#self.child_dispositivo1 = dispositivo.Dispositivo(self, 1, (2+100,2), (280,135), 'BLUE')
	#self.child_dispositivo2 = dispositivo.Dispositivo(self, 2, (2+100+281,2), (280,135), 'ORANGE')
	#self.child_dispositivo3 = dispositivo.Dispositivo(self, 3, (2+100+281*2,2), (280,135), 'BLUE')


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
