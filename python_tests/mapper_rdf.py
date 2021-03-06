#!/usr/bin/env python3

"""A more advanced Mapper, using Python iterators and generators."""
import subprocess
import sys
import rdflib
import os
import signal

def main(separator='\t'):
    # input comes from STDIN (standard input)

    g = rdflib.Graph()
    #read the dimensions from hdfs by first coping to a local file
    for rdffile in ['trade/dimensions/countries.rdf','trade/dimensions/country-continent.rdf','trade/dimensions/commodity.rdf']:
        if os.path.exists("temp.rdf"):
            os.remove("temp.rdf")
        cat = subprocess.call(["/usr/local/bin/hadoop", "fs", "-copyToLocal", rdffile, "temp.rdf"], stdout=subprocess.DEVNULL)
        g.load("temp.rdf")
            
    g.load(sys.stdin)
    #q = g.query('CONSTRUCT WHERE {?country aa:Continent ?continent}', #. ?continent aa:Continent "Europe"}',
    #            initNs = { 'aa' : 'http://www.example.org/'})
    
    #countries in Africa
    #q = g.query('CONSTRUCT {?cn aa:Continent "Africa"} WHERE {?country aa:Continent "Africa" . ?country aa:CountryName ?cn}', initNs = { 'aa' : 'http://www.example.org/'})
    q = g.query('CONSTRUCT {?country aa:EXPORT_VAL ?export} WHERE {?country aa:Continent "Africa" . ?country aa:ISO3digit ?iso . ?e_id aa:ORIGIN ?iso . ?e_id aa:EXPORT_VAL ?export }',
                initNs = { 'aa' : 'http://www.example.org/'})

    #must be a format in which the whole triple is on one line
    qs=q.serialize(destination=None,format='nt').decode()
    #signal.signal(signal.SIGPIPE, signal.SIG_DFL) #helps broken pipes
    print(qs)
  
    
if __name__ == "__main__":
    main()



