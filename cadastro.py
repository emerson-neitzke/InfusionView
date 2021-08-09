# -*- iso-8859-1 -*-

"""Modulo Cadastro
"""

import wx

"""Classe Cadastro
"""
class Cadastro(wx.Frame):	#classe herdada da classe "Frame"
	def __init__(self, posx, posy, color):  #parametrized constructor
          #wx.Frame.__init__(self, None, wx.ID_ANY, "Cadastro de Pacientes e Dispositivos", size=(800,320), style = wx.STAY_ON_TOP)
          wx.Frame.__init__(self, None, wx.ID_ANY, "Cadastro", size=(880,320), style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
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

          #Medico responsavel
          self.lbl_medico = wx.StaticText(self, -1, "Medico responsavel ", (10, 184))
          self.lbl_medico.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_medico.SetFont(self.font)

          self.medico = wx.TextCtrl(self, pos = (10, 200), size = (400,25))

          #buttons
          self.cadastrar = wx.Button(self, -1, 'Cadastrar(+)', pos = (10, 235), size = (180, 25))
          self.alta = wx.Button(self, -1, 'Dar Alta(-)', pos = (228, 235), size = (180, 25))
          self.dispositivo_plus = wx.Button(self, -1, '->', pos = (615, 28), size = (50, 25))
          self.dispositivo_minus = wx.Button(self, -1, '<-', pos = (615, 60), size = (50, 25))
          #button2 = wx.Button(self, -1, '-', (10, 60))
          #self.Bind(wx.EVT_BUTTON, self.OnPlus, id=button1.GetId())
          #self.Bind(wx.EVT_BUTTON, self.OnMinus, id=button2.GetId())

          self.dispositivo_p = wx.TextCtrl(self, pos = (428, 28), size = (180,195), style = wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_AUTO_URL)
          self.dispositivo_m = wx.TextCtrl(self, pos = (672, 28), size = (180,195), style = wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_AUTO_URL)          


          

# Codigo de inicializacao
print "Inicializando modulo cadastro..."
