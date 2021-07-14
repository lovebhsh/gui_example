# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Adder
###########################################################################

class Adder ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"무엇이든 더해 보세요.", pos = wx.DefaultPosition, size = wx.Size( 500,120 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.text_num1 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.text_num1, 0, wx.ALL, 5 )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )

        self.text_num2 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.text_num2, 0, wx.ALL, 5 )

        self.btn_compute = wx.Button( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.btn_compute, 0, wx.ALL, 5 )

        self.lbl_result = wx.StaticText( self, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_result.Wrap( -1 )

        bSizer3.Add( self.lbl_result, 0, wx.ALL, 5 )


        self.SetSizer( bSizer3 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.btn_compute.Bind( wx.EVT_BUTTON, self.evt_click )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def evt_click( self, event ):
        event.Skip()


