from base import Page
from locators import *
from datetime import date
from dateutil.relativedelta import relativedelta
from selenium.webdriver.common.keys import Keys
import numpy as np


class BetPage(Page):
    def stake_to_num(self, stake, separator):
        return stake.split(separator)[1].replace('.', ',')

    def get_line(self, bet):
        # encontra o número de childs bet selection em uma bet
        participants = (bet.find_elements(*BetHistoryLocators.BET_ENTRY_PARTICIPANT))
        markets = (bet.find_elements(*BetHistoryLocators.BET_ENTRY_MARKET))
        fixtures = (bet.find_elements(*BetHistoryLocators.BET_ENTRY_FIXTURE))
        odds = (bet.find_elements(*BetHistoryLocators.BET_ENTRY_ODDS))

        output = []
        for index, participant in enumerate(participants):
            a = (participant.text[:-4])
            b = (markets[index].text)
            c = (fixtures[index].text[5:])
            d = (odds[index].text.replace('.', ','))
            line_entry = "{} ({}) - {} - {}".format(a,b,c,d)

            output.append(line_entry)

        return '\n'.join(output)

    def get_odds(self, bet):
        odds = (bet.find_elements(*BetHistoryLocators.BET_ENTRY_ODDS))

        output = []
        for odd in odds:
            output.append(float(odd.text))

        return (str(np.prod(output)).replace('.', ','))


    def return_bets(self):
        self.bet_list = []

        bets = self.driver.find_elements(*BetHistoryLocators.BET_ENTRY)

        bet_stakes = self.driver.find_elements(*BetHistoryLocators.BET_ENTRY_STAKE)

        for index, bet in enumerate(bets):

            try:
                self.bet_obj = {}

                self.bet_obj['bet_line'] = self.get_line(bet)
                self.bet_obj['bet_stake'] = self.stake_to_num(bet_stakes[index].text, "R$")
                self.bet_obj['bet_odds'] = self.get_odds(bet)

            except Exception as e:
                pass
            finally:
                pass

            self.bet_list.append(self.bet_obj)

        return self.bet_list
