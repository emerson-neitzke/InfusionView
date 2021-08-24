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

        self.lbl_nome = wx.StaticText(self, -1, "", (3, 45))
        self.lbl_nome.SetForegroundColour('WHITE')
        self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.lbl_nome.SetFont(self.font)

        self.lbl_mid_nome = wx.StaticText(self, -1, "", (3, 63))
        self.lbl_mid_nome.SetForegroundColour('WHITE')
        self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.lbl_mid_nome.SetFont(self.font)

        self.lbl_sub_nome = wx.StaticText(self, -1, "", (3, 81))
        self.lbl_sub_nome.SetForegroundColour('WHITE')
        self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.lbl_sub_nome.SetFont(self.font)

        self.lbl_prontuario = wx.StaticText(self, -1, "", (3, 105))
        self.lbl_prontuario.SetForegroundColour('WHITE')
        self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.lbl_prontuario.SetFont(self.font)

    """metodos
    """
    def onMouseLeftClicked(self, event):
        print("Left button of the mouse was clicked\n", self.leito)
        self.cadastro = cadastro.Cadastro(self.parent, self.leito, 1, 1, '#3C4043')

    def prontuarioSetposition(self, prontuario):
        self.lbl_prontuario.Destroy()

        self.st = ""
        self.dx = 3

        if (len(prontuario)*8) >= 88:
            for i in range(9):
                self.st = self.st + prontuario[i]
            self.st += "..."
        else:
            """centraliza
            """
            self.dx = 88/2 - ((len(prontuario)*8)/2)        
            self.st = prontuario

        self.lbl_prontuario = wx.StaticText(self, -1, "", (self.dx, 105))
        self.lbl_prontuario.SetForegroundColour('WHITE')
        self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.lbl_prontuario.SetFont(self.font)

        self.lbl_prontuario.SetLabel(self.st)

    def nomeSetposition(self, nome):
        self.lbl_nome.Destroy()
        self.lbl_mid_nome.Destroy()        
        self.lbl_sub_nome.Destroy()        

        self.st = ["", "", ""]
        self.stc = 0
        self.dx1 = 3
        self.dx2 = 3        
        self.dx3 = 3

        for i in range(len(nome)):
            if nome[i] != ' ':
                self.st[self.stc] += nome[i]
                continue
            else:
                if len((self.st[self.stc])*8) >= 88:
                    self.st[self.stc] = ""
                    for i in range(9):
                        self.st[self.stc] += nome[i]
                    self.st[self.stc] += "..."
                    self.stc += 1
                else:
                    self.stc += 1
                    if self.stc > 2:
                        self.st[2] += "..."
                        break

        """centraliza
        """
        self.dx1 = 88/2 - ((len(self.st[0])*7)/2)
        self.dx2 = 88/2 - ((len(self.st[1])*7)/2)
        self.dx3 = 88/2 - ((len(self.st[2])*7)/2)

        self.lbl_nome = wx.StaticText(self, -1, "", (self.dx1, 45))
        self.lbl_nome.SetForegroundColour('WHITE')
        self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.lbl_nome.SetFont(self.font)

        self.lbl_mid_nome = wx.StaticText(self, -1, "", (self.dx2, 63))
        self.lbl_mid_nome.SetForegroundColour('WHITE')
        self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.lbl_mid_nome.SetFont(self.font)

        self.lbl_sub_nome = wx.StaticText(self, -1, "", (self.dx3, 81))
        self.lbl_sub_nome.SetForegroundColour('WHITE')
        self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.lbl_sub_nome.SetFont(self.font)

        self.lbl_nome.SetLabel(self.st[0])
        self.lbl_mid_nome.SetLabel(self.st[1])
        self.lbl_sub_nome.SetLabel(self.st[2])

        

# Codigo de inicializacao
print "Inicializando modulo paciente..."
