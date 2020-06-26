from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
# browser = webdriver.Firefox()
url = 'https://www.bigbasket.com/pd/240125/dabur-honey-india-s-no1-honey-400-g-squeezy-pack/'
# url = "https://www.bigbasket.com/pd/1203960/lays-potato-chips-indias-magic-masala-party-pack-2x167g/"
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
    t = 0
except:
    a = browser.find_elements_by_class_name("_2yfKw")[0].text
    t = 1
    
res = a.split("\n")[1:]

def clean(i,o):
    if len(i) >= 7:
        return i[i.index(o)-5:i.index(o)]
    else:
        return i


# print(res)
quan = []
cost = []
res2 = []
quan_type = []
for i in res:
    if "out of stock" in i.lower() or "price" in i.lower() :
        # res.remove(i)
        # print("o",i)
        # print("o",i)
        continue
    else:
        # print("e",i)
        res2.append(i)
    # print(i)
    if "%" in i:
        # print(i)
        i = i.replace(i[int(i.index("%")-2):int(i.index("%"))+1],"")
        i = i.replace("Off","")
        # print(i)
    if "g" in i:
        i = clean(i,"g")
        quan_type.append('g')
        quan.append(i.replace("g","").strip())
        # print(i)
    # else:
    #     print(i)
    if "kg" in i:
        i = clean(i,"kg")
        quan_type.append('kg')
        quan.append(i.replace("kg","").strip())
    if "ml" in i:
        i = clean(i,"ml")
        quan_type.append('ml')
        quan.append(i.replace("ml","").strip())
    if "L" in i:
        i = clean(i,"L")
        quan_type.append('L')
        quan.append(i.replace("L","").strip())
    if "MRP: Rs" in i:
        i = i.replace(i[:int(i.index("MRP: "))+5],"")
        # print(i)
        # t = i.split("MRP: Rs ")
        # cost.append(i.replace("Rs ",""))
    if "Price" in i:
        continue
    if "Rs" in i:
        cost.append(i.replace("Rs","").strip())

for i in range(len(quan)):
    if "x" in quan[i]:
        spli = quan[i].split("x")
        quan[i] = float(spli[0])*float(spli[1])
# print(res)

# print(quan)
# print(cost)
ratio = []
for i in range(len(quan)) :
    ratio.append(int(quan[i])/int(cost[i]))

# print(res2)
print(ratio)
print(ratio.index(max(ratio)))
fin_ratio = ratio
chec = max(fin_ratio)
fin_ratio.remove(chec)
# print(ratio)
if t != 0:
    if len(fin_ratio) > 0 and chec == max(fin_ratio) and len(quan) == len(cost) and len(quan) == len(quan_type):
        print("All the following deals are profitable...")
        for i in range(int(len(cost))):
            print(quan[i],quan_type[i]," ",cost[i],"Rs")
    elif len(quan) == len(cost):
        print("Best deal for you is: ",quan[int(ratio.index(max(ratio)))])
        # ,quan_type[int(ratio.index(max(ratio)))]," ",cost[int(ratio.index(max(ratio)))],"Rs")
    else:
        print("Some unexpected error has occurred...")
else:
    if len(fin_ratio) > 0 and chec == max(fin_ratio):
        print("All the following deals are profitable...")
        for i in range(int(len(res2)/3)):
            print(res2[int(i*3)],res2[int(i*3)+1],res2[int(i*3)+2])
    elif len(quan) == len(cost):
        print("Best deal for you is: ",res2[int(ratio.index(max(ratio))*3)],res2[int(ratio.index(max(ratio))*3)+1],res2[int(ratio.index(max(ratio))*3)+2])
    else:
        print("Some unexpected error has occurred...")
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