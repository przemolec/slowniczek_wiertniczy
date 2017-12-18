import json, collections

slownikDict = collections.OrderedDict(json.load(open(plik_zrodlowy,"r")))

def translate(slowo):
    return slownikDict[slowo]
slowo = input("Podaj słowo: ")

print(translate(slowo))
