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
        
        t=0
        for index, tickets_row in tickets_rows_df.iterrows():
            users_row_df["ticket_" + str(t)] = tickets_row['subject']
            t = t + 1

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

        # add users data to org row
        u=0
        for index, users_row in users_row_df.iterrows():
            organizations_row_df["user_" + str(u)] = users_row['name']
            u = u + 1
        
        #search ticket data for user
        tickets_rows_df = tickets_df.loc[tickets_df["organization_id"] == organization_id]
        
        t=0
        for index, tickets_row in tickets_rows_df.iterrows():
            organizations_row_df["ticket_" + str(t)] = tickets_row['subject']
            t = t + 1

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

        # add users data to org row
        u=0
        for index, users_row in users_row_df.iterrows():
            tickets_rows_df["user_" + str(u)] = users_row['name']
            u = u + 1
        
        display_output(tickets_rows_df)
        
    else:
        print ("No results found")



    

