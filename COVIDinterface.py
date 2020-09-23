# This is the file for the interface of the pandemic tracker

# Imports And Setup
from time import time
start = time()
print("Loading...")
import COVIDlearner
import COVIDscraper

# Interface Startup
print("""____________________________________
|WELCOME TO THE CORONAVIRUS TRACKER|
------------------------------------
_____________
|GLOBAL DATA|
-------------
Cases:""",
COVIDscraper.total_list[0],
"\nDeaths:",
COVIDscraper.total_list[1],
"\n\nLoaded Successfully In",
str(time() - start)[:4],
"Seconds"
)

# Input For Regional Data
region = input("Type In A Country, And All Of Its COVID Info According To The WHO Will Be Given. (Type In \"US\" for United States Data) ").lower()
start = time()
case_predict = COVIDlearner.predict([[COVIDscraper.initialize_learner_scraping(region)[1][0].replace(",", "")], [COVIDscraper.initialize_learner_scraping(region)[0][0].replace(",", "")]])
death_predict = COVIDlearner.predict([[COVIDscraper.initialize_learner_scraping(region)[1][1].replace(",", "")], [COVIDscraper.initialize_learner_scraping(region)[0][1].replace(",", "")]])
print("""_______________
|REGIONAL DATA|
---------------
Country:""",
COVIDscraper.initialize_interface_scraping(region)[3],
"\nGlobal Rank:",
COVIDscraper.initialize_interface_scraping(region)[2],
"\nCases:",
COVIDscraper.initialize_interface_scraping(region)[0],
"\nDeaths:",
COVIDscraper.initialize_interface_scraping(region)[1],
"\nIf This Country Were To Continue Its Rate Of Coronavirus Spread, \nIt Would Have",
int(case_predict[0]),
"Cases And",
int(death_predict[0]),
"Deaths By The End Of The Day, \nAnd Will Have",
int(case_predict[1]),
"Cases And",
int(death_predict[1]),
"Deaths By The End Of Tomorrow.",
"\n\nIf A Country's Actual Numbers Turn Out To Be Higher Than What The Program Predicted, \nIts Rate Of Spread Is Accelerating. The Opposite Is True If The Program Overestimated The Numbers."
)

# Finishes Process
print(
"These Results Were Given In",
str(time() - start)[:4],
"Seconds\n\nThe Process Has Ended. Restart The Program To Try Again"
)


