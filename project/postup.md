# Podklady k fakturaci Resibo

## Cíle

Cílem je vytvoření aplikace, která dokáže jednoduše a rychle visualisovat, zda došlo u jednotlivých odběratelů ke změně čerpání služeb (licencí) ve srovnání s předchozím fakturačním obdobím.

## Funkční požadavky

### Základní

1. Naimportovat aktuální přehled čerpání služeb ze souboru ve formátu CSV.
2. Udržovat historii již naimportovaných přehledů z minulých období (minimálně z toho posledního).
3. Porovnat čerpání licencí (služeb) mezi aktuálním obdobím a obdobím předcházejícím v přijatelné visuální formě.

### Volitelné

1. Umožnit filtrování za zákazníky, u kterých došlo ke změně v čerpaných licencích (službách).
2. Zobrazit trend vývoje čerpaných licencí (služeb) za zákazníka.

## Technické požadavky

1. Ideálně by řešení mělo být nezávislé na externích komponentách nebo službách (SQL server, cloud, atd.).

## Řešení

### Komponenty

Naimportovaná data budou uložena v souborové databázi SQLite. Soubor bude součástí projektového adresáře. Pravděpodobně nebude pushován na GitHub.

Originální CSV soubory nebudou uloženy společně s projektem. Dále budou data v CSV souborech anonymizována.

Pro visualisaci bude použit Flatpak a pro práci s databází modul SQLAlchemy.

### Struktura

~~Třídy a metody pro založení neexistující databáze budou v odděleném zdrojovém souboru 'base.py'.~~

~~(Třída pro import bude v odděleném zdrojovém souboru 'import.py'.)~~

