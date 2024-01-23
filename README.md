# Estudi de programes de televisió
Fem una anàlisi dels més de 159.000 programes de televisió que hem obtingut 
a través de la base de dades _The Movie Database (TMDB)_. L'objectiu d'aquesta anàlisi
és poder trobar aquells programes populars que permetin fer un bon plantejament 
a l'hora d'adquirir les llicències per emetre'ls.  
L'estudi està separat en 5 exercicis. Un primer per tal de descomprimir els fitxers
amb què treballem, el segon per processar les dades, el tercer per filtrar dades,
el quart on farem una anàlisi més gràfica i acabem amb unes conclusions generals.

## Instal·lació del projecte
Per tal de poder executar bé el projecte primer s'hauria de fer una instal·lació prèvia
de certes llibreries que es fan servir. Per això recomanem primer muntar un entorn
virtual. I un cop ja el teniu, executeu la següent comanda. 
```shell
pip install -r requirements.txt
```

## Executar el projecte
Un cop ja estan les llibreries instal·lades, podem executar el projecte. Ho podem fer
de dues maneres. Per una banda, podem executar el projecte sencer o si no podem 
executar els exercicis que ens interessi. Comencem amb el primer cas. Per veure
tots els exercicis haurem d'executar la següent comanda:
```shell
python main.py
```
En cas de voler executar algun o alguns exercicis en concret els haurem d'especificar
com a arguments dins de la comanda. Veiem un exemple en què vulguem veure els 
resultats de l'exercici 3. 
```shell
python main.py 3
```
Si fos el cas que en volguéssim veure més d'un, els hauríem de posar igual com a 
arguments separats. Posem per cas que volem veure els exercicis 1 i 4:
```shell
python main.py 1 4
```

De cara al primer exercici, cal tenir en compte que per defecte buscarà l'arxiu 
per descomprimir a la ruta ```./data/TMDB.zip```. En cas de no trobar-lo, el terminal
demanarà la ruta de l'arxiu.  
I per l'exercici 4 cal tenir en compte que perquè se segueixi executant s'han 
d'anar tancant els gràfics. Un cop es tanqui el gràfic, el programa seguirà amb 
el següent.

## Executar els tests
Per tal d'executar els tests d'aquest projecte s'haurà d'executar la següent comanda:
```shell
 python3 -m tests.test_public
```
Això executarà els tests i per veure els resultats haurem d'accedir a la carpeta 
```reports```. Allà hi trobarem, entre altres coses, un arxiu html que conté el 
resultat de tots els tests de ```test_public.py```. 