library(igraph)

args <- commandArgs(trailingOnly = TRUE) 
people <- as.matrix(read.csv(args[1])) # input file - first command line argument
people.g <- graph.adjacency(people, mode="undirected", weighted=TRUE, diag=FALSE)
people.g <- delete.edges(people.g, which(E(people.g)$weight <=as.integer(args[3])))
people.g <- delete.vertices(people.g,which(degree(people.g)<1))
la <- layout.fruchterman.reingold(people.g, niter=500, weights=E(people.g)$weight)

png(file=args[2], width=1000, height=1000) # output file - second command line argument
plot(people.g, layout=la, vertex.shape="circle", vertex.size=0, edge.width=1)

dev.off()
