'''
Created on Jun 28, 2012

@author: sharvey3
'''

import gui

#def click_hit(self, event):
#	val = int(self.counter.GetLabel())
#	val += 1
#	self.counter.SetLabel(str(val))
#	
#	if val == 10:
#		self.ShowDlg()
	
	
def click_stand(self, event):
	val = int(self.counter.GetLabel())
	val += -1
	self.counter.SetLabel(str(val))