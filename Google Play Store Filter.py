# Google Play Store Data Filter
# Authored by Matthew Steuerer, Nikhil Sankepalli, and Seth Curry
# October 7th, 2020
# Demonstrates the use of Lists is Python with 2018 Google Play Store Data
# Data Source URL: https://www.kaggle.com/lava18/google-play-store-apps

# Initial Ideas: create a list of objects where each entry in the list is an app object
# Each app will have attributes that correspond to column titles
# The user needs to be able to filter on up to three of these attributes
# Need to confirm if user should be able to apply multiple filters (ex: category type and content rating)
# User inputs their criteria and the program needs to find all records that match
# Minimum Requirements: Be able to run the program once and return result, user may have to rerun for additional queries
# Ideal Requirements: Be able to have program run in a loop and filter on multiple criteria
# Shoot for the Stars Requirements: GUI with program logic

import csv


# Class to represent an app object and all its properties (columns) from the data source


class GoogleApp:
    def __init__(self, app, category, rating, reviews, size, installs, type, price, contentRating, genres, lastUpdated,
                 currentVer, androidVer):
        self.app = app
        self.category = category
        self.rating = rating
        self.reviews = reviews
        self.size = size
        self.installs = installs
        self.type = type
        self.price = price
        self.contentRating = contentRating
        self.genres = genres
        self.lastUpdated = lastUpdated
        self.currentVer = currentVer
        self.androidVer = androidVer

    # String Representation of Google App Object (How its displayed once its printed)
    def __str__(self):
        appString = self.app + " " + self.category + " " + self.rating + " " + self.reviews + " "
        appString = appString + " " + self.size + " " + self.installs + " " + self.type + " "
        appString = appString + " " + self.price + " " + self.contentRating + " " + self.genres + " "
        appString = appString + " " + self.lastUpdated + " " + self.currentVer + " " + self.androidVer
        return appString

# Our list object which will hold the entire data source for processing
appList = []

# Use a reader object to read from csv file data source
with open('googleplaystore.csv') as csvFile:
    readCSV = csv.reader(csvFile, delimiter=',')
    i = 0
    for row in readCSV:
        # Note: needed to edit data source as one row had two columns that were null and reader object threw errors
        # For each row in the file, make an object and append it to the list of items
        appList.append(
            GoogleApp(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                      row[12]))
        # The first object in the list is the column headings, and could be ignored
        # just used for debugging print(appList[0])

        # just used for debugging i = i + 1

# No more needs to be done to load the source
# Now just need to offer a menu with search options for user;
# Different options depending on which column they want to search on
# Requirements state user must be able to search by up to three values (Need to check up to 3 columns)
# Ask user how many search values they will enter (up to three allowed)
# Have a switch statement depending on which columns user would like to search by
# Have the switch run in a loop with an exit command
