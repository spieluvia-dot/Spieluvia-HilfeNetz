# SPIELUVIA – MASTER-ENTWICKLUNGSAUFTRAG H01

## Spieluvia HilfeNetz – kostenlose Prävention, Beratung und Orientierung

**Repository:** spieluvia-dot/Spieluvia-HilfeNetz  
**Status:** Entwicklungsprototyp, keine öffentliche Freigabe  
**Ziel:** Eigenständige barrierearme, responsive Hilfeplattform, später integrierbar in die Spieluvia-Hauptseite und Apps.

### Zielgruppen
Kinder, Jugendliche, Eltern, Angehörige, Erwachsene, Lehrkräfte, sozial und finanziell belastete Menschen.

### Themen
Prävention und Medienkompetenz; problematisches Gaming und Mediennutzung; Familie und Erziehung; psychische und soziale Belastungen; digitale Gefahren und Cybermobbing; Schule; soziale und finanzielle Hilfe; Krisenhilfe.

### Recherchepflicht
Mindestens 30 offizielle und überprüfte Hilfsangebote. Für jedes Angebot erfassen: Name, Träger, offizieller Link, Kategorie, Zielgruppe, Art der Hilfe, Kosten, Zugangsbedingungen, Anonymität, regionale Geltung, Sprachen, Barrierefreiheit, Prüfdatum und Quellen. Keine nicht verifizierten Leistungen oder Kooperationen behaupten. Informationsangebote und persönliche Beratungsstellen deutlich unterscheiden.

### Nutzererlebnis
Thematische Einstiegskarten, Suche, Filter nach Zielgruppe und Situation, gut sichtbare Notfallhinweise, verständliche Beschreibung und direkte offizielle Links. Mobile-first, Tastaturbedienbarkeit, ausreichende Kontraste, verständliche Sprache.

### Datenschutz und Sicherheit
Kein Konto, keine Übertragung von Suchbegriffen an Spieluvia, kein Tracking, keine unnötigen Cookies. Statische Datenbasis und lokale Suche. Keine Diagnose aus Nutzungsdaten, keine automatische Datenweitergabe an Hilfsstellen. Externe Seiten transparent kennzeichnen. Datenschutz und Impressum vor Freigabe vervollständigen.

### Forschungsaspekt
Freiwillige, rechtlich und technisch geprüfte Forschungsperspektive. Strikte Unterscheidung anonymisiert/pseudonymisiert. Keine Forschungsteilnahme als Nutzungsvoraussetzung; keine behaupteten Partnerschaften.

### Umsetzung
- H01 Grundlagen: Architektur, Design, Datenschema, Kategorien, Masterauftrag.
- H02 Recherche: mindestens 30 verifizierte Angebote mit Prüfdatum und Quellen.
- H03 Oberfläche: Filter, Suche, Detailinformationen und mobile Ansicht.
- H04 Qualität: Links, Datenschutz, Impressum, Barrierefreiheit, Krisenhinweise, Browser-Tests.
- H05 Erweiterung: regionale Suche, weitere Länder, optionale App-Verknüpfung und redaktioneller Aktualisierungsprozess.

### Abnahme
Mindestens 30 geprüfte Einträge; korrekte Kennzeichnung der Hilfearten; mobil und mit Tastatur nutzbar; keine personenbezogenen Suchdatenübertragungen; vollständige Rechtsseiten; geprüfte Krisenhinweise; funktionierende Links; dokumentierte Aktualisierung; keine behaupteten Kooperationen; keine Beeinträchtigung anderer Spieluvia-Projekte.

### Aktueller Stand
Erste Version mit 15 Orientierungseinträgen. Diese sind **noch nicht einzeln vollständig redaktionell verifiziert**. Vor öffentlicher Bewerbung muss die Prüfung abgeschlossen werden. Rechtsseiten sind Platzhalter.


## Erweiterungsbeschluss H02 – 300 recherchierte Angebote (06.11.2026)

Die bisherige Mindestzahl 30 wird durch **300 individuell geprüfte, eindeutig identifizierte Hilfsangebote** ersetzt. Die Zahl ist ein **Recherche- und Abnahmeziel**, keine Behauptung über den aktuellen Datenbestand. Die ersten 15 Einträge bleiben vorläufig und sind noch nicht vollständig redaktionell verifiziert.

### Zielverteilung (keine künstliche Auffüllung)
| Kategorie | Ziel |
|---|---:|
| Medienkompetenz und Prävention | 40 |
| Gaming, Social Media und Mediensucht | 35 |
| Familie, Erziehung und Elternberatung | 40 |
| Psychische Gesundheit und persönliche Krisen | 40 |
| Cybermobbing, Online-Gewalt und digitale Sicherheit | 35 |
| Kinder- und Jugendschutz | 35 |
| Schule, Bildung und soziale Teilhabe | 25 |
| Soziale, finanzielle und rechtliche Hilfe | 25 |
| Selbsthilfe, Forschung und Fachnetzwerke | 25 |
| **Summe** | **300** |

Jede Einrichtung wird **einmal** geführt und kann mehrere Themen-Tags haben. Ein Dachverband und seine eigenständig beratenden regionalen Stellen zählen nur getrennt, wenn sie unterschiedliche, belegte Zugangswege und Leistungen besitzen. Keine Dubletten, generierten Ortsvarianten oder bloßen Linklisten zum Auffüllen der Zielzahl.

### Verbindliches Datenschema
`id` (stabil), `name`, `traeger`, `website`, `beratung_url`, `beschreibung`, `themen[]`, `zielgruppen[]`, `hilfeart` (information|praevention|beratung|krise|forschung), `region`, `bundesland`, `online`, `telefon`, `kosten`, `anonymitaet`, `zugang`, `sprachen[]`, `barrierefreiheit`, `quellen[]`, `geprueft_am`, `pruefstatus` (unverifiziert|teilgeprueft|verifiziert|inaktiv), `hinweise`.

Unbekannte Angaben als `null` kennzeichnen, niemals erraten. Datensätze getrennt von UI-Code in `data/angebote.json` verwalten. Die Anzeige soll nur verifizierte Einträge standardmäßig als geprüft kennzeichnen. Künftige regionale Suche muss ohne IP-Geolokalisierung möglich sein; Nutzer können ihren Ort freiwillig eingeben und lokal filtern.

### Redaktioneller Ablauf
1. Offizielle Primärquelle prüfen und URL dokumentieren.
2. Hilfsangebot von bloßer Information, Forschung und Fachnetzwerk unterscheiden.
3. Zielgruppe, Erreichbarkeit, Kosten, Regionalität und Zugang aus Quellen übernehmen.
4. Eindeutige ID und Tags vergeben, Dubletten prüfen.
5. Datensatz mit Prüfdatum versehen und erst danach als verifiziert kennzeichnen.
6. Krisen- und Notfallangebote priorisiert und häufiger nachprüfen; übrige spätestens halbjährlich.

### Abnahme H02
Mindestens 300 echte, einzeln quellengeprüfte Angebote; davon darf kein Eintrag nur zum Erreichen einer Quote erfunden oder dupliziert sein. Vollständige Trennung von Daten und Darstellung; Suche und Filter nach Thema, Zielgruppe, Hilfeart, Region; klarer Stand der Datenprüfung; Quellen- und Prüfdatum je Eintrag. Vorher keine Aussage „300 geprüfte Angebote online“.
