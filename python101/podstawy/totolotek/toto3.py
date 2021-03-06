#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from totomodul import ustawienia, losujliczby, pobierztypy, wyniki
from totomodul import czytaj_json, zapisz_json
from totomodul import zapisz_str
import time


def main(args):
    # ustawienia gry
    nick, ileliczb, maksliczba, ilerazy = ustawienia()

    # losujemy liczby
    liczby = losujliczby(ileliczb, maksliczba)

    # pobieramy typy użytkownika i sprawdzamy, ile liczb trafił
    for i in range(ilerazy):
        typy = pobierztypy(ileliczb, maksliczba)
        iletraf = wyniki(set(liczby), typy)
        wylosowane = list(set(liczby) & typy)


    nazwapliku = nick + ".json"  # nazwa pliku z historią losowań
    losowania = czytaj_json(nazwapliku)
    #losowania = []

    losowania.append({
        "czas": time.time(),
        "dane": (ileliczb, maksliczba),
        "wylosowane": liczby,
        "ile": iletraf
    })

    zapisz_json(nazwapliku, losowania)

    losowania = []
    losowania.append({
        "wylosowane": wylosowane,
        "dane": (ileliczb, maksliczba),
        "ile": iletraf,
        "czas": time.time()
    })

    zapisz_str(nick+".str", losowania)

    print("\nLosowania:", liczby)
    return 0




if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
