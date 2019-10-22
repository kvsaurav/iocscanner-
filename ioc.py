#!/usr/bin/env python
# coding: utf-8



#Threat IOC GRAPH CO-RELATION 

# in-python-58k02xsiq
#THIS PROGRAM WILL TAKE HASH AS AN INPUT AND TRY TO FETCH EVERY SINGLE POTHENTIALY USEFUL DATA 


import hashlib
import urllib
import urllib2
import json
import os
import requests
import re
import threatcrowd
import pprint


from virus_total_apis import PublicApi as VirusTotalPublicApi

API_KEY_VT = 'd7959a3bbf007326c2c60d551af452e64d05b9d9b377241ee73ee2d0a08cf3d3'





print ''''
	
  

	
     -------	     *  *	     ******     *
    	|  	    *    *          *           *
	|          *      *         *           *
	|          *      *         *           *
    	|           *    *          *           *
     -------         *  *            ******     *
		
===========================================================

			WElcome to IOC-REL
===========================================================

A thret RElationship Finder Between hash ,Email, ip and domain 



1 = ip 		2 = email  	3 = hash   4 = Domain  	5 = AV_name



'''''

# x = raw_input ("enter your choice ")
x = int(input("Enter a number: "))


if x==1:
	# try ip 

	# def (ip):

	ip = raw_input("Enter Ip adress :")

	print " OTX_REPORT " * 80
	pprint.pprint(threatcrowd.ip_report(ip))

	print "**" * 80
	print "VIRUSTOTAL_REPORT " * 80

	vt = VirusTotalPublicApi(API_KEY_VT)
	response = vt.get_ip_report(ip)

	print(json.dumps(response, sort_keys=False, indent=4))



elif x==2:
	# email_report(address)
	email = raw_input("Enter Email :")
	pprint.pprint(threatcrowd.email_report(email))

	print "/n"
	print "virustotal report"
	print "**" * 80


	vt = VirusTotalPublicApi(API_KEY_VT)
	response = vt.get_file_report(hash)
	print(json.dumps(response, sort_keys=False, indent=4))




elif x==3:
	# def(hash):
	hash = raw_input("Enter the hash : ")
	pprint.pprint(threatcrowd.file_report(hash))

	print "/n"
	print "virustotal report"
	print "**" * 80


	vt = VirusTotalPublicApi(API_KEY_VT)
	response = vt.get_file_report(hash)
	print(json.dumps(response, sort_keys=False, indent=4))

	print "/n","/n"

	vt = VirusTotalPublicApi(API_KEY_VT)
	response = vt.get_network_traffic(hash)
	print(json.dumps(response, sort_keys=False, indent=4))






elif x==4:
	# def(domain):
	domain =raw_input("Enter the domain : ")
	pprint.pprint(threatcrowd.domain_report(domain))

	print "**" * 80
	print "VIRUSTOTAL_REPORT " * 80

	vt = VirusTotalPublicApi(API_KEY_VT)
	response = vt.get_domain_report(domain)

	print(json.dumps(response, sort_keys=False, indent=4))








elif x==5:
	# def (virus_name):
	av = raw_input("Enter the Virus Name : ")
	pprint.pprint(threatcrowd.antivirus_report(av))


else:
    print("Invalid input!")
# import requests, json
# result =  requests.get("https://www.threatcrowd.org/searchApi/v2/email/report/", 
# params = {"email": "HEALTHYBLOODPRESSURE.INFO@domainsbyproxy.com"})
# print result.text


# virustotal public api 
# we are fetching details from virus total public api 


# Hybrid analysis public api 
# fetching same details for virus 