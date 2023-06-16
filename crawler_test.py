import requests 
import json

url = "https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=86D0C4D258FACC7CE8F8DD55D50C62F2&country=ca&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(CA)%26filter%3Dlanguage(en-GB)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(16633190-45e5-4830-a068-232ac7aea82c)%26searchTerms%3Djordan%26anchor%3D48%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en-GB&localizedRangeStr=%7BlowestPrice%7D%E2%80%94%7BhighestPrice%7D"


html = requests.get(url=url)
out = json.loads(html.text)

for item in out['data']['products']['products']:
    print(item)
