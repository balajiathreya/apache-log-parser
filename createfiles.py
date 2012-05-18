import sys
import os
import random

"""
2011/06/29 17:18:40 +0000 | HTTP/1.1 | 100 | 55
2011/06/29 17:18:40 +0000 | HTTP/1.1 | 200 | 55
2011/06/30 00:00:00 +0000 log file rolled over
2011/06/30 17:19:22 +0000 | HTTP/1.0 | 200 | 45
2011/06/30 19:07:09 +0000 | HTTP/1.0 | 300 | 75
"""

format= sys.argv[1]
print format;
print sys.argv[2]
format_file = open(sys.argv[2], "a")

if(format == "1"):
    for i in range(100000):
        text = "2011/06/"+str(random.randrange(1,10)).zfill(2)+" "+str(random.randrange(1,24)).zfill(2)+":"+str(random.randrange(1,59)).zfill(2)+":"+str(random.randrange(1,59)).zfill(2);
        text = text + " +0000 | HTTP/1.1 | "+str(random.randrange(1,250000))+" | "+str(random.randrange(1,60))+"\n"
        #print text
        format_file.write(text);
elif(format == "2"):
    for i in range(100000):
        text = "06"+str(random.randrange(1,10)).zfill(2)+"2011Z"+str(random.randrange(1,24)).zfill(2)+":"+str(random.randrange(1,59)).zfill(2)+":"+str(random.randrange(1,59)).zfill(2);
        text = text + "Z0000 - 192.168.0.1 - Mozilla/5.0 (Windows; Windows NT 5.1) Chrome - "+str(random.randrange(1,250000))+" - "+str(random.randrange(1,60))+" - message\n"
        #print text
        format_file.write(text);

format_file.close();
