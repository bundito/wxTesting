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
	
	
	
	
	
	

class MyApp(wx.App):
	def OnInit(self):
		self.frame = mf(None)
		self.SetTopWindow(self.frame)
		self.frame.Show()
		
		return True
	


	
	
if __name__ == "__main__":
	app = MyApp(False)
	app.MainLoop()