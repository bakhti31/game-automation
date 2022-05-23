import uiautomator2 as u2
from time import sleep
from datetime import datetime, timedelta
d = u2.connect("NZV8TKIBMV5LOBPF")
last = datetime.now();

def defaceRandom():
	for x in d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/*/android.view.View[*]').all() :
	    x.click()
	    sleep(.2)
	    # print(d(description="FIREWALL: ").right(className="android.view.View").info['contentDescription'])
	    fw = d.xpath('//*[@content-desc="FIREWALL: "]/following::android.view.View[1]').info['contentDescription'].replace(",","")
	    # firewall=fw.
	    print(fw)
	    if int(fw) < 1000000000:
	    	
	    	d(description="EXPLOIT").click()
	    	d(description="TERMINAL").click()
	    	break
	    sleep(1)

while True:
	now = datetime.now()
	if (last == -1 or (now >= last)):
		nexttime = timedelta(minutes=+30)
		last = nexttime + now
		print(last)

		# #defacing by end of target in terminal
		# if not d(description="TERMINAL").exists:
		#     d(description="HOME").click()

		# d(description="TERMINAL").click()
		# d(scrollable=True).fling.toEnd()
		# d.click(0.443, 0.867)
		# d.double_click(0.758, 0.848)
		# d.click(0.528, 0.803)
		# d(description="HOME").click()