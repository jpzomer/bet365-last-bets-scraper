from base import Page
from locators import *
from datetime import date
from dateutil.relativedelta import relativedelta
from selenium.webdriver.common.keys import Keys
import numpy as np


class BetPage(Page):
    def bet_id_to_uuid(self, bet_id):
        # pegar os ultimos 12 números pra fazer o hex
        return hex(int(bet_id[-12:]))[2:]

    def stake_to_num(self, stake, separator):
        return stake.split(separator)[1]

    def print_thing(self,thing):
        print(thing)

    def discover_bet_type(self, bet):
        # encontra o número de childs bet selection em uma bet
        if len(bet.find_elements(*BetHistoryLocators.BET_SELECTION)) == 1:
            bet_type = "simple"

        else:
            if len(bet.find_elements(*BetHistoryLocators.BET_BUILDER_EVENT))!=0:
                bet_type = "bet_builder"

            else:
                bet_type = "multiple"

        return bet_type

    def get_bet_name(self, bet_type, bet):
        match bet_type:
            case "simple":
                return bet.find_element(*BetHistoryLocators.BET_SIMPLE_NAME).text
            case "multiple":
                element = bet.find_elements(*BetHistoryLocators.BET_MULTIPLE_NAME)
                output = "{} + {}{}".format(element[0].text, element[1].text, " + {} bets".format(len(element)-2) if len(element)>2 else '')
                return output
            case "bet_builder":
                return bet.find_element(*BetHistoryLocators.BET_BUILDER_EVENT).text


    def get_bet_odd(self, bet):
        original_odds = bet.find_elements(*BetHistoryLocators.BET_BOOST_ORIGINAL_ODDS)
        if len(original_odds)!=0:
            output = bet.find_element(*BetHistoryLocators.BET_SIMPLE_ODDS).text
            return output.split(original_odds[0].text)[1]

        else:
            multiple_odds = bet.find_elements(*BetHistoryLocators.BET_SIMPLE_ODDS)
            if len(multiple_odds)>1:
                odd_list = []
                for odd in multiple_odds:
                    odd_list.append(float(odd.text))
                       
                return round(np.prod(odd_list),2)
            else:
                return bet.find_element(*BetHistoryLocators.BET_SIMPLE_ODDS).text

    def return_bets(self):
        self.bet_list = []

        bets = self.driver.find_elements(*BetHistoryLocators.BET_SUMMARY_RECORD)

        # bet_summary = self.driver.find_elements(*BetHistoryLocators.BET_SUMMARY_DETAIL)

        bet_dates = self.driver.find_elements(*BetHistoryLocators.BET_DATE)
        bet_hours = self.driver.find_elements(*BetHistoryLocators.BET_HOUR)

        bet_stakes = self.driver.find_elements(*BetHistoryLocators.BET_STAKE)
        bet_returns = self.driver.find_elements(*BetHistoryLocators.BET_RETURN)

        for index, bet in enumerate(bets):

            try:
                self.bet_obj = {}

                self.bet_obj['bet_id'] = self.bet_id_to_uuid(bet.get_attribute("data-betid"))

                self.bet_obj['bet_type'] = self.discover_bet_type(bet)

                self.bet_obj['bet_name'] = self.get_bet_name(self.bet_obj['bet_type'], bet)

                self.bet_obj['bet_odds'] = self.get_bet_odd(bet)

                self.bet_obj['bet_stake'] = self.stake_to_num(bet_stakes[index].text, "R$")
            
                self.bet_obj['bet_return'] = self.stake_to_num(bet_returns[index].text, "R$")

                self.bet_obj['bet_date'] = bet_dates[index].text

            except Exception as e:
                pass
            finally:
                pass

            self.bet_list.append(self.bet_obj)

        return self.bet_list
