# -*- iso-8859-1 -*-

"""Modulo Password
"""

import wx

"""Classe Password
"""
class Password(wx.Frame):	#classe herdada da classe "Frame"
	def __init__(self, idef, posx, posy, color):  #parametrized constructor
          frame = wx.Frame.__init__(self, None, wx.ID_ANY, "Password", size=(260,150), style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
          #self.SetPosition(wx.Point(posx, posy))
          self.Centre()
          self.SetBackgroundColour(color)
          self.Show(True)

          self.mypanel = wx.Panel(self, -1)

          self.txt_password = wx.TextCtrl(self, pos = (30, 25), size = (200,25), style=wx.TE_PASSWORD)          
          self.btn_entrar = wx.Button(self, -1, 'Entrar', pos = (65, 70), size = (130, 25))

          self.btn_entrar.SetDefault()
          self.btn_entrar.SetFocus()
          self.btn_entrar.Bind(wx.EVT_BUTTON, self.OnClicked)
          #self.btn_entrar.Bind(wx.EVT_CHAR_HOOK, self.OnKey)

	def OnClicked(self, event):
          self.txt_passw = self.txt_password.GetLineText(0)
          if self.txt_passw == 'senha#123mudar':
            print("Access granted", self.txt_passw)
          else:
            print("Access denied")
          return True



# Codigo de inicializacao
print "Inicializando modulo password..."
