import urllib,re,json

#CHALLENGE 1: Create a read-only instance of the log file
file = open('Log.txt', 'r')


regex=r'/setup.php$'
regexAttack = r'^/xmlrpc.php$'
#CHALLENGE 2: Output the total number of events
lines = file.readlines()
list = []
listByes = []
listRegex = []
listRegexAttack = []
counter = 0
request = ""
for line in lines:
    counter += 1
    data = line.split('\t')
    list.append(data[4])
    listByes.append(data[7])
    if (data[7] == "307"):
        request = data[10]
    if re.search(regex, data[10]):
        listRegex.append(line)
    if re.search(regexAttack, data[10]):
        listRegexAttack.append(line)




print "Number of Lines: %i %s" % (counter, "this thing")
print counter

for ip in list:
    print ip




#CHALLENGE 3: Put all the IPs into a list





#CHALLENGE 4: Output number of unique IPs
lastip = ""
listOfUnique = []

lastip = list[0]
listOfUnique.append(list[0])

print "-" * 70
for ip in list:
    if(ip <> lastip):
        listOfUnique.append(ip)
    lastip = ip

for ip in listOfUnique:
    print ip


#CHALLENGE 5: What was the largest request made? (In Bytes)
print "Max Bytes=", max(listByes)



#Challenge 5B: What was the request?
print "Request %s" % request
print request



#Challenge 6: Using the RegEx below, find all events with a matching request
# regex=r'/setup.php$'
#
#     if re.search(r'.php', data[5]):
#         print '\nMatch Found: Event Requests .php page!'
#     else:
#         print '\nNo Regex Match Found'
for l in listRegex:
    print l


#Challenge 7: Load the events into a dictionary, separating suspicious and non-suspicious events.
for l in listRegexAttack:
    print l


#Challenge 8: Using the dictionary created above, summarize the suspicious events to show IP, Request, Status, and Origin Location

for line in listRegexAttack:
    dataAttack = line.split('\t')
    url = 'http://freegeoip.net/json/%s' % (data[4])
    print url
    try:
        response = json.loads(urllib.urlopen(url).read())
        print '\nLocation Information:'
        print response
        print response["country_name"]
    except:
        continue
    print "Ip Address: %s, Request: %s, Status: %s, Origin Location: %s" % (dataAttack[4],dataAttack[10],dataAttack[6], response["country_code"])
    print "http://maps.google.com/maps?z=12&t=m&q=loc:%s+%s" % (response["longitude"],response["latitude"])


#BONUS!!! Generate a map displaying the Origin Locations of attacks





#BONUS!!! Research the events to learn more about what they are targeting and how they work. What conclusions can you reach from the data you've discovered?



