# -*- iso-8859-1 -*-

"""Modulo Dispositivo

"""
import wx
import leito

"""Classe Dispositivo
"""

class Status(wx.Panel):	#classe herdada da classe "Panel"
    def __init__(self, parent, id, caption, posxy, sizexy, color):
    	self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_SIMPLE)
	self.SetBackgroundColour(color)

	"""class variable shared by all instances
	"""
	tipo = 'Status'

	"""instance variable unique to each instance
	"""
	self.nome = ''
	self.flux = wx.StaticText(self, -1, caption, (130, 3))
	self.flux.SetForegroundColour('WHITE')
	self.font = wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
	self.flux.SetFont(self.font)
	


class VolRestante(wx.Panel):	#classe herdada da classe "Panel"
    def __init__(self, parent, id, posxy, sizexy, color):
    	self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_SIMPLE)
	self.SetBackgroundColour(color)

	"""class variable shared by all instances
	"""
	tipo = 'Volume'

	"""instance variable unique to each instance
	"""
	self.nome = ''

class TempoRestante(wx.Panel):	#classe herdada da classe "Panel"
    def __init__(self, parent, id, posxy, sizexy, color):
    	self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_SIMPLE)
	self.SetBackgroundColour(color)

	"""class variable shared by all instances
	"""
	tipo = 'Tempo'

	"""instance variable unique to each instance
	"""
	self.nome = ''


class VolInfundido(wx.Panel):	#classe herdada da classe "Panel"
    def __init__(self, parent, id, posxy, sizexy, color):
    	self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_SIMPLE)
	self.SetBackgroundColour(color)

	"""class variable shared by all instances
	"""
	tipo = 'Volume Infundido'

	"""instance variable unique to each instance
	"""
	self.nome = ''


class Canal(wx.Panel):	#classe herdada da classe "Panel"
    def __init__(self, parent, id, posxy, sizexy, color):
    	painel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_SIMPLE)
	self.SetBackgroundColour(color)

	"""class variable shared by all instances
	"""
	tipo = 'Canal de infusao'

	"""instance variable unique to each instance
	"""
	self.nome = ''
	self.flux = wx.StaticText(self, -1, "100.0", (50, 60))
	self.flux.SetForegroundColour('WHITE')
	self.font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
	self.flux.SetFont(self.font)
	
	self.medicamento = wx.StaticText(self, -1, "Paroxetina", (16, 22))
	self.medicamento.SetForegroundColour('WHITE')
	self.font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
	self.medicamento.SetFont(self.font)

	self.tempo_restante = wx.StaticText(self, -1, "12:00:00", (145, 67))
	self.tempo_restante.SetForegroundColour('WHITE')
	self.font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
	self.tempo_restante.SetFont(self.font)

	self.status = Status(self, 1, "TCH123",(-5,-2), (295,18), color)


class Dispositivo(wx.Panel):	#classe herdada da classe "Panel"
    def __init__(self, parent, id, posxy, sizexy, color):
    	self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_SIMPLE)
	self.SetBackgroundColour(color)

	"""class variable shared by all instances
	"""
	tipo = 'bomba de infusao'

	"""instance variable unique to each instance
	"""
	#self.nome = ''
	#self.flux = wx.StaticText(self, -1, "100.0", (50, 60))
	#self.flux.SetForegroundColour('WHITE')
	#self.font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
	#self.flux.SetFont(self.font)
	
	#self.medicamento = wx.StaticText(self, -1, "Paroxetina", (45, 12))
	#self.medicamento.SetForegroundColour('WHITE')
	#self.font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
	#self.medicamento.SetFont(self.font)

	#self.tempo_restante = wx.StaticText(self, -1, "12:00:00", (145, 67))
	#self.tempo_restante.SetForegroundColour('WHITE')
	#self.font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
	#self.tempo_restante.SetFont(self.font)
	

class MyCanal(wx.Frame):	#classe herdada da classe "Frame"
	def __init__(self, posx, posy, color):
          wx.Frame.__init__(self, None, wx.ID_ANY, "", size=(280,133), style = wx.CAPTION | wx.STAY_ON_TOP)
          self.SetPosition(wx.Point(posx, posy))
          self.SetBackgroundColour(color)
          self.Show(True)



# Codigo de inicializacao
print "Inicializando modulo Bomba..."
