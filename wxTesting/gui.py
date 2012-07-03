'''
Created on Jun 20, 2012

@author: sharvey3
'''

import wx

BTN_HIT = wx.NewId()
BTN_STD = wx.NewId()
BTN_DBL = wx.NewId()
BTN_SPT = wx.NewId()
	
class MainFrame(wx.Frame):
	def __init__ (self, parent, id = wx.ID_ANY, title = "Trainer",
					pos=wx.DefaultPosition, size=wx.DefaultSize,
					style=wx.DEFAULT_FRAME_STYLE, name = "My Frame"):
		
		super (MainFrame, self).__init__(parent, id, title, pos, size, style, name)
		
		
		# Attributes
		panel = wx.Panel(self)
		panel.SetBackgroundColour(wx.WHITE)
		
		
		# Attempt to hack up a gridbagsizer
		gbs = self.gbs = wx.GridBagSizer(5,5)
		
		
		self.counter = wx.StaticText(panel, -1, "0")
		
		hit_button = wx.Button(panel, BTN_HIT, "H")
		std_button = wx.Button(panel, BTN_STD, "S")
		dbl_button = wx.Button(panel, BTN_DBL, "D")
		spt_button = self.spt_button = wx.Button(panel, BTN_SPT, "P")
		
		gbs.Add(self.counter, (0,0) , (1,2), wx.ALIGN_CENTER, 1)
		gbs.Add(hit_button, (2,0))
		gbs.Add(std_button, (2,1))
		gbs.Add(dbl_button, (3,0))
		gbs.Add(spt_button, (3,1))
		
		
		
		box = wx.BoxSizer()
		box.Add(gbs, 0, wx.ALL, 10)
		
		panel.SetSizerAndFit(box)
		self.SetClientSize(panel.GetSize())
		
#				
				
		# Event Handlers
		self.Bind(wx.EVT_BUTTON, self.OnHit, hit_button)
		self.Bind(wx.EVT_BUTTON, self.OnStand, std_button)
		
		def OnHit(self, event):
			event.Skip()
			
		def OnStand(self, event):
			event.Skip()
		


class TestDialog(wx.Dialog):
	def __init__(self, parent, id = wx.ID_ANY, title = "Test", size=wx.DefaultSize, pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE, useMetal=False):
		super (TestDialog, self).__init__(parent, id, title, pos, size, style)
		
		type = "Spam spam spam"
		
		self.type = wx.TextCtrl(self, value=type, style=wx.TE_READONLY)
		self.details = wx.TextCtrl(self, value="", style=wx.TE_READONLY | wx.TE_MULTILINE)
		# Layout
		self.__DoLayout()
		self.SetInitialSize()

	def __DoLayout(self):
		sizer = wx.GridBagSizer(vgap=8, hgap=8)
		type_lbl = wx.StaticText(self, label="Type:")
		detail_lbl = wx.StaticText(self, label="Details:")
		# Add the event type fields
		sizer.Add(type_lbl, (1, 1))
		sizer.Add(self.type, (1, 2), (1, 15), wx.EXPAND)
		# Add the details field
		sizer.Add(detail_lbl, (2, 1))
		sizer.Add(self.details, (2, 2), (5, 15), wx.EXPAND)
		# Add a spacer to pad out the right side
		sizer.Add((5, 5), (2, 17))
		# And another to the pad out the bottom
		sizer.Add((5, 5), (7, 0))
		self.SetSizer(sizer)
			
	