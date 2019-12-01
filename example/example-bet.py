# import packages
import sys

# import custom packages
sys.path.append('..')

from config import config as cfg
from browser import driver as dri
from browser import navigate as nav
from browser import account as act
from browser import bet as bt

# define static variables
username = ''
password = ''

# define dynamic variables
config = cfg.CONFIG
bri = config.browser_refresh_int
dci = config.data_collection_int
slw = config.screen_load_wait
dh = config.driver_headless
dl = config.driver_location
url = config.url


def main():

    # create driver object
    driver = dri.DRIVER(browser_refresh_int=bri, driver_headless=dh, driver_location=dl, url=url)
    navigate = nav.NAVIGATE(driver=driver.driver)
    account = act.ACCOUNT(driver=driver.driver, screen_load_wait=slw)
    bet = bt.BET(driver=driver.driver, screen_load_wait=slw)

    try:

		# check if internet connection exists
        if not driver.check_internet_connection():
            raise Exception('No Internet Connection')

		# close modal window
        navigate.close_modal_window()

        # login to account
        # close modal window
        # close plugin
        # click Live group event tab
        account.login(username=username, password=password)
        navigate.close_modal_window()
        navigate.close_plugin()
        navigate.click_tab(tab_type='event_group', tab_name='Live')

        # check if logged in
        # attempt to submit bet
        # attempt to submit bet
        if account.check_logged_in():
            bet.submit(bet_amount=1, league='NHL', team_name='Edmonton Oilers', compare_bet_type_value=600, bet_type='moneyline', type='less')
            account.logout()

        # close current driver instance windows
        driver.driver.quit()

    except Exception as e:
        print(str(e))

		# check if driver instance exists
		# close current driver instance windows
        if driver.driver:
            driver.driver.quit()


if __name__ == '__main__':
    main()
