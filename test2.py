# -*- iso-8859-1 -*-

"""Modulo main

"""
import wx
 

def main():
	print "Inicializando modulo principal..."

class MyPanel(wx.Panel):	#classe herdada da classe "Panel"
    def __init__(self, parent, sizexy):
        wx.Panel.__init__(self, parent, style=wx.NO_BORDER)
	#self.SetBackgroundColour((179, 179, 179))
        self.Bind(wx.EVT_KEY_DOWN, self.onKey)
	#info = wx.TextCtrl(self,104,pos=(80,250),size=(240,20)) 
        #button1 = wx.Button(self, -1, '100.00', (10, 10))
        #button2 = wx.Button(self, -1, '100.00', (10, 60))

	""" Verifica se a tecla ESC foi pressionada
	"""
    def onKey(self, event):
        key_code = event.GetKeyCode()
        if key_code == wx.WXK_ESCAPE:
            self.GetParent().Close()
        else:
            event.Skip()

    def onSetKey(self, key):
        print(key)


class MyCanal(wx.Frame):	#classe herdada da classe "Frame"
	def __init__(self, posx, posy, color):
          wx.Frame.__init__(self, None, wx.ID_ANY, "", size=(300,200), style = wx.CAPTION | wx.STAY_ON_TOP)
          self.SetPosition(wx.Point(posx, posy))
          self.SetBackgroundColour(color)
          self.Show(True)


class MyForm(wx.Frame):	#classe herdada da classe "Frame"
	def __init__(self):
		#window = wx.Frame.__init__(self, None, title="Full screen")
		wx.Frame.__init__(self, None, wx.ID_ANY, "", size=(327,212), style = wx.CAPTION)
		self.SetBackgroundColour('#333333')
		#self.ShowFullScreen(True)
		self.Show(True)

		self.panel = MyPanel(self, -1)
		self.panel.onSetKey(11)
		#self.canal1 = MyCanal(-10, -10, '#f78700')
		#self.canal2 = MyCanal(-10, 230, '#2d85cf')
		#self.canal.Show(True)
		val = '100.00                                                '
		flux = wx.StaticText(self.panel, -1, val, (50, 88))
		flux.SetForegroundColour('WHITE')
		font = wx.Font(22,  wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
		flux.SetFont(font)
		flux.Wrap(400)

		val = '200.00        '
		flux = wx.StaticText(self.panel, -1, val, (150, 88))
		flux.SetForegroundColour('WHITE')
		font = wx.Font(12,  wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
		flux.SetFont(font)
		flux.Wrap(200)

		#flux = wx.StaticText(panel, -1, "100.00", (88, 88))
		#sizer_1.Add(self.flux, 1, 0, 0)
		#sizer_1.Add(self.flux,30, wx.EXPAND,30)


if __name__ == "__main__":
	main()
	app = wx.App()
	frame = MyForm().Show()
	app.MainLoop()

