import os
import src.private as private

####################
### TESTING MODE ###
####################

# Toggle testing to true/false for testing mode
TESTING = True
TESTING_CHANNEL = private.DEFAULT_CHANNEL

#########################
### FEATURES TOGGLING ###
#########################

# SITES - Set to True/False if you want them scraped
CRAIGSLIST = True
KIJIJI = False

# True if you would like posts with the image preview, and other parameters
# False if you would prefer simple posts with default description & url
ENHANCED_POSTS = True

# Number of thumbs up required for favourites
MIN_THUMBS_UP = 1

######################
### SEARCH FILTERS ###
######################

# The minimum rent you want to pay per month.
MIN_PRICE = 1000

# The maximum rent you want to pay per month.
MAX_PRICE = 2200

# Kijiji/Craiglist image requirement: 0 or 1
HAS_IMAGE = 0

#Kijiji/postal code to search within
POSTAL = 'V5N4B9'

#distance
SEARCH_DISTANCE = 1

#time of the day you leave for work
HOUR_DEPART = 8
MINUTE_DEPART = 0

## how do you get to work?
## accepts: driving, walking, bicycling, transit
TRAVEL_MODE = 'transit'
TRANSIT_MODE = 'subway|bus'
WORK_ADDRESS = "701+W+Georgia+St+Vancvouer+BC+V7Y+1C6"

## longest work commute time your willing to endure!
MAX_COMMUTE_TIME = 250

#######################
### SLACK CONSTANTS ###
#######################

# Name of your slack bot
SLACK_BOT = 'Craig'

# For each site, map the key name from the scraping result to the description
# you would like to appear in the slack post
SLACK_PARAMS = {
    'craigslist': {
        'price': 'Price: ',
        'metro_dist': 'Subway (km): ',
        'area': 'Neighborhood: ',
        'where': 'Address: ',
        'metro': 'Nearest Subway: ',
        'meta': 'Extra Info: ',
        'commute': 'Commute Time (min): '
    },
    'kijiji': {
        'price': 'Price: ',
        'address': 'Address: ',
        'metro_dist': 'Subway (km): ',
        'area': 'Neighborhood: ',
        'metro': 'Nearest Subway: ',
        'commute': 'Commute Time (min): '
    }
}

# enter the parameters you would like to have colour coded
# there are two types of colour coding methodologies
# 1) "range" will check if the parameter value falls within specified range
# 2) "list" will check if the parameter value falls within a specified list
# 3 standard colours - good is green, warning is yellow, danger is red.
# feel free to swap those out with any hex colour code
COLOURS = {
    'price': {
        'levels': {
            'good': [0, 1500],
            'warning': [1501, 1700],
            'danger': [1701, 10000]
        },
        'type': "range"
    },
    'metro_dist': {
        'levels': {
            'good': [0, 0.75],
            'warning': [0.76, 1.5],
            'danger': [1.51, 10]
        },
        'type': "range"
    },
    'commute': {
        'levels': {
            'good': [0, 40],
            'warning': [41, 60],
            'danger': [61, 10000]
        },
        'type': "range"
    },
    'area': {
        'levels': {
            'good': ['commercial-broadway'],
            'warning': [],
            'danger': ['kits', 'Vancouver']
        },
        'type': "list"
    }
}

# for the parameters which will be colour coded as defined in COLOURS,
# enter the order you would like them displayed in so the messages are
# consistently formatted
COLOUR_PARAM_ORDER = ['price', 'area', 'metro_dist', 'commute']

# map each neighborhood to the slack channel you would like it posted in

SLACK_CHANNELS = {
    'commercial-broadway': 'general',
}

# default channel for listings to be posted to
DEFAULT_CHANNEL = private.DEFAULT_CHANNEL

# default colour for slack messages
DEFAULT_COLOUR = '#524e4d'

# This is the order in which the parameters will be posted
# For ex., defaults will be posted first, followed by any fields with a 'good' rating
COLOUR_ORDER = [DEFAULT_COLOUR, 'good', 'warning', 'danger']

###########################
### CRAIGSLIST SETTINGS ###
###########################

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = 'vancouver'

# What Craigslist subdirectories to search on.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
AREAS = ["van"]

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.
CRAIGSLIST_HOUSING_SECTION = 'apa'

#######################
### KIJIJI SETTINGS ###
#######################

UNIT_TYPE_MAP = {
    'studio': 'b-bachelor-studio',
    '1bed': 'b-1-bedroom-apartments-condos/city-of-toronto/c212l1700273',
    '2bed': 'b-2-bedroom-apartments-condos/city-of-toronto/c214l1700273',
    '1bed_den':
    'b-1-bedroom-den-apartments-condos/city-of-toronto/c213l1700273',
    'all': 'b-apartments-condos/city-of-toronto/c37l1700273',
    'house': 'b-house-rental/city-of-toronto/c43l1700273'
}

# enter the types of units you would like to parse
# 'all' includes studios, 1beds, 1beds + den
# 'all' DOES NOT INCLUDE houses
UNIT_TYPES = ['all', 'house']

# 0 if you want un-furnished units, 1 for furnished units
FURNISHED = 0

############################
### LOCATION PREFERENCES ###
############################

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = [("commercial-broadway", [[49.256729, -123.057378],
                                  [49.269590, -123.077093]])]

# A list of neighborhood names to look for in the Craigslist neighborhood name field. If a listing doesn't fall into
# one of the boxes you defined, it will be checked to see if the neighborhood name it was listed under matches one
# of these.  This is less accurate than the boxes, because it relies on the owner to set the right neighborhood,
# but it also catches listings that don't have coordinates (many listings are missing this info).
NEIGHBORHOODS = ['Commercial Drive', 'East Van', 'Commercial-Broadway']

## Transit preferences
# The farthest you want to live from a transit stop.
MAX_TRANSIT_DIST = 1  # kilometers

# Transit stations you want to check against.  Every coordinate here will be checked against each listing,
# and the closest station name will be added to the result and posted into Slack.
TRANSIT_STATIONS = {
    "commercial-broadway": [49.2620791, -123.0674535],
}

# Directory in your folder where you want the log files stored
LOG_PATH = 'logs'

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.

#Any private settings are imported here.
#slack token in private.py
try:
    from private import *
except ImportError:
    try:
        from src.private import *
    except:
        print('no private.py module')
except Exception:
    print('no private.py module')

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass
