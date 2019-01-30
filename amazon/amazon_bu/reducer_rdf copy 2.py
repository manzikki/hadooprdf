#!/usr/bin/env python3

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
    data = read_mapper_output(sys.stdin, separator=separator)
    print(data)
    
   
    #g = rdflib.Graph()
    #g.load(sys.stdin,format='xml')
    ##g.load("test_serial.rdf")
    
    #q = g.query('CONSTRUCT WHERE {?country aa:Continent ?continent}',
     #           initNs = { 'aa' : 'http://www.example.org/'})
    
    #qs=q.serialize(destination=None,format='xml')
    #print(qs.decode())
    
    
if __name__ == "__main__":
    main()
    