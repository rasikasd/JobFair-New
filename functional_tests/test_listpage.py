from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.browser.quit()
        super(AccountTestCase, self).tearDown()

    def test_login(self):
        browser = self.browser
        #Opening the link we want to test
        browser.get('http://127.0.0.1:8000/login/')
        #find the form element
        username = browser.find_element_by_name('username')
        password = browser.find_element_by_name('password')
        submit = browser.find_element_by_name('login')
        print("Element is visible? " + str(submit.is_displayed()))
        #Fill the form with data
        username.send_keys("rasika")
        password.send_keys("rasika@123")
        #submitting the form
        submit.send_keys(Keys.RETURN)
        time.sleep(1)
        print("user logged in successfully")
        assert "logout" in browser.page_source

    def test_register(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000/register/')
        username = browser.find_element_by_name('username')
        email = browser.find_element_by_name('email')
        password1 = browser.find_element_by_name('password1')
        password2 = browser.find_element_by_name('password2')
        submit = browser.find_element_by_name('signup')
        #Fill the form with data
        username.send_keys("punit")
        email.send_keys("punit@gmail.com")
        password1.send_keys("jobs@123")
        password2.send_keys("jobs@123")
        submit.send_keys(Keys.RETURN)
        assert "Your Account has been Created! You can now login" in browser.page_source
        time.sleep(1)
        print("user created successfully")

    def test_missingUsernameReg(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000/register/')
        email = browser.find_element_by_name('email')
        password1 = browser.find_element_by_name('password1')
        password2 = browser.find_element_by_name('password2')
        submit = browser.find_element_by_name('signup')
        email.send_keys("jon@gmail.com")
        password1.send_keys("jon@123")
        password2.send_keys("jon@123")
        submit.send_keys(Keys.RETURN)
        time.sleep(1)
        assert "Your Account has been Created! You can now login" not in browser.page_source
        print("user not created because of missing Username value")

    def test_logout(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000/login/')
        username = browser.find_element_by_name('username')
        password = browser.find_element_by_name('password')
        submit = browser.find_element_by_name('login')
        username.send_keys("rasika")
        password.send_keys("rasika@123")
        submit.send_keys(Keys.RETURN)
        print("user logged in successfully")
        logout = browser.find_element_by_xpath('/html/body/header/nav/div/div/div[2]/a[3]')
        logout.click()
        print("user logged out")
        assert "loginagain" in browser.page_source
        time.sleep(3)

    def test_jobpost(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000/login/')
        username = browser.find_element_by_name('username')
        password = browser.find_element_by_name('password')
        submit = browser.find_element_by_name('login')
        username.send_keys("rasika")
        password.send_keys("rasika@123")
        submit.send_keys(Keys.RETURN)
        print("user logged in successfully")
        newjob = browser.find_element_by_name('newjob')
        newjob.click()
        cname = browser.find_element_by_name('companyname')
        jobplace = browser.find_element_by_name('jobplace')
        jobprofile = browser.find_element_by_name('jobprofile')
        experience = browser.find_element_by_name('experience')
        jobdescription = browser.find_element_by_name('jobdescription')
        contact = browser.find_element_by_name('contact')
        email = browser.find_element_by_name('email')
        applylink = browser.find_element_by_name('applyHere')
        submit = browser.find_element_by_name('postjob')
        cname.send_keys("tesla")
        jobplace.send_keys("Los angeles")
        jobprofile.send_keys("project manager")
        experience.send_keys("minimum 4 years")
        jobdescription.send_keys("The applicant should possess work experience in software development and excellent communication skills")
        contact.send_keys("23456789")
        email.send_keys("tjobs@gmail.com")
        applylink.send_keys("https://forms.gle/enRafh8jXfEqUzBK7")
        submit.send_keys(Keys.ENTER)
        print("Job Posted Successfully")
        assert "Los angeles" in browser.page_source
        time.sleep(3)


    def test_missingEmailReg(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000/register/')
        username = browser.find_element_by_name('username')
        password1 = browser.find_element_by_name('password1')
        password2 = browser.find_element_by_name('password2')
        submit = browser.find_element_by_name('signup')
        username.send_keys("jon")
        password1.send_keys("jon@123")
        password2.send_keys("jon@123")
        submit.send_keys(Keys.RETURN)
        time.sleep(1)
        assert "Your Account has been Created! You can now login" not in browser.page_source
        print("user not created because of missing email field")


    def test_about(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000/')
        about = browser.find_element_by_name('about')
        about.click()
        print("navigated to about page")
        assert "Post Jobs on our website and find the best talent for the role" in browser.page_source
        time.sleep(2)
    
    def test_failedlogin(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000/login/')
        #Find the form element
        username = browser.find_element_by_name('username')
        password = browser.find_element_by_name('password')
        submit = browser.find_element_by_name('login')
        print("Element is visible? " + str(submit.is_displayed()))
        #Fill the form with data
        username.send_keys("jofair")
        password.send_keys("test@123")
        submit.send_keys(Keys.RETURN)
        time.sleep(4)
        assert "Please enter a correct username and password. Note that both fields may be case-sensitive" in browser.page_source
        print("user cannot be logged in because of wrong user credentials")

    def test_profile(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000/login')
        username = browser.find_element_by_name('username')
        password = browser.find_element_by_name('password')
        submit = browser.find_element_by_name('login')
        username.send_keys("rasika")
        password.send_keys("rasika@123")
        submit.send_keys(Keys.RETURN)
        print("user logged in successfully")
        profile = browser.find_element_by_name('profile').click()
        print("Navigated to profile page")
        assert "logged in as" in browser.page_source
        time.sleep(2)

    def test_missingPassReg(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000/register/')
        username = browser.find_element_by_name('username')
        email = browser.find_element_by_name('email')
        #password1 = browser.find_element_by_name('password1')
        password2 = browser.find_element_by_name('password2')
        submit = browser.find_element_by_name('signup')
        #Fill the form with data
        username.send_keys("jon")
        email.send_keys("jon@gmail.com")
        password2.send_keys("jon@123")
        submit.send_keys(Keys.RETURN)
        assert "Your Account has been Created! You can now login" not in browser.page_source
        time.sleep(1)
        print("user not created because of missing conform password value")

    def test_missingReqFieldsJobPost(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000/login/')
        #find the form element
        username = browser.find_element_by_name('username')
        password = browser.find_element_by_name('password')
        submit = browser.find_element_by_name('login')
        username.send_keys("rasika")
        password.send_keys("rasika@123")
        submit.send_keys(Keys.RETURN)
        print("user logged in successfully")
        newjob = browser.find_element_by_name('newjob')
        newjob.click()
        cname = browser.find_element_by_name('companyname')
        # jobplace = browser.find_element_by_name('jobplace')
        # jobprofile = browser.find_element_by_name('jobprofile')
        experience = browser.find_element_by_name('experience')
        jobdescription = browser.find_element_by_name('jobdescription')
        contact = browser.find_element_by_name('contact')
        email = browser.find_element_by_name('email')
        applylink = browser.find_element_by_name('applyHere')
        submit = browser.find_element_by_name('postjob')
        cname.send_keys("amazon")
        experience.send_keys("minimum 4 years")
        jobdescription.send_keys("The applicant should possess work experience in software development and excellent communication skills")
        contact.send_keys("23456789")
        email.send_keys("tjobs@gmail.com")
        applylink.send_keys("https://forms.gle/enRafh8jXfEqUzBK7")
        submit.send_keys(Keys.ENTER)
        assert "amazon" not in browser.page_source
        print("Job was not posted because of missing fields")
        # time.sleep(3)

    def test_incorrectEmailFormat(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000/login/')
        #find the form element
        username = browser.find_element_by_name('username')
        password = browser.find_element_by_name('password')
        submit = browser.find_element_by_name('login')
        username.send_keys("rasika")
        password.send_keys("rasika@123")
        submit.send_keys(Keys.RETURN)
        print("user logged in successfully")
        newjob = browser.find_element_by_name('newjob')
        newjob.click()
        cname = browser.find_element_by_name('companyname')
        jobplace = browser.find_element_by_name('jobplace')
        jobprofile = browser.find_element_by_name('jobprofile')
        experience = browser.find_element_by_name('experience')
        jobdescription = browser.find_element_by_name('jobdescription')
        contact = browser.find_element_by_name('contact')
        email = browser.find_element_by_name('email')
        applylink = browser.find_element_by_name('applyHere')
        submit = browser.find_element_by_name('postjob')
        cname.send_keys("tesla")
        jobplace.send_keys("new york")
        jobprofile.send_keys("project manager")
        experience.send_keys("minimum 4 years")
        jobdescription.send_keys("The applicant should possess work experience in software development and excellent communication skills")
        contact.send_keys("23456789")
        email.send_keys("tjobsgmail")
        applylink.send_keys("https://forms.gle/enRafh8jXfEqUzBK7")
        submit.send_keys(Keys.ENTER)
        assert "Your Account has been Created! You can now login" not in browser.page_source
        print("Job not Posted because email format not detected")
        time.sleep(3)

    def test_profileToHome(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000/login')
        username = browser.find_element_by_name('username')
        password = browser.find_element_by_name('password')
        submit = browser.find_element_by_name('login')
        username.send_keys("rasika")
        password.send_keys("rasika@123")
        submit.send_keys(Keys.RETURN)
        print("user logged in successfully")
        profile = browser.find_element_by_name('profile').click()
        print("Navigated to profile page")
        home = browser.find_element_by_id('home').click()
        assert "logged in as" not in browser.page_source
        print("back to home page")
        time.sleep(2)


    def test_repeatedUsernameRegister(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000/register/')
        username = browser.find_element_by_name('username')
        email = browser.find_element_by_name('email')
        password1 = browser.find_element_by_name('password1')
        password2 = browser.find_element_by_name('password2')
        submit = browser.find_element_by_name('signup')
        #Fill the form with data
        username.send_keys("punit")
        email.send_keys("punit@gmail.com")
        password1.send_keys("jobs@123")
        password2.send_keys("jobs@123")
        submit.send_keys(Keys.RETURN)
        time.sleep(2)
        assert "Your Account has been Created! You can now login" not in browser.page_source
        print("user not created because of repeated Username value")


    def test_navigateToSpecificJob(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000/')
        #find the form element
        elems = browser.find_element_by_name('jobno5')
        elems.click()
        time.sleep(2)
        assert "Apply Here:" in browser.page_source 
        print("Navigated to specific job details page by click action")


    def test_logoutToLogin(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000/login/')
        #find the form element
        username = browser.find_element_by_name('username')
        password = browser.find_element_by_name('password')
        submit = browser.find_element_by_name('login')
        username.send_keys("rasika")
        password.send_keys("rasika@123")
        submit.send_keys(Keys.RETURN)
        print("user logged in successfully")
        logout = browser.find_element_by_name('logout')
        logout.click()
        print("user logged out")
        loginagain = browser.find_element_by_id('loginagain')
        time.sleep(2)
        loginagain.click()
        assert "Log In" in browser.page_source
        print("navigated to login again page after logout through given link")
        time.sleep(2)


    def test_missingConfPassReg(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000/register/')
        username = browser.find_element_by_name('username')
        email = browser.find_element_by_name('email')
        password1 = browser.find_element_by_name('password1')
        submit = browser.find_element_by_name('signup')
        #Fill the form with data
        username.send_keys("jason")
        email.send_keys("j@gmail.com")
        password1.send_keys("jobs@123")
        submit.send_keys(Keys.RETURN)
        assert "Your Account has been Created! You can now login" not in browser.page_source
        time.sleep(1)
        print("user not created because of missing conform password value")

    def test_loginToReg(self):
        browser = self.browser
        #Opening the link we want to test
        browser.get('http://127.0.0.1:8000/login/')
        #find the form element
        signup = browser.find_element_by_name('register')
        print("Element is visible? " + str(signup.is_displayed()))
        signup.click()
        time.sleep(2)
        assert "Join Today" in browser.page_source
        print("user navigated to register page from login page successfully")

    def test_applyHereLink(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000/')
        #find the form element
        elem = browser.find_element_by_name('jobno5')
        elem.click()
        link = browser.find_element_by_id('applylink')
        link.click()
        print("Navigated to apply link from job details page")
        time.sleep(1)
    
    def test_jobUpdate(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000/login/')
        #find the form element
        username = browser.find_element_by_name('username')
        password = browser.find_element_by_name('password')
        submit = browser.find_element_by_name('login')
        username.send_keys("rasika")
        password.send_keys("rasika@123")
        submit.send_keys(Keys.RETURN)
        print("user logged in successfully")
        jobs2 = browser.get("http://127.0.0.1:8000/jobs/5/")
        updatebtn = browser.find_element_by_name('update')
        updatebtn.click()
        updatedesc = browser.find_element_by_name('experience')
        updatedesc.clear()
        updatedesc.send_keys("0-1 years")
        postjob = browser.find_element_by_name('postjob').click()
        print("Job Updated Successfully")
        assert "0-1 years" in browser.page_source
        time.sleep(4)

    def test_jobupdateClearingReqFields(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000/login/')
        #find the form element
        username = browser.find_element_by_name('username')
        password = browser.find_element_by_name('password')
        submit = browser.find_element_by_name('login')
        username.send_keys("rasika")
        password.send_keys("rasika@123")
        submit.send_keys(Keys.RETURN)
        print("user logged in successfully")
        jobs2 = browser.get("http://127.0.0.1:8000/jobs/6/")
        updatebtn = browser.find_element_by_name('update')
        updatebtn.click()
        cname = browser.find_element_by_name('companyname')
        updateExp = browser.find_element_by_name('experience')
        updateExp.clear()
        updateExp.send_keys("0-3 years")
        cname.clear()
        postjob = browser.find_element_by_name('postjob').click()
        assert "0-3 years" not in browser.page_source
        print("Job not Updated because of missing company name")
        time.sleep(4)

    def test_jobdelCancel(self):    
        browser = self.browser
        browser.get('http://127.0.0.1:8000/login/')
        #find the form element
        username = browser.find_element_by_name('username')
        password = browser.find_element_by_name('password')
        submit = browser.find_element_by_name('login')
        username.send_keys("rasika")
        password.send_keys("rasika@123")
        submit.send_keys(Keys.RETURN)
        print("user logged in successfully")
        jobs2 = browser.get("http://127.0.0.1:8000/jobs/5/")
        deletebtn = browser.find_element_by_name('delete')
        deletebtn.click()
        confirmdel = browser.find_element_by_name('cancel')
        confirmdel.send_keys(Keys.RETURN)
        print("Job not Deleted")
        assert "TCS" in browser.page_source
        time.sleep(2)
        
    def test_jobdel(self):    
        browser = self.browser
        browser.get('http://127.0.0.1:8000/login/')
        #find the form element
        username = browser.find_element_by_name('username')
        password = browser.find_element_by_name('password')
        submit = browser.find_element_by_name('login')
        username.send_keys("rasika")
        password.send_keys("rasika@123")
        submit.send_keys(Keys.RETURN)
        print("user logged in successfully")
        jobs2 = browser.get("http://127.0.0.1:8000/jobs/19/")
        deletebtn = browser.find_element_by_name('delete')
        deletebtn.click()
        confirmdel = browser.find_element_by_id('yes')
        confirmdel.send_keys(Keys.RETURN)
        print("Job Deleted")
        assert "jobno19" not in browser.page_source
        time.sleep(2)

