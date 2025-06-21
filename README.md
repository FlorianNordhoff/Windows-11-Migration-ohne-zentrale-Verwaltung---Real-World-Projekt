
# Windows 11 Migration ohne zentrale Verwaltung

## Einleitung

Im Rahmen eines IT-Carve-outs stand unser Unternehmen vor der Herausforderung, rund 300 Windows-10-Clients auf Windows 11 zu migrieren und das unter erschwerten Bedingungen: ohne zentralen Zugriff auf die Endgeräte, ohne bestehende MDM-Lösungen wie Microsoft Intune (zu Beginn) und mit individuell stark variierender Softwarenutzung je Mitarbeiter.

Dieses Projekt beschreibt den vollständigen Ablauf der Migration – von der Analysephase bis zum Rollout sowie die technischen und organisatorischen Lösungen, die wir im Laufe der Umsetzung entwickelt haben.

## Problemstellung

Microsoft hat das Support-Ende für Windows 10 angekündigt. Damit verbunden sind wesentliche Risiken für den Betrieb, etwa das Fehlen sicherheitsrelevanter Updates für Zero-Day-Schwachstellen und mögliche Inkompatibilitäten mit zukünftiger Software.

Eine Migration auf Windows 11 war daher unumgänglich. Gleichzeitig mussten mehrere Herausforderungen gelöst werden. Es bestand kein zentraler Zugriff auf die Geräte, was den Einsatz klassischer Verwaltungswerkzeuge erschwerte. Die Softwareanforderungen waren je nach Nutzer individuell, dokumentiert war das aber nicht. Zusätzlich waren viele Geräte im ITSM-System nicht korrekt oder gar nicht erfasst. Ziel war es, trotz dieser Einschränkungen einen reibungslosen und sicheren Umstieg zu ermöglichen.

## Lösung

### Erfassung der genutzten Software und Systeminformationen

Zur Vorbereitung der Migration habe ich ein Python-Skript entwickelt, das auf jedem Windows-10-Gerät automatisch Informationen wie installierte Software, den Benutzernamen und zentrale Hardwaredaten (CPU, RAM, Festplattenspeicher) erfasst. Die Daten wurden anschließend an einen Webhook in n8n gesendet, einer Low-Code/No-Code-Automatisierungsplattform. Dort habe ich den Workflow aufgebaut und war verantwortlich für die gesamte Weiterverarbeitung: Die Informationen wurden per API automatisiert an unser ITSM-System übertragen und dort strukturiert gespeichert.

Diese Datenbasis ermöglichte es unserem Application Manager, die tatsächlich benötigte Software zu identifizieren. Die Nutzer führten das Skript selbstständig aus. Gleichzeitig halfen die erfassten Systeminformationen dabei, unvollständige oder fehlerhafte Asset-Daten im ITSM zu korrigieren oder neue Geräte zu erfassen.

### Erstellung des Windows-11-Images

Ein einheitliches Windows-11-Image wurde vorbereitet, das alle unternehmensweit benötigten Basistools sowie vorab definierte Sicherheits- und Konfigurationseinstellungen enthielt. Die OneDrive-Integration wurde ebenfalls vorinstalliert, um eine  reibungslose Synchronisation der Nutzerdaten zu ermöglichen. Dieses Image bildete die Grundlage für alle neuen Geräte.

### Paketierung zusätzlicher Software

Basierend auf den gesammelten Softwareprofilen wurde zusätzliche Software in modularen Paketen organisiert. Diese Pakete konnten nach der Intune-Registrierung der Geräte gezielt einzelnen Nutzern oder Nutzergruppen zugewiesen werden. So erhielt jeder Mitarbeiter genau die Anwendungen, die er für seine tägliche Arbeit benötigt – ohne das Basisimage zu überladen.

### Rollout-Prozess (Gerätetausch)

Die neuen Geräte wurden mit dem vorbereiteten Windows-11-Image betankt und vorab in Intune registriert. Über das ITSM-System konnten sich die Nutzer eigenständig einen Termin für den Rollout buchen. Beim eigentlichen Gerätetausch wurden die alten Laptops entgegengenommen. Es wurde geprüft, ob alle Daten insbesondere in OneDrive und in den Browser-Favoriten – korrekt synchronisiert waren. Anschließend wurde das neue Gerät gemeinsam mit dem Nutzer eingerichtet. Die Softwareverteilung erfolgte automatisiert über die zugewiesenen Intune-Gruppen. Durch diese strukturierte Vorgehensweise verlief der gesamte Rollout effizient, transparent und ohne nennenswerte Störungen.

## Mein Mitwirken bei der Umsetzung

Ich habe den Vorschlag eingebracht, ein eigenes Skript zur automatisierten Erfassung der Gerätedaten zu entwickeln. Aufgrund meiner Erfahrungen mit Java und Python im Studium war dieses Projekt für mich eine ideale Möglichkeit, mein technisches Wissen praxisnah zu vertiefen.

Ich war verantwortlich für die Entwicklung des Python-Skripts sowie für die Konzeption und Umsetzung des vollständigen n8n-Workflows, über den die erfassten Daten automatisch in unser ITSM-System integriert wurden.

Auch während der Rollout-Phase war ich aktiv beteiligt. Ich habe Laptops mit dem neuen Windows-11-Image vorbereitet und eingerichtet sowie die Übergabe im persönlichen Gespräch mit den Endnutzern begleitet. Dadurch konnte ich nicht nur meine technischen Fähigkeiten weiterentwickeln, sondern auch wertvolle Erfahrung im Umgang mit realen IT-Prozessen und der Zusammenarbeit mit Anwendern sammeln.

Nach Abschluss des Rollouts habe ich zusätzlich einen weiteren n8n-Workflow implementiert, der mithilfe der Microsoft Graph API fehlende Geräteinformationen aus Intune abruft und diese automatisiert mit unserem ITSM-System abgleicht. Auf diese Weise konnten wir eine kontinuierliche und zuverlässige Datenintegration zwischen Intune und dem ITSM sicherstellen und die Geräteinformationen im System aktuell und vollständig halten.
