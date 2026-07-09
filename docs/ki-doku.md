# KI-Dokumentation

Evaluation und Reflexion zum Einsatz von KI-Werkzeugen im Projekt L'Essence Parfumerie (Modul M293).

## Evaluation der KI-Werkzeuge

Für die Webentwicklung wurden zwei KI-Werkzeuge geprüft: **ChatGPT/Codex** und **Claude**. Beide können Code schreiben, erklären und debuggen, unterscheiden sich aber in einigen Punkten.

### Nutzwertanalyse

| Kriterium | Gewichtung | ChatGPT/Codex | Claude |
|---|---|---|---|
| Codequalität (HTML/CSS/JS) | 25% | 4 | 5 |
| Debugging & Fehlerbehebung | 20% | 4 | 4 |
| Verständnis des Gesamtprojekts (viele Dateien) | 20% | 3 | 5 |
| Konsistenz über mehrere Seiten hinweg | 20% | 4 | 5 |
| Geschwindigkeit / Verfügbarkeit | 15% | 5 | 4 |
| **Gewichteter Total** | | **3.95** | **4.65** |

Bewertungsskala: 1 (schwach) bis 5 (sehr gut).

### Begründung der Werkzeugwahl

Für das Projekt wurde hauptsächlich **Claude** eingesetzt. Der Hauptgrund ist der Umgang mit dem Gesamtprojekt: Da die Website aus vielen einzelnen HTML-Dateien besteht, die alle den gleichen Aufbau (Header, Navigation, Footer, Formularstruktur) haben müssen, war es wichtig, dass die KI den bestehenden Code zuerst liest und Änderungen konsistent über alle Seiten anwendet, statt jede Seite einzeln und leicht unterschiedlich zu generieren. Claude hat hier zuverlässiger gearbeitet und weniger Nacharbeit verursacht. ChatGPT/Codex wurde ergänzend genutzt, vor allem für schnelle Zwischenfragen und einzelne Codeausschnitte.

## Einsatz der KI im Projekt

Die KI wurde während der ganzen Projektarbeit begleitend eingesetzt, nicht um die Website von Grund auf zu erstellen, sondern um bestehenden Code zu verbessern, zu erweitern und zu kontrollieren.

Konkrete Beispiele:

- **Produktseiten:** Die zehn Produktseiten folgen alle dem gleichen Muster (Bild, Duftnoten, Beschreibung, Video, Bestellformular). Die KI half dabei, dieses Muster sauber in `build_pages.py` abzubilden, damit neue Produkte einfach über eine Datenliste ergänzt werden können, statt jede Seite manuell zu kopieren.
- **Formulare:** Beim Kontaktformular und beim Bestellformular hat die KI Vorschläge gemacht für sinnvolle Feldtypen (z. B. `select` für das Thema, `required`-Attribute für Pflichtfelder) und für eine einfache clientseitige Bestätigungsmeldung ohne echten Server.
- **Navigation und Filter:** Die Filterfunktion auf der Kollektionsseite (Duftkategorien) sowie das mobile Burger-Menü wurden mit KI-Unterstützung debuggt, z. B. als der Filter beim direkten Aufruf über einen Link (`#kategorie`) nicht korrekt reagiert hat.
- **Responsive Design:** Bei den Media Queries für Tablet und Mobile hat die KI geholfen, Grid-Layouts (z. B. Produktgrid, Kontaktbereich) so anzupassen, dass sie auf schmalen Bildschirmen nicht brechen.
- **Dokumentation:** Styleguide und Wireframes wurden mit KI-Unterstützung strukturiert und in eine einheitliche Form gebracht.

Der von der KI vorgeschlagene Code wurde jeweils kontrolliert, getestet und wo nötig an das bestehende Design und die eigenen Vorstellungen angepasst. Die KI hat nichts automatisch übernommen, ohne dass es geprüft wurde.

## Reflexion

Der Einsatz von KI hat die Arbeit an der Website deutlich beschleunigt, vor allem bei sich wiederholenden Aufgaben wie den zehn Produktseiten oder den Anpassungen für Mobile/Tablet. Ohne KI hätte das manuelle Kopieren und Anpassen jeder einzelnen Seite deutlich mehr Zeit gekostet und wäre fehleranfälliger gewesen.

**Stärken:** Die KI ist stark darin, bestehende Muster zu erkennen und konsequent weiterzuführen, was bei einer Website mit vielen ähnlichen Seiten sehr hilfreich ist. Auch beim Debugging von JavaScript-Problemen (z. B. Event-Listener, die nicht ausgelöst wurden) war die Hilfe wertvoll, weil Fehler schneller gefunden wurden.

**Schwächen:** Bei rein gestalterischen Entscheidungen (Farben, Bildsprache, Tonalität der Texte) waren die Vorschläge der KI oft zu generisch und mussten stark angepasst werden, damit sie zum gewünschten Look der Marke passen. Auch das Gesamtbild über alle Seiten hinweg musste am Schluss manuell geprüft werden, da die KI einzelne Anpassungen nicht immer automatisch auf alle betroffenen Dateien übertragen hat.

**Erkenntnis:** KI eignet sich gut als Werkzeug für Struktur, Konsistenz und Fehlersuche, ersetzt aber nicht die eigene Kontrolle über Design und Inhalt. Am besten funktioniert der Einsatz, wenn man der KI klar sagt, was sich nicht ändern darf (z. B. das bestehende Layout), und nur gezielt einzelne Teile verbessern lässt.
