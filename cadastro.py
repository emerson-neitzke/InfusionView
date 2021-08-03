# -*- iso-8859-1 -*-

"""Modulo Cadastro
"""

import wx

"""Classe Cadastro
"""
class Cadastro(wx.Frame):	#classe herdada da classe "Frame"
	def __init__(self, posx, posy, color):  #parametrized constructor
          wx.Frame.__init__(self, None, wx.ID_ANY, "Cadastro de Pacientes e Dispositivos", size=(800,320), style = wx.STAY_ON_TOP)
          self.SetPosition(wx.Point(posx, posy))
          self.SetBackgroundColour(color)
          self.Show(True)
          
          self.mypanel = wx.Panel(self, -1)

          #Nome  
          self.lbl_nome = wx.StaticText(self, -1, "Nome  ", (10, 12))
          self.lbl_nome.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_nome.SetFont(self.font)          

          self.nome = wx.TextCtrl(self, pos = (10, 28), size = (405,25))

          #Prontuario
          self.lbl_prontuario = wx.StaticText(self, -1, "Prontuario  ", (10, 55))
          self.lbl_prontuario.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_prontuario.SetFont(self.font)
          
          self.prontuario = wx.TextCtrl(self, pos = (10, 70), size = (200,25))          
          
          #Data entrada
          self.lbl_data_entrada = wx.StaticText(self, -1, "Data Entrada ", (215, 55))
          self.lbl_data_entrada.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_data_entrada.SetFont(self.font)

          self.data_entrada = wx.TextCtrl(self, pos = (215, 70), size = (200,25))

          #CPF
          self.lbl_cpf = wx.StaticText(self, -1, "CPF ", (10, 98))
          self.lbl_cpf.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_cpf.SetFont(self.font)

          self.cpf = wx.TextCtrl(self, pos = (10, 115), size = (200,25))

          #Telefone
          self.lbl_telefone = wx.StaticText(self, -1, "Telefone ", (215, 98))
          self.lbl_telefone.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_telefone.SetFont(self.font)

          self.telefone = wx.TextCtrl(self, pos = (215, 115), size = (200,25))

          #Genero
          self.lbl_genero = wx.StaticText(self, -1, "Genero ", (10, 140))
          self.lbl_genero.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_genero.SetFont(self.font)

          self.genero = wx.TextCtrl(self, pos = (10, 155), size = (200,25))

          #Data Nascimento
          self.lbl_birth_day = wx.StaticText(self, -1, "Data Nascimento ", (215, 140))
          self.lbl_birth_day.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_birth_day.SetFont(self.font)

          self.birth_day = wx.TextCtrl(self, pos = (215, 155), size = (200,25))

          

# Codigo de inicializacao
print "Inicializando modulo cadastro..."
