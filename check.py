from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
# browser = webdriver.Firefox(options=options)
browser = webdriver.Firefox()
# url = 'https://www.bigbasket.com/pd/240125/dabur-honey-india-s-no1-honey-400-g-squeezy-pack/'
# url = "https://www.bigbasket.com/pd/1203960/lays-potato-chips-indias-magic-masala-party-pack-2x167g/"
# url = "https://www.bigbasket.com/pd/100286100/aachi-powder-sambar-100-g-pouch/?nc=as&q=aac"
# url = "https://www.bigbasket.com/pd/263921/colgate-strong-teeth-anticavity-toothpaste-with-amino-shakti-200-g/"
# url = "https://www.bigbasket.com/pd/263921/"
# url = "https://www.bigbasket.com/pd/240125/"
# url = "https://www.bigbasket.com/pd/267758/dabur-badam-tail-100-pure-almond-oil-100-ml/"
url = "https://www.bigbasket.com/pd/60000655/coca-cola-soft-drink-original-taste-600-ml-bottle/"
browser.get(url)
a = browser.find_elements_by_class_name("irDHq")
if not a:
    a = browser.find_elements_by_class_name("_2yfKw")
print(a[0].text)
# res = a.split("\n")_1LiCn_2Z6Vt irDHq
# for i in res:
#     d
# browser.save_screenshot('screenie.png')
# print("Headless Firefox Initialized")
browser.quit()
