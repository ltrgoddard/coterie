#!/usr/bin/env python3

import sys
import csv
import wikipedia
import nltk
from nltk.collocations import *

data, labels, results = [], [], []

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()


# take a list of names in a file (first command line argument)

with open(sys.argv[1], "r") as input:
    
    names = input.readlines()


# find common ngrams or links on the wikipedia page of each entry in the names list

for entry in names:

    try:

        article = wikipedia.page(entry)
        
        if sys.argv[3] == "--ngrams":

            tokens = nltk.word_tokenize(article.content)
            bigram_finder = BigramCollocationFinder.from_words(tokens)
            trigram_finder = TrigramCollocationFinder.from_words(tokens)
            bigram_finder.apply_freq_filter(3)
            trigram_finder.apply_freq_filter(3)
            data.append([entry, bigram_finder.nbest(bigram_measures.pmi, 15), trigram_finder.nbest(trigram_measures.pmi, 15)])  

        elif sys.argv[3] == "--links":

            data.append([entry, article.links])

        else:

            print("Unrecognised flag!")
            quit()

        print(entry, end="")

    except wikipedia.exceptions.PageError:

        print("ERROR: "+ entry[:-1] + " not found on Wikipedia!")


# compare the ngrams/links in each entry to those in every other entry

for entry in data:

    name = str(entry[0])[:-1]
    score = [name]
    phrases = entry[1]

    labels.append(name)

    for entry in data:

        subscore = 0

        for phrase in phrases:

            if phrase in entry[1] and str(entry[0]).find(name) == -1:

                subscore += 1
        
        if subscore < int(sys.argv[4]):
        
            score.append(0)

        else:

            score.append(subscore)

    results.append(score)


# write the results out to a csv (second command line argument) as a labelled
# & weighted adjacency matrix

with open(sys.argv[2], "w") as output:

    writer = csv.writer(output)
    writer.writerow(labels)
    writer.writerows(results)
