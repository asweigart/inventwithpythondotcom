var sourceCodes = {"witze": "print(\'Warum sind Geisterfahrer die freundlichsten Menschen?\')\r\ninput()\r\nprint(\'Weil sie so entgegenkommend sind!\')\r\nprint()\r\nprint(\'Was ist der Unterschied zwischen einem B\u00E4cker und einem Teppich?\')\r\ninput()\r\nprint(\'Der B\u00E4cker muss morgens um 4 aufstehen. Der Teppich kann liegen bleiben.\')\r\nprint()\r\nprint(\'Klopf, klopf.\')\r\ninput()\r\nprint(\"Wer da?\")\r\ninput()\r\nprint(\'Anna!\')\r\ninput()\r\nprint(\'Anna wer?\')\r\ninput()\r\nprint(\'An\\\'na T\u00FCr hat wer geklingelt\', end=\'\')\r\nprint(\'-HAHA!\')\r\n",
    "zahlenRaten": "# Das ist ein Zahlenratespiel.\r\nimport random\r\n\r\nabgegebenTipps = 0\r\n\r\nprint(\'Hallo! Was ist dein Name?\')\r\nmeinName = input()\r\n\r\nzahl = random.randint(1, 20)\r\nprint(\'Also, \' + meinName + \', ich denke an eine Zahl zwischen 1 und 20.\')\r\n\r\nwhile abgegebenTipps < 6:\r\n    print(\'Los, rate.\') # Vor print sind vier Leerzeichen.\r\n    tipp = input()\r\n    tipp = int(tipp)\r\n\r\n    abgegebenTipps = abgegebenTipps + 1\r\n\r\n    if tipp < zahl:\r\n        print(\'Dein Tipp ist zu niedrig.\') # Hier sind acht Leerzeichen vor print.\r\n\r\n    if tipp > zahl:\r\n        print(\'Dein Tipp ist zu hoch.\')\r\n\r\n    if tipp == zahl:\r\n        break\r\n\r\nif tipp == zahl:\r\n    abgegebenTipps = str(abgegebenTipps)\r\n    print(\'Gut gemacht, \' + meinName + \'! Du hast meine Zahl in \' + abgegebenTipps + \' Z\u00FCgen erraten!\')\r\n\r\nif tipp != zahl:\r\n    zahl = str(zahl)\r\n    print(\'Nene. Die Nummer an die ich gedacht habe war \' + zahl)\r\n",
    "drachen": "import random\r\nimport time\r\n\r\ndef zeigeEinfuehrungAn():\r\n    print(\'Du bist ein einem Land voller Drachen. Vor Dir\')\r\n    print(\'siehst Du zwei H\u00F6hlen. In einer H\u00F6hle haust ein freundlicher Drache,\')\r\n    print(\'der seine Sch\u00E4tze mit Dir teilt. Der andere Drache\')\r\n    print(\'ist gierig und hungrig, und wird Dich bei Sichtkontakt auffressen.\')\r\n    print()\r\n\r\ndef sucheHoehleAus():\r\n    hoehle = \'\'\r\n    while hoehle != \'1\' and hoehle != \'2\':\r\n        print(\'In welche H\u00F6hle wirst Du gehen? (1 oder 2)\')\r\n        hoehle = input()\r\n\r\n    return hoehle\r\n\r\ndef ueberpruefeHoehle(ausgewaehlteHoehle):\r\n    print(\'Du n\u00E4herst Dich der H\u00F6hle...\')\r\n    time.sleep(2)\r\n    print(\'Es ist dunkel und gruselig...\')\r\n    time.sleep(2)\r\n    print(\'Ein gro\u00DFer Drache springt vor Deine F\u00FC\u00DFe! Er \u00F6ffnet sein Maul und...\')\r\n    print()\r\n    time.sleep(2)\r\n\r\n    freundlicheHoehle = random.randint(1, 2)\r\n\r\n    if ausgewaehlteHoehle == str(freundlicheHoehle):\r\n         print(\'Gibt Dir seinen Schatz!\')\r\n    else:\r\n         print(\'Verschlingt Dich in einem Mal!\')\r\n\r\nspieleNochEinmal = \'ja\'\r\nwhile spieleNochEinmal == \'ja\' or spieleNochEinmal == \'j\':\r\n\r\n    zeigeEinfuehrungAn()\r\n\r\n    hoehlenNummer = sucheHoehleAus()\r\n\r\n    ueberpruefeHoehle(hoehlenNummer)\r\n\r\n    print(\'M\u00F6chtest Du noch einmal spielen? (ja oder nein)\')\r\n    spieleNochEinmal = input()\r\n",
    "galgenmann": "import random\r\nGALGENMANNBILDER = [\'\'\'\r\n\r\n  +---+\r\n  |   |\r\n      |\r\n      |\r\n      |\r\n      |\r\n=========\'\'\', \'\'\'\r\n\r\n  +---+\r\n  |   |\r\n  O   |\r\n      |\r\n      |\r\n      |\r\n=========\'\'\', \'\'\'\r\n\r\n  +---+\r\n  |   |\r\n  O   |\r\n  |   |\r\n      |\r\n      |\r\n=========\'\'\', \'\'\'\r\n\r\n  +---+\r\n  |   |\r\n  O   |\r\n \/|   |\r\n      |\r\n      |\r\n=========\'\'\', \'\'\'\r\n\r\n  +---+\r\n  |   |\r\n  O   |\r\n \/|\\  |\r\n      |\r\n      |\r\n=========\'\'\', \'\'\'\r\n\r\n  +---+\r\n  |   |\r\n  O   |\r\n \/|\\  |\r\n \/    |\r\n      |\r\n=========\'\'\', \'\'\'\r\n\r\n  +---+\r\n  |   |\r\n  O   |\r\n \/|\\  |\r\n \/ \\  |\r\n      |\r\n=========\'\'\']\r\nworte = \'aal adler alligator ameise amsel b\u00E4r biber bussard cham\u00E4leon dachs delfin eichh\u00F6rnchen eidechse elch elefant faultier fledermaus fuchs gans gepard gorilla hai hamster hase hirsch huhn igel jaguar kamel k\u00E4nguru koala leopard libelle marienk\u00E4fer maulwurf meerschweinchen m\u00F6we nachtigal nilpferd panda pfau qualle ratte regenwurm schaf schimpanse schwan schwein strau\u00DF tausendf\u00FC\u00DFer tintenfisch wachtel wal wolf zebra ziege\'.split()\r\n\r\ndef zufallsWort(wortListe):\r\n    # Diese Funktion gibt eine zuf\u00E4llige Zeichenkette aus der \u00FCbergebenen Zeichenketten-Liste zur\u00FCck.\r\n    wortIndex = random.randint(0, len(wortListe) - 1)\r\n    return wortListe[wortIndex]\r\n\r\ndef zeigeSpielbrettAn(GALGENMANNBILDER, falscheBuchstaben, richtigeBuchstaben, geheimWort):\r\n    print(GALGENMANNBILDER[len(falscheBuchstaben)])\r\n    print()\r\n\r\n    print(\'Falsche Buchstaben:\', end=\' \')\r\n    for buchstabe in falscheBuchstaben:\r\n        print(buchstabe, end=\' \')\r\n    print()\r\n\r\n    luecken = \'_\' * len(geheimWort)\r\n\r\n    for i in range(len(geheimWort)): # Ersetze L\u00FCcken mit korrekt geratenen Buchstaben\r\n        if geheimWort[i] in richtigeBuchstaben:\r\n            luecken = luecken[:i] + geheimWort[i] + luecken[i+1:]\r\n\r\n    for buchstabe in luecken: # Zeige das Geheimwort mit Leerzeichen zwischen den Buchstaben\r\n        print(buchstabe, end=\' \')\r\n    print()\r\n\r\ndef rateBuchstabe(bereitsGeraten):\r\n    # Stellt sicher, dass der Spieler nur einen einzelnen Buchstaben eintippt und gibt ihn zur\u00FCck.\r\n    while True:\r\n        print(\'Rate einen Buchstaben.\')\r\n        eingabe = input()\r\n        eingabe = eingabe.lower()\r\n        if len(eingabe) != 1:\r\n            print(\'Bitte gib einen einzelnen Buchstaben ein.\')\r\n        elif eingabe in bereitsGeraten:\r\n            print(\'Du hast diesen Buchstaben bereits probiert. Rate noch einmal.\')\r\n        elif eingabe not in \'abcdefghijklmnopqrstuvwxyz\':\r\n            print(\'Bitte gib einen BUCHSTABEN ein.\')\r\n        else:\r\n            return eingabe\r\n\r\ndef spieleNochEinmal():\r\n    # Diese Funktion True zur\u00FCck, falls der Spieler noch einmal spielen m\u00F6chte, False sonst.\r\n    print(\'M\u00F6chtest Du noch einmal spielen? (ja oder nein)\')\r\n    return input().lower().startswith(\'j\')\r\n\r\n\r\nprint(\'G A L G E N M A N N\')\r\nfalscheBuchstaben = \'\'\r\nrichtigeBuchstaben = \'\'\r\ngeheimWort = zufallsWort(worte)\r\nspielIstBeendet = False\r\n\r\nwhile True:\r\n    zeigeSpielbrettAn(GALGENMANNBILDER, falscheBuchstaben, richtigeBuchstaben, geheimWort)\r\n\r\n    # Lass den Spieler einen Buchhstaben eingeben.\r\n    buchstabe = rateBuchstabe(falscheBuchstaben + richtigeBuchstaben)\r\n\r\n    if buchstabe in geheimWort:\r\n        richtigeBuchstaben = richtigeBuchstaben + buchstabe\r\n\r\n        # \u00DCberpr\u00FCfe, ob der Spieler gewonnen hat\r\n        alleBuchstabenGeraten = True\r\n        for i in range(len(geheimWort)):\r\n            if geheimWort[i] not in richtigeBuchstaben:\r\n                alleBuchstabenGeraten = False\r\n                break\r\n        if alleBuchstabenGeraten:\r\n            print(\'Ja! Das geheime Wort ist \"\' + geheimWort + \'\"! Du hast gewonnen!\')\r\n            spielIstBeendet = True\r\n    else:\r\n        falscheBuchstaben = falscheBuchstaben + buchstabe\r\n\r\n        # \u00DCberpr\u00FCfe, ob der Spieler zu viele Rateversuche verbraucht und damit verloren hat\r\n        if len(falscheBuchstaben) == len(GALGENMANNBILDER) - 1:\r\n            zeigeSpielbrettAn(GALGENMANNBILDER, falscheBuchstaben, richtigeBuchstaben, geheimWort)\r\n            print(\'Du hast zu viele Versuche gebraucht!\\nNach \' + str(len(falscheBuchstaben)) + \' falsch und \' + str(len(richtigeBuchstaben)) + \' richtig geratenen Buchstaben lautet das Wort \"\' + geheimWort + \'\"\')\r\n            spielIstBeendet = True\r\n\r\n    # Frage den Spieler, ob er noch einmal spielen m\u00F6chte (aber nur, wenn das Spiel zu Ende ist).\r\n    if spielIstBeendet:\r\n        if spieleNochEinmal():\r\n            falscheBuchstaben = \'\'\r\n            richtigeBuchstaben = \'\'\r\n            spielIstBeendet = False\r\n            geheimWort = zufallsWort(worte)\r\n        else:\r\n            break\r\n",
}