# MasterMind_full
MasterMind full game

README for MasterMind_Full

1. In MASTERMIND_RANDOM.py vindt u de desbetreffende code voor de oplissing van het eerste algoritme uit het artikel van de Groningse Universiteit.
2. In MASTERMIND_WORSTCASE.py vindt u de desbetreffende code voor de oplossing van het tweede genoemde algoritme uit het artikel van de Groningse Universiteit.
3. In MASTERMIND_FULL.py vindt u de desbetreffende code voor het zelf verzonnen algoritme volgens de opdracht.
4. In MASTERMIND_pseudocode.py vindt u de pseudecode die van te voren ingeleverd moest worden en waar feedback op verkregen is.

OPBOUW CODE MASTERMIND_RANDOM.py:

De code is zodanig opgebouw dat er bij elke variant van te voren gevraagd wordt of de gebruiker zelf de geheime code wilt verzinnen of dat hij/zij dit overlaat aan de computer.
Wanneer de keuze is gemaakt om de computer een code te laten verzinnen start de mastermind game. Deze is gebaseerd op de code van: ###https://www.daniweb.com/programming/software-development/threads/192328/mastermind-game.
Waneer de keuze is gemaakt om zelf een code te verzinnen, wordt in het geval van MASTERMIND_RANDOM.py gevraagd om een input in de vorm van: rgbo. 
Zodra de code is bedacht gaat de computer aan de slag, en vraagt de computer om feedback. Dit gaat door tot de code is gekraakt.

OPBOUW CODE MASTERMIND_WORSTCASE.py:

De code is zodanig opgebouw dat er bij elke variant van te voren gevraagd wordt of de gebruiker zelf de geheime code wilt verzinnen of dat hij/zij dit overlaat aan de computer.
Wanneer de keuze is gemaakt om de computer een code te laten verzinnen start de mastermind game. Deze is gebaseerd op de code van: https://www.daniweb.com/programming/software-development/threads/192328/mastermind-game.
Waneer de keuze is gemaakt om zelf een code te verzinnen, wordt in het geval van MASTERMIND_WORSTCASE.py door de computer een code verzonnen op numerieke basis.
Rood = 1, Groen = 2, etc. Zodra deze bedacht is gaat de computer meteen aan de slag en wordt in gemiddeld 5 stappen de code geraden. Deze code is gebaseerd op: https://stackoverflow.com/questions/33240666/word-guessing-game-what-algorithm-to-use

OPBOUW CODE MASTERMIND_SELF.py:

De code is zodanig opgebouw dat er bij elke variant van te voren gevraagd wordt of de gebruiker zelf de geheime code wilt verzinnen of dat hij/zij dit overlaat aan de computer.
Wanneer de keuze is gemaakt om de computer een code te laten verzinnen start de mastermind game. Deze is gebaseerd op de code van: https://www.daniweb.com/programming/software-development/threads/192328/mastermind-game.
Waneer de keuze is gemaakt om zelf een code te verzinnen, wordt in het geval van MASTERMIND_RANDOM.py gevraagd om een input in de vorm van: rgbo. 
De computer zal om te beginnnen een random gok doen. Vervolgens wordt er om feedback gevraagd voor de zwarte pinnen (kleuren op de goede plaats).
Door gebruik te maken van de feedback selecteert het algoritme, op basis van de hoeveelheid, een x aantal letters (kleuren) uit de vorige random gegenereerde code.
Wanneer dit er bijv. 2 zijn worden er 2 random kleuren uit de code gepakt (bijv. r, g) en worden er nog 2 random kleuren toegevoegd uit de lijst met mogelijke opties.
zodoende zal het algirtme uiteindelijke de goede code kunnen vinden.
