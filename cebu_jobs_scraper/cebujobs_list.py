"""
"""

import requests
from bs4 import BeautifulSoup

def scrape_job_listing(site_url):
	"""
	Sample Usage: scrape_job_listing('http://www.cebujobs.ph/')
	"""
	response = requests.get(site_url)

	soup = BeautifulSoup(response.text, "html.parser")
	titles = soup.select('.jobpost a')

	result = []
	for title in titles:
		result.append({'position': title.text, 'url': title['href']})

	return result

