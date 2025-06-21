
# Windows 11 Migration ohne zentrale Verwaltung

## Problemstellung 

Mit der offiziellen Ankündigung des Support-Endes für Windows 10 ab 14.10.2025 werden Updates des Betriebssystems nicht mehr kostenlos zu Verfügung gestellt. Dies öffnet insbesondere neu entdeckte Schwachstellen, sogenannte Zero-Day-Sicherheitslücken, die dann nicht mehr geschossen werden. Ebenso ist die künftige Kompatibilität mit neuer Software nicht mehr gewährleistet. Für unser Unternehmen ergab sich daraus ein dringender Handlungsbedarf. Eine zeitnahe Migration auf Windows 11 ist unerlässlich.

### Herausforderungen:

- Die Migration auf Windows 11 erfolgte im Kontext eines laufenden Carve-outs, wodurch der zentrale Zugriff auf Endgeräte stark eingeschränkt war. Somit stand Microsoft Intune oder andere zentrale Verwaltungswerkzeuge nicht zu Verfügung.
- Die Softwareausstattung variierte stark zwischen den Nutzenden und war nicht dokumentiert.
- Viele Endgeräte waren im IT-Service-Management-System (ITSM) unvollständig erfasst oder gar nicht registriert.
- Die mangelhafte Datenlage erschwerte die Planung, Priorisierung und Umsetzung der Migration erheblich.

## Lösung

### Erfassung der genutzten Software und Systeminformationen

Da wir keinen direkten Zugriff auf die Endgeräte der Clients hatten, wurde ein Python-Skript erstellt, mit denen die installierte Software auf den bestehenden Windows-10-Systemen ausgelesen und dokumentiert werden konnte. Die Clients wurden gebeten, diesen Skript selbstständig unter Anleitung auszuführen. Auf Basis dieser Daten konnten individuelle Softwareprofile erstellt werden.

### Erstellung des Windows 11 Images

Ein einheitliches Windows 11 Image wurde vorbereitet, das alle unternehmensweit benötigten Basistools sowie vorab definierte Sicherheits- und Konfigurationseinstellungen enthielt. Die OneDrive-Integration wurde ebenfalls vorinstalliert, um eine reibungslose Synchronisation der Nutzerdaten zu ermöglichen. Dieses Image bildete die Grundlage für alle neuen Geräte.

### Paketierung zusätzlicher Software

Basierend auf den gesammelten Softwareprofilen wurde zusätzliche Software in modularen Paketen organisiert. Diese Pakete konnten nach der Intune-Registrierung der Geräte gezielt einzelnen Nutzern oder Nutzergruppen zugewiesen werden. So erhielt jeder Mitarbeiter genau die Anwendungen, die er für seine tägliche Arbeit benötigt ohne das Basisimage zu überladen.

### Rollout-Prozess (Gerätetausch)

Die neuen Geräte wurden mit der vorbereiteten Windows 11 Image betankt und vorab in Intune registriert. Über das ITSM-System konnten sich die Nutzer eigenständig einen Termin für den Rollout buchen. Beim eigentlichen Gerätetausch wurden die alten Laptops entgegengenommen. Es wurde geprüft, ob alle Daten wichtigen Daten in OneDrive und in den Browser-Favoriten korrekt synchronisiert waren. Anschließend wurde das neue Gerät gemeinsam mit dem Nutzer eingerichtet. Die Softwareverteilung erfolgte automatisiert über die zugewiesenen Intune-Gruppen.

## Mein Mitwirken bei der Umsetzung und Learnings

Ich habe den Vorschlag eingebracht, ein eigenes Skript zur automatisierten Erfassung der Gerätedaten zu entwickeln. Durch meine Erfahrungen mit Java und Python im Studium war diese Aufgabe eine ideale Gelegenheit, mein technisches Wissen praxisnah anzuwenden und weiter auszubauen.

Darüber hinaus wurde ich mit der Konzeption und Umsetzung des gesamten n8n-Workflows beauftragt, über den die erfassten Daten automatisch in unser ITSM-System übertragen wurden. Dies stellte meinen ersten praxisnahen Einstieg in die Arbeit mit APIs dar, eine Herausforderung, die mir nicht nur viel Spaß gemacht hat, sondern auch dazu führte, dass ich heute sicher und routiniert mit REST-Schnittstellen umgehen kann.

Auch während der Rollout-Phase war ich aktiv eingebunden. Ich habe die neuen Windows 11 Geräte vorbereitet, betankt und eingerichtet sowie die Übergabe im direkten Gespräch mit den Endanwendern begleitet. Dadurch konnte ich nicht nur meine technischen Fähigkeiten weiterentwickeln, sondern auch wertvolle Erfahrungen in der praktischen Umsetzung von IT-Prozessen und in der Zusammenarbeit mit Nutzern sammeln.

Nach Abschluss des Rollouts habe ich zusätzlich einen weiteren n8n-Workflow implementiert, der mithilfe der Microsoft Graph API fehlende Geräteinformationen aus Intune automatisiert abruft und mit unserem ITSM-System abgleicht. So konnten wir eine kontinuierliche und zuverlässige Datenintegration zwischen Intune und dem ITSM sicherstellen und die Gerätedaten vollständig und aktuell halten. 

Python-Script: https://github.com/FlorianNordhoff/Windows-11-Migration-ohne-zentrale-Verwaltung---Real-World-Projekt/blob/ddef97b91ecf8940b30533385206b400b4ee09a1/inventarisierung.py
