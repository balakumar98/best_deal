from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
# browser = webdriver.Firefox()
# url = 'https://www.bigbasket.com/pd/240125/dabur-honey-india-s-no1-honey-400-g-squeezy-pack/'
# url = "https://www.bigbasket.com/pd/1203960/lays-potato-chips-indias-magic-masala-party-pack-2x167g/"
# url = "https://www.bigbasket.com/pd/100286100/aachi-powder-sambar-100-g-pouch/?nc=as&q=aac"
url = "https://www.bigbasket.com/pd/100006161/colgate-strong-teeth-anticavity-toothpaste-with-amino-shakti-100-g/"
browser.get(url)
# a = browser.find_elements_by_class_name("_2Z6Vt")
print(len(a))
# res = a.split("\n")_1LiCn
# for i in res:
#     d
# browser.save_screenshot('screenie.png')
# print("Headless Firefox Initialized")
browser.quit()
