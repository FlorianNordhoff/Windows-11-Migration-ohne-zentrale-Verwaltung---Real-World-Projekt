
# Windows 11 Migration ohne zentrale Verwaltung

## Problemstellung

Microsoft hat das Support-Ende für Windows 10 angekündigt. Damit gehen erhebliche betriebliche Risiken einher, etwa das Ausbleiben sicherheitsrelevanter Updates bei Zero-Day-Schwachstellen sowie potenzielle Inkompatibilitäten mit zukünftiger Software.

Eine Migration auf Windows 11 war daher unumgänglich. Gleichzeitig galt es, mehrere Herausforderungen zu bewältigen. Da wir uns in einem Carve-out befanden, fehlte uns der zentrale Zugriff auf die Endgeräte via Verwaltungswerkzeuge wie Microsoft Intune standen in dieser Phase noch nicht zur Verfügung. Die Softwareanforderungen waren von Nutzer zu Nutzer sehr unterschiedlich, jedoch nicht dokumentiert. Darüber hinaus waren viele Geräte im ITSM-System entweder unvollständig erfasst oder überhaupt nicht registriert.

Ziel war es, trotz dieser Einschränkungen eine stabile und möglichst reibungslose Umstellung auf Windows 11 zu realisieren.

## Lösung

### Erfassung der genutzten Software und Systeminformationen

Da wir keinen direkten Zugriff auf die Endgeräte der Nutzer hatten, wurde ein Python-Skript erstellt, mit denen die installierte Software auf den bestehenden Windows-10-Systemen ausgelesen und dokumentiert werden konnte. Die Nutzer wurden gebeten, diesen Skript selbstständig unter Anleitung auszuführen. Auf Basis dieser Daten konnten individuelle Softwareprofile erstellt werden.

### Erstellung des Windows-11-Images

Ein einheitliches Windows-11-Image wurde vorbereitet, das alle unternehmensweit benötigten Basistools sowie vorab definierte Sicherheits- und Konfigurationseinstellungen enthielt. Die OneDrive-Integration wurde ebenfalls vorinstalliert, um eine reibungslose Synchronisation der Nutzerdaten zu ermöglichen. Dieses Image bildete die Grundlage für alle neuen Geräte.

### Paketierung zusätzlicher Software

Basierend auf den gesammelten Softwareprofilen wurde zusätzliche Software in modularen Paketen organisiert. Diese Pakete konnten nach der Intune-Registrierung der Geräte gezielt einzelnen Nutzern oder Nutzergruppen zugewiesen werden. So erhielt jeder Mitarbeiter genau die Anwendungen, die er für seine tägliche Arbeit benötigt ohne das Basisimage zu überladen.

### Rollout-Prozess (Gerätetausch)

Die neuen Geräte wurden mit dem vorbereiteten Windows 11 Image betankt und vorab in Intune registriert. Über das ITSM-System konnten sich die Nutzer eigenständig einen Termin für den Rollout buchen. Beim eigentlichen Gerätetausch wurden die alten Laptops entgegengenommen. Es wurde geprüft, ob alle Daten insbesondere in OneDrive und in den Browser-Favoriten korrekt synchronisiert waren. Anschließend wurde das neue Gerät gemeinsam mit dem Nutzer eingerichtet. Die Softwareverteilung erfolgte automatisiert über die zugewiesenen Intune-Gruppen. Durch diese strukturierte Vorgehensweise verlief der gesamte Rollout effizient.

## Mein Mitwirken bei der Umsetzung und Learnings

Ich habe den Vorschlag eingebracht, ein eigenes Skript zur automatisierten Erfassung der Gerätedaten zu entwickeln. Durch meine Erfahrungen mit Java und Python im Studium war diese Aufgabe eine ideale Gelegenheit, mein technisches Wissen praxisnah anzuwenden und weiter auszubauen.

Darüber hinaus wurde ich mit der Konzeption und Umsetzung des gesamten n8n-Workflows beauftragt, über den die erfassten Daten automatisch in unser ITSM-System übertragen wurden. Dies stellte meinen ersten praxisnahen Einstieg in die Arbeit mit APIs dar, eine Herausforderung, die mir nicht nur viel Spaß gemacht hat, sondern auch dazu führte, dass ich heute sicher und routiniert mit REST-Schnittstellen umgehen kann.

Auch während der Rollout-Phase war ich aktiv eingebunden. Ich habe die neuen Windows-11-Geräte vorbereitet, betankt und eingerichtet sowie die Übergabe im direkten Gespräch mit den Endanwendern begleitet. Dadurch konnte ich nicht nur meine technischen Fähigkeiten weiterentwickeln, sondern auch wertvolle Erfahrungen in der praktischen Umsetzung von IT-Prozessen und in der Zusammenarbeit mit Nutzern sammeln.

Nach Abschluss des Rollouts habe ich zusätzlich einen weiteren n8n-Workflow implementiert, der mithilfe der Microsoft Graph API fehlende Geräteinformationen aus Intune automatisiert abruft und mit unserem ITSM-System abgleicht. So konnten wir eine kontinuierliche und zuverlässige Datenintegration zwischen Intune und dem ITSM sicherstellen und die Gerätedaten vollständig und aktuell halten.
