# HilfeNetz – verbindlicher Erfassungsstandard für neue Einträge

Stand: 2026-11-06. Ziel: 300 sinnvolle, sauber klassifizierte Angebote; keine bloßen Verzeichnisfüller.

## Pflichtfelder vor Veröffentlichung
- id (stabil), name, typ (direkte Beratung / Vermittlung / Prävention / Forschung / Kinderangebot), themen, zielgruppen
- url (offizielle Website), source_url, verified_on (Datum), verification_status (offen / teilgeprüft / geprüft)
- angebot_online (boolean), angebot_vor_ort (boolean), hinweis_zur_leistung
- Bei regionalen Standorten: vollständige Adresse, PLZ, Ort, Bundesland, geografische Zuordnung und Angabe, ob der Standort tatsächlich Beratungen anbietet.

## Zusätzliche Kontaktfelder
- phone (nur verifizierte öffentliche Kontakt- oder Beratungsnummer), email (Art des Postfachs beachten), contact_url, weitere Kontaktwege
- hours_type: beratung_telefonisch / offene_beratung / buero / termin_nach_vereinbarung / online
- hours, hours_source_url, hours_verified_on, appointment_required
- languages, accessibility, cost_information, anonymity, notes
- Wenn unbekannt: null/leer; niemals schätzen oder aus anderen Filialen übernehmen.

## Qualitätsregeln
1. Offizielle Quellen zuerst; Verzeichnisse nur als Recherchehinweis und mit Quellenbeleg.
2. Keine Bewertungen oder Qualitätsnoten ohne belastbare Grundlage. Öffentliche Google-Bewertungen nicht als Qualitätsnachweis für Krisenberatung behandeln.
3. Veröffentlichten Standort von Geschäftsstelle und rein digitalem Angebot unterscheiden.
4. Telefonische Erreichbarkeit und Öffnungszeiten nie vermischen.
5. Keine erfundenen Kooperationen oder behauptete Zertifizierungen.
6. Kontaktdateien (.vcf) dürfen nur bestätigte Werte enthalten; bei unbekannten Angaben keine Platzhalter in die Datei schreiben.
7. Änderungen mit Quelle und Datum dokumentieren. Sensible Kontaktangaben regelmäßig nachprüfen.
8. Keine persönlichen Klientendaten sammeln; lokale PLZ-Suche ohne Tracking.

## Ausbauplan
- Phase A: bestehende 50 Angebote kategorisieren und Kontaktfelder vervollständigen.
- Phase B: regionale Beratungsstellen nach Bundesland mit überprüfter Standortadresse aufnehmen.
- Phase C: Qualitätssicherung und mobile Tests (Android/iOS vCard, Barrierefreiheit, Linkprüfung).
- Phase D: auf 100, später 300 tatsächlich nützliche Einträge wachsen.

## Beispiel (nur Schema, keine reale Einrichtung)
```json
{
  "id": "beispiel-einrichtung-ort",
  "name": "Beispielname",
  "type": "direkte_beratung",
  "topics": ["Mediensucht"],
  "target_groups": ["Eltern"],
  "postal_code": null,
  "city": null,
  "state": null,
  "address": null,
  "phone": null,
  "email": null,
  "contact_url": null,
  "hours_type": null,
  "hours": null,
  "appointment_required": null,
  "url": null,
  "source_url": null,
  "verified_on": null,
  "verification_status": "offen"
}
```
