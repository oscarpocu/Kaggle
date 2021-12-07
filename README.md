# Pràctica Kaggle APC UAB 2021-22
### Nom: Oscar Pocurull Rodríguez
### DATASET: classification of websites
### URL: [kaggle](http://www.kaggle.com/hetulmehta/website-classification)
## Resum
Aquest dataset conté una llista de pàgines web on cadascuna està classificada segons la categoria a la que pertany.
En concret, conté 1408 entrades/dades (files) i 4 atributs (col·lumnes).
## Llista d'atributs
- 0: Unnamed: 0 -> (int64) Indica l'índex de la fila (pàgina web): [0,1,2,3,4...]. (L'eliminarem perque no ens aportarà cap informació rellevant).

- 1: website_url -> (object) Conté la URL de cada pàgina. És única: [www.algo.org, www.mosca.es...].

- 2: cleaned_website_text -> (object) Conté la llista de les paraules clau de la pàgina, i les podrem fer servir per estudiar a quina categoria pertanyen: [official site, good, hotel, vacation...].

- 3: Category -> (object) Té les categories de totes les pàgines web: [Adult, Travel...]. És el atribut objectiu.
## Objectius del dataset
Volem aprendre quina és la categoria ('Category') a la que pertanyen les diferents pàgines web del nostre dataset.
## Tractament de dades
Durant aquesta pràctica hem realitzat diferents experiments per tal de pulir el nostre dataset:
### Experiments
- He tret l'atribut index "Unnamed: 0" ja que no ens està aportant res.
- He probat a afegir l'atribut Category_id que conté un ID únic per cada categoria del nostre dataset (del 0 al 15).
- WORDCLOUD: mostra les paraules de cada categoria en una imatge, on aquestes seran més grans quan més vegades apareguin en la categoria seleccionada.
També he agregat un diccionari 'category_to_id' que conté cada 'Category' amb el seu valor: 'Category_id', per processar les dades mes endavant.

### Preprocessat
- No conté valors nuls en cap atribut, per tant no haurem de tractar-los.
- Com no tenim dades numériques (tret del index) tampoc podem treure outliers ni fer normalitzacions.
- Per a preprocessar les dades transformarem les nostres dades de text del 'cleaned_website_text' en números, tenint en compte la freqüéncia en la que surten les paraules: tf-idf.
- El tf-idf l'utilitzarem per trobar les 3 paraules (unigrams i bigrams) més correlacionades de cada categoria amb la funció chi2() de sklearn.feature_selection.
### Model
Tots els models probats han estat probats i executats en 75% train, 25% test i amb el cross-validation k-fold, amb k=5.
He probat a variar el train i el test en 80-20 o 50-50, he probat a canviar la k amb k=10, k=15... i els resultats no varien gaire. Penso que es degut a que les nostres dades son bastant petites per a que al modificar aquests paràmentres es crei un canvi significatiu.
| Model | Hiperparametres | Mètrica | Temps |
| -- | -- | -- | -- |
| [Random Forest](link) | 100 Trees, max_dept: 5 | 72% | 5227 ms |
| [LinearSVC](link) | penalty: l2, multi_class: ovr, max_iter: 1000 | 90% | 2304 ms |
| [MultinomialNB](link) | alpha: 1.0 | 85% | 812 ms |
| [GaussianNB](link) | var_smoothing: 1e-09 | 73% | 6173 ms |
| [Logistic Regression](link) | penalty: l2, C: 1, max_iter: 100 | 88% | 17900 ms |
| -- | -- | -- | -- |
## Demo
Per tal de fer una prova, es pot fer servir amb la següent comanda
``` python3 demo/demo.py --input here ```
## Conclusions
- El millor model que s'ha aconseguit ha estat el LinearSVC ja que te un accuracy molt alt (del 90%) i s'executa a una gran velocitat.
- En comparació amb altres treballs que he analitzat podem veure que eliminen els valors duplicats del cleaned_website_text (que passen a ser 1375 dades en comptes de 1408), però els resultats no varien gaire el percentatge del accuracy dels models ja que el LinearSVC segueix guanyant amb un 90%. En altres treballs han escollit el classificador de Bayes (multinomialNB) que entrenat normal (sense CV) arriba al 88% d'accuracy, i encara que jo segueixo preferint el LinearSVC, pot ser un model interessant.
## Idees per treballar en un futur
Crec que seria interesant indagar més en...
## Llicencia
El projecte s’ha desenvolupat sota llicència ZZZz.
