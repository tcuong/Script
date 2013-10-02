#!/usr/bin/python

from Tkinter import *
import tkMessageBox
import Tkinter
import subprocess

class  MyHandler(object):
	def  __init__(self):
		self.onChanging = False
	def onselect(self,evt) :
	    w = evt.widget
	    index = int(w.curselection()[0])
	    value = w.get(index)
	    print 'You selected item %d: "%s"' % (index, value)
	    if self.onChanging == True:
	    	return
	    else:
	    	self.onChanging = True
	    if index > 0:
	    	self.limitBW(index)
	    else:
	    	self.removeLimitBW()
	def limitBW(self,index):
		if index == 1:
			speed = "300kbs"
		elif index == 2:
			speed = "30kbs"
		else:
			speed = "1kbs"
		subprocess.call(['sudo','ipfw', 'pipe','1','config','bw',speed])
		subprocess.call(['sudo','ipfw','add','pipe','1','dst-ip','0.0.0.0/0'])
		self.onChanging = False
		print "Finished"

	def removeLimitBW(self):
		subprocess.call(['sudo','ipfw','flush'])
		print "Finished"
		self.onChanging = False

if __name__ == '__main__': 
	handler = MyHandler()

	top = Tk()
	top.title("Change Bandwidth Limit")
	top.geometry("250x250")

	Lb1 = Listbox(top)
	Lb1.insert(0,"Default")
	Lb1.insert(1, "300kbs")
	Lb1.insert(2, "30kbs")
	Lb1.insert(3, "0kbs")
	Lb1.bind('<<ListboxSelect>>', handler.onselect)
	Lb1.pack()

	top.mainloop()

			