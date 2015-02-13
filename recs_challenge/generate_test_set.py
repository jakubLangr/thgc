import csv
#import pandas as pd

def check_presence(file1, file2):
	header = ['CustomerID','ProductID','Timestamp','ProductType','ProductCategory','ProductBrand','PriceBand']
	file1_data = csv.DictReader(open(file1),header)
	file2_data = csv.DictReader(open(file2),header)

	counter = 0

	customer_ids = list(file2_data.CustomerID)

	for row in file1_data:
		if row['Customer ID'] in customer_ids:
			counter += 1 
			if counter==20:
				break


check_presence('given/train.csv','given/customers_to_predict.csv')

