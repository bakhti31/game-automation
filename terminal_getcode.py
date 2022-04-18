import uiautomator2 as u2
d = u2.connect()
# d = u2.connect_adb_wifi("2.tcp.ngrok.io:13275")


# Logs Edit
# for i in range (1,20):
#     d(description="GET LOG FILE").click()
#     d(description="EDIT").click()
#     d(description="SAVE").click()

# lvl = 118;
# # # Searching for player with lvl needed
# if d(description="[ vSCAN BUILD: ").exists:
#     bounty = f"@content-desc,'LEVEL \n{lvl}'"
#     if (d.xpath(f'//*[contains({bounty})]').exists):
#         d.xpath(f'//*[contains({bounty})]').click()
#         d.xpath('//*[@content-desc="EXPLOIT"]').click()
#         print("bisa kok")
#     else:
#         d.click(0.505, 0.716)


# coding: utf-8
#

def first_target():
    d.click(0.604, 0.599)
    d(description="GET LOG FILE").click()

def next_target():
    d.click(0.543, 0.837)
    d.swipe(0,846,0,661)

def long_text():
    anu=d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[13]/android.view.View[1]/android.view.View[1]').info
    if anu['scrollable'] == "true":
        return True;
    else:
        return False;

def get_code():
    if long_text():
        print("Scrollable")
    else:
        print("Perfect")

first_target()
for x in range(4):
    next_target()
    d(description="GET LOG FILE").click()
    get_code()