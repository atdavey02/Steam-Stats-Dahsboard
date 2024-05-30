
import requests
import json
from datetime import datetime
import csv

#Gets player achievments and their global perecentage completions
def getAchievements(appId,steamId):
    key = 'Your API KEY Here' 
    achieve_dict = {}
    r = requests.get(f'http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid={appId}&key={key}&steamid={steamId}&l=EN').text
    jsonn = json.loads(r)
    r2 = requests.get(f'http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid={appId}').text
    jsonn2 = json.loads(r2)
    if 'achievements' not in  jsonn['playerstats']:
        return achieve_dict
    for item in jsonn['playerstats']['achievements']:
        if item['achieved'] != 0:
            for achievement in jsonn2['achievementpercentages']['achievements']:
                if(achievement['name'] == item['apiname']):
                    print('Achievement = ', item['name'], 'Unlocked at = ', datetime.fromtimestamp(item['unlocktime']).strftime('%Y-%m-%d %H:%M:%S'))
                    achieve_dict[item['name']] = [[datetime.fromtimestamp(item['unlocktime']).strftime('%Y-%m-%d %H:%M:%S')],jsonn['playerstats']['gameName'],item['description'],achievement['percent']]
    return achieve_dict

#Gets games in the users library
def getGames(userId): 
    key = '#Your API KEY Here'
    r = requests.get(f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={key}&steamid={userId}&include_appinfo=1 ').text
    jsonn = json.loads(r)
    gamesList = []
    for item in jsonn['response']['games']: 
        print('Game = ' ,item['name'], 'Id = ' , item['appid'])
        gamesList.append((item['appid'],item['name']))
    return gamesList
    

#Gets all achievements for the user
def getPlayerAchievements(userId):
    gamesList = getGames(userId)
    achieve_dict = {}
    for item in gamesList:
        achieve_dict.update(getAchievements(item[0],userId))
    achieve_dict = sorted(achieve_dict.items(), key = lambda kv: kv[1], reverse=True)
    for item in achieve_dict:
        print(item)
    file = open('achievements.csv','w', newline='')
    writer = csv.writer(file)
    for key, value in achieve_dict:
        writer.writerow([key,value[0],value[1],value[2],value[3]])

#Gets amount of global players for every game the user has
def getPlayerAmounts(userId):
    file = open('totalPlayers.csv','w', newline='')
    writer = csv.writer(file)
    gamesList = getGames(userId)
    for item in gamesList:
        r2 =  requests.get(f'http://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={item[0]}').text
        jsonn2 = json.loads(r2)
        writer.writerow([item[1],jsonn2['response']['player_count']]) 

#Groups steam achievements by month
def achievementsByMonth(userId):
    getPlayerAchievements(userId)
    file = open('achievements.csv','r')
    reader = csv.reader(file)
    times_dict = {}
    for row in reader:
        if row[1] != '':
            print(row[1][2:9])
            if row[1][2:9] not in times_dict:
                times_dict[row[1][2:9]] = 1
            else:
                times_dict[row[1][2:9]] += 1
    for item in times_dict.items():
        print(item)
    file2 = open('achievementsmonth.csv','w',newline='')
    writer = csv.writer(file2)
    for key, value in times_dict.items():
        writer.writerow([key,value])
