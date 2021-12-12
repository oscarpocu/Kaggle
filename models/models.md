# Pràctica Kaggle APC UAB 2021-22
### Nom: Oscar Pocurull Rodríguez
### DATASET: classification of websites
### URL: [kaggle](http://www.kaggle.com/hetulmehta/website-classification)

### Models
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
- He escollit el model LinearSVC per fer les proves finals:
Un cop calibrat el nostre classificador ens dona un score força alt del 94% amb molt poques errades que es poden veure en la matriu de confusió.
- També he probat a calcular el accuracy amb el Pipeline en comptes del cross-validation k=5. En general triga uns 5 minuts (molt més que amb el cv) i l'accuracy es del 89% (en comptes del 94% amb el cv).
- He probat amb SVC i amb NuSVC de la llibreria libsvc, pero en general han donat resultats inferiors al LinearSVC i sobretot triguen molt de temps en executar-se:
- SVC kernel:'rbf' = 87% accuracy. (temps d'execució = 260 seg)!
- SVC kernel:'linear' = 90% accuracy. (temps d'execució = 240 seg)!
- SVC kernel:'linear', C=100 = 83% accuracy. (temps d'execució = 240 seg)!
- SVC kernel:'poly' = 43% accuracy. (temps d'execució = 250 seg)!
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

