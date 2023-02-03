from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from pages import *
import json
import io
import pathlib
import csv

def main():
    # binary = FirefoxBinary()
    # driver = webdriver.Firefox(firefox_binary=binary)

    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options)

    path = pathlib.Path().resolve()

    driver.get("file://{}/saved_resource(1).html".format(path.as_posix()))
    
    bet_page = BetPage(driver)
    bets = bet_page.return_bets()

    driver.quit()

    print(bets)
    # with io.open('bets.json', 'w', encoding="utf-8") as f:
    #     f.write(str(json.dumps(bets, ensure_ascii=False)))

    # csv header
    fieldnames = ['bet_line', 'bet_stake', 'bet_odds']

    with open('bets.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(bets)


if __name__ == '__main__':
    main()
