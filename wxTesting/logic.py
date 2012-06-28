'''
Created on Jun 28, 2012

@author: sharvey3
'''



def click_next(self, event):
	val = int(self.counter.GetValue())
	val += 1
	self.counter.SetValue(str(val))
	
	
def click_prev(self, event):
	val = int(self.counter.GetValue())
	val += -1
	self.counter.SetValue(str(val))