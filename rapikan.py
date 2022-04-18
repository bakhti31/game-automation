import uiautomator2 as u2
from time import sleep
from datetime import datetime, timedelta

d = u2.connect() #For already Create ADB
# d = u2.connect_adb_wifi("2.tcp.ngrok.io:13275") #For Connecting over Wifi/Internet

class Network:
	"""docstring for Network"""
	def __init__(self):
		pass

	def scanAll(self):
		for x in d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/*/android.view.View[*]').all() :
		    # x = d(target)
		    print(x.info)
		    x.click()
		    sleep(1)
			
	def scanFW(self,fwlvl):
		for x in d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/*/android.view.View[*]').all() :		    
		    x.click()
		    sleep(.2)
		    # print(d(description="FIREWALL: ").right(className="android.view.View").info['contentDescription'])
		    print(d.xpath('//*[@content-desc="FIREWALL: "]/following::android.view.View[1]').info['contentDescription'])
		    sleep(1)
		pass

	def prototypeScanFW(fw):
		for x in d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/*/android.view.View[*]').all() :
		    
		    x.click()
		    sleep(.2)
		    # print(d(description="FIREWALL: ").right(className="android.view.View").info['contentDescription'])
		    fwlvl=d.xpath('//*[@content-desc="FIREWALL: "]/following::android.view.View[1]').info['contentDescription']
		    
		    fw = fwlvl.replace(",","")
		    if (int(fw) < 20000000000):# 20B Fw LVL
		        d(description="EXPLOIT").click()	
		    sleep(1)

class Terminal:
	"""docstring for Terminal"""
	def __init__(self):
		pass

	def open(self):
		d(description="HOME").click()
		d(description="TERMINAL").click()

	def isLogScrollable(self):
		sleep(.5)
		cek = d(scrollable=True)
		if (len(cek)>1):
			return True;
		else:
			return False;

	def readLog(self):
		if self.isLogScrollable():
			d(scrollable = True)[0].fling.toEnd()
			sleep(.5)
			# logs = d.xpath('//*[@scrollable = "true"]/android.view.View[not(longClickable ="true")]/*/*[last()]').info['contentDescription']
			if d.xpath('//*[@scrollable = "true"]/android.view.View[not(@longClickable ="true")]/*/*[last()]').exists:
				logs = d.xpath('//*[@scrollable = "true"]/android.view.View[@long-clickable="false"]/*/*[last()]').info['contentDescription']
			else:
				logs = d.xpath('//*[@scrollable = "true"]/android.view.View[@long-clickable="false"]').info['contentDescription']
		else:
			child = d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[@focusable="true"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]').info['childCount']
			if (int(child) > 1):
				logs = d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[@focusable="true"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[last()]').info['contentDescription']
			else:
				logs = d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/*/android.view.View[1]/android.view.View[1]/android.view.View[1]').info["contentDescription"]
		return logs

	def openLog(self):
		d(description="GET LOG FILE").click()

	def editLog(self):
		d(description="EDIT").click()
		if(d(description="SAVE").exists(timeout=6.0)):
			return True
		else:
			return False

	def nextTarget(self):
		d.click(0.543, 0.837)
		d.swipe(182, 879, 182, 680.5)
	
	def getCode(self):
		self.openLog()
		log = self.readLog()
		code = log.split("\r\n")[-2]
		print(code)

	def cutAndSaveCode(self):
		self.editLog()
	    
		txtBox = d(className = "android.widget.EditText")
		txt = txtBox.get_text()
		cuttxt=txt.split("\n")
		code = cuttxt[-1]
		pastetxt = txt.replace(code, "")
		txtBox.set_text(pastetxt)
		d(description="SAVE").click()


term = Terminal()
# term.open()
while True:
	codev = term.getCode()
	if codev:
		print(codev)

	term.nextTarget()




# bisascroll = d(scrollable = True)
# if(len(bisascroll) > 1):
    # d(scrollable = True)[0].fling.toEnd()
    # logs = d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/*/android.view.View[1]/android.view.View[1]/android.view.View[last()]').info['contentDescription']
# else:
    # child = d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/*/android.view.View[1]/android.view.View[1]').info['childCount']
    # if (int(child) > 1):
    #     logs = d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/*/android.view.View[1]/android.view.View[1]/android.view.View[last()]').info['contentDescription']
    # else:
    #     logs = d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/*/android.view.View[1]/android.view.View[1]/android.view.View[1]').info["contentDescription"]   
        
    
"""code = logs.split("\r\n")[-2]
print(code)
"""
