from bs4 import BeautifulSoup
import os
import requests
import time
import random

# Pull data from wget

try:
    # Directory to save PDF files
    pdf_dir = 'loi'
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)

    # Iterate across all pages of results, fill in page number in the URL. Start at 0 and go to 100
    min_page = 0
    max_page = 100
    for page_num in range(min_page, max_page):
        # Format the URL with the page number
        request = "https://www.faa.gov/about/office_org/headquarters_offices/agc/practice_areas/regulations/interpretations?search_api_fulltext=cfr&page={}".format(page_num)


        # Use Requests to get the page source and parse with BeautifulSoup
        with requests.Session() as session:
            request = session.get(request)
            soup = BeautifulSoup(request.content, 'html.parser')

            # Find all PDF links
            pdf_links = soup.find_all('a', href=True)

            for link in pdf_links:
                if link['href'].endswith('.pdf'):
                    pdf_url = link['href']
                    pdf_response = requests.get("https://www.faa.gov" + pdf_url)
                    filename = pdf_url.split('/')[-1]

                    # Save PDF to a file
                    with open(os.path.join(pdf_dir, filename), 'wb') as f:
                        f.write(pdf_response.content)
                
                    # Sleep for a random amount of time between 1 and 2 seconds
                    time.sleep(1 + random.random())
finally:
    pass
