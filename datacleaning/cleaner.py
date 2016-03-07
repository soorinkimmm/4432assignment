# Your code goes here
import csv

csvfile = open('./data/cleanme.csv', 'r')
outfile = open('./data/clean.csv', 'w')

reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile, reader.fieldnames)

writer.writeheader()

for row in reader:
	row['first_name'] = row['first_name'].upper()
	row['zip'] = row['zip'].zfill(5)
	row['city'] = row['city'].replace('&nbsp;', '_')
	if int(row['amount']) >= 1000:
		writer.writerow(row)


	

