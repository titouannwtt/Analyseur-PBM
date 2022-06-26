<div id="top"></div>

[![LinkedIn][linkedin-shield]][linkedin-url]

# Analyseur-PBM
Analyseur-PBM, pour "Analyse des Paramètres de Backtests par Mois".

## Contexte, pourquoi Analyser-PBM a été conçu ?

Dans le cadre d'un bot de trading, on applique des conditions d'achats et de ventes (ce que l'on appelle "stratégie") sur des périodes passées à travers une simulation. Cette simulation est appelé "Backtest" (test sur le passé).
Si ce backtest donne des résultats performants, c'est qu'il a été capable d'acheter et de vendre au bon moment pour réaliser du profit, on peut donc en conclure que la stratégie utilisée lors de ce backtest est "rentable" sur cette période.
On peut émettre l'hypothèse que si cette stratégie a fonctionné par le passé, elle fonctionnera généralement tout le temps, et de cette façon si on l'applique à bot de trading qui l'applique en temps réel : on fera du profit.
Le problème de cette façon de procéder est qu'on tombe rapidement dans de la sur-optimisation, consistant à avoir des paramètres optimaux pour un mois précis mais en réalité peu efficient, voir complètement catastrophique sur une autre période.

Dans notre cas, on va réaliser des backtests sur une période de 1 mois avec des paramètres d'entrées différents, c'est à dire que pour chaque mois, on aura les résultats de notre stratégie selon la variation de tel ou tel paramètres.
Ces backtests produisent des fichiers csv respectifs (un pour chaque mois) contenant les paramètres essayés et les performances que ces paramètres ont eu sur le mois donné. 

Ainsi, pour chaque mois nous connaissons les résultats des paramètres donnés, autrement dit on est capable explicitement de dire : "tel mois, tel paramètres a permis une performance de tant."

On a donc pleins de paramètres, on sait que tel paramètre réalise telle performance tel mois, mais d'un mois à l'autre : les meilleurs paramètres ne sont généralement pas les mêmes à cause de la sur-optimisation expliquée plus haut.

Analyseur-PBM centralise l'ensemble des résultats de ces backtests pour chaque mois, selon les paramètres d'entrée. Il va récupérer les résultats de tous les mois, inspecter les paramètres et faire des moyennes de performances par paramètres d'entrées tout mois confondue.
Ainsi pour chaque paramètres nous pourrons déterminer des informations telles que les performances moyennes sur tous les mois, les pires et les meilleures performances, savoir quand elles ont eu lieu, etc. et ainsi se détacher de la sur-optimisation sur un mois précis et essayer d'obtenir des paramètres qui sont profitable sur chaque mois.

## Comment utiliser Analyseur-PBM ?

Avant toutes choses, sachez que j'ai initialement conçu ce code dans mon intérêt personnel, il est donc adapté à mes besoins.
A noter également que je ne partage que la partie Analyseur-PBM qui s'occupe du regroupement des fichiers CSV contenant les informations des backtests par mois.
Le code que j'utilise pour faire mes backtests, ainsi que les stratégies qu'ils inclus ne sont pas partagées.
En revanche l'ensemble des résultats des backtests d'exemple sont partagés à travers les fichiers CSV.
Autrement dit cet analyseur vous permettra de vérifier au sein de votre stratégie si les paramètres d'entrées sont sur-optimisés sur une période précise ou si ils sont de manière générales optimisés, au cas quel cas on pourra considérer que votre stratégie est rentable sur toutes périodes avec ces paramètres.

Ce code vous sera donc utile si vous avez déjà une stratégie, que vous savez mettre en place des backtests selon cette stratégie, et que vous savez enregistrer les résultats de ces backtests dans un fichier csv avec les colonnes suivantes : 
dates, finalBalance, perfVSUSD, holdPercentage, vsHoldPercentage, bestTrade, worstTrade, drawDown, taxes, totalTrades, totalGoodTrades, totalBadTrades, winRateRatio, tradesPerformance, averagePercentagePositivTrades, averagePercentageNegativTrades, startingBalance, (... vos paramètres ...)

## A quoi sert quel fichier/dossier ?

- analyseurPBM.py est le code principal qui va récupérer les csv présents dans les dossiers de 01-2022 à 12-2021, il va ensuite dans un premier temps, les trier et les mettres à sa racine (les fichiers de 01-2022.csv à 12-2021.csv) puis croiser les paramètres communs pour établir des moyennes de performances qu'il enregistrera dans "balance-tf5m-bullOnly-moyenne.csv", "nbOfMonth-tf5m-bullOnly-moyenne...csv", "pireFinalBalance-tf5m-bullOnly-moy...csv" 

- Les dossiers de 01-2022 à 12-2021 contiennent un code python nommé "algo" qui permet de lancer à répétition backtest.py sur une période de 1 mois avec des paramètres qui s'incrémentent. A chaque lancement de backtest.py, les performances réalisés par le backtest avec les paramètres données sont enregistrés dans un fichier csv créé dans ce même dossier.

- Le dossier "database" contient toutes les données historiques permettant aux backtests de faire leur simulation

- Le dossier "utilities" contient tous les fichiers python nécessaires à l'execution du backtest, [source](https://github.com/CryptoRobotFr/cBot-Project/tree/main/utilities)

- les fichiers de 01-2022.csv à 12-2021.csv contiennent les résultats de chaque combinaison de paramètres avec les résultats triés selon la meilleure performance. Ces fichiers sont générés par le code analyseurPBM.py

- "balance-tf5m-bullOnly-moyenne.csv", "nbOfMonth-tf5m-bullOnly-moyenne...", "pireFinalBalance-tf5m-bullOnly-moy..." sont 3 fichiers csv qui regroupent l'ensemble des paramètres avec leurs performances par mois. Triés respectivement selon la finalBalance, le nombre de mois et la pire perf. Ces fichiers sont générés par "analyseurPBM.py" à la fin de son execution.

# Remerciement :
Ce code vous est partagé gratuitement, vous pouvez me remercier en utilisant un de mes liens d'affiliations :

- FTX : https://ftx.com/eu/profile#a=titouannwtt

- Binance : https://www.binance.me/fr/activity/referral/offers/claim?ref=CPA_00C08H2X8E

Ou en me faisant des dons cryptos :

- Adresse BTC : 3GYhBgZMfgzqjYhVhc2w53oMcvZb4jfGfL

- Adresse ETH (Réseau ERC20) : 0x43fC6F9B8b1CfBd83b52a1FD1de510effe0A49a7

- Adresse SOL : 5QKaHfJWxAZ6sbU5QMb2e14yAAZ45iBH91SBgnheK26v

<p align="right">(<a href="#top">back to top</a>)</p>

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/titouan-wtt/
