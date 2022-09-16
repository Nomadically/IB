#from bs4 import BeautifulSoup

from bs4 import BeautifulSoup
import urllib
import requests
import soupsieve as sv
import codecs
import csv
import io
import re
import numpy as np

# html_doc = urllib.request.urlopen('https://www.prisonpro.com/content/eastern-correctional-institution-annex').read()
html_doc = urllib.request.urlopen('https://www.bop.gov/locations/list.jsp').read()


soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())

#head_tag = soup.head
#print(head_tag.contents)

#title_tag = head_tag.contents[0]
#print(title_tag)

#for child in head_tag.descendants:
    #print(child)
holding = []
#f = codecs.open('temptext.txt', encoding='utf-8',mode='w+')
for string in soup.strings:
    holding.append(string)
    #print(repr(string))
    #f.write(string+'\n')
    #'\n'
#f.close()


print(holding)
print(len(holding))
index = holding.index('Inmate Mailing Address:')
print(index)

print(holding[57]) #this is index above of reference point in each website
print(holding[58])
print(holding[59]) #this is the facility name
print(holding[60]) #this is street address
print(holding[61]) #this is city state and zip

print("ok nearly")

"""
header = ['id', 'name', 'address', 'zip']
rows = [
    [1, 'Hannah', '4891 Blackwell Street, Anchorage, Alaska', 99503 ],
    [2, 'Walton', '4223 Half and Half Drive, Lemoore, California', 97401 ],
    [3, 'Sam', '3952 Little Street, Akron, Ohio', 93704],
    [4, 'Chris', '3192 Flinderation Road, Arlington Heights, Illinois', 62677],
    [5, 'Doug', '3236 Walkers Ridge Way, Burr Ridge', 61257],
]



with open('customers.csv', 'wt') as f:
    csv_writer = csv.writer(f)

    csv_writer.writerow(header) # write header

    for row in rows:
        csv_writer.writerow(row)
"""
"""
names = []
addresses = []
zip = []

f = open('customers.csv', 'rt')
csv_reader = csv.DictReader(f, escapechar='\\')
#q = input("what name?")

for row in csv_reader:
    #print(row['name'])
    names.append(row['name'])
    addresses.append(row['address'])
    zip.append(row['zip'])
    f.close


#the below checks created list of elements inside csv to see if input matches
q2 = input("what anything to find?")
try:
    locate = names.index(q2)
    print("found!")
    print(locate)
    print(names[locate])
    print(addresses[locate])
    print(zip[locate])
except ValueError:
    print("not found")


tester = holding[59]
print(tester)

print(holding[61])

#below is so that zip code can be extracted from city state zip entry
address = holding[61]
resulting = re.match('^.*(?P<zipcode>\d{5}).*$', address).groupdict()['zipcode']
print(resulting) #now we have zip code extracted from address

#below is in case string from fac name needs to be stripped of non-ACSII
encoded_string = tester.encode("ascii", "ignore")
decoded_string = encoded_string.decode()

#np.savetxt("customers2.csv", statePrisons, delimiter =", ", fmt ='% s')

#below WORKS to write into csv file first time
"""
"""
with open('customers2.csv', 'w+') as csvfile:
    fieldnames = ['name', 'address', 'zip']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'name': decoded_string, 'address': holding[60], 'zip' : resulting })
    writer.writerow({'name': 'Lovely', 'address': '105 state st',  'zip' : resulting })
    writer.writerow({'name': 'Wonderful', 'address': '102 west st', 'zip' : resulting})
"""
"""

#THE BELOW APPENDS TO CSV WOOOOOOT
"""
"""
file = open('customers2.csv', 'a')
fieldnames = ['name', 'address', 'zip']
writer = csv.DictWriter(file, fieldnames=fieldnames)
writer.writeheader()
writer.writerow({'name': decoded_string, 'address': holding[60], 'zip': resulting})
"""






"""""
            if row['name'] == 'Sam':
                print('ok cool')

with open('prisonlist.csv', 'w', ) as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for word in myStreet:
        wr.writerow([word])
"""""
"""
#for string in soup.stripped_strings:
    #print(repr(string))


#print("ok1.5")


#print("ok ---------------")

#link = soup.h2
#for parent in link.parents:
    #print(parent.name)

#print(soup('h2'))
#print (soup.find_all('strong'))

#print("ok >>")

#print(soup.find('h2', text='Inmate Mailing Address:').text)
#print(soup.find('h2', text='Inmate Mailing Address:').parents)


#testing = []

#for EachPart in soup.select('div[class*="field__item"]'):
    #testing.append(EachPart)
    #print (EachPart.get_text())
    
#print(soup.select("[class~=sister]"))

print("ok <----->")
"""#print(testing)

#print(len(testing))
#print(testing[4])

#parent = soup.find(class_="field__item")
  
# assign n
#n = 2
  
# print the 2nd <b> of parent
#print(parent.select("h2:nth-of-type("+str(n)+")"))
#print(parent.select("div.text-formatted:nth-child(2)"))

  
# print the <b> which is the 2nd child of the parent
#print(parent.select("h2:nth-child("+str(n)+")"))


#print (soup.find('strong', text='Eastern Correctional Institution West and East Compounds').parent)
"""

"""










