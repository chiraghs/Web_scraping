import webbrowser,sys,pyperclip
sys.argv

if len(sys.argv>1):
    address=' '.join(sys.argv[1:0])

else:
    address=pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)    