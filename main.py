# -*- iso-8859-1 -*-

"""Modulo main
   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
"""
from tinydb import where
import wx
import struct
import modulos
import tcp_server
import udp_server
import leito
import paciente
import dispositivo
import cadastro
import password
import dbase
import udp
import tcp

UDP_PORT = 4434
TCP_PORT = 4082
ip_addr = "192.168.43.138"


def main():
    print "Inicializando modulo principal..."

class MyPanel(wx.Panel):    #classe herdada da classe "Panel"
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        self.Bind(wx.EVT_KEY_DOWN, self.onKey)

    """ Verifica se a tecla ESC foi pressionada
    """
    def onKey(self, event):
        key_code = event.GetKeyCode()
        if key_code == wx.WXK_ESCAPE:
            self.GetParent().Close()
        else:
            event.Skip()


class MyForm(wx.Frame): #classe herdada da classe "Frame"
    def __init__(self):
        window = wx.Frame.__init__(self, None, title="Full screen")
        self.SetBackgroundColour('GRAY')
        self.ShowFullScreen(True)

        self.panel = MyPanel(self)

        """ Instantiate UDP server
        """
        #self.broadcom = udp.Udp(ip_addr, UDP_PORT, TCP_PORT)

        """ Instantiate TCP server
        """
        #self.tcp = tcp.Tcp(11, TCP_PORT)


        """ Instantiate Leitos
        """
        self.leito1 = leito.Leito(self, 1, (1,1), (960,135), '#232728')       
        self.leito2 = leito.Leito(self, 2, (1,135), (960,135), '#232728')
        self.leito3 = leito.Leito(self, 3, (1,2*135), (960,135), '#232728')
        self.leito4 = leito.Leito(self, 4, (1,3*135), (960,135), '#232728')
        self.leito5 = leito.Leito(self, 5, (1,4*135), (960,135), '#232728')
        self.leito6 = leito.Leito(self, 6, (1,5*135), (960,135), '#232728')
        self.leito7 = leito.Leito(self, 7, (1,6*135), (960,135), '#232728')
        self.leito8 = leito.Leito(self, 8, (1,7*135), (960,135), '#232728')
        self.leito9 = leito.Leito(self, 9, (960,1), (960,135), '#232728')
        self.leito10 = leito.Leito(self, 10, (960,135), (960,135), '#232728')
        self.leito11 = leito.Leito(self, 11, (960,2*135), (960,135), '#232728')
        self.leito12 = leito.Leito(self, 12, (960,3*135), (960,135), '#232728')
        self.leito13 = leito.Leito(self, 13, (960,4*135), (960,135), '#232728')
        self.leito14 = leito.Leito(self, 14, (960,5*135), (960,135), '#232728')
        self.leito15 = leito.Leito(self, 15, (960,6*135), (960,135), '#232728')
        self.leito16 = leito.Leito(self, 16, (960,7*135), (960,135), '#232728')

        #self, -1, serial, (94, 3), (280, 131), msg_disp, msg_stat, color
        #self.child_canal_11 = dispositivo.Canal(self, -1, (94, 3), (280, 131), '#2A6DF7')
        self.child_canal_11 = dispositivo.Canal(self, -1, "TCH189188012",(94, 3), (280, 131), "", "", '#2A6DF7')
        #self.child_canal_12 = dispositivo.Canal(self, -1, (94+280+1, 3), (280, 131), '#2A6DF7')     

        self.child_canal_11 = '-1'

        """ Update Leitos from database
        """
        for i in range(16):
            results = dbase.db.search(dbase.dbLeitos.leito == str(i+1))
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

                if i == 0:
                    self.leito1.child_paciente.nome = self.nome
                    self.leito1.child_paciente.prontuario = self.prontuario
                    self.leito1.child_paciente.data_entrada = self.data_entrada
                    self.leito1.child_paciente.cpf = self.cpf
                    self.leito1.child_paciente.telefone = self.telefone
                    self.leito1.child_paciente.genero = self.genero
                    self.leito1.child_paciente.data_de_nascimento = self.data_de_nascimento 
                    self.leito1.child_paciente.tipo_sanguineo = self.tipo_sanguineo
                    self.leito1.child_paciente.medico = self.medico

                    self.leito1.child_paciente.lbl_nome.SetLabel(self.nome)
                    self.leito1.child_paciente.lbl_prontuario.SetLabel(self.prontuario)

                    """
                    if self.dsp1 != '-1':
                        #self.child_canal_1 = dispositivo.Canal(self, -1, "", (94, 3), (280, 131), "Dispositivo", "desconectado", '#3C4043')
                        #    def updLeito(self, serial, leito, disp, msg_disp, msg_stat, color):
                        self.updLeito("", 1, 1, "Dispositivo", "desconectado", '#3C4043')
                    if self.dsp2 != '-1':
                        #self.child_canal_2 = dispositivo.Canal(self, -1, "", (94+280+1, 3), (280, 131), "Dispositivo", "desconectado", '#3C4043')
                        self.updLeito("", 1, 2, "Dispositivo", "desconectado", '#3C4043')
                    """    

                elif i == 1:
                    self.leito2.child_paciente.nome = self.nome
                    self.leito2.child_paciente.prontuario = self.prontuario
                    self.leito2.child_paciente.data_entrada = self.data_entrada
                    self.leito2.child_paciente.cpf = self.cpf
                    self.leito2.child_paciente.telefone = self.telefone
                    self.leito2.child_paciente.genero = self.genero
                    self.leito2.child_paciente.data_de_nascimento = self.data_de_nascimento 
                    self.leito2.child_paciente.tipo_sanguineo = self.tipo_sanguineo
                    self.leito2.child_paciente.medico = self.medico

                    self.leito2.child_paciente.lbl_nome.SetLabel(self.nome)
                    self.leito2.child_paciente.lbl_prontuario.SetLabel(self.prontuario)

                elif i == 2:
                    self.leito3.child_paciente.nome = self.nome
                    self.leito3.child_paciente.prontuario = self.prontuario
                    self.leito3.child_paciente.data_entrada = self.data_entrada
                    self.leito3.child_paciente.cpf = self.cpf
                    self.leito3.child_paciente.telefone = self.telefone
                    self.leito3.child_paciente.genero = self.genero
                    self.leito3.child_paciente.data_de_nascimento = self.data_de_nascimento 
                    self.leito3.child_paciente.tipo_sanguineo = self.tipo_sanguineo
                    self.leito3.child_paciente.medico = self.medico

                    self.leito3.child_paciente.lbl_nome.SetLabel(self.nome)
                    self.leito3.child_paciente.lbl_prontuario.SetLabel(self.prontuario)

                elif i == 3:
                    self.leito4.child_paciente.nome = self.nome
                    self.leito4.child_paciente.prontuario = self.prontuario
                    self.leito4.child_paciente.data_entrada = self.data_entrada
                    self.leito4.child_paciente.cpf = self.cpf
                    self.leito4.child_paciente.telefone = self.telefone
                    self.leito4.child_paciente.genero = self.genero
                    self.leito4.child_paciente.data_de_nascimento = self.data_de_nascimento 
                    self.leito4.child_paciente.tipo_sanguineo = self.tipo_sanguineo
                    self.leito4.child_paciente.medico = self.medico

                    self.leito4.child_paciente.lbl_nome.SetLabel(self.nome)
                    self.leito4.child_paciente.lbl_prontuario.SetLabel(self.prontuario)

                elif i == 4:
                    self.leito5.child_paciente.nome = self.nome
                    self.leito5.child_paciente.prontuario = self.prontuario
                    self.leito5.child_paciente.data_entrada = self.data_entrada
                    self.leito5.child_paciente.cpf = self.cpf
                    self.leito5.child_paciente.telefone = self.telefone
                    self.leito5.child_paciente.genero = self.genero
                    self.leito5.child_paciente.data_de_nascimento = self.data_de_nascimento 
                    self.leito5.child_paciente.tipo_sanguineo = self.tipo_sanguineo
                    self.leito5.child_paciente.medico = self.medico

                    self.leito5.child_paciente.lbl_nome.SetLabel(self.nome)
                    self.leito5.child_paciente.lbl_prontuario.SetLabel(self.prontuario)

                elif i == 5:
                    self.leito6.child_paciente.nome = self.nome
                    self.leito6.child_paciente.prontuario = self.prontuario
                    self.leito6.child_paciente.data_entrada = self.data_entrada
                    self.leito6.child_paciente.cpf = self.cpf
                    self.leito6.child_paciente.telefone = self.telefone
                    self.leito6.child_paciente.genero = self.genero
                    self.leito6.child_paciente.data_de_nascimento = self.data_de_nascimento 
                    self.leito6.child_paciente.tipo_sanguineo = self.tipo_sanguineo
                    self.leito6.child_paciente.medico = self.medico

                    self.leito6.child_paciente.lbl_nome.SetLabel(self.nome)
                    self.leito6.child_paciente.lbl_prontuario.SetLabel(self.prontuario)

                elif i == 6:
                    self.leito7.child_paciente.nome = self.nome
                    self.leito7.child_paciente.prontuario = self.prontuario
                    self.leito7.child_paciente.data_entrada = self.data_entrada
                    self.leito7.child_paciente.cpf = self.cpf
                    self.leito7.child_paciente.telefone = self.telefone
                    self.leito7.child_paciente.genero = self.genero
                    self.leito7.child_paciente.data_de_nascimento = self.data_de_nascimento 
                    self.leito7.child_paciente.tipo_sanguineo = self.tipo_sanguineo
                    self.leito7.child_paciente.medico = self.medico

                    self.leito7.child_paciente.lbl_nome.SetLabel(self.nome)
                    self.leito7.child_paciente.lbl_prontuario.SetLabel(self.prontuario)

                elif i == 7:
                    self.leito8.child_paciente.nome = self.nome
                    self.leito8.child_paciente.prontuario = self.prontuario
                    self.leito8.child_paciente.data_entrada = self.data_entrada
                    self.leito8.child_paciente.cpf = self.cpf
                    self.leito8.child_paciente.telefone = self.telefone
                    self.leito8.child_paciente.genero = self.genero
                    self.leito8.child_paciente.data_de_nascimento = self.data_de_nascimento 
                    self.leito8.child_paciente.tipo_sanguineo = self.tipo_sanguineo
                    self.leito8.child_paciente.medico = self.medico

                    self.leito8.child_paciente.lbl_nome.SetLabel(self.nome)
                    self.leito8.child_paciente.lbl_prontuario.SetLabel(self.prontuario)

                elif i == 8:
                    self.leito9.child_paciente.nome = self.nome
                    self.leito9.child_paciente.prontuario = self.prontuario
                    self.leito9.child_paciente.data_entrada = self.data_entrada
                    self.leito9.child_paciente.cpf = self.cpf
                    self.leito9.child_paciente.telefone = self.telefone
                    self.leito9.child_paciente.genero = self.genero
                    self.leito9.child_paciente.data_de_nascimento = self.data_de_nascimento 
                    self.leito9.child_paciente.tipo_sanguineo = self.tipo_sanguineo
                    self.leito9.child_paciente.medico = self.medico

                    self.leito9.child_paciente.lbl_nome.SetLabel(self.nome)
                    self.leito9.child_paciente.lbl_prontuario.SetLabel(self.prontuario)

                elif i == 9:
                    self.leito10.child_paciente.nome = self.nome
                    self.leito10.child_paciente.prontuario = self.prontuario
                    self.leito10.child_paciente.data_entrada = self.data_entrada
                    self.leito10.child_paciente.cpf = self.cpf
                    self.leito10.child_paciente.telefone = self.telefone
                    self.leito10.child_paciente.genero = self.genero
                    self.leito10.child_paciente.data_de_nascimento = self.data_de_nascimento 
                    self.leito10.child_paciente.tipo_sanguineo = self.tipo_sanguineo
                    self.leito10.child_paciente.medico = self.medico

                    self.leito10.child_paciente.lbl_nome.SetLabel(self.nome)
                    self.leito10.child_paciente.lbl_prontuario.SetLabel(self.prontuario)

                elif i == 10:
                    self.leito11.child_paciente.nome = self.nome
                    self.leito11.child_paciente.prontuario = self.prontuario
                    self.leito11.child_paciente.data_entrada = self.data_entrada
                    self.leito11.child_paciente.cpf = self.cpf
                    self.leito11.child_paciente.telefone = self.telefone
                    self.leito11.child_paciente.genero = self.genero
                    self.leito11.child_paciente.data_de_nascimento = self.data_de_nascimento 
                    self.leito11.child_paciente.tipo_sanguineo = self.tipo_sanguineo
                    self.leito11.child_paciente.medico = self.medico

                    self.leito11.child_paciente.lbl_nome.SetLabel(self.nome)
                    self.leito11.child_paciente.lbl_prontuario.SetLabel(self.prontuario)

                elif i == 11:
                    self.leito12.child_paciente.nome = self.nome
                    self.leito12.child_paciente.prontuario = self.prontuario
                    self.leito12.child_paciente.data_entrada = self.data_entrada
                    self.leito12.child_paciente.cpf = self.cpf
                    self.leito12.child_paciente.telefone = self.telefone
                    self.leito12.child_paciente.genero = self.genero
                    self.leito12.child_paciente.data_de_nascimento = self.data_de_nascimento 
                    self.leito12.child_paciente.tipo_sanguineo = self.tipo_sanguineo
                    self.leito12.child_paciente.medico = self.medico

                    self.leito12.child_paciente.lbl_nome.SetLabel(self.nome)
                    self.leito12.child_paciente.lbl_prontuario.SetLabel(self.prontuario)

                elif i == 12:
                    self.leito13.child_paciente.nome = self.nome
                    self.leito13.child_paciente.prontuario = self.prontuario
                    self.leito13.child_paciente.data_entrada = self.data_entrada
                    self.leito13.child_paciente.cpf = self.cpf
                    self.leito13.child_paciente.telefone = self.telefone
                    self.leito13.child_paciente.genero = self.genero
                    self.leito13.child_paciente.data_de_nascimento = self.data_de_nascimento 
                    self.leito13.child_paciente.tipo_sanguineo = self.tipo_sanguineo
                    self.leito13.child_paciente.medico = self.medico

                    self.leito13.child_paciente.lbl_nome.SetLabel(self.nome)
                    self.leito13.child_paciente.lbl_prontuario.SetLabel(self.prontuario)

                elif i == 13:
                    self.leito14.child_paciente.nome = self.nome
                    self.leito14.child_paciente.prontuario = self.prontuario
                    self.leito14.child_paciente.data_entrada = self.data_entrada
                    self.leito14.child_paciente.cpf = self.cpf
                    self.leito14.child_paciente.telefone = self.telefone
                    self.leito14.child_paciente.genero = self.genero
                    self.leito14.child_paciente.data_de_nascimento = self.data_de_nascimento 
                    self.leito14.child_paciente.tipo_sanguineo = self.tipo_sanguineo
                    self.leito14.child_paciente.medico = self.medico

                    self.leito14.child_paciente.lbl_nome.SetLabel(self.nome)
                    self.leito14.child_paciente.lbl_prontuario.SetLabel(self.prontuario)

                elif i == 14:
                    self.leito15.child_paciente.nome = self.nome
                    self.leito15.child_paciente.prontuario = self.prontuario
                    self.leito15.child_paciente.data_entrada = self.data_entrada
                    self.leito15.child_paciente.cpf = self.cpf
                    self.leito15.child_paciente.telefone = self.telefone
                    self.leito15.child_paciente.genero = self.genero
                    self.leito15.child_paciente.data_de_nascimento = self.data_de_nascimento 
                    self.leito15.child_paciente.tipo_sanguineo = self.tipo_sanguineo
                    self.leito15.child_paciente.medico = self.medico

                    self.leito15.child_paciente.lbl_nome.SetLabel(self.nome)
                    self.leito15.child_paciente.lbl_prontuario.SetLabel(self.prontuario)

                elif i == 15:
                    self.leito16.child_paciente.nome = self.nome
                    self.leito16.child_paciente.prontuario = self.prontuario
                    self.leito16.child_paciente.data_entrada = self.data_entrada
                    self.leito16.child_paciente.cpf = self.cpf
                    self.leito16.child_paciente.telefone = self.telefone
                    self.leito16.child_paciente.genero = self.genero
                    self.leito16.child_paciente.data_de_nascimento = self.data_de_nascimento 
                    self.leito16.child_paciente.tipo_sanguineo = self.tipo_sanguineo
                    self.leito16.child_paciente.medico = self.medico

                    self.leito16.child_paciente.lbl_nome.SetLabel(self.nome)
                    self.leito16.child_paciente.lbl_prontuario.SetLabel(self.prontuario)

    """Update leitos
    """
    def updLeito(self, serial, leito, disp, msg_disp, msg_stat, color):
        print serial, leito, disp
        if leito == 1:
            if disp == 1:
                self.child_canal_11 = dispositivo.Canal(self, -1, serial, (94, 3), (280, 131), msg_disp, msg_stat, color)
            elif disp == 2:
                self.child_canal_12 = dispositivo.Canal(self, -1, serial, (94+280+1, 3), (280, 131), msg_disp, msg_stat, color)
        elif leito == 2:
            if disp == 1:
                self.child_canal_21 = dispositivo.Canal(self, -1, serial, (94, 3), (280, 131), msg_disp, msg_stat, color)
            elif disp == 2:
                self.child_canal_22 = dispositivo.Canal(self, -1, serial, (94+280+1, 3), (280, 131), msg_disp, msg_stat, color)
        
                

if __name__ == "__main__":
    main()
    app = wx.App()
    frame = MyForm().Show()
    app.MainLoop()