"""
div.text-formatted:nth-child(2)

html.js body.fontyourface.layout-one-sidebar.layout-sidebar-second.path-node.page-node-type-facility-page.mm-wrapper div#mm-0.mm-page.mm-slideout div.dialog-off-canvas-main-canvas div#page-wrapper div#page div#main-wrapper.layout-main-wrapper.layout-container.clearfix div#main.layout-main.clearfix main#content.column.main-content section.section div.region.region-content div#block-bartik-content.block.block-system.block-system-main-block div.content article.node.node--type-facility-page.node--promoted.node--view-mode-full.clearfix div.node__content.clearfix div.clearfix.text-formatted.field.field--name-body.field--type-text-with-summary.field--label-visually_hidden div.field__item h2
div.field__item:nth-child(2) > h2:nth-child(15)
div.field__item:nth-child(2) > h2:nth-child(15)

<div class="field__item"><h1>&nbsp;</h1><h1><img alt="Eastern Correctional Institution and Annex Maryland" src="https://www.prisonpro.com/images/eastern-correctional-institution.jpg" style="height:163px; width:250px"></h1><h1>Eastern Correctional Institution and Annex</h1><p>Eastern Correctional Institution and Annex is comprised of two facilities, the institution and the annex. &nbsp;Located in Westover Maryland, this prison can incarcerate over 3,500 adult males ranging in custody level from medium to pre-release security levels. &nbsp;Employing over 850 workers, this prison has a yearly budget of over $103 million dollars. &nbsp;This prison participates in the Maryland Correctional Enterprises allowing inmates to work in furniture restoration and in textiles making towels and washing clothing and uniforms. &nbsp;In addition, inmates can work on community projects restoring cemeteries and playgrounds.</p><p>While incarcerated inmates are encouraged to further their education through adult literacy and even earn a GED. &nbsp;Vocational training in masonry, automotive repair, architecture, graphic arts, carpentry and office technologies offer inmates a unique opportunity to learn a skill they can later use for employment. &nbsp;Offenders at Eastern Correctional Institution can also receive substance abuse treatment and counseling services.<a id="visitinghours" name="visitinghours"></a></p><p></p><div><div class="adsense responsive"><script async="" src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script><ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-3874558055196722" data-ad-slot="3854553602" data-ad-format="auto" data-full-width-responsive="true"><iframe id="aswift_2" style="height: 1px !important; max-height: 1px !important; max-width: 1px !important; width: 1px !important;"><iframe id="google_ads_frame1"></iframe></iframe></ins><script>
<!--//--><![CDATA[// ><!--
(adsbygoogle = window.adsbygoogle || []).push({});
//--><!]]>
</script></div></div><h2>Visiting Hours at Eastern Correctional Institution &amp; Annex:</h2><p><strong>Eastern Correctional Institution West and East Compounds</strong> have visitation on Fridays, Saturdays, and Sundays from 8:30am-2:30pm, you must arrive before 1:30pm or you will not be admitted to visitation.<br><strong>Eastern Correctional Institution Annex</strong> has visiting hours on Fridays from 5pm-9pm (must arrive and register by 8pm), and on Saturdays and Sundays from 9am-5pm&nbsp;(You must arrive and register by 4pm).<br><strong>Protective Custody Inmates</strong> have visitation on Fridays, Saturdays and Sundays from 7pm-9pm. &nbsp;You must arrive and be processed by 8pm or you will not be allowed to visit.</p><p>All visits are two hours in duration. &nbsp;Inmates can have a maximum of two visits per week, with up to five visitors, only three of the visitors can be adults. &nbsp;Disciplinary Segregation inmates are only allowed one single hour visit per week.</p><h2>Physical Address:</h2><p>Eastern Correctional Institution<br>30420 Revells Neck Road<br>Westover, Maryland 21890<br><br>Eastern Correctional Institution Annex<br>30430 Revells Neck Road<br>Westover, Maryland 21890</p><h2>Telephone:</h2><p>(410)-845-4000<br>(877)-802-6074</p><h2>Inmate Mailing Address:</h2><p>Inmate Name, ID Number<br><strong>​Eastern Correctional Institution</strong><br>30420 Revells Neck Road<br>Westover, Maryland 21890<br><br>Inmate Name, ID Number<br><strong>Eastern Correctional Institution Annex</strong><br>30430 Revells Neck Road<br>​Westover, Maryland 21890</p></div>
"""

#below is previous

#html_doc = 
"""<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

"""
soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())

print(soup.title)
print(soup.title.string)



for link in soup.find_all('a'):
    print(link.get('href'))
    
print(soup.get_text())


/////////
def ddg(query):
    #url = 'https://duckduckgo.com/html/'
    url = 'https://www.prisonpro.com/search/node?keys='
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0'}

    soup = BeautifulSoup(requests.get(url, params={'q':query}, headers=headers).content, 'html.parser')

    while True:
        for a in soup.select('.result__a'):
            yield a['href']

        f = soup.select_one('input[value="Next"]')
        if not f:
            break

        params = {i['name']: i.get('value', '') for i in f.find_parent('form').select('input[name]')}
        soup = BeautifulSoup(requests.post(url, params=params, headers=headers).content, 'html.parser')


for result in ddg('eastern'):
    print(result)







"""





