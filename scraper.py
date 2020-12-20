from requests_html import HTMLSession

urllist = ['https://www.amazon.com/LG-34WN750-B-Technology-Multi-Tasking-Borderless/dp/B08BCR1SJS/ref=sr_1_11?dchild=1&keywords=lg+ultrawide&qid=1608239463&s=electronics&sr=1-11',
'https://www.amazon.com/ASUS-PA278QV-DisplayPort-Anti-Glare-Adjustable/dp/B088BC5HMM/ref=sr_1_4?crid=37G53EWGNQYI4&dchild=1&keywords=asus+1440p+monitor&qid=1608239541&s=electronics&sprefix=asus+1440p+%2Celectronics%2C182&sr=1-4',
'https://www.amazon.com/dp/B08DP6K1ZT/?coliid=I1SMBGIHW9I4H0&colid=2PN63CU20HWFT&psc=1&ref_=lv_ov_lig_dp_it']

def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)

    product = {
        'title': r.html.xpath('//*[@id="productTitle"]', first= True).text,
        'price': r.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text
    }
    print(product)
    return product

monitorPrices = []
for url in urllist:
    monitorPrices.append(getPrice(url))

print(len(monitorPrices))    