# -*- iso-8859-1 -*-

"""Modulo Dispositivo

"""
import wx
import leito

"""Classe Dispositivo
"""

class widgtBat(wx.Panel): #classe herdada da classe "Panel"
    def __init__(self, parent, id, caption, bars, posxy, sizexy, color):
      wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_NONE)
      self.SetBackgroundColour(color)

      """class variable shared by all instances
      """
      tipo = 'Status'

      """instance variable unique to each instance
      """

      self.wdgtb = widgtBat_body(self, -1, "",(4, 1), (19,8), '#3c4043')

    def ShowPos(self, position):
        if position == 0:
          self.wdgtc1 = widgtBat_cel(self, -1, "",(5, 2), (5,6), 'GRAY')
          self.wdgtc2 = widgtBat_cel(self, -1, "",(11, 2), (5,6), 'GRAY')
          self.wdgtc3 = widgtBat_cel(self, -1, "",(17, 2), (5,6), 'GRAY')
        elif position == 1:
          self.wdgtc1 = widgtBat_cel(self, -1, "",(5, 2), (5,6), '#F5520E')     #red   
        elif position == 2:
          self.wdgtc1 = widgtBat_cel(self, -1, "",(5, 2), (5,6), '#5EBA7D')     #green
          self.wdgtc2 = widgtBat_cel(self, -1, "",(11, 2), (5,6), '#5EBA7D')    #green
        elif position == 3:
          self.wdgtc1 = widgtBat_cel(self, -1, "",(5, 2), (5,6), '#5EBA7D')
          self.wdgtc2 = widgtBat_cel(self, -1, "",(11, 2), (5,6), '#5EBA7D')
          self.wdgtc3 = widgtBat_cel(self, -1, "",(17, 2), (5,6), '#5EBA7D')        
          
        print (position+1)


class widgtBat_body(wx.Panel):  #classe herdada da classe "Panel"
    def __init__(self, parent, id, caption, posxy, sizexy, color):
      self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_NONE)
      self.SetBackgroundColour(color)

      """class variable shared by all instances
      """
      tipo = 'Status'

      """instance variable unique to each instance
      """
      self.nome = ''


class widgtBat_cel(wx.Panel): #classe herdada da classe "Panel"
    def __init__(self, parent, id, caption, posxy, sizexy, color):
      self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_NONE)
      self.SetBackgroundColour(color)

      """class variable shared by all instances
      """
      tipo = 'Status'

      """instance variable unique to each instance
      """
      self.nome = ''

class Status(wx.Panel): #classe herdada da classe "Panel"
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

      if caption != "":
        self.batery = widgtBat(self, -1, "", 0, (2, 4), (24,10), 'GRAY')
        self.batery.ShowPos(2)

class VolRestante(wx.Panel):  #classe herdada da classe "Panel"
    def __init__(self, parent, id, posxy, sizexy, color):
      self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_SIMPLE)
      self.SetBackgroundColour(color)

      """class variable shared by all instances
      """
      tipo = 'Volume'

      """instance variable unique to each instance
      """
      self.nome = ''

class TempoRestante(wx.Panel):  #classe herdada da classe "Panel"
    def __init__(self, parent, id, posxy, sizexy, color):
      self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_SIMPLE)
      self.SetBackgroundColour(color)

      """class variable shared by all instances
      """
      tipo = 'Tempo'

      """instance variable unique to each instance
      """
      self.nome = ''


class VolInfundido(wx.Panel): #classe herdada da classe "Panel"
    def __init__(self, parent, id, posxy, sizexy, color):
      self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_SIMPLE)
      self.SetBackgroundColour(color)

      """class variable shared by all instances
      """
      tipo = 'Volume Infundido'

      """instance variable unique to each instance
      """
      self.nome = ''


class Canal(wx.Panel):  #classe herdada da classe "Panel"
    def __init__(self, parent, id, serial, posxy, sizexy, msg_dsp, msg_stat, color):
      painel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_NONE)
      self.SetBackgroundColour(color)

      """class variable shared by all instances
      """
      tipo = 'Canal de infusao'

      """instance variable unique to each instance
      """
      
      medicamento = ""
      self.medicamento = wx.StaticText(self, -1, medicamento, (14, 22))
      self.medicamento.SetForegroundColour('WHITE')
      self.font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
      self.medicamento.SetFont(self.font)

      fluxo = ""
      self.fluxo = wx.StaticText(self, -1, fluxo, (14, 55))
      self.fluxo.SetForegroundColour('WHITE')
      self.font = wx.Font(22, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
      self.fluxo.SetFont(self.font)
      self.fluxo.Wrap(400)
      
      dot = ""
      self.dot = wx.StaticText(self, -1, dot, (64, 67))
      self.dot.SetForegroundColour('WHITE')
      self.font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
      self.dot.SetFont(self.font)

      decimal = ""
      self.decimal = wx.StaticText(self, -1, decimal, (71, 67))
      self.decimal.SetForegroundColour('WHITE')
      self.font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
      self.decimal.SetFont(self.font)

      unity = ""
      self.unidade = wx.StaticText(self, -1, unity, (91, 67))
      self.unidade.SetForegroundColour('WHITE')
      self.font = wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
      self.unidade.SetFont(self.font)
      
      tempo = ""
      self.tempo_restante = wx.StaticText(self, -1, tempo, (190, 55))
      self.tempo_restante.SetForegroundColour('WHITE')
      self.font = wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
      self.tempo_restante.SetFont(self.font)
      self.tempo_restante.Wrap(400)

      Dispositivo = msg_dsp + "      "
      self.lbl_dispositivo = wx.StaticText(self, -1, Dispositivo, (25, 55))
      self.lbl_dispositivo.SetForegroundColour('WHITE')
      self.font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
      self.lbl_dispositivo.SetFont(self.font)
      self.lbl_dispositivo.Wrap(400)
      
      Desconectado = msg_stat + "       "
      self.lbl_desconectado = wx.StaticText(self, -1, Desconectado, (113, 55))
      self.lbl_desconectado.SetForegroundColour('WHITE')
      self.font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
      self.lbl_desconectado.SetFont(self.font)
      self.lbl_desconectado.Wrap(400)

      lbl_vol_infdo = ""
      self.lbl_volume_infdo = wx.StaticText(self, -1, lbl_vol_infdo, (14, 92))
      self.lbl_volume_infdo.SetForegroundColour('WHITE')
      self.font = wx.Font(7, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
      self.lbl_volume_infdo.SetFont(self.font)
      
      vol_infdo = ""
      self.volume_infdo = wx.StaticText(self, -1, vol_infdo, (14, 102))
      self.volume_infdo.SetForegroundColour('WHITE')
      self.font = wx.Font(13, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
      self.volume_infdo.SetFont(self.font)
      self.volume_infdo.Wrap(400)
      
      lbl_vol_infdo_unity = ""
      self.lbl_volume_infdo_unity = wx.StaticText(self, -1, lbl_vol_infdo_unity, (101, 107))
      self.lbl_volume_infdo_unity.SetForegroundColour('WHITE')
      self.font = wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
      self.lbl_volume_infdo_unity.SetFont(self.font)
      self.lbl_volume_infdo_unity.Wrap(400)
        
      self.status = Status(self, 1, serial, (-5,-2), (295,18), color)

class Dispositivo(wx.Panel):  #classe herdada da classe "Panel"
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
  

class MyCanal(wx.Frame):  #classe herdada da classe "Frame"
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
