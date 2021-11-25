# liedbase_python
LiedBase, maar dan in Python geschreven

# Installatie en afhankelijkheden
* De inhoud van deze repository
* python3
* pip3

Installeren van benodigde bibliotheken:
```pip3 install -r requirements.txt```

Vaste gegevens qua bestandsnamen:
* Invoerbestand moet de naam 'liturgie.txt' hebben
* Het te gebruiken PowerPoint template moet de naam 'template.pptx' hebben
* Het resultaat bestand heet 'presentatie.pptx'

Uitvoeren door:
```python3 liedbase.py```

Template analyse uitvoeren:
```python3 liedbase.py analyze```

Hiermee wordt een pptx gegenereerd met de namen van alle text placeholders voor eventuele aanpasing van het template (vereist ook aanpassingen in de code)

# Regels voor liturgie.txt
Alle regels in de inputfile die beginnen met '#' worden genegeerd. Verder is het alleen mogelijk om liederen en bijbelteksten te genereren via deze versie van liedbase. Andere slides moeten achteraf handmatig worden toegevoegd.

## Bijbelteksten
Bijbelteksten moeten altijd worden opgegeven met een van en een tot vers. Ook als er maar 1 vers wordt bedoeld.

*Let Op*: Er zijn een paar gecombineerde verzen, bijvoorbeeld Genesis 10: 21-25. Daarbij is het niet mogelijk om vers 24 op te geven.

### formaat
[boek] [hoofdstuk] : [van] - [tot]

## Voorbeelden
genesis 2: 2 - 6

1 johannes 1: 6-6

## Liederen
Bij de liederen moeten alle verzen altijd worden uitgeschreven als een komma-gescheiden lijst. Enige uitzondering hierop zijn de opwekkingsliederen aangezien deze geen verzen kennen.

### formaat
[liedbundel] [liednummer] : [vers] (, [vers])*

### Voorbeelden
psalm 7: 1,2,3

opwekking 45