import uiautomator2 as u2
from time import sleep
from datetime import datetime, timedelta

d = u2.connect()
last = datetime.now();
while True:    
    
    # For Task DF
    now = datetime.now()

    sleep(1)    
    if (d.app_wait("vhack.os.reloaded", front=True)):
        if (d(description="RECONNECT").exists):
            d(description="RECONNECT").click() 
            
            
            
# Search for logs code            
        # if d.xpath('//*[@content-desc="ACTIVE SPYWARE"]').exists:
        #     d(scrollable=True)[1].scroll(steps=30)
        #     d(scrollable=True)[0].fling.toEnd()
        #     list(d(focusable=True))
        #     logs = d(focusable=True)[16].info["contentDescription"]
        #     code=logs.split("\r\n")[-2]
        #     if(len(code)==13): print("Its Code")
        #     else: print("Not Code Bitch")
        #     print(code)
    
        
        # Auto Deface from end user in terminal
        if (last == -1 or (now >= last)):
            nexttime = timedelta(minutes=+30)
            last = nexttime + now
            print(last)
            if not d(description="TERMINAL").exists:
                d(description="HOME").click()
            
            d(description="TERMINAL").click()
            d(scrollable=True).fling.toEnd()
            d.click(0.443, 0.867)
            d.double_click(0.758, 0.848)
            d.click(0.528, 0.803)
            d(description="HOME").click()
                
        # DF task daily
        # if (last == -1 || last > x):
        #     d(description="TERMINAL").click()
        #     d.xpath('//*[@content-desc="TERMINAL"]').click()
        #     d.click(0.431, 0.632)
        #     d.click(0.737, 0.731)
        #     last = x
            # addtie every 30 minutes
        # goto network
        # open one connection
        # deface
        # home
            
        #daily mission
        # Edit logs 
        
        # for i in range (1,50):
        #     d(description="GET LOG FILE").click()
        #     d(description="EDIT").click()
        #     d(description="SAVE").click()
        # After you can get Netcoin Miner
        # if d.xpath('//*[contains(@content-desc,"NetCoin Miner refilled! @all")]').exists:
        #     d(description="HOME").click()
        #     d(description="NC MINING").click()

            
        # Auto Defend when someone says defend
        if d.xpath('//*[contains(@content-desc,"@all DEFEND")]').exists:
            d(description="HOME").click()
            d(description="CREW").click()
            d.xpath('//*[@content-desc="WE ARE GETTING ATTACKED!\nTAP HERE TO DEFEND"]').click()
            d(description="HOME").click()
            
        if d.xpath('//*[contains(@content-desc,"@all ATTACK")]').exists:
            d(description="HOME").click()
            d(description="CREW").click()
            d.xpath('//*[@content-desc="WE ARE PREPARING A CREW ATTACK!\n TAP HERE TO JOIN"]').click()
            
        # Prepare when defend but you are on global chat
        # if d(description="!").exists:
        #     d.xpath('//*[contains(@content-desc,"\n:\n")]').click()
        #     d.xpath('//*[@content-desc="#\nCREW"]').click()
        #     d(description="HOME").click()
        #     if d.xpath('//*[contains(@content-desc,"DEFEND")]').exists:
        #         d(description="HOME").click()
        #         d(description="CREW").click()
        #         d.xpath('//*[@content-desc="WE ARE GETTING ATTACKED!\nTAP HERE TO DEFEND"]').click()
            
        #     d(description="HOME").click()
        #     d.xpath('//*[contains(@content-desc,"\n:\n")]').click()
        #     d.xpath('//*[@content-desc="#\nENGLISH"]').click()
        #     d(description="HOME").click()
        
        
        # ads free clicker
        
        if (d(description="FREE \n250").exists):
            d(description="FREE \n250").click()
            sleep(.3)
            d.app_stop("vhack.os.reloaded")
            sleep(2)
            d.app_start("vhack.os.reloaded", ".MainActivity")
        
        
        # tex=d.xpath('//*[contains(@text,"CODE")]').get_text()
        # d(text="SBtf2Dh7vU2y, CODE").click()
        # d.xpath('//*[@resource-id="com.cotedia.clipkey:id/globeButton"]').click()
        
        # Code with clipkey
        # if d.xpath('//*[contains(@text,"CODE")]').exists:
        #     d.xpath('//*[contains(@text,"CODE")]').click()
        #     d.xpath('//*[@resource-id="com.cotedia.clipkey:id/clipboardItemsContainerFrame"]/android.widget.Button[0]').click()
        #     d(description="SEND").click()
        #     d.long_click(0.378, 0.859)
        #     d(text="Delete").click()
        
        
        
        # print(d(className="android.widget.ScrollView").info)
        
        # if (d.xpath('//*[contains(@content-desc,"ATTACK")]').exists) :
        #     for i in range(1,20):
        #         d.xpath('//*[contains(@content-desc,"ATTACK")]').click()
        #         sleep(3)
        #         d.xpath('//*[@content-desc="BACK"]').click()
        #         sleep(3)
        
        # if (d(longClickable=True).exists):
        #     d(longClickable=True).click()
        #     sleep(1)
        #     d.xpath('//*[@content-desc="GET LOG FILE"]').click()
        #     sleep(1)
        #     print(d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[11]/android.view.View[1]/android.view.View[@longClickable=True]').info)
        
        
        # d(description="NC MINING").click()
        # d.click(0.501, 0.936) #Center
        # d(description="-").click() #perkecil
        # d(description="+").click() #perbesar
        # if d(description="NETWORK").exists :
        #     d(description="NETWORK").click()
        
        
        
        # Bounty Hunter
        # d(description="vHack System[NEW BOUNTY!] We are looking for a player on level 111! Search and exploit him for 25,000,000 vTC and a Spin! @all  ").click()
        # d.xpath('//*[@content-desc="vHack System [NEW BOUNTY!] We are looking for a player on level 111! Search and exploit him for 25,000,000 vTC and a Spin! @all  "]').click()
        
        # if d.xpath('//*[contains(@content-desc,"BOUNTY!")]').exists:
        #     info = d.xpath('//*[contains(@content-desc,"BOUNTY!")]').info
        #     a = info['contentDescription'].split("level ")
        #     b = a[0].split(" ")
        #     c = b[0].split("!")
        #     lvl = c[0];
        #     # # Searching for player with lvl needed
        #     if d(description="[ vSCAN BUILD: ").exists:
        #         bounty = f"@content-desc,'LEVEL \n{lvl}'"
        #         if (d.xpath(f'//*[contains({bounty})]').exists):
        #             d.xpath(f'//*[contains({bounty})]').click()
        #             d.xpath('//*[@content-desc="EXPLOIT"]').click()
        #             print("bisa kok")
        #         else:
        #             d.click(0.505, 0.716)
        # d(description="TERMINAL").click()
        
        
#         d(description="vHack System
# [DEV]
# BOT
# [19:21]
# [BOUNTY] We are still looking for a level 84 player! Find and exploit him for 25,000,000 vTC and a Spin!  ").click()
        
        
        
        
#         d(description="vHack System
# [DEV]
# BOT
# [19:24]
# Target found by @Decloved! 25,000,000 vTC and a Spin were credited to your account. @all  ").click()
       