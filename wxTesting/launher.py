'''
Created on Jun 22, 2012

@author: sharvey3
'''

import wx
import bitmaps

"""Subclass of MyFrame1, which is generated by wxFormBuilder."""


# Implementing MyFrame1
class dMyFrame1( bitmaps.MyFrame1 ):
	def __init__( self, parent ):
		bitmaps.MyFrame1.__init__( self, parent )
	
	# Handlers for MyFrame1 events.
	def do_config( self, event ):
		# TODO: Implement do_config
		print "Hello from override"
		pass
	
	

class MyApp(wx.App):
	def OnInit(self):
		self.frame = dMyFrame1(None)
		
		self.frame.Show()
		
		return True
	
	


if __name__ == "__main__":
	app = MyApp(False)
	app.MainLoop()