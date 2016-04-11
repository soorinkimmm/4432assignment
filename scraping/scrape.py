import urllib2, csv, mechanize
from bs4 import BeautifulSoup

# Get the output file ready
output = open('output.csv', 'w')
writer = csv.writer(output)

br = mechanize.Browser()
br.open('http://enr.sos.mo.gov/EnrNet/CountyResults.aspx')

#first drop down
br.select_form(nr=0)
br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']
br.submit('ctl00$MainContent$btnElectionType')
html = br.response().read()
soup = BeautifulSoup(html, "html.parser")

# Second drop down
# Make a list of all the options
dropdown = soup.find('select', id = 'cboCounty').find_all('option')

counties = []

for i in dropdown:
    county = {'name':i.text, 'num':i['value']}
    counties.append(county)

for county in counties: 
    br.select_form(nr=0)
    br.form['ctl00$MainContent$cboCounty'] = [county['num']]
    br.submit('ctl00$MainContent$btnCountyChange')
    html = br.response().read()
    soup = BeautifulSoup(html, "html.parser")
    
    main_table = soup.find('table', {'id': 'MainContent_dgrdResults'})

    output=[]
    output.append(county['name'])

    for row in main_table.find_all('tr'):
        data = [cell.text for cell in row.find_all('td')]
        if data:
            if data[0] in ['Hillary Clinton', 'Bernie Sanders', 'Ted Cruz', 'John R. Kasich', 'Donald J. Trump']:
                output.append(data[3])
    
    writer.writerow(output)


    # for row in main_table.find_all("tr"):
    #     cells = row.find_all("td")
    #     if len(cells) == 2:
    #         candidate = cells[0].find(text=True)
    #         percentage = cells[3].find(text=True)
    #         print percentage


#candidates[x].split(",")


        #//writer.writerow(data)



#('td', {'align': ['left', 'right']})
     
#for row in main_table.find_all('tr'):
    #data = [cell.text.replace(u'\xa0', '') for cell in row.find_all('td')]
    #writer.writerow(data)


#for value in "option value"
    #br.form = list(br.forms())[0] 
    #control = br.form.find_control("ctl00$MainContent$cboCounty")
    #control.get_value_by_label = ["option value"]
    #br.submit('ctl00$MainContent$btnCountyChange')





