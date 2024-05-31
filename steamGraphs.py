from steamFunctions import *
import matplotlib.pyplot as plt
import pandas as pd


#generate pie chart achivements by game
def generateGamesPieChart(userId):
    getPlayerAchievements(userId)
    df = pd.read_csv("achievements.csv",encoding = "ISO-8859-1")
    countsArray = []
    gamesArray = []
    for game in df.groupby("Game"):
        if game[0] in df.groupby("Game")["Name"].count().sort_values(ascending=False).head(10):
            gamesArray.append(game[0])
        else:
            gamesArray.append("")
    for count in df.groupby("Game")["Name"].count():
        countsArray.append(count)
    plt.figure(figsize=(15,9))
    plt.pie(countsArray,labels=gamesArray,startangle = 90)
    plt.show()    

#Generate graph of achivements by month
def generateAchievementsMonthGraph(userId):
    achievementsByMonth(userId)
    df = pd.read_csv("achievementsMonth.csv")
    monthsArray = []
    achievementsArray = []
    currentMonth = df.loc[0]["Month"]
    for index,row in df.iterrows():
        while row["Month"] != currentMonth:
            monthsArray.append(currentMonth)
            achievementsArray.append(0)
            if int(currentMonth[5:]) == 1:
                nextMonth = 12
                nextYear = int(currentMonth[:4])-1
            else:
                nextMonth =  int(currentMonth[5:]) -1
                nextYear = int(currentMonth[:4])
            if nextMonth < 10:
                nextMonth = "0" + str(nextMonth)
            currentMonth = str(nextYear) + "-" + str(nextMonth)
        monthsArray.append(row["Month"])
        achievementsArray.append(row["Achievement Amount"])
        if int(row["Month"][5:]) == 1:
            nextMonth = 12
            nextYear = int(row["Month"][:4])-1
        else:
            nextMonth =  int(row["Month"][5:]) -1
            nextYear = int(row["Month"][:4])
        if nextMonth < 10:
            nextMonth = "0" + str(nextMonth)
        currentMonth = str(nextYear) + "-" + str(nextMonth)
    monthsArray.reverse()
    achievementsArray.reverse()
    plt.figure(figsize=(15,9))
    plt.bar(monthsArray,achievementsArray)
    plt.title("Achievements by Month")
    for i in range(len(monthsArray)):
        plt.text(i, achievementsArray[i]+3, achievementsArray[i], ha = 'center')
    plt.xticks(range(len(monthsArray)), monthsArray, rotation=90)
    plt.xlim([-1,len(monthsArray)])
    plt.xlabel("Month",labelpad=8)
    plt.ylabel("Achievements Earned")
    plt.savefig("achievementsMonth.png")

    



