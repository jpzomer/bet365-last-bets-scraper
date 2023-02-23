from selenium.webdriver.common.by import By

class BetHistoryLocators(object):
    BET_ENTRY = (By.CLASS_NAME, "myb-SettledBetItem")
    #  SettledBetItem  myb-OpenBetItem

    BET_ENTRY_ODDS = (By.CLASS_NAME, "myb-BetParticipant_HeaderOdds") 

    BET_ENTRY_PARTICIPANT = (By.CLASS_NAME, "myb-BetParticipant_ParticipantSpan") 
    BET_ENTRY_MARKET = (By.CLASS_NAME, "myb-BetParticipant_MarketDescription") 

    BET_ENTRY_FIXTURE = (By.CLASS_NAME, "myb-BetParticipant_FixtureName") 
    
    BET_ENTRY_STAKE = (By.CLASS_NAME, "myd-StakeDisplay_StakeWrapper") 