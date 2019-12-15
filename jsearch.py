import configparser
import sys
import pandas as pd
from functions import *

#global config
pd.options.mode.chained_assignment = None

#global vars
search_type = ""  
search_id = ""    
search_value = "" 
settings = None
sections_df = {}
entity_list = {}

#Initial setup and load
def load():
    #inital setup
    global settings
    global sections_df
    global entity_list
    
    settings = configparser.ConfigParser()
    settings._interpolation = configparser.ExtendedInterpolation()
    settings.read('settings.ini')
    sections_df = {}
    entity_list = settings.sections()

    #load json in dataframes
    for section in settings.sections():
        src_file = settings.get(section, 'src_file')
        sections_df[section] = pd.read_json(src_file, orient='columns')




#user input function
def ask_user():
    global search_type
    global search_id
    global search_value
    
    print("Welcome to Zendesk Search")
    print("Type 'quit' to exit at any time, Press 'Enter' to continue")
    print(" ")
    print(" ")
    print(" ")

    #
    begin = input()
    if begin == "quit":
        sys.exit()



    while(True):
        print("    Select search options:")
        print("     • Press 1 to search Zendesk")
        print("     • Press 2 to view a list of searchable fields")
        print("     • Type 'quit' to exit")
        print(" ")
        print(" ")

        main_menu = input()
        if main_menu.strip() == "1":        
            while(True):
                message = "Select "
                for item in entity_list:
                    if entity_list.index(item) > 0:
                        message = message + ", " 
                    message = message + str(entity_list.index(item)+1) + ") " + item.title()

                #print instructions for user input
                print(message)
                line = input()
                if line.strip() != "" and int(line.strip()) > 0 and  int(line.strip()) <= len(entity_list):
                    search_type = entity_list[int(line.strip()) -1]
                    break
                else:
                    print("*** Invalid option ***\n")

            while(True):
                search_id = input("Enter search term\n")
                if search_id == "":
                    continue
                elif search_id in sections_df[search_type].columns:
                    break
                else:
                    print("*** Invalid search term ***\n")                   
            
            search_value = input("Enter search value\n") 
            
            print("Searching " + search_type + " for " + search_id + " with a value of " + search_value)
            break     
        elif main_menu.strip() == "2":
            break
        elif main_menu.strip() == "quit":
            sys.exit()
        else:
            continue


#search function of the module
def search():
    #search data from related entities
    if search_type in entity_list:    

        input_df = sections_df[search_type]

        try:
            key_id = settings.get(search_type, 'key_id')
            relation_to_list = settings.get(search_type, 'relation_to').strip().split(",") if settings.get(search_type, 'relation_to').strip() != "" else {}
            relation_to_id_list = settings.get(search_type, 'relation_to_id').strip().split(",") if settings.get(search_type, 'relation_to_id').strip() != "" else {}
            relation_from_list = settings.get(search_type, 'relation_from').strip().split(",") if settings.get(search_type, 'relation_from').strip() != "" else {}
            relation_from_id_list = settings.get(search_type, 'relation_from_id').strip().split(",") if settings.get(search_type, 'relation_from_id').strip() != "" else {}
        except:
            print("Key doesn't exist, please review settings.ini")
            print("Mandatory keys are: key_id, relation_to, relation_to_id, relation_from, relation_from_id")
            sys.exit("Quitting...")

        #find record from requested entity
        input_row_df = input_df.loc[input_df[search_id] == type_cast(input_df[search_id], search_value)]

        if input_row_df.size > 0:      
            #get primary key from main search entity
            user_id = input_row_df[key_id].values[0]

            if len(relation_to_id_list) > 0:
                
                i = 0
                for relation_to in relation_to_list:
                    relation_to = relation_to_list[i]
                    relation_to_id = relation_to_id_list[i]
                    relation_to_id_val = type_cast(input_row_df[relation_to_id], input_row_df[relation_to_id].values[0])

                    #search related data from other entities
                    related_to_df = sections_df[relation_to]
                    related_to_id = settings.get(relation_to, 'key_id')
                    related_to_title_key = settings.get(relation_to, 'title_key')
                    related_to_row_df = related_to_df.loc[related_to_df[related_to_id] == relation_to_id_val]
                    related_to_name = related_to_row_df[related_to_title_key].values[0]

                    #singularize colum name
                    output_col_prefix = relation_to.rstrip('s')

                    #add data to output dataframe
                    input_row_df = add_data(related_to_row_df, input_row_df, related_to_title_key, output_col_prefix + "_" + related_to_title_key) 

                    i = i + 1    

            
            if len(relation_from_list) > 0:

                i = 0
                for relation_from in relation_from_list:
                    relation_from = relation_from_list[i]
                    relation_from_id = relation_from_id_list[i]
                    #search related data from other entities
                    relation_from_title_key = settings.get(relation_from, 'title_key')
                    related_from_df = sections_df[relation_from]
                    related_from_rows_df = related_from_df.loc[related_from_df[relation_from_id] == int(user_id)]                
                
                    #singularize colum name
                    output_col_prefix = relation_from.rstrip('s')

                    #add data to output dataframe
                    input_row_df = add_data(related_from_rows_df, input_row_df, relation_from_title_key, output_col_prefix)

                    i = i + 1    

            #display results
            display_output(input_row_df)
        else:
            print("No results found")

    else:
        #print search terms list
        print("List of Searchable Fields")
        for item in entity_list:
            print_search_terms(sections_df[item], item.title())


#main function of search module
def main():
    load()
    ask_user()
    search()

if __name__ == '__main__':
    main()


    

