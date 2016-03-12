library(igraph)

args <- commandArgs(trailingOnly = TRUE) 
people <- as.matrix(read.csv(args[1])) # input file - first command line argument
people.g <- graph.adjacency(people, mode="undirected", weighted=TRUE, diag=FALSE)
la <- layout.fruchterman.reingold(people.g, niter=500, weights=E(people.g)$weight)

png(file=args[2], width=1500, height=1500) # output file - second command line argument
plot(people.g, layout=la, vertex.shape="circle", vertex.size=1, edge.width=(E(people.g)$weight)/2)

dev.off()
