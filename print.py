# Modified from teh online problem 0 set to allow for reading tweets
# from thh file captured for problem 1. This was necessary as Twitter
# is no longer supporting the Ver 1.0 API that was referenced in the
# Problem 0 description.

import urllib
import json

f = open('output.txt')
print f
#response = f.readline()
#print response
count = 0
for line in f:
    pyresponse = json.loads(line)
    if 'lang' in pyresponse.keys():     # Verify this is a standard Tweet
        if pyresponse['lang'] == 'en':  #Filter out the english tweets
            count+=1
            #print pyresponse['text']

print count # Total number of english tweets in set
f.close()
