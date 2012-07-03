'''
Created on Jun 20, 2012

@author: sharvey3
'''

import wx

BTN_HIT = wx.NewId()
BTN_STND = wx.NewId()
	
class MainFrame(wx.Frame):
	def __init__ (self, parent, id = wx.ID_ANY, title = "Trainer",
					pos=wx.DefaultPosition, size=wx.DefaultSize,
					style=wx.DEFAULT_FRAME_STYLE, name = "My Frame"):
		
		super (MainFrame, self).__init__(parent, id, title, pos, size, style, name)
		
		
		# Attributes
		self.panel = wx.Panel(self)
		self.panel.SetBackgroundColour(wx.WHITE)
		
#		self.counter = wx.TextCtrl(self.panel, -1, "0", pos = (50, 20))
		
		self.counter = wx.StaticText(self.panel, -1, label = "0", pos = (50, 20))
		
		hit_button = wx.Button(self.panel, BTN_HIT, label = "H", pos = (50,50))
		stand_button = wx.Button(self.panel, BTN_STND, label = "S", pos = (50,75))
		
		
		
				
		def ShowDlg():
			dlg = wx.Dialog(self, wx.ID_ANY, "Test")
			dlg.ShowModal()
			dlg.Destroy()
		
	
	
	
		
		# Event Handlers
		self.Bind(wx.EVT_BUTTON, self.OnHit, hit_button)
		self.Bind(wx.EVT_BUTTON, self.OnStand, stand_button)
		
		def OnHit(self, event):
			event.Skip()
			
		def OnStand(self, event):
			event.Skip()
		


class TestDialog(wx.Dialog):
	def __init__(self, parent, id = wx.ID_ANY, title = "test", size=wx.DefaultSize, pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE, useMetal=False):
		super (TestDialog, self).__init__(parent, id, title, pos, size, style, name="")
		pass
	