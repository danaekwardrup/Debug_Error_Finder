import os
import csv
import re
error_counter = 0
pttrace_counter = 0
filter = 'PtTrace'
file_dict = {}

def parse_text(input):
    """

    :param input:
    :return:
    """
    return input


path = input('Please enter directory path: ')
#user provides path to Recommendation folder
for(root,_,files) in os.walk(path):
    #use os.walk read/print directory path and all filenames in said folder
    #skipping subdirectory parameter bc don't need it
    #returns files in a tuple
    for file in files:
        #for every item in the tuple of filenames...
        error_list = []
        has_error = False
        #set Boolean condition for files with errors counter
        if filter in file:
            #if filename contains string "PtTrace"...removes debug files
            pttrace_counter += 1
            #get total count of pttrace files
            file_path = os.path.join(root, file)
            """use os.path.join to concatenate directory path
            to each filename in the tuple
            these complete filepaths will
            be added to one long string"""
            with open(file_path) as f:
                #use open to open file at filepath and return as file object (f)
                content = f.readlines()
                #readlines to return all lines in file_path string
                #each line is item in list (content)
                for item in content:
                    # item in our list content = line in PtTrace file
                    if 'error' in item.lower():
                        #if line is error message
                        item.strip('\n')
                        #remove newline from strings
                        item = re.sub(r"[^a-zA-Z0-9]+", ' ', item)
                        #regular expression to remove any special characters
                        error_list.append(item)
                        #add that line to error_list
                        has_error = True
                        #also update Boolean to True (for our error_counter)
                        #print(f'File path: {file_path}. Error message: {item}')
                        #for each error message print file path and error message string
            if has_error:
                #if PtTrace file has error
                file_dict[file] = error_list
                #take empty dictionary file_dict
                #set filename as key, relative error message(s) as value(s)
                error_counter += 1
                #also add 1 to error counter

"""
so now we have a dictionary in which the keys are the file names
and the values are the error messages. now we need to write this dictionary
to a csv file so we can look at actual error messages/assess how many
different types of error messages 
"""
with open('pttrace_errors.csv', mode = 'w', newline='') as pttrace_file:
    #open (or create) csv file, write mode
    #assign file object to pttrace_file variable
    pttrace_writer = csv.writer(pttrace_file, delimiter=',')
    pttrace_writer.writerow(['File Path', 'File Errors'])
    #use csv.writer to create headers of csv

    for i in file_dict.items():
        file_name = i[0]

        for x in i[1]:
            pttrace_writer.writerow([file_name, x])
        #for each item (key:value) in our dictionary
        #write key to column 1, value to column 2

print(f'Found {error_counter} files with errors out of {pttrace_counter} PtTrace files.')
#final output to that tells user how many files out of all pttrace files had errors"""











