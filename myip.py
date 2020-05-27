#!/usr/bin/env python3

import urllib.request

def retrive_page(url):
    """ Retrieve the contents of a web page.
        The contents is converted to a string before returning it.
    """
    my_socket = urllib.request.urlopen(url)
    dta = str(my_socket.readall())
    my_socket.close()
    return dta

ip_text = retrive_page("https://api.myip.com")
print(ip_text)
