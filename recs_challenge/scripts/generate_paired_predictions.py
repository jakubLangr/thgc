#!/usr/bin/python

import operator

# Generates a set of predictions for each customer, based on products which we know to be connected to those in their purchase history

customer_purchases = {}
with open('data/customer_products.csv', 'rb') as f:
    for line in f:
        values = line.strip().split(',')
        customer_purchases[values[0]] = values[1:]

product_pairs = {}
with open('data/paired_products.csv', 'rb') as f:
    for line in f:
        values = line.strip().split(',')
        product_pairs[values[0]] = map(lambda s : (s.split(':')[0], float(s.split(':')[1])), values[1:])

with open('data/customer_paired_predictions.csv', 'w+') as f:
    for customer in customer_purchases:
        customer_paired_products = []
        for product in customer_purchases[customer]:
            if product in product_pairs:
                customer_paired_products += product_pairs[product]

        paired_predictions = sorted(customer_paired_products, key = operator.itemgetter(1), reverse = True)[:6]

        f.write(customer)
        for rec_product in paired_predictions:
            f.write(',%s:%s' % (rec_product[0], str(rec_product[1])))
        f.write('\n')
