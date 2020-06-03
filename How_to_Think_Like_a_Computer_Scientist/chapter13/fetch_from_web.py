import urllib.request

url = "https://xml2rfc.tools.ietf.org/public/rfc/xml/rfc2441.xml"
destination_filename = "rfc2441.xml"

urllib.request.urlretrieve(url, destination_filename)
