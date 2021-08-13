# -*- iso-8859-1 -*-

"""Modulo Paciente
"""

import wx
import cadastro
import password

"""Classe Paciente
"""
class Paciente(wx.Panel):   #classe herdada da classe "Panel"
    def __init__(self, parent, parent2, id, posxy, sizexy, color): #parametrized constructor
        self.paciente = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_NONE)
        self.SetBackgroundColour(color)
        self.Bind(wx.EVT_LEFT_UP, self.onMouseLeftClicked)

        """class variable shared by all instances
        """
        tipo = "humano"

        """instance variable unique to each instance
        """
        self.parent = parent2

        self.leito = id
        self.nome = ''
        self.prontuario = 0
        self.data_entrada = ''
        self.cpf = 0
        self.telefone = 0
        self.idade = 0
        self.genero = ''
        self.data_nascimento = ''
        self.tipo_sanguineo = ''
        self.medico = ''
        self.dispositivos = {
            "dp1":"0",
            "dp2":"0",
            "dp3":"0",
            "dp4":"0",
        }

        self.lbl_id = wx.StaticText(self, -1, "%02d" % id, (33, 16))
        self.lbl_id.SetForegroundColour('WHITE')
        self.font = wx.Font(12, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self.lbl_id.SetFont(self.font)

        self.lbl_nome = wx.StaticText(self, -1, "", (3, 50))
        self.lbl_nome.SetForegroundColour('WHITE')
        self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.lbl_nome.SetFont(self.font)

        self.lbl_prontuario = wx.StaticText(self, -1, "", (3, 75))
        self.lbl_prontuario.SetForegroundColour('WHITE')
        self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.lbl_prontuario.SetFont(self.font)

    """metodos
    """
    def onMouseLeftClicked(self, event):
        print("Left button of the mouse was clicked\n", self.leito)
        self.cadastro = cadastro.Cadastro(self.parent, self.leito, 1, 1, '#3C4043')



# Codigo de inicializacao
print "Inicializando modulo paciente..."
