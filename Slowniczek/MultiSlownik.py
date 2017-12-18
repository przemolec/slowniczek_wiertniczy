import re, json, collections
from difflib import SequenceMatcher, get_close_matches

def contentMaker(baza):
    with open(baza,'r') as plik:
        data = plik.readlines()
    #ordereddict.sorted slownik = collections.OrderedDict()
    slownik ={}
    v = ''
    k = ''
    for line in data:
        if re.search(r"\|",line):
            k,v = re.split(r"\|",line,1) #re.sub(r'\([^)]*\)', '', s)
            try:
                wymowa =''
                wymowa = re.search(r"\([^=)]*\)", k).group(0)
            except: pass
            k = re.sub(r" \([^)]*\)",'',k) #czy mozna ten dziwny ciag zastapic "wymowa"?
            v = wymowa + v
        slownik[k] = v
    json.dump(slownik,open("slownik.json",'w'))
    return slownik

def dataLoader(plik_zrodlowy="slownik.json"):
    plik_zrodlowy = str(input("Wskaż plik słownika (enter uruchamia standardowy słownik): "))
    if plik_zrodlowy == "": plik_zrodlowy = "slownik.json"
    slownikDict = collections.OrderedDict(json.load(open(plik_zrodlowy,"r")))
    return slownikDict

def translate(slownikDict): #TODO wykrywanie błędów w pisowni, dopasowanie nawet gdy definicja zawiera cos w nawiasie
    slowo = str(input("Podaj słowo: ")).lower()
    if slowo in slownikDict:
        return slownikDict[slowo]
    else:
        closeMatches = get_close_matches(slowo, slownikDict.keys())
        if (len(closeMatches)) < 1: return "Brak słowa w bazie."
        print("Czy chodziło Ci o: ")
        for i in range(len(closeMatches)):
            print(i+1,': ',closeMatches[i])
        try:
            wybranynr = input("Jeśli tak, podaj numer i zatwierdź enter\nW przeciwnym razie kliknij enter\n")
            if wybranynr == '':
                return "Pa!"
            else:
                wybranynr = int(wybranynr)
        except:
            return "Błędny wybór"
        if type(wybranynr) == int and wybranynr in range(1,4):
            return slownikDict[closeMatches[wybranynr-1]]
        else:
            return "Błędny wybór."
        #TODO: wyszukiwanie możliwych opcji, podanie kilku z nich do wyboru na zasadzie
        # 1,2,3 wybierz numer
        #wyszukiwanie, najpierw przeszukiwanie początków kluczy, później środka klucza,
        #albo od rzu policzyc similarity
        #a jak będę wiedział jak, to też poprawianie literówek

print(translate(dataLoader("slownik.json")))
