import subprocess
#cat = subprocess.Popen(["/usr/local/bin/hadoop", "fs", "-cat", "trade/data/countries.rdf"], stdout=subprocess.PIPE)
#for line in cat.stdout:
#    print(line)
    
import rdflib
import os

if os.path.exists("temp.rdf"):
    os.remove("temp.rdf")
#cat = subprocess.Popen(["/usr/local/bin/hadoop", "fs", "-copyToLocal", "trade/data/countries.rdf", "temp.rdf"], stdout=subprocess.PIPE)
cat = subprocess.call(["/usr/local/bin/hadoop", "fs", "-copyToLocal", "trade/data/countries.rdf", "temp.rdf"], stdout=subprocess.DEVNULL)

g = rdflib.Graph()
g.load("temp.rdf")
