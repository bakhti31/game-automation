import uiautomator2 as u2
from time import sleep
from datetime import datetime, timedelta

d = u2.connect()

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
	
	def scanWith(self, fw=None,crewName=None, spamLvl=None):
		for x in d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/*/android.view.View[*]').all() :
		    
		    x.click()
		    sleep(.2)
		    # print(d(description="FIREWALL: ").right(className="android.view.View").info['contentDescription'])
		    try:
			    fwlvl=d.xpath('//*[@content-desc="FIREWALL: "]/following::android.view.View[1]').info['contentDescription']
			    fw = fwlvl.replace(",","")
			    spmlvl=d.xpath('//*[@content-desc="SPAM: "]/following::android.view.View[1]').info['contentDescription']
			    spm = spmlvl.replace(",","")
			    if (int(fw) < 50000000000 & int(spm) > 1000000000):# 20B Fw LVL
			        d(description="EXPLOIT").click()	
		    except:
		    	pass
		    sleep(1)
		    

	def scanFW(self,fwlvl):
		for x in d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/*/android.view.View[*]').all() :		    
		    x.click()
		    sleep(.2)
		    # print(d(description="FIREWALL: ").right(className="android.view.View").info['contentDescription'])
		    print(d.xpath('//*[@content-desc="FIREWALL: "]/following::android.view.View[1]').info['contentDescription'])
		    sleep(1)
		pass

	def prototypeScanSpam(self):
		for x in d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/*/android.view.View[*]').all() :
		    
		    x.click()
		    sleep(.2)
		    ip=x.info['contentDescription'].split("\nLEVEL")[0]
		    try:
		    	if(d.xpath('//*[@content-desc="SPAM: "]').exists):
		    		spmlvl=d.xpath('//*[@content-desc="SPAM: "]/following::android.view.View[1]').info['contentDescription']
		    		spm = spmlvl.replace(",","")
		    		if (int(spm) > 1000000000):# 20B Fw LVL
		    			d(description="EXPLOIT").click()
		    		sleep(.8)
		    except e:
		    	pass
		    # print(d(description="FIREWALL: ").right(className="android.view.View").info['contentDescription'])
		    

net = Network()
while True:
	# net.prototypeScanSpam()
	# net.scanAll()
	# net.scanFW(20000000000)
	net.scanWith()
