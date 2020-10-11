
class Menus:

    # operations to assign
    CREATE_USER = 'create user'
    LOGIN_DETAILS = 'login details'
    LOGIN_REQ = 'login request'
    CREATE_SCHEDULE = 'create schedule'
    CREATE_JOB = 'create job'
    BILLING = 'billing'
    RATING = 'rating'
    SHOW_DATA = 'show'

    def __init__(self, opt_assign: dict):
        self.opts = opt_assign
        self.main_menu = dict()
        self.login_menu = dict()
        self.create_schedule_menu = dict()
        self.create_job_menu = dict()
        self.rating_menu = dict()
        self.billing_menu = dict()
        self.show_data_menu = dict()

    def create_menus(self):
        # Main Menu
        self.main_menu = {'Create User': self.opts[self.CREATE_USER],
                          'Login': self.opts[self.LOGIN],
                          'Create Schedule': self.opts[self.CREATE_SCHEDULE],
                          'Create Job': self.opts[self.CREATE_JOB],
                          'Billing': self.opts[self.BILLING],
                          'Rating': self.opts[self.RATING],
                          'Show Data': self.opts[self.SHOW_DATA]}

        self.login_menu = ['Enter Username: ', 'Enter Password: ', self.opts[self.LOGIN_REQ]]

