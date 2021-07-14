import wx
import adder_module

class Compute(adder_module.Adder):
    def evt_click( self, event ):
        a = int(self.text_num1.GetValue())
        b = int(self.text_num2.GetValue())
        self.lbl_result.SetLabel(str(a+b))

app = wx.App()
frame = Compute(parent=None)
frame.Show(True)
app.MainLoop()
