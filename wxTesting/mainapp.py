'''
Created on Jun 27, 2012

@author: sharvey3
'''
import wx
import gui

import logging
logging.basicConfig(level = logging.WARNING)

class mf(gui.MainFrame):
	def __init__(self, parent ):
		gui.MainFrame.__init__(self, parent )
		
		logging.debug("mf initialized")
			
	# Handlers for MyFrame1 events.
	def OnHit(self, event):
		val = int(self.counter.GetLabel())
		val += 1
		self.counter.SetLabel(str(val))
	
		if val == 10:
			dlg = gui.TestDialog(self)
			dlgval = dlg.ShowModal()
			dlg.Destroy()
			print dlgval
		
	def OnStand(self, event):
		val = int(self.counter.GetLabel())
		val += -1
		self.counter.SetLabel(str(val))

		if val % 3 == 0:
			self.spt_button.Enabled = False
		else:
			self.spt_button.Enabled = True
	
	def keypress(self, event):
		logging.debug("OnKey triggered in mainapp")
		keycode = event.GetKeyCode()
		if keycode <= 256:
			key = chr(keycode)
			
			if key == "H":
				self.OnHit(event)	
			elif key == "S":
				self.OnStand(event)



class MyApp(wx.App):
	def OnInit(self):
		self.frame = mf(None)
		self.SetTopWindow(self.frame)
		self.frame.Show()
		
		return True
	


	
	
if __name__ == "__main__":
	app = MyApp(False)
	app.MainLoop()