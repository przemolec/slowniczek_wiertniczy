import re, json

def contentMaker(baza):
    with open(baza,'r') as plik:
        data = plik.readlines()
    #ordereddict.sorted slownik = collections.OrderedDict()
    slownik ={}
    v = ''
    k=''
    for line in data:
        if re.search(r"\|",line):
            k,v = re.split(r"\|",line,1) #re.sub(r'\([^)]*\)', '', s)
            try:
                wymowa =''
                wymowa = re.search(r"\([^=)]*\)", k).group(0)
            except: pass
            k = re.sub(r" \([^)]*\)",'',k) #czy mozna ten dziwny ciag zastapic "wymowa"?
            if k[-1] == " ": k = k[:-1]
            v = wymowa + v
        slownik[k] = v
    json.dump(slownik,open("slownik.json",'w'))
    return slownik
contentMaker(input("Wskaż plik słownika: "))
