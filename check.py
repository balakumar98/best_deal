from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
# browser = webdriver.Firefox()
# url = 'https://www.bigbasket.com/pd/240125/dabur-honey-india-s-no1-honey-400-g-squeezy-pack/'
url = "https://www.bigbasket.com/pd/1203960/lays-potato-chips-indias-magic-masala-party-pack-2x167g/"
# url = "https://www.bigbasket.com/pd/100286100/aachi-powder-sambar-100-g-pouch/?nc=as&q=aac"
# url = "https://www.bigbasket.com/pd/263921/colgate-strong-teeth-anticavity-toothpaste-with-amino-shakti-200-g/"
# url = "https://www.bigbasket.com/pd/263921/"
# url = "https://www.bigbasket.com/pd/240125/"
# url = "https://www.bigbasket.com/pd/267758/dabur-badam-tail-100-pure-almond-oil-100-ml/"
# url = "https://www.bigbasket.com/pd/60000655/coca-cola-soft-drink-original-taste-600-ml-bottle/"
# url = "https://www.bigbasket.com/pd/287005/sunfeast-yippee-magic-masala-noodles-60-g-pouch/?nc=as&q=yip"
browser.get(url)
try:
    a = browser.find_elements_by_class_name("irDHq")[0].text
except:
    a = browser.find_elements_by_class_name("_2yfKw")[0].text
    
res = a.split("\n")[1:]

# print(res)
quan = []
cost = []
for i in res:
    if "%" in i:
        # print(i)
        i = i.replace(i[int(i.index("%")-2):int(i.index("%"))+1],"")
        i = i.replace("Off","")
        # print(i)
    if "g" in i:
        quan.append(i.replace("g","").strip())
    if "kg" in i:
        quan.append(i.replace("kg","").strip())
    if "ml" in i:
        quan.append(i.replace("ml","").strip())
    if "L" in i:
        quan.append(i.replace("L","").strip())
    if "MRP: Rs" in i:
        i = i.replace(i[:int(i.index("MRP: "))+5],"")
        # print(i)
        # t = i.split("MRP: Rs ")
        # cost.append(i.replace("Rs ",""))
    if "Rs" in i:
        cost.append(i.replace("Rs","").strip())
for i in range(len(quan)):
    if "x" in quan[i]:
        spli = quan[i].split("x")
        quan[i] = float(spli[0])*float(spli[1])

print(quan)
print(cost)
ratio = []
for i in range(len(quan)) :
    ratio.append(int(quan[i])/int(cost[i]))

print(ratio)
    # if i%2 == 0:
    #     quantity = res[i].replace("g","")
    #     quantity = quantity.replace("ml","")
    #     quantity = quantity.replace("L","")
    #     quantity = quantity.replace("kg","")
    #     print(quantity)
    # if 4*i %

# res = a.split("\n")_1LiCn_2Z6Vt irDHq
# for i in res:
#     d
# browser.save_screenshot('screenie.png')
# print("Headless Firefox Initialized")
browser.quit()
