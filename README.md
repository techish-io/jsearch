# jsearch
```
➜  python3 jsearch.py users _id 2                                       
 
Searching users for _id with a value of 2
_id                                                                2
url                   http://initech.zendesk.com/api/v2/users/2.json
external_id                     c9995ea4-ff72-46e0-ab77-dfe0ae1ef6c2
name                                                    Cross Barlow
alias                                                      Miss Joni
created_at                                2016-06-23T10:31:39 -10:00
active                                                          True
verified                                                           1
shared                                                         False
locale                                                         zh-CN
timezone                                                     Armenia
last_login_at                             2012-04-12T04:03:28 -10:00
email                                        jonibarlow@flotonic.com
phone                                                   9575-552-585
signature                                      Don't Worry Be Happy!
organization_id                                                  106
tags                       [Foxworth, Woodlands, Herlong, Henrietta]
suspended                                                      False
role                                                           admin
organizations_name                                         Qualitern
ticket_0                                    A Catastrophe in Bermuda
ticket_1                 A Problem in Svalbard and Jan Mayen Islands
```

```
➜  python3 jsearch.py organizations _id 101                             

Searching organizations for _id with a value of 101
_id                                                             101
url               http://initech.zendesk.com/api/v2/organization...
external_id                    9270ed79-35eb-4a38-a46f-35725197ea8d
name                                                        Enthaze
domain_names       [kage.com, ecratic.com, endipin.com, zentix.com]
created_at                               2016-05-21T11:10:28 -10:00
details                                                    MegaCorp
shared_tickets                                                False
tags                              [Fulton, West, Rodriguez, Farley]
user_0                                              Loraine Pittman
user_1                                               Francis Bailey
user_2                                                 Haley Farmer
user_3                                               Herrera Norman
ticket_0                                        A Drama in Portugal
ticket_1                                      A Problem in Ethiopia
ticket_2                      A Problem in Turks and Caicos Islands
ticket_3                                        A Problem in Guyana
```

```
➜  python3 jsearch.py tickets _id "0ebe753c-9c78-458a-817f-3993780bedbf"
 
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
