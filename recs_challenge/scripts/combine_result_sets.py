#!/usr/bin/python

import operator

# Combines the two sources of predictions to produce the overall output,
# mainly using paired predictions and filling in gaps with best selling products

customers_to_predict = []
with open('given/customers_to_predict.csv', 'rb') as f:
    for line in f:
        customers_to_predict.append(line.strip())

popular_predictions = {}
with open('data/customer_bestseller_predictions.csv', 'rb') as f:
    for line in f:
        values = line.strip().split(',')
        popular_predictions[values[0]] = values[1:]

customer_purchases = {}
with open('data/customer_products.csv', 'rb') as f:
    for line in f:
        values = line.strip().split(',')
        customer_purchases[values[0]] = values[1:]

paired_predictions = {}
with open('data/customer_paired_predictions.csv', 'rb') as f:
    for line in f:
        values = line.strip().split(',')
        paired_predictions[values[0]] = dict((entry.split(':')[0], float(entry.split(':')[1])) for entry in values[1:])

with open('overall_output.csv', 'w+') as f:
    for line_number, customer in enumerate(customers_to_predict):

        final_predictions = {}

        if customer in paired_predictions:
            for product, score in paired_predictions[customer].items():
                if product not in customer_purchases[customer]:
                    try:
                        final_predictions[product] += score
                    except:
                        final_predictions[product] = score

        # Fill in any gaps with the most popular products
        num_missing = 6 - len(final_predictions)
        if num_missing > 0:
            for popular_product in popular_predictions[customer][:num_missing]:
                # It's possible that popular_product is already in final_predictions at this point - which will result in fewer than 6 predictions
                final_predictions[popular_product] = 0

        results = sorted(final_predictions.items(), key = operator.itemgetter(1), reverse = True)

        f.write(','.join([product for (product, score) in results][:6]))

        if line_number < len(customers_to_predict) - 1:
            f.write('\n')
