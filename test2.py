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


class MyCanal(wx.Frame):	#classe herdada da classe "Frame"
	def __init__(self, posx, posy, color):
          wx.Frame.__init__(self, None, wx.ID_ANY, "", size=(300,200), style = wx.CAPTION | wx.STAY_ON_TOP)
          self.SetPosition(wx.Point(posx, posy))
          self.SetBackgroundColour(color)
          self.Show(True)


class MyForm(wx.Frame):	#classe herdada da classe "Frame"
	def __init__(self):
		window = wx.Frame.__init__(self, None, title="Full screen")
		self.SetBackgroundColour('#333333')
		self.ShowFullScreen(True)

		self.panel = MyPanel(self)
		self.canal1 = MyCanal(-10, -10, '#f78700')
		self.canal2 = MyCanal(-10, 230, '#2d85cf')
		#self.canal.Show(True)



if __name__ == "__main__":
	main()
	app = wx.App()
	frame = MyForm().Show()
	app.MainLoop()

