import time
import qprompt
from httpreq import *
from prompt_toolkit import prompt


class Menus:

    # operations to assign
    OPTS_CREATE_USER = 'create user'
    OPTS_LOGIN_DETAILS = 'login details'
    OPTS_LOGIN_REQ = 'login request'
    OPTS_CREATE_SCHEDULE = 'create schedule'
    OPTS_CREATE_JOB = 'create job'
    OPTS_BILLING = 'billing'
    OPTS_RATING = 'rating'
    OPTS_SHOW_DATA = 'show'

    # menu names
    MENU_MAIN = 'main-menu'
    MENU_CREATE_USER = 'create-user'

    def __init__(self, opts_assign: dict):
        self.opts = opts_assign
        self.invoke_menus = {self.MENU_MAIN: self.show_main_menu,
                             self.MENU_CREATE_USER: self.show_create_user_menu}
        self.username, self.password = '', ''
        self.login_status = (False, '')
        self.main_menu = qprompt.Menu()

        # init methods
        self.create_menus()

        #prompt('>')

    def create_menus(self):
        # Main Menu
        self.main_menu.add('u', 'Create user')
        self.main_menu.add('l', 'Login')
        self.main_menu.add('s', 'Create schedule')
        self.main_menu.add('j', 'Create job')
        self.main_menu.add('b', 'Billing')
        self.main_menu.add('r', 'Rating')
        self.main_menu.add('d', 'Display info')

    def show_main_menu(self):
        selection = self.main_menu.show()
        if selection == 'u':
            self.show_menu(self.MENU_CREATE_USER)

    def show_create_user_menu(self):
        # TODO: uncomment it: qprompt.ask_captcha(length=6)
        username = qprompt.ask_str("Enter username", valid=lambda x: len(x) > 3)
        password = qprompt.ask_str("Enter password", valid=lambda x: len(x) > 4, shw=False)
        create_user_callback = self.opts.get(self.OPTS_CREATE_USER, None)
        if create_user_callback is not None:
            status, msg = create_user_callback(username, password)
            if status:
                qprompt.status("Creating user succeeded.", time.sleep, [2])
                self.username = username
                self.password = password
                self.login_status = (True, self.username)
            else:
                qprompt.error("Creating user failed: {}".format(msg))
        else:
            qprompt.error("Cannot proceed with creating user - internal error")

    def show_menu(self, menu_name: str):
        func = self.invoke_menus.get(menu_name, None)
        if func is None:
            print("Wrong menu event!")
            return
        func()

    def start(self):
        while True:
            self.show_menu(self.MENU_MAIN)

        print('end of life')


menu = Menus(opts_assign={Menus.OPTS_CREATE_USER: create_user})
menu.start()
