#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys
import rdflib

def main(separator='\t'):
    # input comes from STDIN (standard input)
    g = rdflib.Graph()
    g.load(sys.stdin)
    q = g.query('SELECT ?a WHERE { ?a hip:hasContinent hip:Asia }',
            initNs = { 'hip' : 'http://wiki.hip.fi/xml/ontology/olapdim_st.owl#'}) 
    for row in q:
        print (row)

if __name__ == "__main__":
    main()



