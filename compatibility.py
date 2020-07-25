import json
from json import JSONEncoder

#class to hold all of the applicants
class Applicants:
    def __init__(self, name, score):
        self.name = name
        self.score = score

#class to make Applicants class serializable
class ApplicantEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

#Assign a weight to each of the attributes
#Differnt functions can be written in order to change the way applicants are scored
def weightedValues(appInt, appStr, appSta, appSRes):
    #stat weights 
    totalScore = appInt + appStr + appSta + appSRes
    value = appInt*0.55 + appStr*0.1 + appSta*0.3 + appSRes/totalScore*0.05
    return(value)

def bringToTeam(appInt, appStr, appSta, appSRes, teamInt, teamStr, teamSta, teamSRes):
    
    #Amount that each applicants attribute increases the overall team's attribute stat
    intIncrease = (teamInt + appInt)/teamInt - 1
    if intIncrease > 1:
        intIncrease = 1
    elif intIncrease < 0:
        intIncrease = 0
    strIncrease = (teamStr + appStr)/teamStr - 1
    if strIncrease >= 1:
        strIncrease = 1
    elif strIncrease < 0:
        strIncrease = 0
    staIncrease = (teamSta + appSta)/teamSta - 1
    if staIncrease >= 1:
        staIncrease = 1
    elif staIncrease < 0:
        staIncrease = 0
    SResIncrease = (teamSRes + appSRes)/teamSRes - 1
    if SResIncrease >= 1:
        SResIncrease = 1
    elif SResIncrease < 0:
        SResIncrease = 0

    #weights could be mutable
    totalStats = intIncrease*50 + strIncrease*10 + staIncrease*20 + SResIncrease*20
    
    #Change into a fraction
    value = totalStats/100
    return(value)

     
# Parse json file using json.load()
with open('input.json') as f:
    # dictionary named data
    data = json.load(f)

# Set variables to determine what the team is lacking
intelligence = 0
strength = 0
endurance = 0
spicyFoodTolerance = 0

#Create an applicants dictionary holding an array
applicantsDict = {}
applicantsArr = []

#Iterate through the team data and determine team totals
for value in data["team"]:

    #Determine the total for each attribute
    intelligence += (value["attributes"]["intelligence"])
    strength += (value["attributes"]["strength"])
    endurance += (value["attributes"]["endurance"])
    spicyFoodTolerance += (value["attributes"]["spicyFoodTolerance"])
    
teamTotal = intelligence + strength + endurance + spicyFoodTolerance

#Iterate through the applicant data to determine compatability
for value in data["applicants"]:

    #Find which applicant can contribute most to what the team is lacking
    #Assign each of the values to the cooresponding variable
    appInt = value["attributes"]["intelligence"]
    appStr = value["attributes"]["strength"]
    appSta = value["attributes"]["endurance"]
    appSRes = value["attributes"]["spicyFoodTolerance"]

    #Create an object for each of the applicants and store them into an array of size applicants
    #applicant = Applicants(value["name"], "{:.1f}".format(weightedValues(appInt, appStr, appSta, appSRes)))

    #What each applicant can bring to the team
    applicant = Applicants(value["name"], "{:.1f}".format(bringToTeam(appInt, appStr, appSta, appSRes, intelligence,
    strength, endurance, spicyFoodTolerance)))

    #Store in applicantsArr
    applicantsArr.append(applicant)

applicantsDict["scoredApplicants"] = applicantsArr

# Convert the python dict into JSON string 
jsonData = json.dumps(applicantsDict, indent=4, cls=ApplicantEncoder)
print(jsonData)




