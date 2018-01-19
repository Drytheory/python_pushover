# python_pushover


Viel Spaß mit der Datei.
Einfach und schnell mit Python Pushnachrichten über den Service Pushover ans Smartphone oder Tablet senden.


# Wie funktioniert es?

Ihr habt die Datei push.py, in dieser werden alle Variablen die übergeben werden definiert.
Ich könnt euch alle möglichen Variablen zur Übermittlung auf https://pushover.net/api sehen.
Passt die Datei erstmal so an, wie ihr sie haben möchtet.

Um einfach sofort Pushnachrichten zu senden, fügt einfach euren User-Key in die Datei ein.

```python
#Hier den User Key eintragen
user_token = 'User-Key'
```

Wenn ihr jetzt ein Projekt habt, in dem ihr Pushnachrichten verwenden wollt. Schiebt erstmal die datei <push.py> in den Ordner eures Projekts.

Anschließend müsst ihr in der Datei, in der Nachrichten versendet werden sollen, die Funktion importieren.

```python
from push import send_push_message
```

Jetzt nur noch an der geschwünschten Stelle die Funktion aufrufen!

```python
send_push_message("APP_KEY", "TITLE", "MESSAGE")
```


Viel Spaß damit!


