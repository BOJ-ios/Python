from kr_indeed import extract_indeed_jobs
from wwr import extract_wwr_jobs
from file import save_to_file

keyword = input("키워드 입력 : ")
indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = indeed + wwr

save_to_file(keyword, jobs)
