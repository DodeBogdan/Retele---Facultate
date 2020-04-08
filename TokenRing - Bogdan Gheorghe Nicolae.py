class Token:
    istoric = []

    def __init__(self, ipSursa='0', ipDestinatie='0', mesajTrimis='None', ajunsLaDestinatie=False, liber=False,
                 istoric=[]):
        self.ipSursa = ipSursa
        self.ipDestinatie = ipDestinatie
        self.mesajTrimis = mesajTrimis
        self.ajunsLaDestinatie = ajunsLaDestinatie
        self.liber = liber
        self.istoric = istoric

    def setIpSursa(self, ipSursa):
        self.ipSursa = ipSursa

    def setIpDestinatie(self, ipDestinatie):
        self.ipDestinatie = ipDestinatie

    def setMesajTrimis(self, mesajTrimis):
        self.mesajTrimis = mesajTrimis

    def setAjunsLaDestinatie(self):
        if (self.ajunsLaDestinatie == False):
            self.ajunsLaDestinatie = True
        else:
            self.ajunsLaDestinatie = False

    def setLiber(self):
        if (self.liber == False):
            self.liber = True
        else:
            self.liber = False

    def addIstoric(self, ip):
        self.istoric.append(ip)

    def __str__(self):
        return ('IPSursa: ' + self.ipSursa
                + '\nIPDestinatie: ' + self.ipDestinatie
                + "\nMesaj Trimis: " + self.mesajTrimis
                + "\nA ajuns la destinatie: " + str(self.ajunsLaDestinatie)
                + "\nLiber: " + str(self.liber)
                + "\nIstoric: " + str(self.istoric))

    def removeAll(self):
        self.ipSursa = '-'
        self.ipDestinatie = '-'
        self.mesajTrimis = '-'
        self.ajunsLaDestinatie = False
        self.liber = True
        self.istoric = []


def ceasornic(token, list, startPoint):
    while token.liber is False:

        if startPoint == len(list):
            startPoint = 0

        if token.ipDestinatie != list[startPoint]:
            token.addIstoric(list[startPoint])
        else:
            print("Mesajul trimis este: ", token.mesajTrimis)
            print()
            token.setAjunsLaDestinatie()
            token.addIstoric(list[startPoint])

        if token.ajunsLaDestinatie == True and token.ipSursa == list[startPoint]:
            token.setLiber()
            token.removeAll()

        print('Calculatorul:', str(list[startPoint][-1]))
        print(token)
        print()
        startPoint = startPoint + 1


def invers(token, list, startPoint):
    while token.liber is False:

        if startPoint == -1:
            startPoint = len(list) - 1

        if token.ipDestinatie != list[startPoint]:
            token.addIstoric(list[startPoint])
        else:
            print("Mesajul trimis este: ", token.mesajTrimis)
            print()
            token.setAjunsLaDestinatie()
            token.addIstoric(list[startPoint])

        if token.ajunsLaDestinatie == True and token.ipSursa == list[startPoint]:
            token.setLiber()
            token.removeAll()

        print('Calculatorul:', str(list[startPoint][-1]))
        print(token)
        print()
        startPoint = startPoint - 1

ip = '192.168.0.'

print("Cate calculatoare sa fie introduse?")
numbersOfPC = int(input())

listOfPC = []

for index in range(0,numbersOfPC):
    newIp = ip + str(index+1)
    listOfPC.append(newIp)

print(listOfPC)

print("De la ce calculator sa inceapa?")
ipSursa = int(input())

print("La ce calculator sa ajunga?")
ipDestinatie = int(input())

if ipSursa == ipDestinatie or ipSursa > numbersOfPC or ipDestinatie > numbersOfPC or ipSursa < 1 or ipDestinatie < 1:
    print("S-a introdus un ip invalid!")
    sys.exit(0)

print("Ce mesaj sa se trimita?")
mesaj = input()

ipSursa, ipDestinatie = ipSursa-1, ipDestinatie-1

token = Token(ipSursa = listOfPC[ipSursa], ipDestinatie= listOfPC[ipDestinatie], mesajTrimis= mesaj)

print("In ce sens sa mearga?\n1.Ceasornic.\n-1.Invers.\n")
mers = int(input())

if mers == 1:
    ceasornic(token,listOfPC, ipSursa)
else:
    invers(token,listOfPC, ipSursa)