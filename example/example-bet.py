# import packages
import sys

# import custom packages
sys.path.append('..')

from config import config as cfg
from browser import driver as dri
from browser import navigate as nav
from browser import account as act

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

        # attempt to submit bet
        bet.submit(bet_amount=1, league='NHL', team_name='Nashville Predators', compare_bet_type_value=200, bet_type='moneyline', type='less')

        # logout of account
        account.logout()


if __name__ == '__main__':
	main()