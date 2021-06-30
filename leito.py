# -*- iso-8859-1 -*-

"""Modulo Leito	

"""

import wx
import paciente
import dispositivo
import main


"""Class Leito
"""

class Leito(wx.Panel):	#classe herdada da classe "Panel"
    def __init__(self, parent, id, posxy, sizexy, color): #parametrized constructor
    	self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_SIMPLE)
	self.SetBackgroundColour(color)

	"""class variable shared by all instances
	"""


	"""instance variable unique to each instance
	"""
	self.child_paciente = paciente.Paciente(self, id, (1,1), (88,131), '#3C4043')
	#self.child_dispositivo1 = dispositivo.Canal(self, 1, (89,2), (280,135), '#2A6DF7')
	#self.child_dispositivo2 = dispositivo.Canal(self, 2, (370,2), (280,135), '#EF850F')
	#self.child_canal = dispositivo.MyCanal(92, -20,'#2A6DF7')

	"""metodos
	"""

# Codigo de inicializacao
print "Inicializando modulo Leito..."
