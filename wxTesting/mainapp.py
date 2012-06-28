'''
Created on Jun 27, 2012

@author: sharvey3
'''
import wx
import gui
import logic

class mf(gui.MainFrame):
	def __init__(self, parent ):
		gui.MainFrame.__init__(self, parent )
	
	# Handlers for MyFrame1 events.
	def OnNext(self, event):
		logic.click_next(self, event)
		
	
	def OnPrev(self, event):
		logic.click_prev(self, event)


class MyApp(wx.App):
	def OnInit(self):
		self.frame = mf(None)
		self.SetTopWindow(self.frame)
		self.frame.Show()
		
		return True
	


	
	
if __name__ == "__main__":
	app = MyApp(False)
	app.MainLoop()