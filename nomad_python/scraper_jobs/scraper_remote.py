import requests
from bs4 import BeautifulSoup as bs

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def collect_job_info(job_soup):
  title = job_soup.select_one("h2", {"itemprop":"title"}).get_text(strip=True)
  company = job_soup.select_one("h3", {"itemprop":"name"}).get_text(strip=True)
  region = job_soup.select_one("div.location")

  try:
    region.get_text(strip=True)
  except Exception:
    region = None
  
  link_detail = job_soup["data-id"]
  link_detail = f"https://remoteok.io/remote-jobs/{link_detail}"
  soup = bs(requests.get(link_detail, headers=headers).text, 'html.parser')
  link_application = soup.select_one("a.action-apply")

  try:
    link_application = link_application["href"]
  except:
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
  soup = bs(requests.get(url,headers=headers).text,"html.parser")
  jobs_list = soup.select("tr.job:not(.closed)")
  for job_soup in jobs_list:
    job_detail = collect_job_info(job_soup)
    jobs_detail.append(job_detail)
  return jobs_detail



def collect_jobs_remote(word):
  URL= f"https://remoteok.io/remote-dev+{word}-jobs"
  jobs = collect_jobs(URL)
  return jobs
