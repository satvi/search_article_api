# Python code to illustrate parsing of XML files
# importing the required modules
import csv
import pickle
import requests
import lxml.html
import xml.etree.ElementTree as ET



def parseXML():
    print('Parse RSS feed')
    # url of rss feed
    url = 'https://www.financialreporter.co.uk/rss.asp?v=1'
    # creating HTTP response object from given url
    resp = requests.get(url)
    # saving the xml file
    with open('financialreporter.xml', 'wb') as f:
        f.write(resp.content)
    xmlfile='financialreporter.xml'
    # create element tree object
    tree = ET.parse(xmlfile)
    # get root element
    root = tree.getroot()

    # create empty list for news items
    allitems = []
    # iterate news items
    for item in root.findall('./channel/item'):

        info = {}

        # getting elements of item
        info['title']=item.find('./title').text
        info["publish_date"]=item.find('./pubDate').text
        info["Article_URL"]=item.find('./link').text
        allitems.append(info)
    details = {}
    print('started scraping the Article website')
    for i in allitems:
        url=i["Article_URL"]
        res = requests.get(url)
        doc = lxml.html.fromstring(res.content)
        title=doc.xpath('//*[@id="afterHeader"]/div/div/h1/text()')
        details[title[0]]=''.join(doc.xpath('//*[@class="js-sidebar-parent"]/div/div/div/article/p/text()'))
    with open('data2.pkl', 'wb') as f:
        pickle.dump(details, f)
    print('scrapping finished')
    return details


def get_data(searchQuery):
    keyword=searchQuery['search_title']
    with open('data2.pkl', 'rb') as f:
        data = pickle.load(f)
    output=[value for key, value in data.items() if keyword in key.lower()]
    if output:
        return output
    else:
        return []








































