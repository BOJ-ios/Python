from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_page_count(keyword):
    options = webdriver.ChromeOptions()
    options.add_argument("disable-gpu")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(options=options)
    base_url = "https://kr.indeed.com/jobs?q="
    browser.get(f"{base_url}{keyword}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("nav", attrs={"aria-label": "pagination"})
    if (pagination == None):
        print("페이지 없음")
        return 1
    else:
        pages = pagination.select("div a")
        count = len(pages)
        print("총", count, "페이지")
        if (count >= 5):
            return 5
        else:
            return count


def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    results = []
    for page in range(pages):
        print(page+1, "페이지")
        options = webdriver.ChromeOptions()
        options.add_argument("disable-gpu")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        browser = webdriver.Chrome(options=options)
        base_url = "https://kr.indeed.com/jobs"
        browser.get(f"{base_url}?q={keyword}&start={page*10}")
        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find('ul', class_="jobsearch-ResultsList")
        if (job_list == None):
            return results
        else:
            jobs = job_list.find_all('li', recursive=False)
            for job in jobs:
                zone = job.find('div', class_="mosaic-zone")
                if (zone == None):
                    anchor = job.select_one("h2 a")
                    title = anchor['aria-label']
                    link = anchor['href']
                    company = job.find('span', class_="companyName")
                    location = job.find('div', class_="companyLocation")
                    job_data = {
                        'company': company.string.replace(",", " "),
                        'title': title.replace(",", " "),
                        'location': location.string.replace(",", " "),
                        'link': f"https://kr.indeed.com{link}"
                    }
                    results.append(job_data)
    return results
