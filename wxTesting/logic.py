'''
Created on Jun 28, 2012

@author: sharvey3
'''

import det_dialog

def click_hit(self, event):
	val = int(self.counter.GetLabel())
	val += 1
	self.counter.SetLabel(str(val))
	
	if val == 10:
		dlg = det_dialog.DetailsDialog(self)
		dlg.ShowModal()
		dlg.Destroy()
	
	
def click_stand(self, event):
	val = int(self.counter.GetLabel())
	val += -1
	self.counter.SetLabel(str(val))