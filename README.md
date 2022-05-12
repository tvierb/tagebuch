# Tagebuch (Script)

Aktuelle Version: 0.1-8

Dieses Python-Script (Name: tb) legt bei Aufruf ohne Parameter eine Textdatei fuer den aktuellen Tag an und startet einen Editor.
Dabei schaut es nach, ob in einem der letzten vier Tagesdateien ein Todo-Marker enthalten ist. Dieser sowie alle Folgezeilen werden in die neue Tagesdatei uebernommen.

Bei Folgeaufrufen fuer den aktuellen Tag die Datei nicht neu erzeugt.

Optional kann man ueber einen Parameter wie "+3" oder "-2" die jeweilige Tagesdatei relativ zu heute oeffnen.

Die Uebernahme von Todo-Text ist beschraenkt auf die Tagesdatei von heute sowie fuer den Aufruf mit positiver Zahl.

Der Todo-Marker ist: "# Todo", kann aber in der generierten .tagebuchrc geaendert werden.

## Beispiele

Der einfach Aufruf von "tb" generiert eine Datei "~/Tagebuch/2014/2014-07-30-Mi.md" und oeffnet sie im Editor:

     # 30.07.2014 (Mittwoch)

     * ( )
     * ( )
     * ( )
     * ( )
     * ( )

Notiert man darin (unten):
     # Todo

       * Das Tagebuchtool um eine eigene Configdatei erweitern

Und ruft morgen wieder "tb" auf, dann wird morgen eine Datei "~/Tagebuch/2014/2014-07-31-Do.md" generiert:

     # 31.07.2014 (Donnerstag)

     * ( )
     * ( )
     * ( )
     * ( )
     * ( )

     # Todo

     * Das Tagebuchtool um eine eigene Configdatei erweitern

## Todos:

* Sicheres Erkennen des Homedirs
* ggf Ausfuehren von git-Autocommits im Tagebuch-Ordner (geht auch via Cron)
* Docs verbessern

