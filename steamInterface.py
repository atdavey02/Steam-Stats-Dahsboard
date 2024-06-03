from steamFunctions import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *




class Homepage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(1300, 700))
        self.SteamID= QLineEdit()
        self.APIID = QLineEdit()
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
        final.addSpacing(52)
        final.addLayout(layout)
        final.addStretch()
        final.setSpacing(0)
        container = QWidget()
        container.setLayout(final)
        container.setStyleSheet("background-color: #161920 ")
        self.setCentralWidget(container)
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


        def getValues():
            key = self.APIID.text()
            user = self.SteamID.text()
            self.setCentralWidget(loadingContainer)
            self.setWindowTitle("Loading")





app = QApplication([])

window = Homepage()
window.show() 
app.exec()

