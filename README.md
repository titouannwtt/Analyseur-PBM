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

blabla
