# jsearch

A simple command line application to search the data from multiple json files and return the results in a human readable format.

# Prerequisites

* Python3
* pandas
* Tested on on linux only

## Setup pip3 and pandas library
```
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python3 get-pip.py --user
pip3 install pandas
```
## settings.ini

| [Entity]  | Name of the Entity/Section e.g. Users |
| ------------- | ------------- |
| src_file  | relative path of source json file e.g.  jdb/users.json |
| key_id  | Primary key of a particular entity/json file  |
| title_key  | Used when when populating data for linked entities  |
| relation_to  | Name of the entity(s) a particular entity is linked to. Comma separated list  |
| relation_to_id  | Primary key of the entity(s) a particular entity is linked to. Comma separated list  |
| relation_from  | Name of the entity a particular entity(s) is linked from. Comma separated list  |
| relation_from_id  | Primary key of the entity(s) a particular entity is linked from. Comma separated list  |

#### Sample settings.ini file
```
[users]
src_file: jdb/users.json
key_id: _id
title_key: name
relation_to: organizations
relation_to_id: organization_id
relation_from: tickets
relation_from_id: assignee_id

[tickets]
src_file: jdb/tickets.json
key_id: _id
title_key: subject
relation_to: organizations,users
relation_to_id: organization_id,assignee_id
relation_from: 
relation_from_id:

[organizations]
src_file: jdb/organizations.json
key_id: _id
title_key: name
relation_to: 
relation_to_id: 
relation_from: users,tickets
relation_from_id: organization_id,organization_id
```

# Installation and Usage


Run following commands and follow the prompts

```
cd ~
git clone https://github.com/techish1/jsearch
cd jsearch

python3 jsearch.py
```

# Examples
```
➜  python3 jsearch.py                    



Welcome to Zendesk Search
Type 'quit' to exit at any time, Press 'Enter' to continue
 
 
 

    Select search options:
     • Press 1 to search Zendesk
     • Press 2 to view a list of searchable fields
     • Type 'quit' to exit
 
 
1
Select 1) Users 2) Tickets or 3) Organizations
1
Enter search term
_id
Enter search value
1
Searching users for _id with a value of 1
_id                                                                   1
url                      http://initech.zendesk.com/api/v2/users/1.json
external_id                        74341f74-9c79-49d5-9611-87ef9b6eb75f
name                                                Francisca Rasmussen
alias                                                       Miss Coffey
created_at                                   2016-04-15T05:19:46 -10:00
active                                                             True
verified                                                              1
shared                                                            False
locale                                                            en-AU
timezone                                                      Sri Lanka
last_login_at                                2013-08-04T01:03:27 -10:00
email                                      coffeyrasmussen@flotonic.com
phone                                                      8335-422-718
signature                                         Don't Worry Be Happy!
organization_id                                                     119
tags                  [Springville, Sutton, Hartsville/Hartley, Diap...
suspended                                                          True
role                                                              admin
organizations_name                                              Multron
ticket_0                                A Problem in Russian Federation
ticket_1                                            A Problem in Malawi
```

```
➜  python3 jsearch.py



Welcome to Zendesk Search
Type 'quit' to exit at any time, Press 'Enter' to continue
 
 
 

    Select search options:
     • Press 1 to search Zendesk
     • Press 2 to view a list of searchable fields
     • Type 'quit' to exit
 
 
1
Select 1) Users 2) Tickets or 3) Organizations
2
Enter search term
_id
Enter search value
0ebe753c-9c78-458a-817f-3993780bedbf
Searching tickets for _id with a value of 0ebe753c-9c78-458a-817f-3993780bedbf
_id                                0ebe753c-9c78-458a-817f-3993780bedbf
url                   http://initech.zendesk.com/api/v2/tickets/0ebe...
external_id                        537ad752-9056-42c9-86db-f0bdf06d3c10
created_at                                   2016-05-19T12:19:56 -10:00
type                                                            problem
subject                                        A Nuisance in Seychelles
description           Consequat enim velit magna ad sit. Lorem molli...
priority                                                           high
status                                                          pending
submitter_id                                                         23
assignee_id                                                          56
organization_id                                                     118
tags                      [Missouri, Alabama, Virginia, Virgin Islands]
has_incidents                                                      True
due_at                                        2016-08-18 03:33:30-10:00
via                                                                chat
organizations_name                                              Limozen
user_0                                                 Faulkner Holcomb
user_1                                                       Key Mendez
```

```
➜  python3 jsearch.py



Welcome to Zendesk Search
Type 'quit' to exit at any time, Press 'Enter' to continue
 
 
 

    Select search options:
     • Press 1 to search Zendesk
     • Press 2 to view a list of searchable fields
     • Type 'quit' to exit
 
 
1
Select 1) Users 2) Tickets or 3) Organizations
3
Enter search term
_id
Enter search value
103
Searching organizations for _id with a value of 103
_id                                                             103
url               http://initech.zendesk.com/api/v2/organization...
external_id                    e73240f3-8ecf-411d-ad0d-80ca8a84053d
name                                                        Plasmos
domain_names       [comvex.com, automon.com, verbus.com, gogol.com]
created_at                               2016-05-28T04:40:37 -10:00
details                                                  Non profit
shared_tickets                                                False
tags                          [Parrish, Lindsay, Armstrong, Vaughn]
user_0                                              Shelly Clements
user_1                                                 Adriana Ryan
user_2                                                Finley Conrad
ticket_0                                            A Drama in Iraq
ticket_1                                A Catastrophe in Azerbaijan
ticket_2                                     A Catastrophe in Palau
ticket_3                                A Catastrophe in Yugoslavia
ticket_4                                      A Problem in Malaysia
ticket_5                                  A Problem in South Africa
```

```
➜  python3 jsearch.py



Welcome to Zendesk Search
Type 'quit' to exit at any time, Press 'Enter' to continue
 
 
 

    Select search options:
     • Press 1 to search Zendesk
     • Press 2 to view a list of searchable fields
     • Type 'quit' to exit
 
 
1
Select 1) Users 2) Tickets or 3) Organizations
3
Enter search term
_id
Enter search value
1
Searching organizations for _id with a value of 1
No results found
```

# Extensibility

* Utility is configurable through settings.ini
* settings.ini makes this utility exendible
* Main interactive menue is created with the entities/sections data from settings.ini
* More entities (json files) can be added for search without modifying a single line of code, only by adding config into settings.ini

# Performance

* Utility gracefully handles a significant increase in amount of data

# Robustness

* Utility handles errors where possible
* Input data is validated
* Search terms are validated
* Incorrect input is handled gracefully

# Limitations

* tags search term not supported in this version
