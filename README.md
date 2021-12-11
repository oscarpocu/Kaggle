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
- Les webs duplicades s'han eliminat, per tant hem reduït el dataset de 1408 dades a 1384.
- He probat a afegir l'atribut Category_id que conté un ID únic per cada categoria del nostre dataset (del 0 al 15).
- WORDCLOUD: mostra les paraules de cada categoria en una imatge, on aquestes seran més grans quan més vegades apareguin en la categoria seleccionada.
- També he agregat un diccionari 'category_to_id' que conté cada 'Category' amb el seu valor: 'Category_id', per processar les dades mes endavant.

### Preprocessat
- No conté valors nuls en cap atribut, per tant no haurem de tractar-los.
- Com no tenim dades numériques (tret del index) tampoc podem treure outliers ni fer normalitzacions.
- Per a preprocessar les dades transformarem les nostres dades de text del 'cleaned_website_text' en números, tenint en compte la freqüéncia en la que surten les paraules: tf-idf.
- Paràmetres del tf-idf -> min_df: 6 (si es mes gran dona pitjor accuracy, si es mes petit mes temps triga), ngram_range(1,2) (per unigrams i bigrams), stop_words='english'.
- El tf-idf l'utilitzarem per trobar les 3 paraules (unigrams i bigrams) més correlacionades de cada categoria amb la funció chi2() de sklearn.feature_selection.
### Model
Tots els models probats han estat probats i executats en 70% train, 30% test i amb el cross-validation k-fold, amb k=5.
He probat a variar el train i el test en 80-20 o 50-50 i els resultats no varien gaire.
A mesura que la k del CV s'anava augmentant de valor, els resultats eren millors, pero el temps d'execució augmenta molt. Per tant he agafat la k=5 perque és molt bó en rendiment i temps.
| Model | Hiperparametres | Mètrica | Temps |
| -- | -- | -- | -- |
| [Random Forest](link) | 100 Trees, max_dept: 5 | 68% | 5227 ms |
| [Random Forest](link) | 100 Trees, max_dept: inf | 83% | 17310 ms |
| [LinearSVC](link) | penalty: l2, multi_class: ovr, max_iter: 1000 | 91% | 2304 ms |
| [MultinomialNB](link) | alpha: 1.0 | 85% | 812 ms |
| [GaussianNB](link) | var_smoothing: 1e-09 | 73% | 6173 ms |
| [Logistic Regression](link) | penalty: l2, C: 1, max_iter: 100 | 89% | 17900 ms |
## Resultats
- He escollit el model LinearSVC per fer les proves finals:
Un cop calibrat el nostre classificador ens dona un score força alt del 94% amb molt poques errades que es poden veure en la matriu de confusió.
- Aplicant només unigrames al tf-idf: s'executa una mica mes ràpid, baixa lleugerament l'accuracy del GaussianNB. 

| Model | Hiperparametres | Mètrica | Temps |
| -- | -- | -- | -- |
| [Random Forest](link) | 100 Trees, max_dept: inf | 84% | 13776 ms |
| [LinearSVC](link) | penalty: l2, multi_class: ovr, max_iter: 1000 | 91% | 1511 ms |
| [MultinomialNB](link) | alpha: 1.0 | 85% | 420 ms |
| [GaussianNB](link) | var_smoothing: 1e-09 | 64% | 3365 ms |
| [Logistic Regression](link) | penalty: l2, C: 1, max_iter: 100 | 89% | 13563 ms |
- Aplicant només bigrames al tf-idf: s'executa molt més ràpid ja que no hi han tantes paraules. En general els accuracys baixen aproximadament un 15%.

| Model | Hiperparametres | Mètrica | Temps |
| -- | -- | -- | -- |
| [Random Forest](link) | 100 Trees, max_dept: inf | 65% | 17830 ms |
| [LinearSVC](link) | penalty: l2, multi_class: ovr, max_iter: 1000 | 76% | 555 ms |
| [MultinomialNB](link) | alpha: 1.0 | 71% | 195 ms |
| [GaussianNB](link) | var_smoothing: 1e-09 | 74% | 1700 ms |
| [Logistic Regression](link) | penalty: l2, C: 1, max_iter: 100 | 73% | 4926 ms |
## Conclusions
- El millor model que s'ha aconseguit ha estat el LinearSVC ja que de tots els models probats te el accuracy més alt i s'executa a una gran velocitat.
- En comparació amb altres treballs que he analitzat podem veure que eliminen els valors duplicats del cleaned_website_text (que passen a ser 1375 dades en comptes de 1408), però els resultats no varien gaire el percentatge del accuracy dels models ja que el LinearSVC segueix guanyant amb un 91%. En altres treballs han escollit el classificador de Bayes (multinomialNB) que entrenat normal (sense CV) arriba al 89% d'accuracy, i encara que jo segueixo preferint el LinearSVC, pot ser un model interessant.
## Idees per treballar en un futur
Crec que seria interesant indagar més en optimitzar més les dades de text per aconseguir resultats millors amb el balanç de millor temps i rendiment.
## Llicencia
El projecte s’ha desenvolupat sota llicència del Jupyter Notebook 6.1.4.
