from selenium.webdriver.common.by import By

class BetHistoryLocators(object):
    BET_SUMMARY_RECORD = (By.CLASS_NAME, "fn-bet-summary-record")
    BET_SUMMARY_DETAIL = (By.CLASS_NAME, "bet-summary-detail")

    BET_SELECTION = (By.CLASS_NAME, "bet-summary-detail-bet-selection")
    BET_BUILDER_EVENT = (By.CLASS_NAME, "bet-summary-detail-bet-selection-bet-builder-event")

    BET_SIMPLE_NAME = (By.CLASS_NAME, "selection")
    BET_MULTIPLE_NAME = (By.CLASS_NAME, "bet-summary-detail-bet-selection-name-selection-wrap")

    BET_SIMPLE_ODDS = (By.CLASS_NAME, "bet-summary-detail-odds")

    BET_BOOST_ORIGINAL_ODDS = (By.CLASS_NAME, "original-odds")

    BET_STAKE = (By.CLASS_NAME, "bet-summary-detail-amounts-total-stake-value")
    BET_RETURN = (By.CLASS_NAME, "bet-summary-detail-amounts-return-value")

    BET_DATE = (By.CLASS_NAME, "bet-summary-detail-placement-date-date")
    BET_HOUR = (By.CLASS_NAME, "bet-summary-detail-placement-date-time")

    # find_elements("xpath", "(.//*[contains(@class, 'bet-summary-detail-bet-selection')])"))
    # find_elements("xpath", "(.//*[@class = 'bet-summary-detail-bet-selection'])"))  
