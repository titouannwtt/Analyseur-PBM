# Analyseur-PBM
Analyseur-PBM, pour "Analyse des Paramètres de Backtests par Mois".

## Contexte, pourquoi Analyser-PBM a été conçu ?

Des backtests sont réalisés sur une période de 1 mois avec des paramètres d'entrées différents, ces backtests produisent des fichiers csv contenant les paramètres essayés et les performances que ces paramètres ont eu sur le mois données. 
Ainsi, pour chaque mois nous connaissons les résultats de paramètres donnés, autrement dit on est capable explicitement de dire : "tel mois, tel paramètres a permis une performance de tant.", le problème de cette façon de procédé est qu'on tombe rapidement dans de la sur-optimisation, consistant à avoir des paramètres optimaux pour un mois précis mais en réalité peu efficient, voir complètement catastrophique sur une autre période.

On a donc pleins de paramètres, on sait que tel paramètre réalise telle performance tel mois, mais d'un mois à l'autre : les meilleurs paramètres ne sont généralement pas les mêmes à cause de la sur-optimisation.

Analyseur-PBM centralise l'ensemble des résultats de ces backtests pour chaque mois, selon les paramètres. Il va récupérer les résultats de tous les mois, inspecter les paramètres et faire des moyennes de performances par paramètres d'entrées tout mois confondue 
Ainsi pour chaque paramètres nous pouvons déterminer des informations telles que les performances moyennes sur tous les mois, les pires et les meilleures performances (qui nous donnent une idée claire de la sur-optimisation), savoir quand elles ont eu lieu, etc.

## Comment utiliser Analyseur-PBM ?

Avant toutes choses, sachez que j'ai initialement conçu ce code dans mon intérêt personnel, il est donc adapté à mes besoins.
A noter également que je ne partage que la partie Analyseur-PBM qui s'occupe du regroupement des fichiers CSV contenant les informations des backtests par mois, le code que j'utilise pour faire mes backtests, ainsi que les stratégies qu'ils inclus ne sont pas partagées.
En revanche l'ensemble des résultats d'un backtest d'exemple sont partagés à travers les fichiers CSV.

Ce code vous sera donc utile si vous avez déjà une stratégie, que vous savez mettre en place des backtests selon cette stratégie, et que vous savez enregistrer les résultats de ces backtests dans un fichier csv avec les colonnes suivantes : 
dates, finalBalance, perfVSUSD, holdPercentage, vsHoldPercentage, bestTrade, worstTrade, drawDown, taxes, totalTrades, totalGoodTrades, totalBadTrades, winRateRatio, tradesPerformance, averagePercentagePositivTrades, averagePercentageNegativTrades, startingBalance, (... vos paramètres ...)

