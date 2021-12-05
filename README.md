# Pràctica Kaggle APC UAB 2021-22
### Nom: Oscar Pocurull Rodríguez
### DATASET: classification of websites
### URL: [kaggle](http://www.kaggle.com/hetulmehta/website-classification)
## Resum
Aquest dataset conté una llista de pàgines web on cadascuna està classificada segons la categoria a la que pertany.
En concret, conté 1408 entrades/dades (files) i 4 atributs (col·lumnes).
## Llista d'atributs
#0: Unnamed: 0 -> (int32) Indica l'índex de la fila (pàgina web): [0,1,2,3,4...].
#1: website_url -> (object) Conté la URL de cada pàgina. És única: [www.algo.org, www.mosca.es...].
#2: cleaned_website_text -> (object) Conté la llista de les paraules clau de la pàgina, i les podrem fer servir per estudiar a quina categoria pertanyen: [official site, good, hotel, vacation...].
#3: Category -> (object) Té les categories de totes les pàgines web: [Adult, Travel...]. És el atribut objectiu.
### Objectius del dataset
Volem aprendre quina és la categoria ('Category') a la que pertanyen les diferents pàgines web.
## Tractament de dades
Durant aquesta pràctica hem realitzat diferents experiments.
# Observacions
No conté valors nuls en cap atribut, per tant no haurem de tractar-los.
Com no tenim dades numériques (tret del index) tampoc podem treure outliers ni fer normalitzacions.
# Experiments
Hem tret l'atribut index "Unnamed: 0" ja que no ens està aportant res.

### Preprocessat
Quines proves hem realitzat que tinguin a veure amb el pre-processat? com han afectat als resultats?
### Model
| Model | Hiperparametres | Mètrica | Temps |
| -- | -- | -- | -- |
| [Random Forest](link) | 100 Trees, XX | 57% | 100ms |
| Random Forest | 1000 Trees, XX | 58% | 1000ms |
| SVM | kernel: lineal C:10 | 58% | 200ms |
| -- | -- | -- | -- |
| [model de XXX](link al kaggle) | XXX | 58% | ?ms |
| [model de XXX](link al kaggle) | XXX | 62% | ?ms |
## Demo
Per tal de fer una prova, es pot fer servir amb la següent comanda
``` python3 demo/demo.py --input here ```
## Conclusions
El millor model que s'ha aconseguit ha estat...
En comparació amb l'estat de l'art i els altres treballs que hem analitzat....
## Idees per treballar en un futur
Crec que seria interesant indagar més en...
## Llicencia
El projecte s’ha desenvolupat sota llicència ZZZz.
