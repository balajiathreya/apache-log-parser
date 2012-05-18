import sys
import os
import re
import time

### Globals
#regex pattern for file format 1.
pattern1_list = [r'(?P<date>[0-9/:+\s]+)', r'(?P<request>\S+)', r'(?P<userid>[0-9]+)',r'(?P<pageid>[0-9]+)'];
pattern1 = re.compile(r'\s*\|*\s*'.join(pattern1_list)+r'\s*\Z')
date_pattern1 = "%Y%m%d";
# regex pattern for file format 2
pattern2_list = [r'(?P<date>(.[^-])*)', r'[-]', r'(?P<ip>\S+)', r'[-]', r'(?P<useragent>(.[^-])*)', r'[-]' , r'(?P<userid>[0-9]+)', r'[-]',r'(?P<pageid>[0-9]+)', r'[-]', r'(?P<message>.*)'];
pattern2 = re.compile(r'\s*'.join(pattern2_list)+r'\s*\Z')
date_pattern2 = "%d%m%Y";

#read command line inputs and pass the file_names to process_file()
def read_input(argv):
    for arg in argv:
        if(os.path.isfile(arg)):
            process_file(arg)
        else:
            print arg+" is not a file or does not exist. Ignoring it."


"""
finds the format of the input file and calls process_file_with_pattern()
passing the appropriate regex pattern object
"""
def process_file(file_name):
    print "Processing file - "+file_name
    f = open(file_name, 'r')
    line = f.readline();
    m = pattern1.match(line)
    f.close()
    if(m == None):
        process_file_with_pattern(file_name,pattern2,date_pattern2)
    else:
        process_file_with_pattern(file_name,pattern1,date_pattern1)
    
"""
parses the input file and creates a dictionary in memory
holding the user_id, date of visit and page id. After parsing the file,
it passes the processed dictionary to check_for_users() that checks for the 
requirement. The date_dictionary doesnot hold more than 2 page ids even though
the user might have visited more than 2 pages on a specific day. Since, the
requirement is to just print out the user_ids that meeet the criterion, additional
page visits are not recorded - this saves both memory and time

The following is the format of the dictionary in memory:
{
  "19905": {
    "06072011": ["38"]
  },
  "158223": {
    "06072011": ["49","22"],
    "06012011": ["11","54"]
  },
  "177594": {
    "06052011": ["30"]
  }
}
"""
def process_file_with_pattern(file_name,pattern,date_pattern):
    data = {}
    f = open(file_name, 'r')
    for line in f:
        m = pattern.match(line)
        if(m != None):
            res = m.groupdict();
            # remove "/" from the date string and take only in the first 8
            # digits which gives the date in this format - 06052011
            date =res["date"].replace("/","")[0:8]
            # make sure the date is valid.
            try:
                valid_date = time.strptime(date, date_pattern)
            except ValueError:
                print('Invalid date! Ignoring entry '+line.rstrip())
                continue;

            user_object = {}
            # check if user id exists as a key in the dictionary. get
            # the value. user_object example:
        
            # "158223": {
            #            "06072011": ["49","22"],
            #            "06012011": ["11","54"]
            # },
            user_object = data.get(res["userid"])
            # user_id doesn't exist. create the member and add it to
            # the dictionary
            if(user_object == None):
                page_array = [res["pageid"]]
                date_object = {date:page_array}
                data[res["userid"]]=date_object
            # user_id already exists. Now, check if atleast one visit 
            # is made on this date - res["date"]. if not,create a 
            # dictionary with date as key and [pageid] as value. if, one
            # visit already exists, add the page id to the existing array
            # if two visits already exists, skip - dont' do anything as the
            # program has to output only the user_ids and not specific page ids
            else:
                date_object = user_object.get(date)
                if(date_object == None):
                    page_array = [res["pageid"]]
                    user_object[date]=page_array
                elif(len(date_object) < 2):
                    # check if the pageid already exists. add the pageid
                    # to the array only if not exists already.
                    if (not res["pageid"] in date_object):
                        date_object.append(res["pageid"])
    f.close()
    #print data;
    check_for_users(file_name,data)
    print "Processing file - "+file_name+" completed"
    
"""
loops through the data object and print all user_ids
that have alteast 2 different visits and 2 different days
i.e - aleast two dictionaries under a user_id and the two dictionaries
have an array each containing two page_ids.
"""
def check_for_users(file_name,data):
    f = open(file_name+".out", 'w')
    # date_dictionary example: "06072011": ["49","22"]
    for user_id,date_dictionary in data.iteritems():
        count = 0
        if(len(date_dictionary) >= 2):
            for date,page_array in date_dictionary.iteritems():
                if(len(page_array) == 2):
                    count=count+1
                if(count == 2):
                    f.write(user_id+"\n")
                    break;
    f.close();
            
def main():
    if(len(sys.argv) > 1):
        read_input(sys.argv[1:])
        print "Please find the output in *.out files"
    else:
        print "please specify file names to process"

if __name__ == "__main__":
    main()

        



