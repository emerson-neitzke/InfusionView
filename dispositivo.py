# -*- iso-8859-1 -*-

"""Modulo Dispositivo

"""
import wx
import leito

"""Classe Dispositivo
"""

class widgtBat_body(wx.Panel):	#classe herdada da classe "Panel"
    def __init__(self, parent, id, caption, posxy, sizexy, color):
    	self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_NONE)
	self.SetBackgroundColour(color)

	"""class variable shared by all instances
	"""
	tipo = 'Status'

	"""instance variable unique to each instance
	"""
	self.nome = ''


class widgtBat_cel(wx.Panel):	#classe herdada da classe "Panel"
    def __init__(self, parent, id, caption, posxy, sizexy, color):
    	self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_NONE)
	self.SetBackgroundColour(color)

	"""class variable shared by all instances
	"""
	tipo = 'Status'

	"""instance variable unique to each instance
	"""
	self.nome = ''
	
class widgtBat(wx.Panel):	#classe herdada da classe "Panel"
    def __init__(self, parent, id, caption, posxy, sizexy, color):
    	self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_NONE)
	self.SetBackgroundColour(color)

	"""class variable shared by all instances
	"""
	tipo = 'Status'

	"""instance variable unique to each instance
	"""
	self.nome = ''	
	self.wdgtb = widgtBat_body(self, -1, "BAT",(4, 1), (19,8), '#3c4043')
	self.wdgtc1 = widgtBat_cel(self, -1, "BAT",(5, 2), (5,6), '#5EBA7D')
	self.wdgtc2 = widgtBat_cel(self, -1, "BAT",(11, 2), (5,6), '#5EBA7D')
	self.wdgtc3 = widgtBat_cel(self, -1, "BAT",(17, 2), (5,6), '#5EBA7D')	

class Status(wx.Panel):	#classe herdada da classe "Panel"
    def __init__(self, parent, id, caption, posxy, sizexy, color):
    	self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_NONE)
	self.SetBackgroundColour(color)

	"""class variable shared by all instances
	"""
	tipo = 'Status'

	"""instance variable unique to each instance
	"""
	self.nome = ''
	self.serial = wx.StaticText(self, -1, caption, (130, 3), style = wx.ALIGN_CENTER)
	self.serial.SetForegroundColour('GRAY')
	self.font = wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
	self.serial.SetFont(self.font)
	sizer = wx.BoxSizer(wx.HORIZONTAL)
	sizer.Add(self.serial, 1, flag = wx.CENTER)
	self.SetSizer(sizer)
	self.widg = widgtBat(self, -1, "BAT",(2, 4), (24,10), 'GRAY')


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
    	painel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_NONE)
	self.SetBackgroundColour(color)

	"""class variable shared by all instances
	"""
	tipo = 'Canal de infusao'

	"""instance variable unique to each instance
	"""
	self.nome = ''
	caption = '100.00                                                '
	self.flux = wx.StaticText(self, -1, caption, (50, 60))
	self.flux.SetForegroundColour('WHITE')
	self.font = wx.Font(22, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
	self.flux.SetFont(self.font)
	self.flux.Wrap(400)
	
	self.medicamento = wx.StaticText(self, -1, "Paroxetina     ", (16, 22))
	self.medicamento.SetForegroundColour('WHITE')
	self.font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
	self.medicamento.SetFont(self.font)

	self.tempo_restante = wx.StaticText(self, -1, "12:00:00", (145, 67))
	self.tempo_restante.SetForegroundColour('WHITE')
	self.font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
	self.tempo_restante.SetFont(self.font)

	self.status = Status(self, 1, "TCH18090123",(-5,-2), (295,18), '#3C4043')


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
          wx.Frame.__init__(self, None, wx.ID_ANY, "", size=(280,137), style = wx.STAY_ON_TOP)
          self.SetPosition(wx.Point(posx, posy))
          self.SetBackgroundColour(color)
          self.Show(True)
          self.flux = wx.StaticText(self, -1, "100.0", (150, 160))
          self.flux.SetForegroundColour('WHITE')
          self.font = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.flux.SetFont(self.font)



# Codigo de inicializacao
print "Inicializando modulo Bomba..."
