import rdflib
import bsddb3

#g = rdflib.Graph()
#g.load("../countries.rdf")
#g.load("../country-continent.rdf")
#g.load("../commodity.rdf")

from rdflib import Graph
#graph = Graph(store='Sleepycat', identifier="mygraph")
#graph.open('myRDFLibTest',create=True)
#graph.load("../country-continent.rdf")
#graph.load("../countries.rdf")
#graph.load("../commodity.rdf")
#graph.load("../trade_data.rdf")
#graph.close()
print("data loaded")

graph = Graph(store='Sleepycat', identifier="mygraph")
graph.open('myRDFLibTest',create=False)

#q = graph.query('SELECT ?a ?b ?c WHERE {?a aa:iso3code "ARM" . ?a aa:gdppp ?b . ?a aa:Continent ?c}',
 #               initNs = { 'aa' : 'http://www.example.org/'})
        
#sparql_wrapper.setReturnFormat(XML)
           
#q = graph.query('SELECT ?country ?continent WHERE {?country aa:Continent ?continent}',
#    initNs = { 'aa' : 'http://www.example.org/'})

q = graph.query('CONSTRUCT WHERE {?country aa:Continent ?continent}',
    initNs = { 'aa' : 'http://www.example.org/'})

#for row in q:
#    print (row)

print()

#qs=q.serialize(destination=None,format='xml')
qs=q.serialize(destination='ser_file.rdf',format='xml')
#print(qs)

#graph.close()

g2 = rdflib.Graph()
#g2.parse(data=qs,format='xml')
g2.load("ser_file.rdf",format='xml')

q = g2.query('SELECT ?country ?continent WHERE {?country aa:Continent ?continent}',
    initNs = { 'aa' : 'http://www.example.org/'})
for row in q:
    print (row)


#q = g.query('SELECT ?a WHERE { ?a hip:hasContinent hip:Asia }',
#           initNs = { 'hip' : 'http://wiki.hip.fi/xml/ontology/olapdim_st.owl#'})

#q = g.query('SELECT ?a ?b ?c WHERE {?a ?b ?c}')
#
#q = g.query('SELECT ?a WHERE {?a aa:iso3code "ARM"}',
#           initNs = { 'aa' : 'http://www.example.org/'})

#q = g.query('SELECT ?a ?b WHERE {?a aa:iso3code "ARM" . ?a aa:gdppp ?b}',
#           initNs = { 'aa' : 'http://www.example.org/'})

#q = g.query('SELECT ?a ?b WHERE {?a aa:iso3code "ARM" . ?a aa:gdppp ?b}',
#           initNs = { 'aa' : 'http://www.example.org/'})

#q = g.query('SELECT ?a ?b ?c WHERE {?a aa:iso3code "ARM" . ?a aa:gdppp ?b . ?a aa:Continent ?c}',
#           initNs = { 'aa' : 'http://www.example.org/'})

#for row in q:
#    print (row)

#qs=q.serialize(destination='test.rdf',format='xml')

#qs=q.serialize(destination=None,format='xml')
#print(qs)

#for row in q.serialize(format='xml'):
#    print (row)

#g2=rdflib.Graph()

