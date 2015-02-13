import csv
import pandas as pd

def check_presence(file1, file2):
	header = ['CustomerID','ProductID','Timestamp','ProductType','ProductCategory','ProductBrand','PriceBand']
	file1_data = csv.DictReader(open(file1),header)
	#file2_data = csv.DictReader(open(file2),header)
	#file1_data = pd.read_csv(file1, names=header)
	file2_data = pd.read_csv(file2, names=header)

	counter = 0

	customer_ids = set(file2_data.CustomerID)
	# print list(customer_ids)[:20]
	customers = []


	for row in file1_data:
		cust_id = int(row['CustomerID'])
		#print cust_id in customer_ids
		if cust_id in customer_ids:
			customers.append(row)

	cust_df = pd.DataFrame(customers)
	cust_df.to_csv('final.csv')

check_presence('given/train0.csv','given/train1.csv')

