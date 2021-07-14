import wx
import myframe

app = wx.App()
frame = myframe.JHKFrame(parent=None)
frame.Show(True)
app.MainLoop()
