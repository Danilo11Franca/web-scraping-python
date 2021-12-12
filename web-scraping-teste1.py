from bs4 import BeautifulSoup
import requests

url = 'https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss'
# requisição feita ao site
req = requests.get(url)
# html da página
soup = BeautifulSoup(req.content, 'html.parser')
# elemento que contém a url para a versão mais recente do Padrão TISS
newer_version_url = soup.find_all("a", class_="alert-link internal-link")[0]["href"]

# requisição feita à página com os arquivos
new_req = requests.get(newer_version_url)
# html da página
soup = BeautifulSoup(new_req.content, 'html.parser')
# elemento que contém a url do arquivo
file_url = soup.find_all("a", class_="btn btn-primary btn-sm center-block internal-link")[0]["href"]

# download do arquivo
file_req = requests.get(file_url)
# nome do arquivo
file_name = file_url[str(file_url).find("padrao-tiss_componente-organizacional"):]
open(file_name, 'wb').write(file_req.content)