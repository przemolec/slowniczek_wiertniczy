import json, collections
def dataLoader():
    plik_zrodlowy = str(input("Wskaż plik słownika: "))
    slownikDict = collections.OrderedDict(json.load(open(plik_zrodlowy,"r")))
    return slownikDict
