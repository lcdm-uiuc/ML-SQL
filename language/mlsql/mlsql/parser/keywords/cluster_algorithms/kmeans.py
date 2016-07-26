"""
Defines the parsing for the kmeans algorithm for intended use in clustering
"""
from pyparsing import oneOf, Literal, Optional, Word
from ..grammer import numbers, openParen, closeParen

def define_kmeans():
    kmeansPhrase = oneOf(["k-means", "kmeans", "K-MEANS", "KMEANS", "KMeans", "K-Means"])

    #Definitions for options of kmeans (number of clusters)
    clusters_phrase = (Literal("clusters") + Literal("=")).suppress()

    clusters = Optional(clusters_phrase + Word(numbers).setResultsName("clusters"), default = 3)

    #Compositions
    kmeans = kmeansPhrase + Optional(openParen + clusters + closeParen)

    return(kmeans)