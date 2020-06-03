import urllib.request

def retrieve_page(url):
    """ Retrieve the contents of a web page.
        The contents is converted to a string before returning it.
    """
    my_socket = urllib.request.urlopen(url)
    dta = str(my_socket.read())
    my_socket.close()
    return dta

the_text = retrieve_page("https://api.myip.com/")
print(the_text)
