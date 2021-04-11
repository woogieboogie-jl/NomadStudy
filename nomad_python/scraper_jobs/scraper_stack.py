import requests
from bs4 import BeautifulSoup as bs

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def collect_last_page(url):
  soup = bs(requests.get(url, headers=headers).text, 'html.parser')
  pagination = soup.select_one("div.s-pagination")
  
  if pagination:
    last_page = pagination.select("a")
    last_page = int(last_page[-2].select_one("span").string)
  else:
    last_page = -1
  
  return last_page


def collect_job_info(job_soup):
  title = job_soup.select_one("a.s-link")["title"]
  region = job_soup.select_one("h3.fc-black-700").select("span")
  company = region[0].get_text(strip=True)
  
  try:
    region = region[1].get_text(strip=True)
  except Exception:
    region = None

  id = job_soup["data-jobid"]
  link_detail = f"https://stackoverflow.com/jobs/{id}"
  link_application = f"https://stackoverflow.com/jobs/apply/{id}"
  
  return {
    "title":title, 
    "company":company, 
    "region":region, 
    "link_detail":link_detail, 
    "link_application":link_application
    }
  

def collect_jobs(url, last_page):
  print("collecting data from stackoverflow")
  jobs_detail = []
  for page in range(last_page):
    print(f"page {page+1}")
    soup = bs(requests.get(f"{url}&pg={page+1}", headers=headers).text, 'html.parser')
    jobs_list = soup.select("div.-job")
    for job_soup in jobs_list:
      job_detail = collect_job_info(job_soup)
      jobs_detail.append(job_detail)
  return jobs_detail


def collect_jobs_stack(word):
  URL= f"https://stackoverflow.com/jobs?r=true&q={word}"
  last_page = collect_last_page(URL)
  if last_page != -1:
    jobs = collect_jobs(URL, last_page)
  else:
    jobs = []
  return jobs
