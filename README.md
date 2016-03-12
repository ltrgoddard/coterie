# coterie

Tools for basic social network analysis, intended to be applied to literary coteries but potentially useful for other things. Current components are listed below, with more to follow.

## wiki.py

*Requirements*: Python 3 (though easily modifiable to work with 2.x), [Wikipedia](https://github.com/goldsmith/Wikipedia) API wrapper for Python.

*Usage*:

    python wiki.py [input.txt] [output.csv]

This script takes a line-by-line list of Wikipedia article titles (e.g. a list of poets' names), looks up links shared between them, then outputs the resulting data as a labelled and weighted adjacency matrix, suitable for processing in a stats package like R.

## wiki.R

*Requirements*: R and its packages ggplot2 and igraph.

*Usage*:

    Rscript wiki.R [input.csv] [output.png]

Working with the output of the script above, this short R script plots a graph using the Fruchterman-Reingold algorithm and saves it as a PNG image.
