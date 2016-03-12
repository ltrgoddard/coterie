#!/usr/bin/env python

import sys
import csv
import wikipedia

data, labels, results = [], [], []


# take a list of names in a file (first command line argument)

with open(sys.argv[1], "r") as input:
    
    names = input.readlines()


# find links on the wikipedia page of each entry in the names list

for entry in names:

    try:

        article = wikipedia.page(entry)
        data.append([entry, article.links])
        print(entry, end="")

    except:

        print("Bad name!")


# compare the links in each entry to those in every other entry

for entry in data:

    name = str(entry[0])[:-1]
    score = [name]
    links = entry[1]

    labels.append(name)

    for entry in data:

        subscore = 0

        for link in links:

            if link in entry[1] and str(entry[0]).find(name) == -1:

                subscore += 1
                    
        score.append(subscore)

    results.append(score)


# write the results out to a csv (second command line argument) as
# a labelled & weighted adjacency matrix

with open(sys.argv[2], "w") as output:

    writer = csv.writer(output)
    writer.writerow(labels)
    writer.writerows(results)
