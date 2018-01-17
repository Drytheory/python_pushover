# python_pushover


Viel Spaß mit der Datei.
Einfach und schnell mit Python Pushnachrichten über den Service Pushover ans Smartphone oder Tablet senden.


# Wie funktioniert es?

Ihr habt zwei Dateien, diese beiden Dateien müssen immer im selben Ordner liegen.

Ihr wollt eine Pushnachricht versenden?

```python
from push import send_push_message
send_push_message("APP_KEY, "TITLE", "MESSAGE")
```
