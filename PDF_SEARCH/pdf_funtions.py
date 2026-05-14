from math import e
import time
from turtle import pd
import Levenshtein
import requests
from bs4 import BeautifulSoup
import os
from markitdown import MarkItDown


#OCR para python
#descargar libreria que convierta las imagenes a tecto
class pdf_document:
    """Class to represent a PDF document with its URL, pdf path, markdown path filename"""
    def __init__(self, url, pdf_path, markdown_path):
        self.url = url
        self.pdf_path = pdf_path
        self.markdown_path = markdown_path
        self.content = None
        self.convert_pdf_to_markdown() #convierte el pdf a markdown al crear el objeto

    def convert_pdf_to_markdown(self):
            """Converts a PDF file to Markdown format using MarkItDown."""
            try:
                converter = MarkItDown()
                result = converter.convert(self.pdf_path)
                markdown_content = result.markdown or result.text_content
                with open(self.markdown_path, 'w', encoding='utf-8') as f:
                    f.write(markdown_content)
                    self.content = markdown_content #salva en el objeto el contenido de markdown
            except Exception as e:
                print(f"Error converting PDF to Markdown: {e}")

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

def get_pdfs(url = "https://fi-ing.unison.mx/acuerdos-de-sesiones-del-h-colegio-de-la-facultad-interdisciplinaria-de-ingenieria-2026/"):
    url = "https://fi-ing.unison.mx/acuerdos-de-sesiones-del-h-colegio-de-la-facultad-interdisciplinaria-de-ingenieria-2026/"
    html = get_webpage(url)
    download_path = "downloaded_pdfs"
    markdown_path = "markdown_files"
    if not os.path.exists(download_path):
        # Create the directory if it doesn't exist
        os.makedirs(download_path)
    if not os.path.exists(markdown_path):
        os.makedirs(markdown_path)
    html = get_webpage(url) #obtener html de la pagina
    if not html:
        print(f"Failed to retrieve the webpage. {url}")
        exit(1)
    pdf_links = extract_pdf_links(html) #extraer los links de los pdfs del html
    pdf_dict = {}#diccionario para guardar los objetos pdf_document con su url como clave

    for link in pdf_links:
        print(link) #ver que url se descargan
        filename = link.split('/')[-1]
        download_file = os.path.join(download_path, filename)
        download_pdf(link, f"{download_file}")
        markdown_file = os.path.join(markdown_path, f"{os.path.splitext(filename)[0]}.md")
        pdf_doc = pdf_document(link, download_file, markdown_file) #crear un objeto pdf_document con la url, ruta del pdf descargado y ruta del markdown a crear
        pdf_dict[filename] = pdf_doc
        pdf_dict[filename] = markdown_file
       
        print(f"Downloaded:  {download_file}") 

        return pdf_dict #regresa el diccionario con los nombres de los archivos pdf y markdown   


    
    
def main ():
    """Main function to orchestrate the PDF downloading process."""
    pdf_diccionary = get_pdfs()
    print(pdf_diccionary.keys())
    main_diccionary = {}
    for key, pdf_doc in pdf_diccionary.items():
        content = pdf_doc.content
        #split the content into 3 words chunks
        chunk_length = 20
        chunks = [content[i:i+chunk_length] for i in range(0, len(content), chunk_length)]
        for chunk in chunks:
            if chunk not in main_diccionary:
                main_diccionary[chunk] = [key]
            else:
                main_diccionary[chunk].append(key)
    print(main_diccionary.keys())


#queremos que nos traiga el url del documento que tiene 
def buscar_palabras_ratio(frases:list, frase_a_buscar:str, umbral:float=0.50)->list:
    """ Busca una frase en una lista de frases """
    frases_encontradas = []
    frase_a_buscar = frase_a_buscar.lower()
    for frase in frases:
        frase_lower = frase.frase.lower()
        ratio = Levenshtein.ratio(frase_lower, frase_a_buscar)
        if ratio >=umbral:
            frase.ratio = ratio
            frases_encontradas.append(frase)
    return frases_encontradas

    
if __name__ == "__main__":
    main()