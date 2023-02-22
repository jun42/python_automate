#! python3 
# mapIt.py

import webbrowser, sys,pyperclip
if len(sys.argv) > 1:
    #명령 행에서 주소를 받는다. 
    print(sys.argv)
    address = ' '.join(sys.argv[1:])

else: 
    #take address from clipboard
    address = pyperclip.paste()


webbrowser.open('https://www.google.com/maps/place/'+ address)
