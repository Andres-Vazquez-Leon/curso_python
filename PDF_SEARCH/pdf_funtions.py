import time
from turtle import pd
import requests
from bs4 import BeautifulSoup
import os


def get_webpage(url):
    """Fetches the content of a webpage given its URL."""
    try: 
        response = requests.get(url, timeout=10)  
        response.raise_for_status() # check if the request was successful
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None
    
def extract_pdf_links(html):
    """Parses the HTML content and extracts all PDF links."""
    soup = BeautifulSoup(html, 'html.parser')
    pdf_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.endswith('.pdf'):
            pdf_links.append(href)
    return pdf_links

def download_pdf(url, filename):
    """Downloads a PDF from a given URL and saves it with the specified filename."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            f.write(response.content)
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the PDF: {e}")

    
if __name__ == "__main__":
    url = "https://fi-ing.unison.mx/acuerdos-de-sesiones-del-h-colegio-de-la-facultad-interdisciplinaria-de-ingenieria-2026/"
    html = get_webpage(url)
    if not html:
        print("Failed to retrieve the webpage.")
        exit(1)
    pdf_links = extract_pdf_links(html)
    for link in pdf_links:
        print(link)
        filename = link.split('/')[-1]
        download_pdf(link, f"pdf_{filename}")
        print(f"Downloaded: {filename}")