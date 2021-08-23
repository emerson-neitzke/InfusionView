# -*- iso-8859-1 -*-

"""Modulo Cadastro
"""

import wx
import password
import dbase
import dispositivo

"""Classe Cadastro
"""
class Cadastro(wx.Frame):	#classe herdada da classe "Frame"
	def __init__(self, parent2, idef, posx, posy, color):  #parametrized constructor
          self.frm = wx.Frame.__init__(self, None, wx.ID_ANY, "Cadastro Leito" + str(idef), size=(870,300), style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
          #self.SetPosition(wx.Point(posx, posy))
          self.Centre()
          self.SetBackgroundColour(color)
          self.Show(True)

          self.mypanel = wx.Panel(self, -1)

          self.parent = parent2  

          self.leito = idef
          self.dispositivos = ['TCH18023190', 'TCH18023191', 'TCH18023192', 'TCH18023193', 'TCH18023194', 'TCH18023195', 'TCH18023187', 'TCH18023188']
          self.disp_alocados = ['-1','-1','-1','-1']

          """Nome
          """
          self.lbl_nome = wx.StaticText(self, -1, "Nome*  ", (10, 12))
          self.lbl_nome.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_nome.SetFont(self.font)          

          self.txt_nome = wx.TextCtrl(self, pos = (10, 28), size = (405,25))
          self.txt_nome.Disable()

          """Prontuario
          """
          self.lbl_prontuario = wx.StaticText(self, -1, "Prontuario*  ", (10, 55))
          self.lbl_prontuario.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_prontuario.SetFont(self.font)
          
          self.txt_prontuario = wx.TextCtrl(self, pos = (10, 70), size = (200,25))
          self.txt_prontuario.Disable()
          
          """Data entrada
          """
          self.lbl_data_entrada = wx.StaticText(self, -1, "Data Entrada* ", (215, 55))
          self.lbl_data_entrada.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_data_entrada.SetFont(self.font)

          self.txt_data_entrada = wx.TextCtrl(self, pos = (215, 70), size = (200,25))
          self.txt_data_entrada.Disable()

          """CPF
          """
          self.lbl_cpf = wx.StaticText(self, -1, "CPF ", (10, 98))
          self.lbl_cpf.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_cpf.SetFont(self.font)

          self.txt_cpf = wx.TextCtrl(self, pos = (10, 115), size = (200,25))
          self.txt_cpf.Disable()

          """Telefone
          """
          self.lbl_telefone = wx.StaticText(self, -1, "Telefone ", (215, 98))
          self.lbl_telefone.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_telefone.SetFont(self.font)

          self.txt_telefone = wx.TextCtrl(self, pos = (215, 115), size = (200,25))
          self.txt_telefone.Disable()

          """Genero
          """
          self.lbl_genero = wx.StaticText(self, -1, "Genero ", (10, 141))
          self.lbl_genero.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_genero.SetFont(self.font)

          self.txt_genero = wx.TextCtrl(self, pos = (10, 155), size = (200,25))
          self.txt_genero.Disable()

          """Data Nascimento
          """
          self.lbl_birth_day = wx.StaticText(self, -1, "Data Nascimento ", (215, 141))
          self.lbl_birth_day.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_birth_day.SetFont(self.font)

          self.txt_birth_day = wx.TextCtrl(self, pos = (215, 155), size = (200,25))
          self.txt_birth_day.Disable()

          """Medico responsavel
          """
          self.lbl_medico = wx.StaticText(self, -1, "Medico responsavel* ", (10, 184))
          self.lbl_medico.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_medico.SetFont(self.font)

          self.txt_medico = wx.TextCtrl(self, pos = (10, 200), size = (400,25))
          self.txt_medico.Disable()

          """buttons
          """
          self.btn_cadastrar = wx.Button(self, -1, 'Cadastrar(+)', pos = (10, 235), size = (130, 25))
          self.btn_editar = wx.Button(self, -1, 'Editar', pos = (145, 235), size = (130, 25))          
          self.btn_alta = wx.Button(self, -1, 'Dar Alta(-)', pos = (280, 235), size = (130, 25))
          self.btn_cadastrar.Disable()
          self.btn_editar.Disable()
          self.btn_alta.Disable()

          """
          """
          self.lbl_disp_plus = wx.StaticText(self, -1, "Dispositivos Disponiveis  ", (428, 12))
          self.lbl_disp_plus.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_disp_plus.SetFont(self.font)          

          self.lst_disp_disp = wx.ListBox(self, choices = self.dispositivos, pos = (428, 28), size = (180,195), style = wx.LB_SINGLE)

          self.btn_disp_right = wx.Button(self, -1, '->', pos = (615, 28), size = (50, 25))

          self.lbl_disp_plus = wx.StaticText(self, -1, "Dispositivos Alocados  ", (672, 12))
          self.lbl_disp_plus.SetForegroundColour('WHITE')
          self.font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
          self.lbl_disp_plus.SetFont(self.font)

          self.lst_disp_aloc = wx.ListBox(self, pos = (672, 28), size = (180,195), style = wx.LB_SINGLE)
          self.btn_disp_left = wx.Button(self, -1, '<-', pos = (615, 60), size = (50, 25))

          """ Update Leito from database
          """

          results = dbase.db.search(dbase.dbLeitos.leito == str(self.leito))
          self.flag = dbase.dbParse(results, 'flag')
          if self.flag == 'true':
            self.nome = dbase.dbParse(results, 'nome')
            self.prontuario = dbase.dbParse(results, 'prontuario')
            self.data_entrada = dbase.dbParse(results, 'data_entrada')
            self.cpf = dbase.dbParse(results, 'cpf')
            self.telefone = dbase.dbParse(results, 'telefone')
            self.genero = dbase.dbParse(results, 'genero')
            self.data_de_nascimento = dbase.dbParse(results, 'data_de_nascimento')
            self.tipo_sanguineo = dbase.dbParse(results, 'tipo_sanguineo')
            self.medico = dbase.dbParse(results, 'medico')
            self.dsp1 = dbase.dbParse(results, 'dispositiv_1')
            self.dsp2 = dbase.dbParse(results, 'dispositiv_2')
            self.dsp3 = dbase.dbParse(results, 'dispositiv_3')
            self.dsp4 = dbase.dbParse(results, 'dispositiv_4')

            self.txt_nome.SetValue(self.nome)
            self.txt_prontuario.SetValue(self.prontuario)
            self.txt_data_entrada.SetValue(self.data_entrada)
            self.txt_cpf.SetValue(self.cpf)
            self.txt_telefone.SetValue(self.telefone)
            self.txt_genero.SetValue(self.genero)
            self.txt_birth_day.SetValue(self.data_de_nascimento)
            self.txt_medico.SetValue(self.medico)

            if self.dsp1 != '-1':
                self.lst_disp_aloc.Append(self.dsp1)
            if self.dsp2 != '-1':
                self.lst_disp_aloc.Append(self.dsp2)
            if self.dsp3 != '-1':
                self.lst_disp_aloc.Append(self.dsp3)
            if self.dsp4 != '-1':
                self.lst_disp_aloc.Append(self.dsp4)

            self.btn_editar.Enable()
            self.btn_alta.Enable()
            
          else:
            self.txt_nome.Enable()
            self.txt_prontuario.Enable()
            self.txt_data_entrada.Enable()
            self.txt_cpf.Enable()
            self.txt_telefone.Enable()
            self.txt_genero.Enable()
            self.txt_birth_day.Enable()
            self.txt_medico.Enable()
            self.btn_cadastrar.Enable()
            

          """Events
          """
          self.btn_cadastrar.Bind(wx.EVT_BUTTON, self.CadastrarOnClicked)
          self.btn_editar.Bind(wx.EVT_BUTTON, self.EditarOnClicked)
          self.btn_alta.Bind(wx.EVT_BUTTON, self.AltaOnClicked)
          self.btn_disp_right.Bind(wx.EVT_BUTTON, self.RightOnClicked)
          self.btn_disp_left.Bind(wx.EVT_BUTTON, self.LeftOnClicked)

          #self.txt_disp_disp.Bind(EVT_TEXT, self.OnRowSelected)
          self.lst_disp_disp.Bind(wx.EVT_LISTBOX, self.OnDispDispRowSelected, self.lst_disp_disp)
          self.lst_disp_aloc.Bind(wx.EVT_LISTBOX, self.OnDispAlocRowSelected, self.lst_disp_aloc)

	"""metodos
	"""
	def CadastrarOnClicked(self, event):
          print("click button cadastrar")
          #self.parent.leito1.child_paciente.nome = "Publisher"

          if Cadastro.isDataValid(self) == True:
            dbase.db.update({'nome': self.txt_nome.GetLineText(0)}, dbase.dbLeitos.leito == str(self.leito))
            dbase.db.update({'prontuario': self.txt_prontuario.GetLineText(0)}, dbase.dbLeitos.leito == str(self.leito))
            dbase.db.update({'data_entrada': self.txt_data_entrada.GetLineText(0)}, dbase.dbLeitos.leito == str(self.leito))
            dbase.db.update({'cpf': self.txt_cpf.GetLineText(0)}, dbase.dbLeitos.leito == str(self.leito))
            dbase.db.update({'telefone': self.txt_telefone.GetLineText(0)}, dbase.dbLeitos.leito == str(self.leito))
            dbase.db.update({'genero': self.txt_genero.GetLineText(0)}, dbase.dbLeitos.leito == str(self.leito))
            dbase.db.update({'data_de_nascimento': self.txt_birth_day.GetLineText(0)}, dbase.dbLeitos.leito == str(self.leito))
            dbase.db.update({'medico': self.txt_medico.GetLineText(0)}, dbase.dbLeitos.leito == str(self.leito))
            dbase.db.update({'flag': 'true'}, dbase.dbLeitos.leito == str(self.leito))

            self.btn_cadastrar.Disable()
            
            self.txt_nome.Disable()
            self.txt_prontuario.Disable()
            self.txt_data_entrada.Disable()
            self.txt_cpf.Disable()
            self.txt_telefone.Disable()
            self.txt_genero.Disable()
            self.txt_birth_day.Disable()
            self.txt_medico.Disable()

            """Update dispositivos alocados
            """
            for i in range(4):
                self.disp = 'dispositiv_' + str(i+1)
                dbase.db.update({self.disp: '-1'}, dbase.dbLeitos.leito == str(self.leito))           
            
            for i in range(self.lst_disp_aloc.GetCount()):
                self.disp = 'dispositiv_' + str(i+1)
                print self.disp
                dbase.db.update({self.disp: self.lst_disp_aloc.GetString(i)}, dbase.dbLeitos.leito == str(self.leito))

            if self.leito == 1:
                self.parent.leito1.child_paciente.lbl_nome.SetLabel(self.txt_nome.GetLineText(0))
                self.parent.leito1.child_paciente.lbl_prontuario.SetLabel(self.txt_prontuario.GetLineText(0))

                self.parent.leito1.child_paciente.nome = self.txt_nome.GetLineText(0)
                self.parent.leito1.child_paciente.prontuario = self.txt_prontuario.GetLineText(0)
                self.parent.leito1.child_paciente.data_entrada = self.txt_data_entrada.GetLineText(0)
                self.parent.leito1.child_paciente.cpf = self.txt_cpf.GetLineText(0)
                self.parent.leito1.child_paciente.telefone = self.txt_telefone.GetLineText(0)
                self.parent.leito1.child_paciente.genero = self.txt_genero.GetLineText(0)
                self.parent.leito1.child_paciente.data_nascimento = self.txt_birth_day.GetLineText(0)
                self.parent.leito1.child_paciente.medico = self.txt_medico.GetLineText(0)

                self.parent.updateLeito(self, self.leito)

            elif self.leito == 2:
                self.parent.leito2.child_paciente.lbl_nome.SetLabel(self.txt_nome.GetLineText(0))
                self.parent.leito2.child_paciente.lbl_prontuario.SetLabel(self.txt_prontuario.GetLineText(0))
                
                self.parent.leito2.child_paciente.nome = self.txt_nome.GetLineText(0)
                self.parent.leito2.child_paciente.prontuario = self.txt_prontuario.GetLineText(0)
                self.parent.leito2.child_paciente.data_entrada = self.txt_data_entrada.GetLineText(0)
                self.parent.leito2.child_paciente.cpf = self.txt_cpf.GetLineText(0)
                self.parent.leito2.child_paciente.telefone = self.txt_telefone.GetLineText(0)
                self.parent.leito2.child_paciente.genero = self.txt_genero.GetLineText(0)
                self.parent.leito2.child_paciente.data_nascimento = self.txt_birth_day.GetLineText(0)
                self.parent.leito2.child_paciente.medico = self.txt_medico.GetLineText(0)
                
                self.parent.updateLeito(self, self.leito)
                
            elif self.leito == 3:
                self.parent.leito3.child_paciente.lbl_nome.SetLabel(self.txt_nome.GetLineText(0))
                self.parent.leito3.child_paciente.lbl_prontuario.SetLabel(self.txt_prontuario.GetLineText(0))

                self.parent.leito3.child_paciente.nome = self.txt_nome.GetLineText(0)
                self.parent.leito3.child_paciente.prontuario = self.txt_prontuario.GetLineText(0)
                self.parent.leito3.child_paciente.data_entrada = self.txt_data_entrada.GetLineText(0)
                self.parent.leito3.child_paciente.cpf = self.txt_cpf.GetLineText(0)
                self.parent.leito3.child_paciente.telefone = self.txt_telefone.GetLineText(0)
                self.parent.leito3.child_paciente.genero = self.txt_genero.GetLineText(0)
                self.parent.leito3.child_paciente.data_nascimento = self.txt_birth_day.GetLineText(0)
                self.parent.leito3.child_paciente.medico = self.txt_medico.GetLineText(0)

                self.parent.updateLeito(self, self.leito)                
                
            elif self.leito == 4:
                self.parent.leito4.child_paciente.lbl_nome.SetLabel(self.txt_nome.GetLineText(0))
                self.parent.leito4.child_paciente.lbl_prontuario.SetLabel(self.txt_prontuario.GetLineText(0))
                
                self.parent.leito4.child_paciente.nome = self.txt_nome.GetLineText(0)
                self.parent.leito4.child_paciente.prontuario = self.txt_prontuario.GetLineText(0)
                self.parent.leito4.child_paciente.data_entrada = self.txt_data_entrada.GetLineText(0)
                self.parent.leito4.child_paciente.cpf = self.txt_cpf.GetLineText(0)
                self.parent.leito4.child_paciente.telefone = self.txt_telefone.GetLineText(0)
                self.parent.leito4.child_paciente.genero = self.txt_genero.GetLineText(0)
                self.parent.leito4.child_paciente.data_nascimento = self.txt_birth_day.GetLineText(0)
                self.parent.leito4.child_paciente.medico = self.txt_medico.GetLineText(0)

                self.parent.updateLeito(self, self.leito)                
                
            elif self.leito == 5:
                self.parent.leito5.child_paciente.lbl_nome.SetLabel(self.txt_nome.GetLineText(0))
                self.parent.leito5.child_paciente.lbl_prontuario.SetLabel(self.txt_prontuario.GetLineText(0))
                
                self.parent.leito5.child_paciente.nome = self.txt_nome.GetLineText(0)
                self.parent.leito5.child_paciente.prontuario = self.txt_prontuario.GetLineText(0)
                self.parent.leito5.child_paciente.data_entrada = self.txt_data_entrada.GetLineText(0)
                self.parent.leito5.child_paciente.cpf = self.txt_cpf.GetLineText(0)
                self.parent.leito5.child_paciente.telefone = self.txt_telefone.GetLineText(0)
                self.parent.leito5.child_paciente.genero = self.txt_genero.GetLineText(0)
                self.parent.leito5.child_paciente.data_nascimento = self.txt_birth_day.GetLineText(0)
                self.parent.leito5.child_paciente.medico = self.txt_medico.GetLineText(0)

                self.parent.updateLeito(self, self.leito)                

            elif self.leito == 6:
                self.parent.leito6.child_paciente.lbl_nome.SetLabel(self.txt_nome.GetLineText(0))
                self.parent.leito6.child_paciente.lbl_prontuario.SetLabel(self.txt_prontuario.GetLineText(0))
                
                self.parent.leito6.child_paciente.nome = self.txt_nome.GetLineText(0)
                self.parent.leito6.child_paciente.prontuario = self.txt_prontuario.GetLineText(0)
                self.parent.leito6.child_paciente.data_entrada = self.txt_data_entrada.GetLineText(0)
                self.parent.leito6.child_paciente.cpf = self.txt_cpf.GetLineText(0)
                self.parent.leito6.child_paciente.telefone = self.txt_telefone.GetLineText(0)
                self.parent.leito6.child_paciente.genero = self.txt_genero.GetLineText(0)
                self.parent.leito6.child_paciente.data_nascimento = self.txt_birth_day.GetLineText(0)
                self.parent.leito6.child_paciente.medico = self.txt_medico.GetLineText(0)

                self.parent.updateLeito(self, self.leito)                
                
            elif self.leito == 7:
                self.parent.leito7.child_paciente.lbl_nome.SetLabel(self.txt_nome.GetLineText(0))
                self.parent.leito7.child_paciente.lbl_prontuario.SetLabel(self.txt_prontuario.GetLineText(0))

                self.parent.leito7.child_paciente.nome = self.txt_nome.GetLineText(0)
                self.parent.leito7.child_paciente.prontuario = self.txt_prontuario.GetLineText(0)
                self.parent.leito7.child_paciente.data_entrada = self.txt_data_entrada.GetLineText(0)
                self.parent.leito7.child_paciente.cpf = self.txt_cpf.GetLineText(0)
                self.parent.leito7.child_paciente.telefone = self.txt_telefone.GetLineText(0)
                self.parent.leito7.child_paciente.genero = self.txt_genero.GetLineText(0)
                self.parent.leito7.child_paciente.data_nascimento = self.txt_birth_day.GetLineText(0)
                self.parent.leito7.child_paciente.medico = self.txt_medico.GetLineText(0)

                self.parent.updateLeito(self, self.leito)                
                
            elif self.leito == 8:
                self.parent.leito8.child_paciente.lbl_nome.SetLabel(self.txt_nome.GetLineText(0))
                self.parent.leito8.child_paciente.lbl_prontuario.SetLabel(self.txt_prontuario.GetLineText(0))
                
                self.parent.leito8.child_paciente.nome = self.txt_nome.GetLineText(0)
                self.parent.leito8.child_paciente.prontuario = self.txt_prontuario.GetLineText(0)
                self.parent.leito8.child_paciente.data_entrada = self.txt_data_entrada.GetLineText(0)
                self.parent.leito8.child_paciente.cpf = self.txt_cpf.GetLineText(0)
                self.parent.leito8.child_paciente.telefone = self.txt_telefone.GetLineText(0)
                self.parent.leito8.child_paciente.genero = self.txt_genero.GetLineText(0)
                self.parent.leito8.child_paciente.data_nascimento = self.txt_birth_day.GetLineText(0)
                self.parent.leito8.child_paciente.medico = self.txt_medico.GetLineText(0)

                self.parent.updateLeito(self, self.leito)                
                
            elif self.leito == 9:
                self.parent.leito9.child_paciente.lbl_nome.SetLabel(self.txt_nome.GetLineText(0))
                self.parent.leito9.child_paciente.lbl_prontuario.SetLabel(self.txt_prontuario.GetLineText(0))
                
                self.parent.leito9.child_paciente.nome = self.txt_nome.GetLineText(0)
                self.parent.leito9.child_paciente.prontuario = self.txt_prontuario.GetLineText(0)
                self.parent.leito9.child_paciente.data_entrada = self.txt_data_entrada.GetLineText(0)
                self.parent.leito9.child_paciente.cpf = self.txt_cpf.GetLineText(0)
                self.parent.leito9.child_paciente.telefone = self.txt_telefone.GetLineText(0)
                self.parent.leito9.child_paciente.genero = self.txt_genero.GetLineText(0)
                self.parent.leito9.child_paciente.data_nascimento = self.txt_birth_day.GetLineText(0)
                self.parent.leito9.child_paciente.medico = self.txt_medico.GetLineText(0)

                self.parent.updateLeito(self, self.leito)                

            elif self.leito == 10:
                self.parent.leito10.child_paciente.lbl_nome.SetLabel(self.txt_nome.GetLineText(0))
                self.parent.leito10.child_paciente.lbl_prontuario.SetLabel(self.txt_prontuario.GetLineText(0))
                
                self.parent.leito10.child_paciente.nome = self.txt_nome.GetLineText(0)
                self.parent.leito10.child_paciente.prontuario = self.txt_prontuario.GetLineText(0)
                self.parent.leito10.child_paciente.data_entrada = self.txt_data_entrada.GetLineText(0)
                self.parent.leito10.child_paciente.cpf = self.txt_cpf.GetLineText(0)
                self.parent.leito10.child_paciente.telefone = self.txt_telefone.GetLineText(0)
                self.parent.leito10.child_paciente.genero = self.txt_genero.GetLineText(0)
                self.parent.leito10.child_paciente.data_nascimento = self.txt_birth_day.GetLineText(0)
                self.parent.leito10.child_paciente.medico = self.txt_medico.GetLineText(0)

                self.parent.updateLeito(self, self.leito)                
                
            elif self.leito == 11:
                self.parent.leito11.child_paciente.lbl_nome.SetLabel(self.txt_nome.GetLineText(0))
                self.parent.leito11.child_paciente.lbl_prontuario.SetLabel(self.txt_prontuario.GetLineText(0))
                
                self.parent.leito11.child_paciente.nome = self.txt_nome.GetLineText(0)
                self.parent.leito11.child_paciente.prontuario = self.txt_prontuario.GetLineText(0)
                self.parent.leito11.child_paciente.data_entrada = self.txt_data_entrada.GetLineText(0)
                self.parent.leito11.child_paciente.cpf = self.txt_cpf.GetLineText(0)
                self.parent.leito11.child_paciente.telefone = self.txt_telefone.GetLineText(0)
                self.parent.leito11.child_paciente.genero = self.txt_genero.GetLineText(0)
                self.parent.leito11.child_paciente.data_nascimento = self.txt_birth_day.GetLineText(0)
                self.parent.leito11.child_paciente.medico = self.txt_medico.GetLineText(0)

                self.parent.updateLeito(self, self.leito)                
                
            elif self.leito == 12:
                self.parent.leito12.child_paciente.lbl_nome.SetLabel(self.txt_nome.GetLineText(0))
                self.parent.leito12.child_paciente.lbl_prontuario.SetLabel(self.txt_prontuario.GetLineText(0))

                self.parent.leito12.child_paciente.nome = self.txt_nome.GetLineText(0)
                self.parent.leito12.child_paciente.prontuario = self.txt_prontuario.GetLineText(0)
                self.parent.leito12.child_paciente.data_entrada = self.txt_data_entrada.GetLineText(0)
                self.parent.leito12.child_paciente.cpf = self.txt_cpf.GetLineText(0)
                self.parent.leito12.child_paciente.telefone = self.txt_telefone.GetLineText(0)
                self.parent.leito12.child_paciente.genero = self.txt_genero.GetLineText(0)
                self.parent.leito12.child_paciente.data_nascimento = self.txt_birth_day.GetLineText(0)
                self.parent.leito12.child_paciente.medico = self.txt_medico.GetLineText(0)

                self.parent.updateLeito(self, self.leito)                
                
            elif self.leito == 13:
                self.parent.leito13.child_paciente.lbl_nome.SetLabel(self.txt_nome.GetLineText(0))
                self.parent.leito13.child_paciente.lbl_prontuario.SetLabel(self.txt_prontuario.GetLineText(0))
                
                self.parent.leito13.child_paciente.nome = self.txt_nome.GetLineText(0)
                self.parent.leito13.child_paciente.prontuario = self.txt_prontuario.GetLineText(0)
                self.parent.leito13.child_paciente.data_entrada = self.txt_data_entrada.GetLineText(0)
                self.parent.leito13.child_paciente.cpf = self.txt_cpf.GetLineText(0)
                self.parent.leito13.child_paciente.telefone = self.txt_telefone.GetLineText(0)
                self.parent.leito13.child_paciente.genero = self.txt_genero.GetLineText(0)
                self.parent.leito13.child_paciente.data_nascimento = self.txt_birth_day.GetLineText(0)
                self.parent.leito13.child_paciente.medico = self.txt_medico.GetLineText(0)

                self.parent.updateLeito(self, self.leito)                

            elif self.leito == 14:
                self.parent.leito14.child_paciente.lbl_nome.SetLabel(self.txt_nome.GetLineText(0))
                self.parent.leito14.child_paciente.lbl_prontuario.SetLabel(self.txt_prontuario.GetLineText(0))
                
                self.parent.leito14.child_paciente.nome = self.txt_nome.GetLineText(0)
                self.parent.leito14.child_paciente.prontuario = self.txt_prontuario.GetLineText(0)
                self.parent.leito14.child_paciente.data_entrada = self.txt_data_entrada.GetLineText(0)
                self.parent.leito14.child_paciente.cpf = self.txt_cpf.GetLineText(0)
                self.parent.leito14.child_paciente.telefone = self.txt_telefone.GetLineText(0)
                self.parent.leito14.child_paciente.genero = self.txt_genero.GetLineText(0)
                self.parent.leito14.child_paciente.data_nascimento = self.txt_birth_day.GetLineText(0)
                self.parent.leito14.child_paciente.medico = self.txt_medico.GetLineText(0)

                self.parent.updateLeito(self, self.leito)                
                
            elif self.leito == 15:
                self.parent.leito15.child_paciente.lbl_nome.SetLabel(self.txt_nome.GetLineText(0))
                self.parent.leito15.child_paciente.lbl_prontuario.SetLabel(self.txt_prontuario.GetLineText(0))
                
                self.parent.leito15.child_paciente.nome = self.txt_nome.GetLineText(0)
                self.parent.leito15.child_paciente.prontuario = self.txt_prontuario.GetLineText(0)
                self.parent.leito15.child_paciente.data_entrada = self.txt_data_entrada.GetLineText(0)
                self.parent.leito15.child_paciente.cpf = self.txt_cpf.GetLineText(0)
                self.parent.leito15.child_paciente.telefone = self.txt_telefone.GetLineText(0)
                self.parent.leito15.child_paciente.genero = self.txt_genero.GetLineText(0)
                self.parent.leito15.child_paciente.data_nascimento = self.txt_birth_day.GetLineText(0)
                self.parent.leito15.child_paciente.medico = self.txt_medico.GetLineText(0)

                self.parent.updateLeito(self, self.leito)                
                
            elif self.leito == 16:
                self.parent.leito16.child_paciente.lbl_nome.SetLabel(self.txt_nome.GetLineText(0))
                self.parent.leito16.child_paciente.lbl_prontuario.SetLabel(self.txt_prontuario.GetLineText(0))
                
                self.parent.leito16.child_paciente.nome = self.txt_nome.GetLineText(0)
                self.parent.leito16.child_paciente.prontuario = self.txt_prontuario.GetLineText(0)
                self.parent.leito16.child_paciente.data_entrada = self.txt_data_entrada.GetLineText(0)
                self.parent.leito16.child_paciente.cpf = self.txt_cpf.GetLineText(0)
                self.parent.leito16.child_paciente.telefone = self.txt_telefone.GetLineText(0)
                self.parent.leito16.child_paciente.genero = self.txt_genero.GetLineText(0)
                self.parent.leito16.child_paciente.data_nascimento = self.txt_birth_day.GetLineText(0)
                self.parent.leito16.child_paciente.medico = self.txt_medico.GetLineText(0)

                self.parent.updateLeito(self, self.leito)


	def EditarOnClicked(self, event):
          print("click button Editar")
          #self.passw = password.Password(-1, 960, 540, '#3C4043')
          self.txt_nome.Enable()
          self.txt_prontuario.Enable()
          self.txt_data_entrada.Enable()
          self.txt_cpf.Enable()
          self.txt_telefone.Enable()
          self.txt_genero.Enable()
          self.txt_birth_day.Enable()
          self.txt_medico.Enable()
          self.btn_cadastrar.Enable()


	def AltaOnClicked(self, event):
          """Remove do DB
          """
          dbase.db.update({'nome': '-1'}, dbase.dbLeitos.leito == str(self.leito))
          dbase.db.update({'prontuario': '-1'}, dbase.dbLeitos.leito == str(self.leito))
          dbase.db.update({'data_entrada': '-1'}, dbase.dbLeitos.leito == str(self.leito))
          dbase.db.update({'cpf': '-1'}, dbase.dbLeitos.leito == str(self.leito))
          dbase.db.update({'telefone': '-1'}, dbase.dbLeitos.leito == str(self.leito))
          dbase.db.update({'genero': '-1'}, dbase.dbLeitos.leito == str(self.leito))
          dbase.db.update({'data_de_nascimento': '-1'}, dbase.dbLeitos.leito == str(self.leito))
          dbase.db.update({'medico': '-1'}, dbase.dbLeitos.leito == str(self.leito))
          dbase.db.update({'flag': 'false'}, dbase.dbLeitos.leito == str(self.leito))

          for i in range(4):
            self.disp = 'dispositiv_' + str(i+1)
            dbase.db.update({self.disp: '-1'}, dbase.dbLeitos.leito == str(self.leito))

          self.txt_nome.SetValue("")
          self.txt_prontuario.SetValue("")
          self.txt_data_entrada.SetValue("")
          self.txt_cpf.SetValue("")
          self.txt_telefone.SetValue("")
          self.txt_genero.SetValue("")
          self.txt_birth_day.SetValue("")
          self.txt_medico.SetValue("")

          for i in range(self.lst_disp_aloc.GetCount()):
            self.lst_disp_disp.Append(self.lst_disp_aloc.GetString(i))

          for i in range(self.lst_disp_aloc.GetCount()):
            self.lst_disp_aloc.Delete(0)

          if self.leito == 1:
            self.parent.leito1.child_paciente.lbl_nome.SetLabel("")
            self.parent.leito1.child_paciente.lbl_prontuario.SetLabel("")

            self.parent.leito1.child_paciente.nome = ""
            self.parent.leito1.child_paciente.prontuario = ""
            self.parent.leito1.child_paciente.data_entrada = ""
            self.parent.leito1.child_paciente.cpf = ""
            self.parent.leito1.child_paciente.telefone = ""
            self.parent.leito1.child_paciente.genero = ""
            self.parent.leito1.child_paciente.data_nascimento = ""
            self.parent.leito1.child_paciente.medico = ""

          elif self.leito == 2:
            self.parent.leito2.child_paciente.lbl_nome.SetLabel("")
            self.parent.leito2.child_paciente.lbl_prontuario.SetLabel("")

            self.parent.leito2.child_paciente.nome = ""
            self.parent.leito2.child_paciente.prontuario = ""
            self.parent.leito2.child_paciente.data_entrada = ""
            self.parent.leito2.child_paciente.cpf = ""
            self.parent.leito2.child_paciente.telefone = ""
            self.parent.leito2.child_paciente.genero = ""
            self.parent.leito2.child_paciente.data_nascimento = ""
            self.parent.leito2.child_paciente.medico = ""
            
          elif self.leito == 3:
            self.parent.leito3.child_paciente.lbl_nome.SetLabel("")
            self.parent.leito3.child_paciente.lbl_prontuario.SetLabel("")

            self.parent.leito3.child_paciente.nome = ""
            self.parent.leito3.child_paciente.prontuario = ""
            self.parent.leito3.child_paciente.data_entrada = ""
            self.parent.leito3.child_paciente.cpf = ""
            self.parent.leito3.child_paciente.telefone = ""
            self.parent.leito3.child_paciente.genero = ""
            self.parent.leito3.child_paciente.data_nascimento = ""
            self.parent.leito3.child_paciente.medico = ""

          elif self.leito == 4:
            self.parent.leito4.child_paciente.lbl_nome.SetLabel("")
            self.parent.leito4.child_paciente.lbl_prontuario.SetLabel("")

            self.parent.leito4.child_paciente.nome = ""
            self.parent.leito4.child_paciente.prontuario = ""
            self.parent.leito4.child_paciente.data_entrada = ""
            self.parent.leito4.child_paciente.cpf = ""
            self.parent.leito4.child_paciente.telefone = ""
            self.parent.leito4.child_paciente.genero = ""
            self.parent.leito4.child_paciente.data_nascimento = ""
            self.parent.leito4.child_paciente.medico = ""

          elif self.leito == 5:
            self.parent.leito5.child_paciente.lbl_nome.SetLabel("")
            self.parent.leito5.child_paciente.lbl_prontuario.SetLabel("")

            self.parent.leito5.child_paciente.nome = ""
            self.parent.leito5.child_paciente.prontuario = ""
            self.parent.leito5.child_paciente.data_entrada = ""
            self.parent.leito5.child_paciente.cpf = ""
            self.parent.leito5.child_paciente.telefone = ""
            self.parent.leito5.child_paciente.genero = ""
            self.parent.leito5.child_paciente.data_nascimento = ""
            self.parent.leito5.child_paciente.medico = ""

          elif self.leito == 6:
            self.parent.leito6.child_paciente.lbl_nome.SetLabel("")
            self.parent.leito6.child_paciente.lbl_prontuario.SetLabel("")

            self.parent.leito6.child_paciente.nome = ""
            self.parent.leito6.child_paciente.prontuario = ""
            self.parent.leito6.child_paciente.data_entrada = ""
            self.parent.leito6.child_paciente.cpf = ""
            self.parent.leito6.child_paciente.telefone = ""
            self.parent.leito6.child_paciente.genero = ""
            self.parent.leito6.child_paciente.data_nascimento = ""
            self.parent.leito6.child_paciente.medico = ""

          elif self.leito == 7:
            self.parent.leito7.child_paciente.lbl_nome.SetLabel("")
            self.parent.leito7.child_paciente.lbl_prontuario.SetLabel("")

            self.parent.leito7.child_paciente.nome = ""
            self.parent.leito7.child_paciente.prontuario = ""
            self.parent.leito7.child_paciente.data_entrada = ""
            self.parent.leito7.child_paciente.cpf = ""
            self.parent.leito7.child_paciente.telefone = ""
            self.parent.leito7.child_paciente.genero = ""
            self.parent.leito7.child_paciente.data_nascimento = ""
            self.parent.leito7.child_paciente.medico = ""

          elif self.leito == 8:
            self.parent.leito8.child_paciente.lbl_nome.SetLabel("")
            self.parent.leito8.child_paciente.lbl_prontuario.SetLabel("")

            self.parent.leito8.child_paciente.nome = ""
            self.parent.leito8.child_paciente.prontuario = ""
            self.parent.leito8.child_paciente.data_entrada = ""
            self.parent.leito8.child_paciente.cpf = ""
            self.parent.leito8.child_paciente.telefone = ""
            self.parent.leito8.child_paciente.genero = ""
            self.parent.leito8.child_paciente.data_nascimento = ""
            self.parent.leito8.child_paciente.medico = ""

          elif self.leito == 9:
            self.parent.leito9.child_paciente.lbl_nome.SetLabel("")
            self.parent.leito9.child_paciente.lbl_prontuario.SetLabel("")

            self.parent.leito9.child_paciente.nome = ""
            self.parent.leito9.child_paciente.prontuario = ""
            self.parent.leito9.child_paciente.data_entrada = ""
            self.parent.leito9.child_paciente.cpf = ""
            self.parent.leito9.child_paciente.telefone = ""
            self.parent.leito9.child_paciente.genero = ""
            self.parent.leito9.child_paciente.data_nascimento = ""
            self.parent.leito9.child_paciente.medico = ""
            
          elif self.leito == 10:
            self.parent.leito10.child_paciente.lbl_nome.SetLabel("")
            self.parent.leito10.child_paciente.lbl_prontuario.SetLabel("")

            self.parent.leito10.child_paciente.nome = ""
            self.parent.leito10.child_paciente.prontuario = ""
            self.parent.leito10.child_paciente.data_entrada = ""
            self.parent.leito10.child_paciente.cpf = ""
            self.parent.leito10.child_paciente.telefone = ""
            self.parent.leito10.child_paciente.genero = ""
            self.parent.leito10.child_paciente.data_nascimento = ""
            self.parent.leito10.child_paciente.medico = ""

          elif self.leito == 11:
            self.parent.leito11.child_paciente.lbl_nome.SetLabel("")
            self.parent.leito11.child_paciente.lbl_prontuario.SetLabel("")

            self.parent.leito11.child_paciente.nome = ""
            self.parent.leito11.child_paciente.prontuario = ""
            self.parent.leito11.child_paciente.data_entrada = ""
            self.parent.leito11.child_paciente.cpf = ""
            self.parent.leito11.child_paciente.telefone = ""
            self.parent.leito11.child_paciente.genero = ""
            self.parent.leito11.child_paciente.data_nascimento = ""
            self.parent.leito11.child_paciente.medico = ""

          elif self.leito == 12:
            self.parent.leito12.child_paciente.lbl_nome.SetLabel("")
            self.parent.leito12.child_paciente.lbl_prontuario.SetLabel("")

            self.parent.leito12.child_paciente.nome = ""
            self.parent.leito12.child_paciente.prontuario = ""
            self.parent.leito12.child_paciente.data_entrada = ""
            self.parent.leito12.child_paciente.cpf = ""
            self.parent.leito12.child_paciente.telefone = ""
            self.parent.leito12.child_paciente.genero = ""
            self.parent.leito12.child_paciente.data_nascimento = ""
            self.parent.leito12.child_paciente.medico = ""

          elif self.leito == 13:
            self.parent.leito13.child_paciente.lbl_nome.SetLabel("")
            self.parent.leito13.child_paciente.lbl_prontuario.SetLabel("")

            self.parent.leito13.child_paciente.nome = ""
            self.parent.leito13.child_paciente.prontuario = ""
            self.parent.leito13.child_paciente.data_entrada = ""
            self.parent.leito13.child_paciente.cpf = ""
            self.parent.leito13.child_paciente.telefone = ""
            self.parent.leito13.child_paciente.genero = ""
            self.parent.leito13.child_paciente.data_nascimento = ""
            self.parent.leito13.child_paciente.medico = ""

          elif self.leito == 14:
            self.parent.leito14.child_paciente.lbl_nome.SetLabel("")
            self.parent.leito14.child_paciente.lbl_prontuario.SetLabel("")

            self.parent.leito14.child_paciente.nome = ""
            self.parent.leito14.child_paciente.prontuario = ""
            self.parent.leito14.child_paciente.data_entrada = ""
            self.parent.leito14.child_paciente.cpf = ""
            self.parent.leito14.child_paciente.telefone = ""
            self.parent.leito14.child_paciente.genero = ""
            self.parent.leito14.child_paciente.data_nascimento = ""
            self.parent.leito14.child_paciente.medico = ""

          elif self.leito == 15:
            self.parent.leito15.child_paciente.lbl_nome.SetLabel("")
            self.parent.leito15.child_paciente.lbl_prontuario.SetLabel("")

            self.parent.leito15.child_paciente.nome = ""
            self.parent.leito15.child_paciente.prontuario = ""
            self.parent.leito15.child_paciente.data_entrada = ""
            self.parent.leito15.child_paciente.cpf = ""
            self.parent.leito15.child_paciente.telefone = ""
            self.parent.leito15.child_paciente.genero = ""
            self.parent.leito15.child_paciente.data_nascimento = ""
            self.parent.leito15.child_paciente.medico = ""

          elif self.leito == 16:
            self.parent.leito16.child_paciente.lbl_nome.SetLabel("")
            self.parent.leito16.child_paciente.lbl_prontuario.SetLabel("")

            self.parent.leito16.child_paciente.nome = ""
            self.parent.leito16.child_paciente.prontuario = ""
            self.parent.leito16.child_paciente.data_entrada = ""
            self.parent.leito16.child_paciente.cpf = ""
            self.parent.leito16.child_paciente.telefone = ""
            self.parent.leito16.child_paciente.genero = ""
            self.parent.leito16.child_paciente.data_nascimento = ""
            self.parent.leito16.child_paciente.medico = ""

          self.parent.updateLeito(self, self.leito)

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

	def isDataValid(self):
          if self.txt_nome.GetLineLength(0) > 0 and \
            self.txt_prontuario.GetLineLength(0) and \
            self.txt_data_entrada.GetLineLength(0) > 0 and \
            self.txt_medico.GetLineLength(0) > 0:
            return True
          else:
            return False
            

# Codigo de inicializacao
print "Inicializando modulo cadastro..."
