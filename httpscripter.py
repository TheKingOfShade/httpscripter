"""
This script was built to generate random, user-defined, non-TLS encrypted traffic for analysis with wireshark. It generates GET requestes either with a single user agent string or with many different user agent strings, based on user input. It outputs the following:
1)A status code for the requested site (200:Ok, 404:Not Found)
2)The User Agent String used to get that site
3)The URL of the GET request
It will send a GET request for the user defined search term on a random search engine every 5 seconds.
Written by www.github.com/TheKingOfShade
"""
import requests
import random
import timeit
import argparse

#Create the argument parser
parser = argparse.ArgumentParser()
parser.add_argument("--UASet",help="Sets a random User Agent String", action="store_true")
args=parser.parse_args()

#Gets the user agent strings from an unfortunately poorly formatted list of user agent strings, scraped from http://useragentstring.com/pages/useragentstring.php?name=All
lineslist = open('UAList').read().splitlines()

#List of search engines that do not default to https
traf = ['http://www.ask.com/web?q=','http://www.bing.com/search?q=','http://www.wikihow.com/wikiHowTo?search=','http://www.alibaba.com/trade/search?SearchText=','http://www.globo.com/busca/?q=']

#Reads the input from the user and makes it useable for web browsers
inp = str(input("What would you like to search for? "))
fixedin = inp.replace(' ','+')

#Fixes the poor formatting of the list
#def cutprefix(str):
#	return str[18:]
#Sets an initial UA string to use in case user wants to use the same one over and over
Grandt = random.randint(0,len(lineslist))
GrUAString = lineslist[Grandt]

#Builds a packet based on UA and one of the Search engines defined in traf[]
def buildapacket(UA,Searcher):
	top = {'user-agent':UA}
	s = requests.get(Searcher,headers=top)
	print(s)
	print(UA)
	print(Searcher)

#Creates packet with random UA String and Random Search engine
def sendapacket():
	randu=random.randint(0,len(traf)-1)
	rSearcher = traf[randu]+fixedin
	if args.UASet==False:
		randt = random.randint(0,len(lineslist))
		rUAString = lineslist[randt]
		buildapacket(rUAString,rSearcher)
	else:
		buildapacket(GrUAString,rSearcher)

#Timer to keep the process automated. Set at 5 Seconds.		
ans=0
strt = timeit.default_timer()
while (ans > -1):
	now = timeit.default_timer()
	ans = now-strt
	if ans >5:
		strt=timeit.default_timer()
		sendapacket()
