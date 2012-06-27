'''
Created on Jun 20, 2012

@author: sharvey3
'''

import wx

	
class MainFrame(wx.Frame):
	def __init__ (self, parent, id = wx.ID_ANY, title = "Trainer",
					pos=wx.DefaultPosition, size=wx.DefaultSize,
					style=wx.DEFAULT_FRAME_STYLE, name = "My Frame"):
		
		super (MainFrame, self).__init__(parent, id, title, pos, size, style, name)
		
		
		# Attributes
		self.panel = wx.Panel(self)
		self.panel.SetBackgroundColour(wx.BLACK)
		
		button = wx.Button(self.panel, label = "Get Children", pos = (50,50))
		self.btnId = button.GetId()
		
		# Event Handlers
		self.Bind(wx.EVT_BUTTON, self.OnButton, button)
		
		
		
		def OnButton(self, event):
			event.Skip()
			
		

		
		

	
	