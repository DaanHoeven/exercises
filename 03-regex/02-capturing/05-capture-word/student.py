import re

text = """1987-2009: Beginjaren
Kendrick Lamar is geboren in Compton, Californië, een voorstad ten zuidoosten van Los Angeles. Zijn ouders kwamen uit Chicago, Illinois. Op zijn achtste was Kendrick getuige van het filmen van de Tupac Shakur en Dr. Dre music video over hun hitsingle "California Love". In 2003 bracht Kendrick zijn eerste mixtape uit, Youngest Head Nigga In Charge onder de naam K. Dot. De mixtape zorgde voor genoeg aandacht om een platencontract met Top Dawg Entertainment, een platenmaatschappij in Los Angeles, te krijgen. Hij bracht twee jaar later een mixtape uit die Training Day genoemd werd. Na het ontvangen van een co-sign van Lil Wayne bracht hij een derde mixtape uit in 2009 onder de naam C4, gethematiseerd rond Tha Carter III LP. Kort daarna, besloot hij zijn stage name, K. Dot op te geven en met zijn geboortenaam verder te gaan.

2010-2011: Overly Dedicated en Section. 80
In 2010 toerde hij met Tech N9ne en Jay Rock op The Independent Grind Tour. Op 23 september 2010 kwam de mixtape O(verly) D(edicated) uit, met het nummer Ignorance is Bliss. Naar aanleiding hiervan wilde hiphopproducer Dr. Dre met hem samenwerken.

Op 2 juli 2011 werd zijn derde solo project Section.80 uitgebracht. Section 80 is een conceptalbum en Lamar liet weten dat het album gemaakt is voor mensen die in de jaren '80 geboren zijn. Met liedjes die gaan over Ronald Reagan en over de 'crack epidimic' in de States werd dit al snel duidelijk. Maar Lamar behandelt ook een heleboel andere onderwerpen op dit album en rapt vanuit verschillende perspectieven. In de tweede helft van 2011 verscheen Kendrick Lamar op Game's The R.E.D. Album, Tech N9ne's All 6's and 7's, 9th Wonder's The Wonder Years en Drake's Take Care."""


def count_word_in_text(text, word):
    text_in_lowercase = text.lower()
    return len(re.findall(rf"{word}", text_in_lowercase))


print(count_word_in_text(text, "zijn"))
