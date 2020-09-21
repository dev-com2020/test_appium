from appium import webdriver
import random
import string
from phone_gen import PhoneNumber

# foodsi app test by signing up for an new account and logging in with registration data.
# for logging in - test login: kwp@tlen.pl pass: asg123

# randomize phone number
telefon = PhoneNumber("Poland")
number = telefon.get_number(full=False)

# randomize e-mail adress
domains = ["tlen.pl", "gmail.com", "onet.eu", "interia.eu", "wp.pl", "yahoo.com"]
letters = string.ascii_lowercase[:12]


def get_random_domain(domains):
    return random.choice(domains)


def get_random_name(letters, length):
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_emails(nb, length):
    return [get_random_name(letters, length) + '@' + get_random_domain(domains) for i in range(nb)]


# webdriver setup
desired_cap = {
    'deviceName': "emulator-5554",
    'platformName': "Android",
    'appPackage': "com.applover.foodsi",
    'app': "C:/apk/Foodsi_2.20.662.apk",
    'newCommandTimeout': "360",
    'autoGrantPermissions': True
}
# remote connection on Android emulator
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
# setup waiting time
driver.implicitly_wait(10)
# click log_in_email element
driver.find_element_by_id('com.applover.foodsi:id/new_account_button').click()
# click on new customer, and similar elements, input new customer data
register_name = driver.find_element_by_id('com.applover.foodsi:id/new_account_fragment_full_name')
register_name.send_keys('Jan Testowy')
register_mail = driver.find_element_by_id('com.applover.foodsi:id/new_account_fragment_email')
register_mail.send_keys(generate_random_emails(1, 5))
register_phone = driver.find_element_by_id('com.applover.foodsi:id/new_account_fragment_phone_number')
register_phone.send_keys(number)
register_pass = driver.find_element_by_id('com.applover.foodsi:id/new_account_fragment_password')
register_pass.send_keys('pass098')
register_pass2 = driver.find_element_by_id('com.applover.foodsi:id/new_account_fragment_repeat_password')
register_pass2.send_keys('pass098')
# click on sign_up button and tutorial button
driver.find_element_by_id('com.applover.foodsi:id/sign_up_fragment_button').click()
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.c[1]').click()
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.c[2]').click()
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.c[3]').click()
driver.find_element_by_id('com.applover.foodsi:id/tutorial_fab').click()
#  find menu and logout element by xpath
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.view.ViewGroup[1]/android.widget.ImageButton[1]').click()
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.support.v7.widget.LinearLayoutCompat[9]/android.widget.CheckedTextView').click()
# click logout position on handle menu
driver.find_element_by_id('android:id/button1').click()
# login to app
login_name = driver.find_element_by_id('com.applover.foodsi:id/log_in_fragment_email').send_keys("kwp@tlen.pl")
login_pass = driver.find_element_by_id('com.applover.foodsi:id/log_in_fragment_password').send_keys("asg123")
driver.find_element_by_id('com.applover.foodsi:id/log_in_button').click()
