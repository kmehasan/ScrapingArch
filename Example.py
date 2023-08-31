from Browser import Browser

browser = Browser.getChromeBrowser()
browser.get('https://www.google.com')
print(browser.title)
