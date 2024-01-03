

from atlassian import Confluence

import os
import requests
import json
import base64


headers = {
    'Accept': 'application/json',
    'Authorization': "Basic" + base64.b64encode('erik:ATATT3xFfGF0ey6nWDI_x9ZATCPtvKtA6fnS4YzWnYc5e1STsS1rWiymYCAXbDeB42VlcLy8eaFaYo52YfRSwHC79mcINL6tt68k'.encode("ascii")).decode("ascii")
}

def test_auth():
  confluence = Confluence(
      url='https://clearfunction.atlassian.net/',
      username='erik@clearfunction.com',
      password='ATATT3xFfGF0ey6nWDI_x9ZATCPtvKtA6fnS4YzWnYc5e1STsS1rWiymYCAXbDeB42VlcLy8eaFaYo52YfRSwHC79mcINL6tt68k',
      cloud=True)

  result =confluence.page_exists('Erik Scofield', 'hamburger', type=None)
  print(result)


def test_auth2():
  searchText = "how*"
  url = "https://clearfunction.atlassian.net/wiki/rest/api/search?expand=content.version&cql=title=" + searchText

  response = requests.request(
      "GET",
      url,
      headers=headers
  )

  print(response)

  print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
  
  
if __name__ == '__main__':
  test_auth2()
