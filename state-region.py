import pandas as pd 

def gen_data():
    '''
    Brought in regional crosswalk from Census at referenced link below.
    Needed to remove the numbering, creates a dictionary where the key
    is the name of a region and the value is a list of states in that
    region, and returns a pandas dataframe
    Reference: http://www2.census.gov/geo/pdfs/maps-data/maps/reference/us_regdiv.pdf
    '''
    state_region = {'Northeast': ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', \
    'Rhode Island', 'Vermont', 'New Jersey', 'New York', 'Pennsylvania'], \
    'Midwest': ['Iowa (19)', 'Nebraska (31)','Kansas (20)', 'North Dakota (38)', \
    'Minnesota (27)', 'South Dakota (46)', 'Missouri (29)', \
    'Indiana (18)', 'Illinois (17)', 'Michigan (26)', 'Ohio (39)', 'Wisconsin (55)'], \
    'South': ['Delaware (10)', 'District of Columbia (11)', 'Florida (12)', 'Georgia (13)', \
    'Maryland (24)', 'North Carolina (37)', 'South Carolina (45)', 'Virginia (51)',\
    'West Virginia (54)', 'Alabama (01)', 'Kentucky (21)', 'Mississippi (28)', 'Tennessee (47)', \
    'Arkansas (05)', 'Louisiana (22)', 'Oklahoma (40)', 'Texas (48)'], \
    'West': ['Alaska (02)', 'California (06)', 'Hawaii (15)', 'Oregon (41)', 'Washington (53)']}

    crosswalk_region = ['region']
    crosswalk_state = ['state']
    for key in state_region.keys():
        for i in range(len(state_region[key])):
            crosswalk_region.append(key)
            if '(' in state_region[key][i]:
                crosswalk_state.append(state_region[key][i][:-5])
            else:
                crosswalk_state.append(state_region[key][i])



    f = open('state_region.csv', 'w')

    for i in range(len(crosswalk_state)):
        f.write("{},{}\n".format(crosswalk_state[i], crosswalk_region[i]))

    f.close()