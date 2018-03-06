"""
read json blob and sum log errors
reference URLs below
http://blog.appliedinformaticsinc.com/how-to-parse-and-convert-json-to-csv-using-python/
http://json.org/example.html
http://pandas.pydata.org/pandas-docs/stable/enhancingperf.html#eval-examples
https://docs.python.org/2/reference/compound_stmts.html
https://stackoverflow.com/questions/16819222/how-to-return-dictionary-keys-as-a-list-in-python
https://linuxconfig.org/how-to-parse-data-from-json-into-python
"""
import json

""" junk ideas below - no need for csv
import csv

jsondata = json.load(open('output_json.js', 'r'))

print jsondata
jsontmp = open('/tmp/jsontmp.csv', 'w')
json2csv = csv.writer(jsontmp)
hostcount = 0
logLevel =
timeStamp =
host =
user =
msg =

for x in jsondata:
    print("%s: %s" % (x, jsondata[host]))
"""

with open('output_json.js', 'r') as f:
    hostdict = json.load(f)

for key in list(hostdict):
    print key

sumtotaldebug = sumtotalerr = sumtotalwarn = sumtotalinfo = 0
sumbobd = sumbobe = sumbobw = sumbobi = 0
sumjoed = sumjoee = sumjoew = sumjoei = 0
sumkarend = sumkarene = sumkarenw = sumkareni = 0
sumsusand = sumsusane = sumsusanw = sumsusani = 0

for hostdetails in hostdict:

    if hostdetails['logLevel'] == "DEBUG":
        sumtotaldebug += 1
    if hostdetails['logLevel'] == "ERR":
        sumtotalerr += 1
    if hostdetails['logLevel'] == "WARN":
        sumtotalwarn += 1
    if hostdetails['logLevel'] == "INFO":
        sumtotalinfo += 1

    if (hostdetails['logLevel'] == "DEBUG") and (hostdetails['user'] == "bob"):
        sumbobd += 1
    if hostdetails['logLevel'] == "ERR" and hostdetails['user'] == "bob":
        sumbobe += 1
    if hostdetails['logLevel'] == "WARN" and hostdetails['user'] == "bob":
        sumbobw += 1
    if hostdetails['logLevel'] == "INFO" and hostdetails['user'] == "bob":
        sumbobi += 1

    if hostdetails['logLevel'] == "DEBUG" and hostdetails['user'] == "joe":
        sumjoed += 1
    if hostdetails['logLevel'] == "ERR" and hostdetails['user'] == "joe":
        sumjoee += 1
    if hostdetails['logLevel'] == "WARN" and hostdetails['user'] == "joe":
        sumjoew += 1
    if hostdetails['logLevel'] == "INFO" and hostdetails['user'] == "joe":
        sumjoei += 1

    if hostdetails['logLevel'] == "DEBUG" and hostdetails['user'] == "karen":
        sumkarend += 1
    if hostdetails['logLevel'] == "ERR" and hostdetails['user'] == "karen":
        sumkarene += 1
    if hostdetails['logLevel'] == "WARN" and hostdetails['user'] == "karen":
        sumkarenw += 1
    if hostdetails['logLevel'] == "INFO" and hostdetails['user'] == "karen":
        sumkareni += 1

    if hostdetails['logLevel'] == "DEBUG" and hostdetails['user'] == "susan":
        sumsusand += 1
    if hostdetails['logLevel'] == "ERR" and hostdetails['user'] == "susan":
        sumsusane += 1
    if hostdetails['logLevel'] == "WARN" and hostdetails['user'] == "susan":
        sumsusanw += 1
    if hostdetails['logLevel'] == "INFO" and hostdetails['user'] == "susan":
        sumsusani += 1


print "\nTotal DEBUG is", sumtotaldebug
print "Total ERR   is", sumtotalerr
print "Total WARN  is", sumtotalwarn
print "Total INFO  is", sumtotalinfo

print "\nBob DEBUG is", sumbobd
print "Bob ERR   is", sumbobe
print "Bob WARN  is", sumbobw
print "Bob INFO  is", sumbobi

print "\nJoe DEBUG is", sumjoed
print "Joe ERR   is", sumjoee
print "Joe WARN  is", sumjoew
print "Joe INFO  is", sumjoei

print "\nKaren DEBUG is", sumkarend
print "Karen ERR   is", sumkarene
print "Karen WARN  is", sumkarenw
print "Karen INFO  is", sumkareni

print "\nSusan DEBUG is", sumsusand
print "Susan ERR   is", sumsusane
print "Susan WARN  is", sumsusanw
print "Susan INFO  is", sumsusani
