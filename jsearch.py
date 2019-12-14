import pandas as pd
import numpy as np
import sys
from functions import *
import configparser

#inital setup
settings = configparser.ConfigParser()
settings._interpolation = configparser.ExtendedInterpolation()
settings.read('settings.ini')
sections_df = {}
entity_list = settings.sections()

#### load json in dataframes
for section in settings.sections():
    src_file = settings.get(section, 'src_file')
    print ("Loading " + section + " database from " + src_file)
    sections_df[section] = pd.read_json(src_file, orient='columns')

stype = ""
sid = ""
svalue = ""


print ("Welcome to Zendesk Search")
print ("Type 'quit' to exit at any time, Press 'Enter' to continue")
print (" ")
print (" ")
print (" ")

#
begin = input()
if begin == "quit":
    sys.exit()

#global config
pd.options.mode.chained_assignment = None

while(True):
    print ("    Select search options:")
    print ("     • Press 1 to search Zendesk")
    print ("     • Press 2 to view a list of searchable fields")
    print ("     • Type 'quit' to exit")
    print (" ")
    print (" ")

    main_menu = input()
    if main_menu.strip() == "1":        
        while(True):
            message = "Select "
            for item in entity_list:
                if entity_list.index(item) > 0:
                   message = message + ", " 
                message = message + str(entity_list.index(item)+1) + ") " + item.title()

            #print instructions for user input
            print ( message )
            line = input()
            if int(line.strip()) > 0 and  int(line.strip()) <= len(entity_list):
                stype = entity_list[int(line.strip()) -1 ]
                break
            else:
                print ("*** Invalid option ***\n")

        while(True):
            sid = input("Enter search term\n")
            if sid == "":
                continue
            elif sid in sections_df[stype].columns:
                break
            else:
                print ("*** Invalid search term ***\n")                   
        
        svalue = input("Enter search value\n") 
        
        print ("Searching " + stype + " for " + sid + " with a value of " + svalue)
        break     
    elif main_menu.strip() == "2":
        print ("List of Searchable Fields")
        break
    elif main_menu.strip() == "quit":
        sys.exit()
    else:
        continue



if stype in entity_list:    

    input_df = sections_df[stype]

    try:
        key_id = settings.get(stype, 'key_id')
        relation_to_list = settings.get(stype, 'relation_to').strip().split(",") if settings.get(stype, 'relation_to').strip() != "" else {}
        relation_to_id_list = settings.get(stype, 'relation_to_id').strip().split(",") if settings.get(stype, 'relation_to_id').strip() != "" else {}
        relation_from_list = settings.get(stype, 'relation_from').strip().split(",") if settings.get(stype, 'relation_from').strip() != "" else {}
        relation_from_id_list = settings.get(stype, 'relation_from_id').strip().split(",") if settings.get(stype, 'relation_from_id').strip() != "" else {}
    except:
        print("Key doesn't exist, please review settings.ini")
        print("Mandatory keys are: key_id, relation_to, relation_to_id, relation_from, relation_from_id")
        sys.exit("Quitting...")

    #find record from requested entity
    input_row_df = input_df.loc[input_df[sid] == type_cast(input_df[sid], svalue)]

    if input_row_df.size > 0 :        
        #get primary key from main search entity
        user_id = input_row_df[key_id].values[0]

        print (user_id)

        if len(relation_to_id_list) > 0:
            
            i=0
            for relation_to in relation_to_list:
                relation_to = relation_to_list[i]
                relation_to_id = relation_to_id_list[i]
                relation_to_id_val = type_cast(input_row_df[relation_to_id], input_row_df[relation_to_id].values[0])

                print (relation_to_id_val)

                #search related data from other entities
                other_df = sections_df[relation_to]
                other_id = settings.get(relation_to, 'key_id')
                other_title_key = settings.get(relation_to, 'title_key')
                other_row_df = other_df.loc[other_df[other_id] == relation_to_id_val]
                other_name = other_row_df[other_title_key].values[0]

                #singularize colum name
                output_col_prefix = relation_to.rstrip('s')

                #add data to output dataframe
                input_row_df = add_data(other_row_df, input_row_df, other_title_key, output_col_prefix + "_" + other_title_key) 

                i = i + 1    

        
        if len(relation_from_list) > 0:

            i=0
            for relation_from in relation_from_list:
                print ("relation_from " + relation_from)
                relation_from = relation_from_list[i]
                relation_from_id = relation_from_id_list[i]
                #search related data from other entities
                relation_from_title_key = settings.get(relation_from, 'title_key')
                tickets_df = sections_df[relation_from]
                tickets_rows_df = tickets_df.loc[tickets_df[relation_from_id] == int(user_id)]                
            
                #singularize colum name
                output_col_prefix = relation_from.rstrip('s')

                #add data to output dataframe
                input_row_df = add_data(tickets_rows_df, input_row_df, relation_from_title_key, output_col_prefix)

                i = i + 1    

        #display results
        display_output(input_row_df)
    else:
        print ("No results found")

else:
    #print search terms list
    for item in entity_list:
        print_search_terms(sections_df[item], item.title())




    

