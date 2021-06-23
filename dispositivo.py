# -*- iso-8859-1 -*-

"""Modulo Dispositivo

"""
import wx


"""Classe Dispositivo
"""
class Dispositivo(wx.Panel):
    def __init__(self, parent, id, posxy, sizexy, color):
    	self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_SIMPLE)
	self.SetBackgroundColour(color)

	"""atributos publicos(+)
	"""
	tipo = 'bomba de infusao'

	"""atributos privados(-)
	"""
	self.nome = ''



# Codigo de inicializacao
print "Inicializando modulo Bomba..."
