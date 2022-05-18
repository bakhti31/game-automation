# coding: utf-8
#
import uiautomator2 as u2

d = u2.connect()

havewinner = 0
while havewinner:
	for x in d.xpath('//*[contains(@content-desc, "LEVEL \n48")]').all() :
		# if :
			# pass
	    x.click()
	    # print(x.info)
	    time.sleep(.2)
	    d(description="EXPLOIT").click()
	    # print(d(description="FIREWALL: ").right(className="android.view.View").info['contentDescription'])
	    # print(d.xpath('//*[@content-desc="LEVEL: "]/following::android.view.View[1]').info['contentDescription'])
	    # time.sleep(1)
    



# # coding: utf-8
# #
# import uiautomator2 as u2

# d = u2.connect()
# running = True
# while running:
#     for x in d.xpath('//*[contains(@content-desc, "LEVEL \n")]').all() :		    
#     # for x in d.xpath('//*[contains(@content-desc, "LEVEL \n57")]').all() :
#         x.click()
        
#         time.sleep(.2)
#         if d(description="UNABLE TO RETRIEVE DATA, SCAN BLOCKED \nUPGRADE YOUR SCAN SOFTWARE").exists:
#             continue
#         spam = d.xpath('//*[@content-desc="SPAM: "]/following::android.view.View[1]').info['contentDescription']
#         spamlvl = spam.replace(",","")
#         print(int(spamlvl))
#         time.sleep(1)
#         if int(spamlvl) > 1000000000:
#             d(description="EXPLOIT").click()
#         # time.sleep(1)
#         # d(description="EXPLOIT").click()
#     d.click(0.526, 0.72)