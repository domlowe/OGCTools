#!/usr/bin/python
"
__author__ = "d.lowe@bom.gov.au"
__version__ = "0.1"
"

import sys
import urllib2
from bs4 import BeautifulSoup

print "\n".join(sys.argv)

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print "Usage: %s http://path.to.html outputText.txt" % (sys.argv[0])
        exit(0)

    #set up input and output files according to command line arguments
    inputHTML=sys.argv[1]
    outputTextFile=sys.argv[2]
    #download html file
    response = urllib2.urlopen(sys.argv[1])
    #open text file for writing out to
    outputf=open(outputTextFile,'wb')

    #parse the html and write requirements to text file
    print 'Downloading and parsing HTML... please wait'
    soup = BeautifulSoup(response.read(), 'html.parser')
    reqClasses=soup.find_all('table', class_='requirements_class')

    for reqClass in reqClasses:
        unicode=reqClass.text
        s=unicode.encode('utf-8').strip()
        outputf.write(s)

    #close text file
    outputf.close()
    print 'Written to output file... %s'%outputTextFile
