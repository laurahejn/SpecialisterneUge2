# Python Intro
Dette repository indeholder min besvarelse af anden uges opgaver. Hver delopgave har sin egen mappe således, at delopgave 1 ligger i mappen **Delopgave_1**, delopgave 2 ligger i mappen **Delopgave_2**, delopgave 3 ligger i mappen **Delopgave_3**, og delopgave 4 ligger i mappen **Delopgave_4**.

## Kom godt igang

### Afhængigheder
Før vi begynder er det en god ide at installere bibliotekerne *matplotlib*, *seaborn*, *wordcloud* og *pandas*. Dette gøres ved pip.
```bash
pip install mathplotlib
pip install seaborn
pip install wordcloud
pip install pandas
```

### Installation
Download hele repository'et - eller i hvert fald mappen **Data** og den delopgave, du er interesseret i. Måske programmet køres uden at downloade filerne, men i så fald ved jeg ikke hvordan.

## Sådan køres koden
Det er nok at vælge den fil, man gerne vil køre, og kalde den i python. Bemærk, at graferne skal lukkes før koden kan fortsætte.


## Kommentarer til processen og problemer med løsningen af opgaverne
### Delopgave 1
Det første problem, vi løb ind i, var at finde datasættet, når det lå i en anden mappe. Vi startede med at lave en lokal lappeløsning, hvor andre ville blive nødt til at ændre i direkte i kildekoden for at hente filen. Dette problem blev senere løst ved at se, hvad man skulle gøre i de følgende delopgaver.

Det næste problem opstod i installationen af ekstrapakker til Python. Min pip virkede ikke, men så geninstallerede vi Python og tilføjede denne gang Python til PATH, og så ville pip gerne være med. 

Endelig havde jeg ikke tidligere arbejdet med hverken *wordcloud* eller *seaborn*, så der skulle lidt googling til for at finde ud af, hvordan de skulle bruges. Jeg kunne heller ikke få *wordcloud* til at virke med strenge, men det kom vi udenom ved at bruge en frekvensdictionary istedet.

### Delopgave 2
Denne opgave løste mine problemer med at indlæse datasættet i delopgave 1. I hvert fald hvis vi har løst det her rigtigt.

Vi havde store problemer med at få sat de rette tillader op for at få lov til at oprette dokumenterne til at lagere vores resultater. Det krævede, så vidt jeg kunne se, at vores directory havde tilladelse 777 fremfor blot 755. Dette er godt nok lidt problematisk i forhold til idiotsikring, men det vides ikke helt, hvordan det ellers skal løses.

Sidste del af denne opgave består af et sanity tjek. Jeg var ret usikker på, hvad det præcist skulle indebære, og jeg er ikke helt sikker på, at jeg har løst det rigtigt. Vi endte med at tjekke resultatet af koden ved at sortere på en anden måde og sammenligne de to resultater. Hvis 'Delopgave_2\test\forventningsafstemningstest.py' kører, bør der ikke være nogle problemer. Hvis der er uoverensstemmelser, bør en AssertionError forekomme.

### Delopgave 3
Her havde vi problemer med at regne den overordnede struktur af koden ud. Jeg skulle lige regne ud, hvordan det var bedst at sætte tingene op, og hvordan man kunne stoppe programmet, når det ikke gav mening at fortsætte det. Det blev lidt et spørgsmål om, hvornår det var smartest at bruge try-except og if-udsagn, og ikke mindst hvilke meddelser de skulle give os. 

Det var også besværligt at finde på de forskellige faldgruber. Især fordi jeg ikke har arbejdet med CSV filer før, så her var lidt kreativ googlesøgning også påkrævet. 

En ting var også at identificere mulige fejl, men så skulle man også regne ud, hvilken form fejlmeddelsen ville tage - eller det var nok i virkeligheden ikke nødvendigt, man kunne nok godt have lavet det lidt mere generelt, men opgaven bad om specifikationer.

### Delopgave 4
Her drillede specifikationerne af det, som vi skulle plotte, mig en smule. En ting var, hvilken gruppering var ønsket, men så skulle vi også lige finde ud af, hvad denne gruppering skulle vise. 

Jeg kan ikke lide at eksperimentere med data. Jeg synes, det er svært at finde på noget at undersøge. 



## Forfatter
Laura Brædder

laura.braedder@specialisterne.dk

