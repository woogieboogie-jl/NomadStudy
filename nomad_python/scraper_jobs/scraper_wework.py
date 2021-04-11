import requests
from bs4 import BeautifulSoup as bs

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


def collect_job_info(job_soup):
  #get title / company info
  title = job_soup.select_one("span.title").string
  company = job_soup.select_one("span.company").string
  
  #get region + exceptions
  try:
    region = job_soup.select_one("span.region").get_text(strip=True)
  except Exception:
    region = None
  
  #get application links and detail links per job
  link_detail = job_soup.select_one("a", recursive=False)["href"]
  link_detail = f"https://weworkremotely.com{link_detail}"

  #request to receive application & detail inofs
  soup = bs(requests.get(link_detail, headers=headers).text, 'html.parser')
  link_application = soup.find("a",{"id":"job-cta-alt-2"})

  #get application links + exceptions
  try:
    link_application = link_application["href"]
  except Exception:
    link_application = None
  
  return {
    "title":title, 
    "company":company, 
    "region":region, 
    "link_detail":link_detail, 
    "link_application":link_application
    }


def collect_jobs(url):
  print("collecting data from weworkremotely")
  jobs_detail = []
  soup = bs(requests.get(url, headers=headers).text, 'html.parser')
  jobs_list = soup.select("li.feature")
  for idx, job_soup in enumerate(jobs_list):
    job_detail = collect_job_info(job_soup)
    jobs_detail.append(job_detail)
  return jobs_detail


def collect_jobs_wework(word):
  URL= f"https://weworkremotely.com/remote-jobs/search?term={word}+developer"
  jobs_detail = collect_jobs(URL)
  return jobs_detail
