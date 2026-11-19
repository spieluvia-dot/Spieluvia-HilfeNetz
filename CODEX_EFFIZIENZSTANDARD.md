# CODEX_EFFIZIENZSTANDARD.md — Allgemeinverbindlicher Standard V2.0
Stand: 2026-11-20. Gilt für Codex-, Work- und sonstige agentische Entwicklungsarbeiten in diesem Repository, soweit der konkrete Auftrag dies erlaubt.

## Priorität und Grenzen
Dieser Standard ergänzt AGENTS.md, projektspezifische Arbeitsanweisungen, Sicherheits- und Datenschutzvorgaben, Lizenzanforderungen, Tests und konkrete Nutzeraufträge. Strengere Schutz- und Abnahmevorgaben haben Vorrang. Keine selbstständige Freigabe für kostenpflichtige Dienste, neue Entwicklungsaufträge, Pushes auf andere Branches, Merges, Releases, Veröffentlichungen oder destruktive Aktionen. Vorhandene Projektregeln nicht löschen oder abschwächen.

## Verbindlicher Ablauf
1. **Gezielter Einstieg:** Branch, HEAD, Arbeitsbaum, letzte relevante Änderungen, Projektanweisungen und vorhandene Status-/Testnachweise prüfen. Erst Dateiliste/Suche/Diff, dann gezielt betroffene Dateien und Abhängigkeiten lesen. Kein pauschaler Vollscan bei kleinen Aufgaben.
2. **Arbeitsstufe wählen:** SPARSAM für klar begrenzte Routine (geringer Denkaufwand); AUSGEWOGEN als Standard für Entwicklung (mittlerer Denkaufwand); GRÜNDLICH für Architektur, Sicherheit, Datenverlustgefahr oder schwierige Fehler (höherer Denkaufwand). Nur tatsächlich verfügbare Modelle/Einstellungen wählen; Qualität hat Vorrang. Fast-Modus nicht automatisch als kontingentsparend betrachten.
3. **Änderungsumfang begrenzen:** Zusammenhängende Arbeiten in prüfbaren Schritten bearbeiten; keine ungefragten Refactorings, Formatierungswellen oder Neuaufbauten unveränderter Teile. Bestehende Werkzeuge und Dokumentation bevorzugen.
4. **Ein Agent als Standard:** Zusätzliche Agenten, parallele Vollanalysen und doppelte Recherchen nur bei begründetem Nutzen. Keine künstliche Aufteilung in neue Sitzungen.
5. **Ergebnisse gültig wiederverwenden:** Vorhandene Analysen, Tests, Builds und Artefakte nur übernehmen, wenn Änderungen, Eingaben, Umgebung und nötige Nachweise dies erlauben; bei kritischen Artefakten ggf. Hashes/Versionen prüfen. Keine Wiederverwendung allein aufgrund eines Dateinamens.
6. **Risikobasiert testen:** Zuerst kleinste aussagekräftige Prüfung, dann betroffene Integrationen; vollständige Regressionen bei Sicherheitsrisiken, übergreifenden Änderungen, Pflichtgates oder konkretem Fehlerverdacht. Niemals Datenschutz-, Sicherheits-, Lizenz- oder verpflichtende Abnahmetests wegsparen.
7. **Fehler lokal eingrenzen:** Reproduzierbaren Fehler isolieren, kleinste geeignete Korrektur durchführen und Auswirkungen nachtesten. Keine unbelegten Erfolgsmeldungen.
8. **Unterbrechungen fortsetzen:** Bestehenden Thread/Branch und überprüfbaren Stand bevorzugen. Bei längeren Arbeiten nach sinnvollen Meilensteinen eine kurze Fortsetzungsnotiz pflegen: Branch/Commit, erledigt, offen, gültige Ergebnisse, Invalidierungsbedingungen, nächster Schritt, Risiken. Sicherung/Push nur im autorisierten Rahmen; keine unnötigen Checkpoint-Läufe.
9. **Kompakte Kommunikation:** Nur wesentliche Entscheidungen, Risiken und Meilensteine; große Logs nicht in den Chat kopieren, sondern Pfad und Kurzbefund angeben. Abschluss: geänderte Dateien, echte Tests, Ergebnis, Risiken und nächste Schritte.
10. **Verbrauch transparent messen:** Wenn verfügbar und datenschutzverträglich: Datum, Auftrag, Modell, Denkstufe, Dauer, Umfang, Kontingent vorher/nachher, ausgeführte/wiederverwendete Tests und Nacharbeit dokumentieren. Keine persönlichen Kontingent-Screenshots oder Geheimnisse in öffentliche Repos. Ohne vergleichbare Baseline keine Prozent-Einsparungen behaupten. ChatGPT-Kontingente nicht mit API-Tokenkosten gleichsetzen.

## Erfolgskriterium
Optimierung ist nur gelungen, wenn Verbrauch und Laufzeit sinken, **ohne** Qualität, Sicherheit, nachvollziehbare Tests oder spätere Nacharbeit unverhältnismäßig zu verschlechtern. Kein künstliches Tokenlimit und keine pauschale Testvermeidung.

## Projektregeln
Projektbezogene Anweisungen in AGENTS.md und bestehenden Dokumenten bleiben gültig. Projektspezifische Zusatzregeln dürfen diesen Standard konkretisieren und verschärfen. Konflikte offen benennen; Sicherheitsvorgaben nicht stillschweigend überschreiben.
