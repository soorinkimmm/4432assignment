import urllib2, json, urllib,csv
from urllib import urlencode

output = open('api.csv','w')
writer = csv.writer(output)

response = urllib2.urlopen('http://openstates.org/api/v1/bills/?apikey=1f366e0712bd4ad6b079afe3bb993434&state=mo&search_window=session').read()

bills = json.loads(response)

bill_a = []

for bill in bills:

    encoded_bill_id = urllib.quote(bill['bill_id'])

    encoded_url = 'http://openstates.org/api/v1/bills/mo/2016/'+encoded_bill_id+'/?apikey=1f366e0712bd4ad6b079afe3bb993434'

    encoded_page = urllib2.urlopen(encoded_url).read()
    bill_b = json.loads(encoded_page)
    bill_a.append(bill_b)

    for bill_b in bill_a:

        sponsor_info = bill_b['sponsors']

        for sponsors in sponsor_info:

            sponsor_name = sponsors['name'].encode('utf-8')
            title = bill_b['title'].encode('utf-8')

    writer.writerow([sponsor_name, title])