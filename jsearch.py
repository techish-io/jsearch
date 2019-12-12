import pandas as pd
import numpy as np
import sys
from functions import *

stype = ""
sid = ""
svalue = ""

print (stype)
print (sid)
print (svalue)


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

### load json in dataframes
users_file = "jdb/users.json"
users_df = pd.read_json(users_file, orient='columns')

organizations_file = "jdb/organizations.json"
organizations_df = pd.read_json(organizations_file, orient='columns')

tickets_file = "jdb/tickets.json"
tickets_df = pd.read_json(tickets_file, orient='columns')

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
            print ("Select 1) Users 2) Tickets or 3) Organizations")
            line = input()
            if line.strip() == "1":
                stype = "users" 
                break
            elif line.strip() == "2":
                stype = "tickets" 
                break
            elif line.strip() == "3":
                stype = "organizations"
                break
            else:
                print ("*** Invalid option ***\n")

        while(True):
            sid = input("Enter search term\n")
            if sid == "":
                continue
            elif stype == "users" and sid in users_df.columns:
                break
            elif stype == "tickets" and sid in tickets_df.columns:
                break
            elif stype == "organizations" and sid in organizations_df.columns:
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



if stype == "users" :    
    #search for user row
    users_row_df = users_df.loc[users_df[sid] == type_cast(users_df[sid], svalue)]

    if users_row_df.size > 0 :        
        #get user primary key and org foreign key
        user_id = users_row_df["_id"].values[0]
        organization_id = int(users_row_df["organization_id"].values[0])

        #search org data for the user
        organizations_row_df = organizations_df.loc[organizations_df["_id"] == organization_id]
        organizations_name = organizations_row_df["name"].values[0]

        # add org data to user row
        users_row_df = users_row_df.assign(organizations_name = organizations_name)

        #search tickets of this user
        tickets_rows_df = tickets_df.loc[tickets_df["assignee_id"] == int(user_id)]
        
        #add ticket data to output dataframe
        users_row_df = add_data(tickets_rows_df, users_row_df, "subject", "ticket")    

        #display results
        display_output(users_row_df)
    else:
        print ("No results found")

elif stype == "organizations" :    
    
    #search org data for the user
    organizations_row_df = organizations_df.loc[organizations_df[sid] == type_cast(organizations_df[sid], svalue)]
   
    if organizations_row_df.size > 0 :        
        #get user primary key and org foreign key
        organization_id = int(organizations_row_df["_id"].values[0])
        
        #search for users of this organization
        users_row_df = users_df.loc[users_df['organization_id'] == organization_id]

        #add users data to output dataframe
        organizations_row_df = add_data(users_row_df, organizations_row_df, "name", "user")

        #search tickets of this organization
        tickets_rows_df = tickets_df.loc[tickets_df["organization_id"] == organization_id]
        
        #add tickets data to output dataframe
        organizations_row_df = add_data(tickets_rows_df, organizations_row_df, "subject", "ticket")

        #display results
        display_output(organizations_row_df)
    else:
        print ("No results found")

elif stype == "tickets" :    

    
    #search org data for the user
    tickets_rows_df = tickets_df.loc[tickets_df[sid] == type_cast(tickets_df[sid], svalue)]
   
    if tickets_rows_df.size > 0 :        
        #get user primary key and org foreign key
        organization_id = int(tickets_rows_df["organization_id"].values[0])
        user_id = int(tickets_rows_df["assignee_id"].values[0])
        
        #search org data for the user
        organizations_row_df = organizations_df.loc[organizations_df["_id"] == organization_id]
        organizations_name = organizations_row_df["name"].values[0]

        # add org data to user row for this ticket
        tickets_rows_df = tickets_rows_df.assign(organizations_name = organizations_name)
        
        #search for user row for this ticket
        users_row_df = users_df.loc[users_df['_id'] == user_id]
        user_name = users_row_df["name"].values[0]

        #add users data to output dataframe
        tickets_rows_df = tickets_rows_df.assign(user_name = user_name)
        
        #display results
        display_output(tickets_rows_df)
        
    else:
        print ("No results found")
else:
    #print search terms list
    print_search_terms(users_df, "Users")
    print_search_terms(tickets_df, "Tickets")
    print_search_terms(organizations_df, "Organizations") 




    

