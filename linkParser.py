import requests
from bs4 import BeautifulSoup as BS


def parse_link(link):
    r = requests.get(link)
    soup = BS(r.text, "html.parser")
    el = soup.find_all('script', id='__NEXT_DATA__')
    s = str(el[0])
    s = s[51:-8]
    start_id = int(s[43:].find('"Snippet"'))
    code = s[start_id+54:]
    end_id = code.find('","Slug"')
    code = code[:end_id]
    code = code.replace("\\u003e", '>')
    code = code.replace('\\u0026', '&')
    code = code.replace("\\r", "")
    code = code.replace("\\t", "")
    code = code.replace("\\u003c", '<')
    code = code.replace("\\n", """
    """)
    return code
