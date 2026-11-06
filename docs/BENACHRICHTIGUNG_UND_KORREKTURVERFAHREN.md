# Spieluvia HilfeNetz – Benachrichtigungs- und Korrekturverfahren

Stand: 2026-11-06. Dieses Dokument beschreibt ein Verfahren, keine rechtliche Freigabe für Massen-E-Mails.

## Kontakt und Zuordnung
- Allgemeines Postfach: spieluvia@gmail.com
- Zugeordnete Empfangsadresse: **spieluvia+hilfenetz@gmail.com** (Gmail-Plus-Adressierung, kein separates Postfach).
- Für Berichtigungen: spieluvia+hilfenetz-korrektur@gmail.com.
- Antworten werden an spieluvia@gmail.com zugestellt. In Gmail einen Filter für `to:(spieluvia+hilfenetz@gmail.com OR spieluvia+hilfenetz-korrektur@gmail.com)` und das Label `Spieluvia / HilfeNetz` einrichten. Filter ist noch nicht eingerichtet.
- Absender muss beim Versand korrekt konfiguriert sein; die Plus-Adresse allein garantiert keine auswählbare Absenderidentität. Für sachliche Mitteilungen kann der tatsächliche Absender spieluvia@gmail.com und die eindeutig bezeichnete Antwortadresse genutzt werden, sofern technisch eingerichtet und getestet.

## Rechtliche Prüfpunkte vor Versand
1. Nur offizielle, öffentlich verifizierte Organisationsdaten veröffentlichen. Personenbezogene Angaben separat beurteilen (DSGVO Art. 6, 14, 21).
2. Keine ungefragte Werbe-E-Mail: sachliche Information über einen vorhandenen Eintrag von Werbung und Kooperationsanfragen trennen; § 7 UWG beachten. Massenversand erst nach juristischer Prüfung.
3. Datenschutzhinweise mit Verantwortlichem, Rechtsgrundlage, Datenquelle, Zwecken, Speicherfristen, Betroffenenrechten und Kontakt bereitstellen; vorhandene Hinweise vor Veröffentlichung prüfen.
4. Keine Daten aus fremden Verzeichnissen ohne Prüfung der Datenbank- und Nutzungsrechte massenhaft übernehmen.
5. Kein automatischer Versand, bevor Rechtmäßigkeit, Datenschutztext, konkrete Profil-URL und Absender/Antwortadresse geprüft sind.

## Interner Ablauf
1. Eintrag mit stabiler ID, offizieller Quelle, Prüfdatum, Themen, Zielgruppen und möglichst vollständigen Kontaktdaten erfassen.
2. Kontaktart kennzeichnen: Beratung, Geschäftsstelle, technische Unterstützung oder Vermittlung; Unbekanntes leer lassen.
3. Benachrichtigungsstatus intern führen: `nicht_geprueft`, `rechtlich_geprueft`, `informiert`, `antwort_erhalten`, `korrektur_offen`, `entfernung_offen`, `abgeschlossen`.
4. Eine individuelle sachliche Nachricht nur nach rechtlicher Freigabe und mit direktem Profillink versenden; Datum, Kontaktkanal, Zuständigkeit und Antwort dokumentieren.
5. Korrektur- oder Löschwünsche zeitnah prüfen, Eingang bestätigen und nach Entscheidung Daten aktualisieren oder entfernen; notwendige interne Nachweise datensparsam aufbewahren.
6. Keine personenbezogenen Antwortinhalte im öffentlichen GitHub-Repository speichern. Interne Statusdateien mit personenbezogenen Kontakten gehören in einen geschützten Speicher.

## Muster: sachliche Eintragsinformation (nicht automatisch versenden)

**Betreff:** Information zu Ihrem Eintrag im Spieluvia HilfeNetz

Guten Tag,

Ihre Einrichtung ist im kostenfreien Informationsverzeichnis Spieluvia HilfeNetz aufgeführt. Wir möchten Ihnen die Möglichkeit geben, die öffentlich recherchierten Angaben zu prüfen.

**Ihr Eintrag:** [individueller Direktlink]

Falls Angaben falsch oder veraltet sind oder Sie eine Berichtigung beziehungsweise Entfernung wünschen, antworten Sie bitte an **spieluvia+hilfenetz@gmail.com**. Ihre Nachricht erreicht das Spieluvia-HilfeNetz-Team.

Informationen zur Datenverarbeitung und Ihren Rechten: [geprüfter Link zu den Datenschutzhinweisen]

Mit freundlichen Grüßen

Sebastian Bilicki
Spieluvia HilfeNetz
spieluvia@gmail.com
https://spieluvia-hilfenetz.pages.dev/

## Offene Umsetzungsschritte
- Gmail-Label und Filter im Konto manuell einrichten und mit Testmail prüfen.
- Datenschutzhinweise und Impressum auf konkrete Datenverarbeitung und Zuständigkeiten prüfen.
- Rechtliche Prüfung des geplanten E-Mail-Verfahrens.
- Öffentliche Kontakt-/Korrekturfunktion ohne Veröffentlichung persönlicher Nachrichten.
- Nach Freigabe: private Verwaltungsdatenbank für Versandstatus, Korrekturhistorie und Opt-out.
