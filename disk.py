from bs4 import BeautifulSoup
import urllib.request

finalband = []
finaltitle = []
finalprice = []
finalimage = []

# def fixthing(con):
#     co = 0
#     nnew = []
#     new = list(con)
#     for i in new:
#         if co == 1:
#             if i == ';':
#                 co = 0
#             continue
#         if i == "&":
#             co = 1
#             nnew.append(i)
#         else:
#             nnew.append(i)
#     simple = ''.join(nnew)
#     return simple


for l in range(1): #51
    with urllib.request.urlopen('https://www.newburycomics.com/collections/exclusive-vinyl?page=' + str(l) + '&view=data') as response:
        html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    soup2 = soup.prettify()
    images = soup.select('div img')

    band = []
    title = []
    lvl1 = 0
    lvl2 = 0
    lvl3 = 0
    lvl4 = 0
    c1 = 0
    c2 = 0
    c3 = 0
    preo = 0

    # print(soup2.split())

    for i in soup2.split():
        if i == "tag_property_pre-order":
            preo = 1
            c2 += 1
        if lvl1 == 1:
            if i == "<span>":
                lvl2 += 1
                lvl1 = 0
                continue
        if lvl2 == 1:
            if i == "</span>":
                bandsent = ' '.join(band)
                print('-----------------------')
                print("Band: " + str(bandsent))
                finalband.append(bandsent)
                band.clear()
                lvl2 = 0
                lvl3 += 1
                continue
            else:
                band.append(i)
                continue
        if lvl3 == 1:
            if c1 == 1:
                if "</a>" == i:
                    titlesent = ' '.join(title)
                    print("Title: " + str(titlesent))
                    finaltitle.append(titlesent)
                    title.clear()
                    c1 = 0
                    lvl3 = 0
                    lvl4 += 1
                    continue
                else:
                    if "<" in i:
                        continue
                    else:
                        title.append(i)
                        continue
            else:
                c1 += 1
                continue
        if lvl4 == 1:
            c1 += 1
            if c1 == 2:
                if i == '<strong>':
                    print('This is a SALE')
                    c1 = -2
                    continue
                print("Price: " + str(i))
                finalprice.append(i[1:])
                images_url = images[c2]['src']
                if "DFDstarburst" in images_url:
                    c2 += 1
                    images_url = images[c2]['src']
                print("Image: " + str(images_url))
                finalimage.append(images_url)
                c2 += 1
                c1 = 0
                lvl4 = 0
                continue
        if i == "<br/>":
            if preo:
                if c3:
                    preo = 0
                    c3 = 0
                    continue
                else:
                    c3 = 1
            else:
                lvl1 += 1

# print(len(finalimage))
# print(len(finalband))
# print(len(finalprice))
# print(len(finaltitle))