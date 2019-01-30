#!/usr/bin/env python
"""A more advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter
import sys
import rdflib

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    #data = read_mapper_output(sys.stdin, separator=separator)
    g = rdflib.Graph()
    g.load(sys.stdin)
    q = g.query('SELECT ?a WHERE { ?a hip:hasContinent hip:Asia }',
                initNs = { 'hip' : 'http://wiki.hip.fi/xml/ontology/olapdim_st.owl#'}) 
    
    import pprint
    for stmt in q:
        pprint.pprint(stmt)
    #for row in q:
    #    print (row)
    
if __name__ == "__main__":
    main()
    