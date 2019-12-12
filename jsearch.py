import pandas as pd
import numpy as np
import sys
from functions import *

stype = sys.argv[1]
sid = sys.argv[2]
svalue = sys.argv[3]

print (stype)
print (sid)
print (svalue)


print ("Welcome to Zendesk Search")
print ("Type 'quit' to exit at any time, Press 'Enter' to continue")
print (" ")
print (" ")
print (" ")
print ("    Select search options:")
print ("     • Press 1 to search Zendesk")
print ("     • Press 2 to view a list of searchable fields")
print ("     • Type 'quit' to exit")
print (" ")
print (" ")

#global config
pd.options.mode.chained_assignment = None

### load json in dataframes
users_file = "users.json"
users_df = pd.read_json(users_file, orient='columns')

organizations_file = "organizations.json"
organizations_df = pd.read_json(organizations_file, orient='columns')

tickets_file = "tickets.json"
tickets_df = pd.read_json(tickets_file, orient='columns')

print ("Searching " + stype + " for " + sid + " with a value of " + svalue)
if stype == "users" :    
    #search for user row
    users_df['_id'] = users_df._id.astype(str)
    users_row_df = users_df.loc[users_df[sid] == svalue]

    if users_row_df.size > 0 :        
        #get user primary key and org foreign key
        user_id = users_row_df["_id"].values[0]
        organization_id = int(users_row_df["organization_id"].values[0])

        #search org data for the user
        organizations_row_df = organizations_df.loc[organizations_df["_id"] == organization_id]
        organizations_name = organizations_row_df["name"].values[0]

        # add org data to user row
        users_row_df = users_row_df.assign(organizations_name = organizations_name)

        #search ticket data for user
        tickets_rows_df = tickets_df.loc[tickets_df["assignee_id"] == int(user_id)]
        
        #add ticket data to output dataframe
        users_row_df = add_data(tickets_rows_df, users_row_df, "subject", "ticket")    

        display_output(users_row_df)
    else:
        print ("No results found")

elif stype == "organizations" :    
    
    #search org data for the user
    organizations_df['_id'] = organizations_df._id.astype(str)
    organizations_row_df = organizations_df.loc[organizations_df[sid] == svalue]
   
    if organizations_row_df.size > 0 :        
        #get user primary key and org foreign key
        organization_id = int(organizations_row_df["_id"].values[0])
        
        #search for user row
        users_row_df = users_df.loc[users_df['organization_id'] == organization_id]

        #add users data to output dataframe
        organizations_row_df = add_data(users_row_df, organizations_row_df, "name", "user")

        #search ticket data for user
        tickets_rows_df = tickets_df.loc[tickets_df["organization_id"] == organization_id]
        
        #add tickets data to output dataframe
        organizations_row_df = add_data(tickets_rows_df, organizations_row_df, "subject", "ticket")

        display_output(organizations_row_df)
    else:
        print ("No results found")

elif stype == "tickets" :    
    
    #search org data for the user
    tickets_rows_df = tickets_df.loc[tickets_df[sid] == svalue]
   
    if tickets_rows_df.size > 0 :        
        #get user primary key and org foreign key
        organization_id = int(tickets_rows_df["organization_id"].values[0])
        user_id = int(tickets_rows_df["assignee_id"].values[0])
        
        #search org data for the user
        organizations_row_df = organizations_df.loc[organizations_df["_id"] == organization_id]
        organizations_name = organizations_row_df["name"].values[0]

        # add org data to user row
        tickets_rows_df = tickets_rows_df.assign(organizations_name = organizations_name)
        
        #search for user row
        users_row_df = users_df.loc[users_df['organization_id'] == organization_id]

        #add users data to output dataframe
        tickets_rows_df = add_data(users_row_df, tickets_rows_df, "name", "user")
        
        display_output(tickets_rows_df)
        
    else:
        print ("No results found")



    

