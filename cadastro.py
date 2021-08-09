# -*- iso-8859-1 -*-

"""Modulo Cadastro
"""

import wx
import password

"""Classe Cadastro
"""
class Cadastro(wx.Frame):	#classe herdada da classe "Frame"
	def __init__(self, idef, posx, posy, color):  #parametrized constructor
          self.frm = wx.Frame.__init__(self, None, wx.ID_ANY, "Cadastro Leito" + str(idef), size=(870,300), style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
          #self.SetPosition(wx.Point(posx, posy))
          self.Centre()
          self.SetBackgroundColour(color)
          self.Show(True)

          self.mypanel = wx.Panel(self, -1)

          self.dispositivos = ['TCH18023190', 'TCH18023191', 'TCH18023192', 'TCH18023193', 'TCH18023194', 'TCH18023195', 'TCH18023187', 'TCH18023188']

          #Nome  
          self.lbl_nome = wx.StaticText(self, -1, "Nome  ", (10, 12))
          self.lbl_nome.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_nome.SetFont(self.font)          

          self.txt_nome = wx.TextCtrl(self, pos = (10, 28), size = (405,25))

          #Prontuario
          self.lbl_prontuario = wx.StaticText(self, -1, "Prontuario  ", (10, 55))
          self.lbl_prontuario.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_prontuario.SetFont(self.font)
          
          self.txt_prontuario = wx.TextCtrl(self, pos = (10, 70), size = (200,25))          
          
          #Data entrada
          self.lbl_data_entrada = wx.StaticText(self, -1, "Data Entrada ", (215, 55))
          self.lbl_data_entrada.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_data_entrada.SetFont(self.font)

          self.txt_data_entrada = wx.TextCtrl(self, pos = (215, 70), size = (200,25))

          #CPF
          self.lbl_cpf = wx.StaticText(self, -1, "CPF ", (10, 98))
          self.lbl_cpf.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_cpf.SetFont(self.font)

          self.txt_cpf = wx.TextCtrl(self, pos = (10, 115), size = (200,25))

          #Telefone
          self.lbl_telefone = wx.StaticText(self, -1, "Telefone ", (215, 98))
          self.lbl_telefone.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_telefone.SetFont(self.font)

          self.txt_telefone = wx.TextCtrl(self, pos = (215, 115), size = (200,25))

          #Genero
          self.lbl_genero = wx.StaticText(self, -1, "Genero ", (10, 141))
          self.lbl_genero.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_genero.SetFont(self.font)

          self.txt_genero = wx.TextCtrl(self, pos = (10, 155), size = (200,25))

          #Data Nascimento
          self.lbl_birth_day = wx.StaticText(self, -1, "Data Nascimento ", (215, 141))
          self.lbl_birth_day.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_birth_day.SetFont(self.font)

          self.txt_birth_day = wx.TextCtrl(self, pos = (215, 155), size = (200,25))

          #Medico responsavel
          self.lbl_medico = wx.StaticText(self, -1, "Medico responsavel ", (10, 184))
          self.lbl_medico.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_medico.SetFont(self.font)

          self.txt_medico = wx.TextCtrl(self, pos = (10, 200), size = (400,25))

          #buttons
          self.btn_cadastrar = wx.Button(self, -1, 'Cadastrar(+)', pos = (10, 235), size = (130, 25))
          self.btn_editar = wx.Button(self, -1, 'Editar', pos = (145, 235), size = (130, 25))          
          self.btn_alta = wx.Button(self, -1, 'Dar Alta(-)', pos = (280, 235), size = (130, 25))
          
          #
          self.lbl_disp_plus = wx.StaticText(self, -1, "Dispositivos Disponiveis  ", (428, 12))
          self.lbl_disp_plus.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_disp_plus.SetFont(self.font)          

          self.lst_disp_disp = wx.ListBox(self, choices = self.dispositivos, pos = (428, 28), size = (180,195), style = wx.LB_SINGLE)
          #self.txt_disp_disp = wx.TextCtrl(self, pos = (428, 28), size = (180,195), style = wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_AUTO_URL)          
          self.btn_disp_right = wx.Button(self, -1, '->', pos = (615, 28), size = (50, 25))

          #  
          self.lbl_disp_plus = wx.StaticText(self, -1, "Dispositivos Alocados  ", (672, 12))
          self.lbl_disp_plus.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_disp_plus.SetFont(self.font)

          #self.txt_dispositivo_alloc = wx.TextCtrl(self, pos = (672, 28), size = (180,195), style = wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_AUTO_URL)
          self.lst_disp_aloc = wx.ListBox(self, pos = (672, 28), size = (180,195), style = wx.LB_SINGLE)
          self.btn_disp_left = wx.Button(self, -1, '<-', pos = (615, 60), size = (50, 25))

          #events
          self.btn_cadastrar.Bind(wx.EVT_BUTTON, self.CadastrarOnClicked)
          self.btn_editar.Bind(wx.EVT_BUTTON, self.EditarOnClicked)
          self.btn_alta.Bind(wx.EVT_BUTTON, self.AltaOnClicked)
          self.btn_disp_right.Bind(wx.EVT_BUTTON, self.RightOnClicked)
          self.btn_disp_left.Bind(wx.EVT_BUTTON, self.LeftOnClicked)

          #self.txt_disp_disp.Bind(EVT_TEXT, self.OnRowSelected)
          self.lst_disp_disp.Bind(wx.EVT_LISTBOX, self.OnDispDispRowSelected, self.lst_disp_disp)
          self.lst_disp_aloc.Bind(wx.EVT_LISTBOX, self.OnDispAlocRowSelected, self.lst_disp_aloc)

	def CadastrarOnClicked(self, event):
          print("click button cadastrar")
          #self.txt_disp_disp.AppendText("TCH1921681105\n")
          #self.lst_disp_disp.Append("TCH1921681105")

	def EditarOnClicked(self, event):
          print("click button Editar")
          self.passw = password.Password(-1, 960, 540, '#3C4043')

	def AltaOnClicked(self, event):
          print("click button alta", self.txt_disp_disp.GetLineText(1))

	def RightOnClicked(self, event):
          self.item = self.lst_disp_disp.GetSelection()
          self.lst_disp_aloc.Append(self.lst_disp_disp.GetString(self.item))
          self.lst_disp_disp.Deselect(self.item)
          self.lst_disp_disp.Delete(self.item)
          print("click button Right", str(self.item))

	def LeftOnClicked(self, event):
          self.item = self.lst_disp_aloc.GetSelection()
          self.lst_disp_disp.Append(self.lst_disp_aloc.GetString(self.item))
          self.lst_disp_aloc.Delete(self.item)
          print("click button Right", str(self.item))


	def OnDispDispRowSelected(self, event):
          #print("Row selected ", self.lst_disp_disp.GetSelection)
          print("Current selection: ", self.lst_disp_disp.GetStringSelection()+"\n")

	def OnDispAlocRowSelected(self, event):
          print("Disp Alocados Row selected")          


# Codigo de inicializacao
print "Inicializando modulo cadastro..."
