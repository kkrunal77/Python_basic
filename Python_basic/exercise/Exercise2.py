import csv
import pprint
with open('exp.csv', 'r' ) as csvfile:
    reader = csv.DictReader(csvfile)
    list= {}
    for row in reader:
        # temp = {
        #     row['id']: row['score1']
        # }
        # list.update(temp)
        list[row['score4']] = row['score1']
        # list.append(row['id'])
    print(list)
    # counties = {line['score5']: line['score2'] for line in reader}
    # print(counties)
