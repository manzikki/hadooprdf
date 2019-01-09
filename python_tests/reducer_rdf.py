#!/usr/bin/env python3

"""A more advanced Reducer, using Python iterators and generators."""

import sys
import rdflib

def main(separator='\t'):
    # input comes from STDIN (standard input)
    
    g = rdflib.Graph()
    
    #this works
    lines=sys.stdin.readlines()
    allLines=''.join(lines)
    g.parse(data=allLines,format='nt')
    
   #this does not work 
   # g.load(sys.stdin,format='nt')
   
    q = g.query('CONSTRUCT {?country aa:EXPORT_VAL ?export} WHERE {?country aa:EXPORT_VAL ?export}',
                initNs = { 'aa' : 'http://www.example.org/'})
    # ca marche
    #q = g.query('SELECT ?a ?b WHERE {?a aa:EXPORT_VAL ?b}',
    #            initNs = { 'aa' : 'http://www.example.org/'})
    
    #q = g.query('SELECT ?iso SUM(?export) WHERE {?iso aa:EXPORT_VAL ?export .}', initNs = { 'aa' : 'http://www.example.org/'})
    
    
    qs=q.serialize(destination=None,format='nt').decode()
    #qs=q.serialize(destination=None,format='xml').decode()
    print(qs)
  
    
    
    # to read results: hadoop fs -cat trade-output/*  
    
if __name__ == "__main__":
    main()
    