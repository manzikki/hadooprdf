#!/usr/bin/env python

"""A more advanced Mapper, using Python iterators and generators."""

import subprocess
import sys
import rdflib
import os
import signal
import random

def main(separator='\t'):
    # input comes from STDIN (standard input)

	g = rdflib.Graph()
    #reading xml format        
    	#g.load(sys.stdin)
    #reading nt format
	lines=sys.stdin.readlines()
	#allLines=''.join(lines)
	#g.parse(data=allLines,format='nt')
	allLines=''
	header="<?xml version='1.0'?> \n <rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#' xmlns:a='http://www.example.org/' xml:base='http://www.example.org/'>\n"
	allLines += header
	allLines +=''.join(lines)
	footer = "</rdf:RDF>\n"
	allLines += footer
	g.parse(data=allLines,format='xml')
    #read the dimensions from hdfs by first coping to a local file
	tempfile="/tmp/temp"+str(random.randint(1,1000000))+".rdf"
	for rdffile in ['/user/hadoop/trade/dimensions/countries.rdf','/user/hadoop/trade/dimensions/country-continent.rdf','/user/hadoop/trade/dimensions/commodity.rdf']:
	#cat = subprocess.call(["/usr/local/bin/hadoop", "fs", "-copyToLocal", rdffile, "/home/hadoop/python_tests/temp.rdf"], stdout=subprocess.DEVNULL)
		cat = subprocess.call(["/usr/bin/hadoop", "fs", "-copyToLocal", rdffile, tempfile])
		g.load(tempfile)
		os.remove(tempfile)

    #q = g.query('CONSTRUCT WHERE {?country aa:Continent ?continent}', #. ?continent aa:Continent "Europe"}',
    #            initNs = { 'aa' : 'http://www.example.org/'})
    
    #countries in Africa
	#q = g.query('CONSTRUCT {?country aa:EXPORT_VAL ?export} WHERE {?country aa:Continent "Africa" . ?country aa:ISO3digit ?iso . ?e_id aa:ORIGIN ?iso . ?e_id aa:EXPORT_VAL ?export }',
        #        initNs = { 'aa' : 'http://www.example.org/'})
	#q = g.query('CONSTRUCT {aa:Africa aa:EXPORT_VAL ?export} WHERE {?country aa:Continent "Africa" . ?country aa:ISO3digit ?iso . ?e_id aa:ORIGIN ?iso . ?e_id aa:EXPORT_VAL ?export }',
	q = g.query('CONSTRUCT {?continent aa:EXPORT_VAL ?export} WHERE {?country aa:Continent ?continent . ?country aa:ISO3digit ?iso . ?e_id aa:ORIGIN ?iso . ?e_id aa:EXPORT_VAL ?export }',
                initNs = { 'aa' : 'http://www.example.org/'})

    #must be a format in which the whole triple is on one line
	qs=q.serialize(destination=None,format='nt').decode()
	#signal.signal(signal.SIGPIPE, signal.SIG_DFL) #helps broken pipes
	print(qs)

if __name__ == "__main__":
	main()



