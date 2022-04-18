import uiautomator2 as u2
d = u2.connect()

# Logs Edit
for i in range (1,50):
	d(description="GET LOG FILE").click()
	d(description="EDIT").click()
	d(description="SAVE").click()