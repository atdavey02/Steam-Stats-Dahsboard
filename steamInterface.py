from steamFunctions import *
from steamGraphs import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

monthsDict = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"  
}

class Homepage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget(self)
        self.setMinimumSize(QSize(1300, 700))
        self.SteamID= QLineEdit("")
        self.APIID = QLineEdit("")
        self.enterButton = QPushButton("Enter")
        self.welcomeLabel = QLabel()
        self.welcomeLabel.setText("Welcome to the Steam Stats Dashboard!")
        self.welcomeLabel.setStyleSheet("color: white; background-color: #096295; min-height: 80px;")
        welcomeFont = self.welcomeLabel.font()
        welcomeFont.setPointSize(30)
        self.welcomeLabel.setFont(welcomeFont)
        self.apiLabel = QLabel()
        self.apiLabel.setText("Enter Your API Key:")
        self.apiLabel.setStyleSheet("color: white;")
        self.steamLabel = QLabel()
        self.steamLabel.setText("Enter Your Steam ID:")
        self.steamLabel.setStyleSheet("color: white;")
        self.APIID.setStyleSheet("color: white;")
        self.SteamID.setStyleSheet("color: white;")
        self.enterButton.setStyleSheet("color: white; background-color: #096295 ")
        self.enterButton.setCheckable(True)
        self.enterButton.clicked.connect(lambda: getValues())
        header = QVBoxLayout()
        header.addWidget(self.welcomeLabel)
        layout = QGridLayout()
        layout.setVerticalSpacing(80)
        layout.setHorizontalSpacing(20)
        layout.addWidget(self.apiLabel,1,1)
        layout.addWidget(self.APIID,1,2)
        layout.addWidget(self.steamLabel,2,1)
        layout.addWidget(self.SteamID,2,2)
        layout.addWidget(self.enterButton,3,1)
        final = QVBoxLayout()
        final.addSpacing(5)
        final.addLayout(header)
        final.addSpacing(50)
        final.addLayout(layout)
        final.addStretch()
        final.setSpacing(0)
        container = QWidget()
        container.setLayout(final)
        container.setStyleSheet("background-color: #161920 ")
        self.stack.addWidget(container)
        self.setCentralWidget(self.stack)
        self.setWindowTitle("Home")

        self.loadingLabel = QLabel("Loading...")
        self.loadingLabel.setStyleSheet("color: white;padding: 550px; min-width: 1000px")
        loadingFont = self.loadingLabel.font()
        loadingFont.setPointSize(30)
        self.loadingLabel.setFont(loadingFont)
        loadingLayout = QVBoxLayout()
        loadingLayout.addWidget(self.loadingLabel)
        loadingContainer = QWidget()
        loadingContainer.setLayout(loadingLayout)
        loadingContainer.setStyleSheet("background-color: #161920 ")
        self.stack.addWidget(loadingContainer)

        self.statsHeader = QLabel("Here Are Your Stats")
        self.statsHeader.setStyleSheet("background-color: #096295; max-height: 220px;")
        self.statsHeader.setFont(loadingFont)
        self.achievementsLabel = QLabel("See Achievements By Game")
        self.achievementsButton = QPushButton("Here")
        self.achievementsButton.setStyleSheet("color: white; background-color: #096295")
        self.achievementsButton.clicked.connect(lambda: loadAchievements())
        self.monthsLabel = QLabel("See Achievements by Month")
        self.monthsButton = QPushButton("Here")
        self.monthsButton.setStyleSheet("color: white; background-color: #096295")
        self.monthsButton.clicked.connect(lambda: loadMonths())
        self.playersLabel = QLabel("See How Popular Your Owned Games Are")
        self.playersButton = QPushButton("Here")
        self.playersButton.setStyleSheet("color: white; background-color: #096295")
        self.playersButton.clicked.connect(lambda: loadGamesPopularity())
        statsHeaderLayout = QVBoxLayout()
        statsLayout= QGridLayout()
        statsHeaderLayout.addWidget(self.statsHeader)
        statsLayout.setVerticalSpacing(80)
        statsLayout.setHorizontalSpacing(20)
        statsLayout.addWidget(self.achievementsLabel,1,0)
        statsLayout.addWidget(self.achievementsButton,1,1)
        statsLayout.addWidget(self.monthsLabel,2,0)
        statsLayout.addWidget(self.monthsButton,2,1)
        statsLayout.addWidget(self.playersLabel,3,0)
        statsLayout.addWidget(self.playersButton,3,1)
        finalLayout = QVBoxLayout()
        finalLayout.addSpacing(5)
        finalLayout.addLayout(statsHeaderLayout)
        finalLayout.addSpacing(50)
        finalLayout.addLayout(statsLayout)
        finalLayout.addStretch()
        finalLayout.setSpacing(0)
        statsContainer = QWidget()
        statsContainer.setLayout(finalLayout)
        statsContainer.setStyleSheet("color: white; background-color: #161920")
        self.stack.addWidget(statsContainer)


        self.achievementsHeader = QLabel("What Games do you Have the Most Achievements in?")
        self.achievementsHeader.setStyleSheet("background-color: #096295; min-height: 80px;")
        self.achievementsHeader.setFont(loadingFont)
        self.top5AchievementsLabel = QLabel("Here Are The 5 Games you Have Earned the Most Achievments in:")
        achievementsHeaderLayout = QVBoxLayout()
        achievementsLayout = QVBoxLayout()
        achievementsHeaderLayout.addWidget(self.achievementsHeader)
        achievementsLayout.addWidget(self.top5AchievementsLabel)
        df = pd.read_csv('achievements.csv',encoding = "ISO-8859-1")
        for row in df.groupby("Game").count().sort_values(["Name"],ascending=False).head(5).iterrows():
            self.newLabel = QLabel(row[0] + ": " + str(row[1]["Name"]))
            achievementsLayout.addWidget(self.newLabel)
        graphAchievementsLabel = QLabel()
        graphAchievements = QPixmap('achievementsGame.png')
        graphAchievements = graphAchievements.scaledToWidth(700)
        graphAchievementsLabel.setPixmap(graphAchievements)
        graphAchievementsLayout = QVBoxLayout()
        graphAchievementsLayout.addWidget(graphAchievementsLabel)
        achievementsGridLayout = QGridLayout()
        achievementsGridLayout.addLayout(achievementsLayout,0,0)
        achievementsGridLayout.addLayout(graphAchievementsLayout,0,1)
        finalAchievementsLayout = QVBoxLayout()
        finalAchievementsLayout.addLayout(achievementsHeaderLayout)
        finalAchievementsLayout.addLayout(achievementsGridLayout)
        self.backAchievementsButton = QPushButton("Back")
        self.backAchievementsButton.setStyleSheet("color: white; background-color: #096295")
        self.backAchievementsButton.clicked.connect(lambda: loadNext())
        finalAchievementsLayout.addWidget(self.backAchievementsButton)
        achievementsContainer = QWidget()
        achievementsContainer.setLayout(finalAchievementsLayout)
        achievementsContainer.setStyleSheet("color: white; background-color: #161920")
        self.stack.addWidget(achievementsContainer)

        self.playersHeader = QLabel("How Popular are the Games You Own?")
        self.playersHeader.setStyleSheet("background-color: #096295; min-height: 80px;")
        self.playersHeader.setFont(loadingFont)
        self.top5Label = QLabel("Here Are The 5 Most Popular Games in Your Steam Library:")
        playersLayout = QVBoxLayout()
        playersLayout.addWidget(self.playersHeader)
        playersLayout.addWidget(self.top5Label)
        df = pd.read_csv('totalPlayers.csv',encoding = "ISO-8859-1")
        df = df.sort_values(by=["Players"],ascending=False)
        df = df.head(5)
        for row in df.iterrows():
            self.newLabel = QLabel(row[1]["Game"] + ": " + str(row[1]["Players"]))
            playersLayout.addWidget(self.newLabel)
        self.backPlayersButton = QPushButton("Back")
        self.backPlayersButton.setStyleSheet("color: white; background-color: #096295")
        self.backPlayersButton.clicked.connect(lambda: loadNext())
        playersLayout.addWidget(self.backPlayersButton)
        playersContainer = QWidget()
        playersContainer.setLayout(playersLayout)
        playersContainer.setStyleSheet("color: white; background-color: #161920")
        self.stack.addWidget(playersContainer)

        self.monthsHeader = QLabel("What Month Did You Get The Most Achievements In?")
        self.monthsHeader.setStyleSheet("background-color: #096295; min-height: 80px;")
        self.monthsHeader.setFont(loadingFont)
        self.top5MonthsLabel = QLabel("Here Are Your 5 Most Active Months on Steam:")
        monthsHeaderLayout = QVBoxLayout()
        monthsLayout = QVBoxLayout()
        monthsHeaderLayout.addWidget(self.monthsHeader)
        monthsLayout.addWidget(self.top5MonthsLabel)
        df = pd.read_csv('achievementsmonth.csv',encoding = "ISO-8859-1")
        df = df.sort_values(by=["Achievement Amount"],ascending=False)
        df = df.head(5)
        for row in df.iterrows():
            self.newLabel = QLabel(monthsDict[row[1]["Month"][5:]] + " " + row[1]["Month"][:4] + ": " + str(row[1]["Achievement Amount"]))
            monthsLayout.addWidget(self.newLabel)
        graphMonthLabel = QLabel()
        graphMonth = QPixmap('achievementsMonth.png')
        graphMonth = graphMonth.scaledToWidth(1000)
        graphMonthLabel.setPixmap(graphMonth)
        graphMonthLayout = QVBoxLayout()
        graphMonthLayout.addWidget(graphMonthLabel)
        monthsGridLayout = QGridLayout()
        monthsGridLayout.addLayout(monthsLayout,0,0)
        monthsGridLayout.addLayout(graphMonthLayout,0,1)
        finalMonthsLayout = QVBoxLayout()
        finalMonthsLayout.addLayout(monthsHeaderLayout)
        finalMonthsLayout.addLayout(monthsGridLayout)
        self.backMonthButton = QPushButton("Back")
        self.backMonthButton.setStyleSheet("color: white; background-color: #096295")
        self.backMonthButton.clicked.connect(lambda: loadNext())
        finalMonthsLayout.addWidget(self.backMonthButton)
        monthsContainer = QWidget()
        monthsContainer.setLayout(finalMonthsLayout)
        monthsContainer.setStyleSheet("color: white; background-color: #161920")
        self.stack.addWidget(monthsContainer)




        def loadNext():
            self.stack.setCurrentIndex(2)
            self.setWindowTitle("Your Stats")

        def getValues():
            key = self.APIID.text()
            user = self.SteamID.text()
            self.stack.setCurrentIndex(1)
            self.setWindowTitle("Loading")
            self.dataCollector = dataCollector(user,key)
            self.dataCollector.finished.connect(loadNext)
            self.dataCollector.start()
        
        def loadGamesPopularity():
            self.stack.setCurrentIndex(4)
            self.setWindowTitle("Games by Popularity")

        def loadMonths ():
            self.stack.setCurrentIndex(5)
            self.setWindowTitle("Top Months")

        def loadAchievements():
            self.stack.setCurrentIndex(3)
            self.setWindowTitle("Top Games")


class dataCollector(QThread):
    def __init__(self,user,key):
        super().__init__()
        self.user = user
        self.key = key

    def run(self):
        generateGraphs(self.user,self.key)
        getPlayerAmounts(self.user,self.key)


app = QApplication([])

window = Homepage()
window.show() 
app.exec()

