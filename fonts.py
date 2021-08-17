import wx
  
class PageNoSizer(wx.Panel):
      def __init__(self, parent):
          #super().__init__(parent)
          self.panel = wx.Panel.__init__(self, parent, id, pos=posxy, size=sizexy, style=wx.BORDER_SIMPLE)
          self.SetBackgroundColour(wx.BLACK)
          st = wx.StaticText(self, label="HELLO WORLD", pos=(60, 55), style=wx.TE_CENTER | wx.EXPAND | wx.ALL)
          
          st.SetForegroundColour(wx.Colour(0x00FF44))
          stylish_font = wx.Font(wx.FontInfo(20).FaceName("liberation").Bold())
          st.SetFont(stylish_font)
          st.SetSize(st.GetTextExtent(st.GetLabel()))
          
          btn = wx.Button(self, label="Next Page")
          self.Bind(wx.EVT_BUTTON, parent.OnNextPage, btn)
          
class PageWithSizer(wx.Panel):
      def __init__(self, parent):
          super().__init__(parent)
          self.SetBackgroundColour(wx.BLACK)
          
          vbox = wx.BoxSizer(wx.VERTICAL)
          st = wx.StaticText(self, label="HELLO WORLD", style=wx.TE_CENTER | wx.EXPAND | wx.ALL)
          
          st.SetForegroundColour(wx.Colour(0x00FF44))
          stylish_font = wx.Font(wx.FontInfo(20).FaceName("liberation").Bold())
          st.SetFont(stylish_font)
          st.SetSize(st.GetTextExtent(st.GetLabel()))
          
          vbox.Add(st)
          
          btn = wx.Button(self, label="Next Page")
          vbox.Add(btn, 0, wx.ALIGN_RIGHT)
          self.Bind(wx.EVT_BUTTON, parent.OnNextPage, btn)
          
          self.SetSizer(vbox)
  
  # class TestingBook(wx.Simplebook):
class TestingBook(wx.Choicebook):
  # class TestingBook(wx.Notebook):
      def __init__(self, parent):
          #super().__init__(parent)
  
          noSizer = PageNoSizer(self)      
          withSizer = PageWithSizer(self)  
   
          self.AddPage(noSizer, "PageNoSizer")
          self.AddPage(withSizer, "PageWithSizer")
          
      def OnNextPage(self, evt):
          current = self.GetSelection()
          current += 1
          if current >= self.GetPageCount():
              current = 0
          self.ChangeSelection(current)
  
class MainFrame(wx.Frame):
      
      def __init__(self):
          wx.Frame.__init__(self, None, size=wx.Size(800, 600))
          TestingBook(self)
          self.Show()
  
if __name__ == '__main__':
      app = wx.App(redirect=False)
      frame = MainFrame()
      app.MainLoop()
