# Teil 1 Initialisierung

- [Teil 1 Initialisierung](#teil-1-initialisierung)
- [Versionenverzeichniss](#versionenverzeichniss)
- [Aufgabenstellung](#aufgabenstellung)
  - [Ausgangslage](#ausgangslage)
  - [Ziele](#ziele)
  - [Mittel und Methode](#mittel-und-methode)
    - [Sachmittel](#sachmittel)
    - [Programmiersprache](#programmiersprache)
  - [Werkzeuge](#werkzeuge)
  - [SCRUM-Überblick](#scrum-überblick)
  - [Defenition of Done](#defenition-of-done)
- [Projektorganisation](#projektorganisation)
  - [Beteiligte Personen](#beteiligte-personen)
    - [Kanditatin](#kanditatin)
    - [Dozenten](#dozenten)
- [Datensicherung](#datensicherung)
- [Sprint Planning](#sprint-planning)
  - [Sprint 1 05.05 – 09.05 (5 Tage)](#sprint-1-0505--0905-5-tage)
    - [Ziel: Projektvorbereitung, Architekturentscheidungen](#ziel-projektvorbereitung-architekturentscheidungen)
    - [Priorisierung](#priorisierung)
    - [Aufgabenverteilung](#aufgabenverteilung)
    - [Nächste Schritte](#nächste-schritte)
  - [Sprint 2 10.05 – 09.06 (4 Wochen)](#sprint-2-1005--0906-4-wochen)
    - [Ziel: Umsetzung der Kernfunktionalitäten](#ziel-umsetzung-der-kernfunktionalitäten)
    - [Priorisierung](#priorisierung-1)
    - [Aufgabenverteilung](#aufgabenverteilung-1)
    - [Nächste Schritte](#nächste-schritte-1)
  - [Sprint 3: 10.06 – 07.07 (4 Wochen)](#sprint-3-1006--0707-4-wochen)
    - [Ziel: Feinschliff, Absicherung, Präsentationsvorbereitung](#ziel-feinschliff-absicherung-präsentationsvorbereitung)
      - [Woche 1–2 (10.06 – 24.06):](#woche-12-1006--2406)
      - [Woche 3 (25.06 – 30.06):](#woche-3-2506--3006)
      - [Woche 4 (01.07 – 07.07):](#woche-4-0107--0707)
    - [Priorisierung](#priorisierung-2)
    - [Aufgabenverteilung](#aufgabenverteilung-2)
    - [Nächste Schritte](#nächste-schritte-2)
- [Sprint Reviews](#sprint-reviews)
  - [Sprint Review 1](#sprint-review-1)
    - [Besprechungsnotiz](#besprechungsnotiz)
  - [Sprint Review 2](#sprint-review-2)
    - [Besprechungsnotiz](#besprechungsnotiz-1)
  - [Sprint Review 3](#sprint-review-3)
    - [Besprechungsnotiz](#besprechungsnotiz-2)

# Versionenverzeichniss

| Version | Datum  | Autor | Bemerkung | 
| ------- | ------ | ----  | --------- |
| 1.0 | 05.05.2024 | Laura Dubach | Zeitplan und Notion erstellen |

# Aufgabenstellung

## Ausgangslage

In einer zunehmend vernetzten Welt sind personalisierte, ortsbezogene Event-Empfehlungen für Musikfans sehr gefragt. Bestehende Lösungen sind oft schwer erweiterbar oder bieten keine einfache Integration in bestehende Systeme.
Die Herausforderung besteht darin, einen eigenständigen Microservice zu entwickeln.

**Ambitioniert:** Die Entwicklung eines eigenständigen Services inklusive API-Anbindung, Filterlogik und Bereitstellung via REST ist anspruchsvoll, aber machbar.
**Motivierend:** Persönliches Interesse an Musik, Event-Technologien und Microservices.
**Organisiert:** APIs, Tools und Frameworks sind vorhanden oder beschaffbar.
**Realistisch:** Umfang und Zielsetzungen sind im Rahmen der verfügbaren Zeit gut umsetzbar.
**Echt:** Der Anwendungsfall ist realitätsnah und technologisch aktuell.

## Ziele

1.	Entwicklung eines lauffähigen Microservices mit REST-API zur Abfrage von Musikveranstaltungen
2.	AWS über eine Pipeline zur Verfügung stellen
3.	Anbindung an eine externe Event-API zur Datenbeschaffung
4.	Implementierung von Filterfunktionen
5.	Containerisierung mit Docker zur einfachen Bereitstellung
6.	Einbindung einer Datenbank zur Speicherung von Nutzerinformationen

## Mittel und Methode

### Sachmittel

- Unterrichtsressourcen
- Flask Dokumentationen
- Unterstützung der Dozenten

### Programmiersprache

- Python

## Werkzeuge

- SCRUM
- ChatGPT
- Visual Studio Code
- PowerPoint
- Notion
- Docker Desktop
- API`s
- Flask
- Github
- AWS

## SCRUM-Überblick

Im Rahmen der Entwicklung des Microservices für personalisierte, ortsbezogene Event-Empfehlungen wird SCRUM als agiles Projektmanagement-Framework eingesetzt, um strukturierte Fortschritte zu ermöglichen. Das Projekt wird in mehrere Sprints unterteilt, in denen jeweils konkrete Teilziele wie zum Beispiel die Anbindung der externen Event-API, die Entwicklung der Filterlogik oder die Integration der REST-API fokussiert bearbeitet werden. Zu Beginn jedes Sprints erfolgt eine Sprintplanung, in der die anstehenden Aufgaben priorisiert und aufgeteilt werden. Nach jedem Sprint wird ein Review durchgeführt. Durch den Einsatz von SCRUM bleibt man flexibel und kann trotz der technischen Komplexität effektiv auf Veränderungen und Herausforderungen reagieren.

## Defenition of Done

# Projektorganisation

## Beteiligte Personen

### Kanditatin

```
Laura Joana Dubach
Funktion: Projektleiterin
P: 079 355 78 24
Github: lauradubach
Business E-Mail: laura.dubach@itnetx.ch
School E-Mail: laura.dubach@edu.tbz.ch
```
### Dozenten

```
Parisi Corrado
Funktion: PRJ-Dozent
Github: corrado-parisi
E-Mail: corrado.parisi@tbz.ch
```
```
Langer Boris
Funktion: Fachdozent
Github: 
E-Mail: boris.langer@tbz.ch
```

# Datensicherung

Damit keine Daten verloren gehen, werde ich alle Dokumente auf meinem OneDrive abspeichern. Zusätzlich werde ich die Daten auf einen USB-Stick abspeichern, damit ich im Worstcase Szenario ein Backup besitze.

# Sprint Planning

Entwicklung eines Microservices für Event-Empfehlungen

**Zeitraum:** 05.05.2025 – 07.07.2025  
**Methode:** SCRUM  
**Anzahl Sprints:** 3 (Sprint 1 verkürzt)

## Sprint 1 05.05 – 09.05 (5 Tage)

Sprint-Nummer: Sprint 1
Datum: 05.05.2025
Teilnehmer: Laura Dubach

### Ziel: Projektvorbereitung, Architekturentscheidungen

1. Projektstruktur & Tools vorbereiten
  - Git-Repository einrichten
  - Ordnerstruktur, Linter, README
  - Auswahl: Programmiersprache, Framework

2. Event-API Recherche & Anbindung vorbereiten
  - Recherche zu verfügbaren Event-APIs (z. B. Ticketmaster, Eventbrite, Songkick)
  - API-Key beantragen
  - Testaufrufe mit Tools wie Postman oder cURL durchführen

3. Microservice-Design planen
  - REST-Endpunkte festlegen (z. B. /events, /filter)
  - Grobe Klassendiagramme/Modellierung
  - Wahl einer Datenbank (z. B. PostgreSQL, MongoDB)

### Priorisierung

1. Priorität
2. Priorität
3. Priorität

### Aufgabenverteilung

Alle Aufgaben werden von Laura Dubach umgesetzt.

### Nächste Schritte

- Sprintreview findet am: 09.05.2025 statt

## Sprint 2 10.05 – 09.06 (4 Wochen)

### Ziel: Umsetzung der Kernfunktionalitäten

Woche 1–2 (10.05 – 24.05):

1. REST-API + Event-API + Filterlogik
  - REST-API implementieren (`GET /events`, `GET /events?genre=rock`)
  - Daten aus externer Event-API abrufen und verarbeiten
  - Filterfunktionen integrieren:
    - Ort (z. B. Städte)
    - Datum (Zeitraum)
    - Musikgenre
  - Unit-Tests für Endpunkte und Filterlogik schreiben

Woche 3 (25.05 – 31.05):

2. Datenbankanbindung + Nutzerstruktur
   - Datenbank einrichten & anbinden (Docker-Container oder lokal)
   - Nutzer-Modell erstellen (z. B. Name, Standort, Interessen)
   - Erste einfache Speicherung implementieren (z. B. Favoriten, Suchhistorie)

Woche 4 (01.06 – 09.06):

3. Containerisierung & erste Bereitstellung
  - Dockerfile erstellen (für App und Datenbank)
  - Docker-Compose zur lokalen Orchestrierung
  - Pipeline (CI/CD) für automatisierten Build & Push vorbereiten
  - Erstes Deployment über AWS (z. B. ECS, EC2, Elastic Beanstalk)

### Priorisierung

1. Priorität
2. Priorität
3. Priorität

### Aufgabenverteilung

Alle Aufgaben werden von Laura Dubach umgesetzt.

### Nächste Schritte

- Sprintreview findet am: statt

## Sprint 3: 10.06 – 07.07 (4 Wochen)

### Ziel: Feinschliff, Absicherung, Präsentationsvorbereitung

#### Woche 1–2 (10.06 – 24.06):

1. Feinschliff & Erweiterung
  - API absichern (z. B. API Key, Rate Limiting, CORS-Konfiguration)
  - Weitere Filteroptionen

#### Woche 3 (25.06 – 30.06):

1. Stabilisierung & Test
  - Integrationstests & End-to-End Tests
  - Fehlerbehandlung

#### Woche 4 (01.07 – 07.07):

3. Abschluss & Abgabevorbereitung
  - Technische Dokumentation
  - Fertigstellen Dokumentation
  - Optional: Demo-Frontend oder Swagger-Dokumentation
  - Präsentationsvorbereitung

### Priorisierung

1. Priorität
2. Priorität
3. Priorität

### Aufgabenverteilung

Alle Aufgaben werden von Laura Dubach umgesetzt.

### Nächste Schritte

- Sprintreview findet am: statt

# Sprint Reviews

## Sprint Review 1

| Besprechung | Datum | Uhrzeit | Teilnehmer | 
| ---- | ---- | ---- | ---- |
| 1 | 09.05.2025| 19:30 | Corrado Parisi, Laura Dubach |

1. Erreichte Sprintziel
2. Fertige Items
3. Feedback
4. Neue Erkenntnisse

### Besprechungsnotiz

## Sprint Review 2

| Besprechung | Datum | Uhrzeit | Teilnehmer | 
| ---- | ---- | ---- | ---- |
| 2 | 02.06.2025 | | Corrado Parisi, Laura Dubach |

1. Erreichte Sprintziel
2. Fertige Items
3. Feedback
4. Neue Erkenntnisse

### Besprechungsnotiz

## Sprint Review 3

| Besprechung | Datum | Uhrzeit | Teilnehmer | 
| ---- | ---- | ---- | ---- |
| 2 | 20.06.2025 | | Corrado Parisi, Laura Dubach |

1. Erreichte Sprintziel
2. Fertige Items
3. Feedback
4. Neue Erkenntnisse

### Besprechungsnotiz

> Back [Page](https://github.com/lauradubach/Semesterarbeit3/blob/main/README.md)
>
> Next [Page](https://github.com/lauradubach/Semesterarbeit3/blob/main/Sites/Teil%202%20Konzeption.md)