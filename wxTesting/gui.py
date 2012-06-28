'''
Created on Jun 20, 2012

@author: sharvey3
'''

import wx

NEXT_BUTTON = 1
PREV_BUTTON = wx.NewId()
	
class MainFrame(wx.Frame):
	def __init__ (self, parent, id = wx.ID_ANY, title = "Trainer",
					pos=wx.DefaultPosition, size=wx.DefaultSize,
					style=wx.DEFAULT_FRAME_STYLE, name = "My Frame"):
		
		super (MainFrame, self).__init__(parent, id, title, pos, size, style, name)
		
		
		# Attributes
		self.panel = wx.Panel(self)
		self.panel.SetBackgroundColour(wx.WHITE)
		
		self.counter = wx.TextCtrl(self.panel, -1, "0", pos = (50, 20))
		
		next_button = wx.Button(self.panel, NEXT_BUTTON, label = "Next", pos = (50,50))
		prev_button = wx.Button(self.panel, PREV_BUTTON, label = "Prev", pos = (50,75))
		
		
		
		# Event Handlers
		self.Bind(wx.EVT_BUTTON, self.OnNext, next_button)
		self.Bind(wx.EVT_BUTTON, self.OnPrev, prev_button)
		
		def OnNext(self, event):
			event.Skip()
			
		def OnPrev(self, event):
			event.Skip()
		

		
		

	
	