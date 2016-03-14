# coterie

Tools for basic social network analysis, intended to be applied to literary coteries but potentially useful for other things. Current components are listed below, with more to follow.

[Example output: poets from *The New Poetry* (1966 edn., ed. by Al Alvarez) and *Children of Albion* (1969, ed. by Michael Horovitz) with at least eight shared links between their Wikipedia articles.](example.png)

## wiki.py

*Requirements*: Python 3 (though easily modifiable to work with 2.x), NLTK and the [Wikipedia](https://github.com/goldsmith/Wikipedia) API wrapper for Python.

*Usage*:

    python wiki.py [input.txt] [output.csv] [--ngrams OR --links] [cut-off number]

This script takes a line-by-line list of Wikipedia article titles (e.g. a list of poets' names), looks up either common bigrams/trigrams or links shared between them, then outputs the resulting data as a labelled and weighted adjacency matrix, suitable for processing in a stats package like R. If the number of links or ngrams for a given pairing is below the cut-off number, it will be recorded as zero&mdash;this helps to avoid cluttered graphs.

## wiki.R

*Requirements*: R and its packages ggplot2 and igraph.

*Usage*:

    Rscript wiki.R [input.csv] [output.png]

Working with the output of the script above, this short R script plots a graph using the Fruchterman-Reingold algorithm and saves it as a PNG image.
