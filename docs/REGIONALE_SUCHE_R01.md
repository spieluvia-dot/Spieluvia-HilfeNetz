# Regionale Suche – Implementierungsstand R01 (2026-11-06)

## Fertig im Repository
- Stadt/PLZ-Eingabe, Bundeslandauswahl, 10/25/50/100-km-Radius
- Haversine-Luftliniendistanz, lokale Filterung ohne Anfrage an externe Geocoding-API
- Standorte nur mit Koordinaten, Treffer sortiert nach Entfernung
- Eigene Datenstrukturen data/orte.json und data/standorte.json
- Offline-Importskript scripts/import_geonames.py

## Noch nicht fertig
- GeoNames-DE-Datensatz wurde **nicht** heruntergeladen/importiert; data/orte.json enthält 0 Orte.
- Noch keine physisch verifizierten Beratungsstellenstandorte; data/standorte.json enthält 0 Standorte.
- Die Umkreissuche liefert daher noch keine Treffer. Kein vorgetäuschter Funktionsstatus.
- Ausbau auf 100 Einträge, Karte und Bewertungslinks noch offen.

## Ortsdaten importieren
1. https://download.geonames.org/export/zip/DE.zip herunterladen.
2. ZIP entpacken, die enthaltene DE.txt bereitstellen.
3. Im Repository-Arbeitsverzeichnis ausführen: python scripts/import_geonames.py DE.txt
4. data/orte.json committen und auf Cloudflare Pages bereitstellen.
5. Quelle und Lizenz nennen: GeoNames, CC BY 3.0, https://www.geonames.org/.

## Standorte hinzufügen
Pro überprüfter Niederlassung in data/standorte.json einen Datensatz mit name, city, lat, lon, url hinzufügen. Adresse, Quelle, Prüfungstag und Leistungsart müssen vor Aufnahme redaktionell dokumentiert werden. Onlineangebote ohne Standort nicht als regionale Treffer behandeln.

## Datenschutz
Keine automatische Browser-Standortfreigabe. Stadt/PLZ wird für die Suche lokal verarbeitet. Keine Google-Places-API oder externe Geocoding-Anfrage.

## QA
Erforderlich: Tests für doppelte Städtenamen, PLZ mit mehreren Ortsbezeichnungen, Bundesland-Mapping, fehlende Koordinaten, Nulltreffer und mobile Bedienung.
