import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InsiderHomePage:
    def __init__(self, driver):
        self.browser = driver
        self.url = "https://useinsider.com/"
        self.company_locator = "//a[contains(text(), 'Company')]"
        self.careers_locator = "//a[contains(text(), 'Careers')]"
        self.locations_section_locator = "//h3[contains(text(), 'Our Locations')]"
        self.teams_section_locator = "//a[contains(text(), 'See all teams')]"
        self.life_at_insider_section_locator = "//h2[contains(text(), 'Life at Insider')]"

    def navigate_to_homepage(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def navigate_to_careers_page(self):
        company = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.company_locator))
        )
        company.click()

        careers = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.careers_locator))
        )
        careers.click()

    def is_locations_section_accessible(self):
        return EC.presence_of_element_located((By.XPATH, self.locations_section_locator))

    def is_teams_section_accessible(self):
        return EC.presence_of_element_located((By.XPATH, self.teams_section_locator))

    def is_life_at_insider_section_accessible(self):
        return EC.presence_of_element_located((By.XPATH, self.life_at_insider_section_locator))


class QualityAssuranceCareersPage:
    def __init__(self, driver):
        self.browser = driver
        self.url = "https://useinsider.com/careers/quality-assurance/"
        self.see_all_jobs_locator = "//a[contains(text(), 'See all QA jobs')]"
        self.location_filter_xpath = "//label[@for='filter-by-location']"
        self.istanbul_option_xpath = "//span[@id='select2-filter-by-location-container']"
        self.qa_department_option_xpath = "//span[@id='select2-filter-by-department-container']"
        self.view_role_button_xpath = "//section[@id='career-position-list']"
        self.job_listing_class_name = "job-item"

    def navigate_to_qa_careers_page(self):
        self.browser.get(self.url)
        time.sleep(5)

    def click_see_all_qa_jobs(self):
        qa_jobs = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.see_all_jobs_locator))
        )
        qa_jobs.click()
        time.sleep(8)

    def filter_jobs_by_location_and_department(self):
        istanbul_option = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.istanbul_option_xpath))
        )
        istanbul_option.click()

        department_filter = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.location_filter_xpath))  # Corrected attribute name
        )
        department_filter.click()

        qa_department_option = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.qa_department_option_xpath))
        )
        qa_department_option.click()

    def check_job_listings(self):
        job_listings = self.browser.find_elements(By.CLASS_NAME, self.job_listing_class_name)
        for job in job_listings:
            position = job.find_element(By.CLASS_NAME, "Quality Assurance").text
            location = job.find_element(By.CLASS_NAME, "İstanbul,Turkey").text
            if "Quality Assurance" not in position or "Quality Assurance" not in department or "İstanbul, Türkiye" not in location:
                print("Error: Job listing does not meet the criteria.")

    def click_view_role_button(self):
        view_role_button_xpath = "//section[@id='career-position-list']"
        view_role_button = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.view_role_button_xpath))  # Corrected attribute name
        )
        view_role_button.click()


if __name__ == "__main__":
    browser = webdriver.Chrome()
    insider_homepage = InsiderHomePage(browser)
    insider_homepage.navigate_to_homepage()
    insider_homepage.navigate_to_careers_page()

    if insider_homepage.is_locations_section_accessible() and insider_homepage.is_teams_section_accessible() and insider_homepage.is_life_at_insider_section_accessible():
        print("Locations, Teams, and Life at Insider sections are accessible.")
    else:
        print("Error: Partitions are not accessible.")

    qa_careers_page = QualityAssuranceCareersPage(browser)
    qa_careers_page.navigate_to_qa_careers_page()
    qa_careers_page.click_see_all_qa_jobs()
    qa_careers_page.filter_jobs_by_location_and_department()
    qa_careers_page.check_job_listings()

    browser.quit()
