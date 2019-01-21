# imagenet-ancestors-descendants
Using all IS-A relations of nouns in WordNet from the ImageNet archive, this program takes in a keyword input and writes a file with ancestors and descendants of all matching nouns in WordNet's hierarchy.

words.txt, gloss.txt, and is_a.txt were all acquired from ImageNet's API Documentation page: http://image-net.org/download-API

words.txt maps all WordNet IDs to their corresponding synonym sets.
gloss.txt maps all WordNet IDs to their corresponding glosses, or short descriptions.
is_a.txt lists all parent-child pairs of WordNet IDs.

This program takes in a keyword input and outputs a text file with, for all synonym sets which include the keyword, synonym set, gloss, and a list of descendents and ancestors.
