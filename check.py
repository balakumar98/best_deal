from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
# browser = webdriver.Firefox()
url = 'https://www.bigbasket.com/pd/240125/dabur-honey-india-s-no1-honey-400-g-squeezy-pack/'
url = "https://www.bigbasket.com/pd/1203960/lays-potato-chips-indias-magic-masala-party-pack-2x167g/"
url = "https://www.bigbasket.com/pd/100286100/aachi-powder-sambar-100-g-pouch/?nc=as&q=aac"
url = "https://www.bigbasket.com/pd/263921/colgate-strong-teeth-anticavity-toothpaste-with-amino-shakti-200-g/"
url = "https://www.bigbasket.com/pd/267758/dabur-badam-tail-100-pure-almond-oil-100-ml/"
url = "https://www.bigbasket.com/pd/60000655/coca-cola-soft-drink-original-taste-600-ml-bottle/"
url = "https://www.bigbasket.com/pd/287005/sunfeast-yippee-magic-masala-noodles-60-g-pouch/?nc=as&q=yip"
url = "https://www.bigbasket.com/pd/100003902/mysore-sandal-bathing-soap-125-g-carton/"
url = "https://www.bigbasket.com/pd/100968/mysore-sandal-bathing-soap-superior-with-pure-sandalwood-oil-150-g-carton/"
url = "https://www.bigbasket.com/pd/10000450/bb-royal-idli-rice-1-kg-pouch/?nc=as&q=bu"
url = "https://www.bigbasket.com/pd/283426/india-gate-basmati-rice-feast-rozzana-5-kg-pouch/?nc=l3category&t_pg=L3Categories&t_p=l3category&t_s=l3category&t_pos=3&t_ch=desktop"
url = "https://www.bigbasket.com/pd/10000422/bb-royal-sooji-ordinarybombay-rava-500-g-pouch/?nc=as&q=rava"
url = "https://www.bigbasket.com/pd/100647221/fortune-rice-bran-oil-1-l-pouch/?nc=as&q=riceb"
url = "https://www.bigbasket.com/pd/274145/fortune-sunflower-refined-oil-1-l-pouch/"
url = "https://www.bigbasket.com/pd/251047/pepsi-soft-drink-750-ml/"
url = "https://www.bigbasket.com/pd/1200128/pepsi-soft-drink-2x750-ml/"

browser.get(url)
try:
    a = browser.find_elements_by_class_name("irDHq")[0].text
    t = 0
except:
    a = browser.find_elements_by_class_name("_2yfKw")[0].text
    t = 1

res = a.split("\n")[1:]

def clean(i,o):
    if len(i) >= 8 and "x" not in i:
        # print(i[i.index(o)-5:i.index(o)])
        if "," in i:
            return i[i.index(o)-5:i.index(o)].split(",")[-1]
        else:
            return i[i.index(o)-5:i.index(o)]
    else:
        return i


# print(res)
quan = []
cost = []
res2 = []
quan_type = []
percent = 0
for i in res:
    if "out of stock" in i.lower() or "price" in i.lower() :
        # res.remove(i)
        # print("o",i)
        # print("o",i)
        continue
    # else:
    #     # print("e",i)
    #     res2.append(i)
    # print(i)
    if "Pack of" in i:
        i = i.replace("Pack of","x")
        # print(i)
    
    if "Buy 1 Get 1 Free" in i:
        # quan[-1] = quan[-1]*2
        inti = re.findall('\d+', i)
        # print(inti)
        i = i.replace(inti[-3],str(int(inti[-3])*2))
        # print(i)

    if "%" in i or "save" in i.lower():
        # print(i)tQ1Iy@browser.find_elements_by_class_name("_2yfKw")[0].text
        # i = i.replace(i[int(i.index("%")-2):int(i.index("%"))+1],"")
        # i = i.replace("Off","")
        # print(i)
        if "MRP: Rs" in i:
            try :
                i = browser.find_elements_by_class_name("tQ1Iy")[percent].text
            except:
                i = browser.find_elements_by_class_name("_23Nyv")[percent].text
            percent += 1
        # i = i.replace(i[:int(i.index("MRP: "))+5],"")
        # cost.append(i.replace("Rs","").strip())
        # print("sa",i)
        # print(len(browser.find_elements_by_class_name("tQ1Iy")))
    if " kg" in i or re.search("\d+kg", i):
        i = clean(i,"kg")
        quan_type.append('kg')
        quan.append(i.replace("kg","").strip())
    elif " g" in i or re.search("\d+g", i): 
        # print(i)
        i = clean(i,"g")
        quan_type.append('g')
        quan.append(i.replace("g","").strip())
        # print(i)
    if " ml" in i or re.search("\d+ml", i):
        i = clean(i,"ml")
        quan_type.append('ml')
        quan.append(i.replace("ml","").strip())
    if " L" in i or re.search("\d+L", i):
        i = clean(i,"L")
        quan_type.append('L')
        quan.append(i.replace("L","").strip())
    if "MRP: Rs" in i:
        # print("th",i)
        i = i.replace(i[:int(i.index("MRP: "))+5],"")
        # print(i)
        # t = i.split("MRP: Rs ")
        # cost.append(i.replace("Rs ",""))
    if "Price" in i:
        continue
    if "Rs" in i:
        # print(i)
        cost.append(i.replace("Rs","").strip())

# print(quan)
for i in range(len(quan)):
    if "x" in quan[i]:
        # print(quan[i])
        spli = quan[i].split("x")
        # print(spli[1])
        # print(re.findall('\d+.\d+', spli[0]))
        # print(re.findall('\d+.\d+', spli[1]))
        if "." in spli[0] and "." in spli[1]:
            quan[i] = float(re.findall('\d+.\d+', str((spli[0])))[0])*float(re.findall('\d+.\d+', str((spli[1])))[0])
        else:
            quan[i] = float(re.findall('\d+', str((spli[0])))[0])*float(re.findall('\d+', str((spli[1])))[0])

# print(res)

# print(quan)
# print(cost)
ratio = []
for i in range(len(quan)) :
    ratio.append(int(quan[i])/int(cost[i]))

# print(res2)
# print(ratio)
# print(ratio.index(max(ratio)))
fin_ratio = ratio[:]
chec = max(fin_ratio)
fin_ratio.remove(chec)
# print(ratio)
if t != 0:
    if len(fin_ratio) > 0 and chec == max(fin_ratio) and len(quan) == len(cost) and len(quan) == len(quan_type):
        print("All the following deals are profitable...")
        for i in range(int(len(cost))):
            print(quan[i],quan_type[i]," ",cost[i],"Rs")
    elif len(quan) == len(cost):
        print("Best deal for you is: ",quan[int(ratio.index(max(ratio)))],quan_type[int(ratio.index(max(ratio)))],",",cost[int(ratio.index(max(ratio)))],"Rs")
    else:
        print("Some unexpected error has occurred...")
else:
    if len(fin_ratio) > 0 and chec == max(fin_ratio) and len(quan) == len(cost) and len(quan) == len(quan_type):
        print("All the following deals are profitable...")
        for i in range(int(len(cost))):
            print(quan[i],quan_type[i]," ",cost[i],"Rs")
    elif len(quan) == len(cost):
        print("Best deal for you is: ",quan[int(ratio.index(max(ratio)))],quan_type[int(ratio.index(max(ratio)))],",",cost[int(ratio.index(max(ratio)))],"Rs")
    else:
        print("Some unexpected error has occurred...")
browser.quit()