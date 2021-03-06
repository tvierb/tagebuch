# Tagebuch (Script)

Aktuelle Version: 0.1

Dieses Python2.7-Script (Name: tb) legt bei Aufruf ohne Parameter eine Textdatei für den aktuellen Tag an und startet einen Editor.
Dabei schaut es nach, ob in einem der letzten vier Tagesdateien ein Todo-Marker enthalten ist. Dieser sowie alle Folgezeilen werden in die neue Tagesdatei übernommen.

Bei Folgeaufrufen für den aktuellen Tag die Datei nicht neu erzeugt.

Optional kann man über einen Parameter wie "+3" oder "-2" die jeweilige Tagesdatei relativ zu heute öffnen.

Die Übernahme von Todo-Text ist beschränkt auf die Tagesdatei von heute sowie für den Aufruf mit positiver Zahl.

Der Todo-Marker ist: "%Todo:"

## Beispiele

Der einfach Aufruf von "tb" generiert eine Datei "~/Tagebuch/2014/2014-07-30-Mi.txt" und öffnet sie im Editor:

    30.07.2014 (Mittwoch)

    ( )
    ( )
    ( )
    ( )
    ( )
    ( )
    ( )

Notiert man darin (unten):
    %Todo:
      * Das Tagebuchtool um eine eigene Configdatei erweitern

Und ruft morgen wieder "tb" auf, dann wird morgen eine Datei "~/Tagebuch/2014/2014-07-31-Do.txt" generiert:

    31.07.2014 (Donnerstag)

    ( )
    ( )
    ( )
    ( )
    ( )
    ( )
    ( )
    %Todo:
      * Das Tagebuchtool um eine eigene Configdatei erweitern

## Todos:

* Sicheres Erkennen des Homedirs
* Konfiguration (zu startender Editor) in Configdatei auslagern (~/.tagebuch)
* gg Vorlage für Tagesdatei in Config auslagern
* ggf Ausführen von git-Autocommit oä im Tagebuch-Ordner
* Docs verbessern
