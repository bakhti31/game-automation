# coding: utf-8
#
import uiautomator2 as u2

d = u2.connect("NZV8TKIBMV5LOBPF")
while True:
    d.xpath('//*[contains(@content-desc,"LEVEL UP")]').click_exists(timeout=2.0)
    d.xpath('//*[contains(@content-desc,"PACK #17")]').click_exists(timeout=2.0)
    d.xpath('//*[contains(@content-desc,"INSTALL NOW")]').click_exists(timeout=2.0)
    