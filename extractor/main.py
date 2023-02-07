from kr_indeed import extract_indeed_jobs
from wwr import extract_wwr_jobs

keyword = input("키워드 입력 : ")
indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)

file = open(f"{keyword}.csv", "w", encoding="utf-8")
file.write("company, title, location, link\n")

jobs = indeed + wwr
for job in jobs:
    file.write(
        f"{job['company']},{job['title']},{job['location']},{job['link']}\n")
file.close()
