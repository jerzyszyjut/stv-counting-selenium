from selenium import webdriver


class CountingVotes:
    driver = ''

    def __init__(self, votes, candidates, mandates):
        self.votes = votes
        self.candidates = candidates
        self.mandates = mandates

    def startCounting(self):
        self.startBrowser()
        self.insertSetup()
        self.insertCandidates()
        self.insertVotes()

    def startBrowser(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://paul-lockett.co.uk/stv.html")

    def insertSetup(self):
        self.driver.find_element_by_id(
            "inputboxseats").send_keys(self.mandates)
        self.driver.find_element_by_id("inputboxcandidates").send_keys(
            str(len(self.candidates)))
        self.driver.find_element_by_id(
            "inputboxvotes").send_keys(str(len(self.votes)))
        self.driver.find_element_by_id("button1").click()

    def insertCandidates(self):
        for i in self.candidates:
            self.driver.find_element_by_id("inputboxcandidate").send_keys(i)
            self.driver.find_element_by_id("button2").click()

    def insertVotes(self):
        for i in self.votes:
            for j in range(len(self.candidates)):
                currentCandidate = i[j]
                currentPosition = j
                if(i[j] == ''):
                    self.driver.find_elements_by_css_selector(
                        'input[value="none"]')[currentPosition].click()
                else:
                    self.driver.find_elements_by_css_selector(
                        'input[value="'+currentCandidate+'"]')[currentPosition].click()
            self.driver.find_element_by_name("button2").click()
