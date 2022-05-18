# coding: utf-8
#
import uiautomator2 as u2

d = u2.connect()

# d.xpath('//*[@content-desc="MERGE"]/following::android.view.View/android.view.View[@content-desc="CPU"]').click()
# d.xpath('//*[@content-desc="MERGE"]/following::android.view.View/android.view.View[@content-desc="CPU"]/').click()
# d.xpath('//*[@content-desc="MERGE"]/following::android.view.View/android.view.View[@content-desc="SSD"]/android.widget.ImageView[1]').click()

congrats = d.xpath('//*[@content-desc="CONGRATULATIONS"]')
merge = d.xpath('//*[@content-desc="MERGE"]')

CPU1 = d.xpath('//*[@content-desc="MERGE"]/following::android.view.View/android.view.View[@content-desc="CPU" and count(android.widget.ImageView)=2]')
CPU2 = d.xpath('//*[@content-desc="MERGE"]/following::android.view.View/android.view.View[@content-desc="CPU" and count(android.widget.ImageView)=3]')
CPU3 = d.xpath('//*[@content-desc="MERGE"]/following::android.view.View/android.view.View[@content-desc="CPU" and count(android.widget.ImageView)=4]')
CPU4 = d.xpath('//*[@content-desc="MERGE"]/following::android.view.View/android.view.View[@content-desc="CPU" and count(android.widget.ImageView)=5]')

SSD1 = d.xpath('//*[@content-desc="MERGE"]/following::android.view.View/android.view.View[@content-desc="SSD" and count(android.widget.ImageView)=2]')
merged = 0
while merged < 10:
    if SSD1.wait(timeout=1):
        if len(SSD1.all()) > 2:
            for x in SSD1.all():
                x.click()
                if d.xpath('//*[@content-desc="YOU CAN ONLY MERGE PARTS WITH THE SAME LEVEL (STARS)"]').wait(timeout=0.5):
                    d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[8]/android.view.View[3]').click()
                    d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[8]/android.view.View[2]').click()
                else:
                    merge.click()
                if congrats.wait(timeout=1):
                    merged += 1 
                    print(merged)
                    congrats.click()
        else:
            d.swipe(448, 820, 0, 820, 0.5)
    else:
        d.swipe(448, 820, 0, 820, 0.5)

# for x in CPU4.all():
    # x.click()

