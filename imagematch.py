import uiautomator2 as u2
d = u2.connect()	


imdata = "target.png" # 也可以是URL, PIL.Image或OpenCV打开的图像

d.image.match(imdata) 
# 匹配待查找的图片，立刻返回一个结果
# 返回一个dict, eg: {"similarity": 0.9, "point": [200, 300]}

d.image.click(imdata, timeout=20.0)
# 在20s的时间内调用match轮询查找图片，当similarity>0.9时，执行点击操作