# -*- iso-8859-1 -*-

"""Modulo main

"""
import wx
 

def main():
	print "Inicializando modulo principal..."

class MyPanel(wx.Panel):	#classe herdada da classe "Panel"
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


class MyForm(wx.Frame):	#classe herdada da classe "Frame"
	def __init__(self):
          wx.Frame.__init__(self, None, wx.ID_ANY, "", size=(327,212), style = wx.CAPTION)
          panel = wx.Panel(self, -1)
          #self.SetBackgroundColour('#2d85cf')
          self.SetBackgroundColour('#f78700')
		#self.ShowFullScreen(True)

		#self.panel = MyPanel(self)





if __name__ == "__main__":
	main()
	app = wx.App()
	frame = MyForm().Show()
	app.MainLoop()

