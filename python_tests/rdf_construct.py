import rdflib

g = rdflib.Graph()
g.load("../countries.rdf")
g.load("../country-continent.rdf")
g.load("../commodity.rdf")

print("data loaded")

q = g.query('CONSTRUCT WHERE {?country aa:Continent ?continent}',
                initNs = { 'aa' : 'http://www.example.org/'})

print()

qs=q.serialize(destination='ser_file.rdf',format='xml')

g2 = rdflib.Graph()
g2.load("ser_file.rdf",format='xml')

q = g2.query('SELECT ?country ?continent WHERE {?country aa:Continent ?continent}',
    initNs = { 'aa' : 'http://www.example.org/'})

for row in q:
    print (row)
