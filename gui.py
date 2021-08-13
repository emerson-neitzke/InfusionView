# -*- iso-8859-1 -*-

"""Modulo main

"""
import wx
import leito
import paciente

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


class Gui(wx.Frame): #classe herdada da classe "Frame"
    def __init__(self):
        window = wx.Frame.__init__(self, None, title="Full screen")
        self.SetBackgroundColour('GRAY')
        self.ShowFullScreen(True)

        self.panel = MyPanel(self)

        self.leito_1 = leito.Leito(self, 1, (1,1), (960,135), '#232728')
        self.leito_2 = leito.Leito(self, 2, (1,135), (960,135), '#232728')



if __name__ == "__main__":
    main()
    app = wx.App()
    frame = Gui().Show()
    app.MainLoop()

