################################################################

import subprocess
import pandas as pd
import sys, getopt
import sys
import telegram_send
from statistics import median

##########################
#   VALEUR PAR DEFAUT
##########################

path="/home/moutonneux/bots/backtest/etudes-5m/"
csvName="tf5m-bullOnly-moyenne.csv"
minFinalBalanceToBeSaved=0.0

pathList = ('03-2022', '01-2022', '02-2022', '12-2021', '11-2021',  '10-2021',  '04-2022' , '09-2021' )

bestValue=0.0
#On récupère la meilleure performance moyenne dans le fichier déjà existant
#A la fin de l'execution on verra si une nouvelle meilleure performance a été trouvée
try :
    ancienClassement = pd.read_csv(path+"balance-"+csvName)
    bestValue=float(ancienClassement['finalBalanceMoyenne'].iloc[0])
except :
    print(f"Le fichier {path+csvName} n'a pas été trouvé, il va être créé")
    pass


#####################################################################
# Cette boucle nous permet de créer un fichier csv pour chaque mois
#####################################################################
classement = pd.DataFrame([])
classement.to_csv(path+csvName, index=False)
for mois in pathList:
    dataframe=pd.DataFrame([])
    del dataframe
    del classement
    classement = pd.DataFrame([])
    dataframe=pd.read_csv(path+mois+"/"+"algo-tf5m.csv")
    #On créé un fichier csv pour chaque mois, on enlève tout ce qui nous convient pas et on trie par finalBalance
    for index, row in dataframe.iterrows() :
        if row['finalBalance'] >= minFinalBalanceToBeSaved:
            parametres=f"{row['maxPositions']} {row['parametrePVO2']} {row['parametrePERF']} {row['parametreTRIX_HISTO']} {row['parametrePVO']} {row['parametreBOL_BANDwindowdev']} {row['parametreBOL_BANDwindow']} {row['parametreMACD']} {row['parametreEMA13D']} {row['parametreEMA9D']} {row['parametreEMA10']} {row['parametreEMA50']} {row['parametreEMA45']}"
            classement = classement.append(pd.DataFrame({
                'mois' : [mois],
                'finalBalance' : [row['finalBalance']],
                'bestTrade': [row['bestTrade']],
                'worstTrade': [row['worstTrade']],
                'drawDown': [row['drawDown']],
                'taxes': [row['taxes']],
                'totalTrades': [row['totalTrades']],
                'totalGoodTrades': [row['totalGoodTrades']],
                'totalBadTrades': [row['totalBadTrades']],
                'winRateRatio': [row['winRateRatio']],
                'tradesPerformance': [row['tradesPerformance']],
                'parametres': [parametres]
            }), ignore_index=True)
    classement=classement.sort_values(by=['finalBalance'], ascending=False)
    classement.to_csv(path+mois+".csv", index=False)

######################################################################################################################
# Ensemble de fonctions qui nous permettent de récupérer les résultats d'un mois spécifié pour des paramètres donnés
######################################################################################################################

def exist(df,parametres):
    for i, col in df.iterrows() :
        if col['parametres']==parametres :
            return True
    return False

def getFinalBalance(df, parametres):
    for i, col in df.iterrows() :
        if col['parametres']==parametres :
            return float(col['finalBalance'])
    return 0.0

def getBestTrade(df, parametres):
    for index, row in df.iterrows() :
        if row['parametres']==parametres :
            return float(row['bestTrade'])
    return 0.0

def getWorstTrade(df, parametres):
    for index, row in df.iterrows() :
        if row['parametres']==parametres :
            return float(row['worstTrade'])
    return 0.0

def getDrawDown(df, parametres):
    for index, row in df.iterrows() :
        if row['parametres']==parametres :
            return float(row['drawDown'])
    return 0.0

def getTaxes(df, parametres):
    for index, row in df.iterrows() :
        if row['parametres']==parametres :
            return float(row['taxes'])
    return 0.0

def getTotalTrades(df, parametres):
    for index, row in df.iterrows() :
        if row['parametres']==parametres :
            return int(row['totalTrades'])
    return 0.0

def getTotalGoodTrades(df, parametres):
    for index, row in df.iterrows() :
        if row['parametres']==parametres :
            return int(row['totalGoodTrades'])
    return 0.0

def getTotalBadTrades(df, parametres):
    for index, row in df.iterrows() :
        if row['parametres']==parametres :
            return int(row['totalBadTrades'])
    return 0.0

def getWinRateRatio(df, parametres):
    for index, row in df.iterrows() :
        if row['parametres']==parametres :
            return float(row['winRateRatio'])
    return 0.0

def getTradesPerformance(df, parametres):
    for index, row in df.iterrows() :
        if row['parametres']==parametres :
            return float(row['tradesPerformance'])
    return 0.0


del classement
classement = pd.DataFrame([])

###############################################################################################
# Cette boucle nous permet de créer le fichier csv qui nous permettra d'étudier nos résultats
###############################################################################################

df=pd.read_csv(path+pathList[0]+".csv")
for index, row in df.iterrows() :
    #Si on est à la première itération
    parametres=str(row['parametres'])
    nbOfMonth=0
    finalBalanceSum=0.0
    bestTradeSum=0.0
    worstTradeSum=0.0
    drawDownSum=0.0
    taxesSum=0.0
    totalTradesSum=0
    totalGoodTradesSum=0
    totalBadTradesSum=0
    winRateRatioSum=0.0
    tradesPerformanceSum=0.0
    pireFinalBalance=100000.0
    bestFinalBalance=0.0
    medianeList=[]
    for mois in pathList:
        df=pd.DataFrame([])
        del df
        df=pd.read_csv(path+mois+".csv")
        if (exist(df,parametres)):
            nbOfMonth=nbOfMonth+1
            finalBalance=getFinalBalance(df,parametres)
            medianeList.append(finalBalance)
            finalBalanceSum=finalBalanceSum+finalBalance
            bestTradeSum=bestTradeSum+getBestTrade(df,parametres)
            worstTradeSum=worstTradeSum+getWorstTrade(df,parametres)
            drawDownSum=drawDownSum+getDrawDown(df,parametres)
            taxesSum=taxesSum+getTaxes(df,parametres)
            totalTradesSum=totalTradesSum+getTotalTrades(df,parametres)
            totalGoodTradesSum=totalGoodTradesSum+getTotalGoodTrades(df,parametres)
            totalBadTradesSum=totalBadTradesSum+getTotalBadTrades(df,parametres)
            winRateRatioSum=winRateRatioSum+getWinRateRatio(df,parametres)
            tradesPerformanceSum=tradesPerformanceSum+getTradesPerformance(df,parametres)
            if (float(pireFinalBalance)>float(finalBalance)):
                pireFinalBalance=finalBalance
            if (float(bestFinalBalance)<float(finalBalance)):
                bestFinalBalance=finalBalance
    classement = classement.append(pd.DataFrame({
                    'nbOfMonth' : [nbOfMonth],
                    'finalBalanceMoyenne' : [finalBalanceSum/nbOfMonth],
                    'finalBalanceMediane' : [median(medianeList)],
                    'pireFinalBalance' : [pireFinalBalance],
                    'bestFinalBalance' : [bestFinalBalance],
                    'finalBalanceList' : [sorted(medianeList)],
                    'bestTradeMoyen': [bestTradeSum/nbOfMonth],
                    'worstTradeMoyen': [worstTradeSum/nbOfMonth],
                    'drawDownMoyen': [drawDownSum/nbOfMonth],
                    'taxesMoyenne': [taxesSum/nbOfMonth],
                    'totalTradesMoyen': [totalTradesSum/nbOfMonth],
                    'totalGoodTradesMoyen': [totalGoodTradesSum/nbOfMonth],
                    'totalBadTradesMoyen': [totalBadTradesSum/nbOfMonth],
                    'winRateRatioMoyen': [winRateRatioSum/nbOfMonth],
                    'tradesPerformanceMoyen': [tradesPerformanceSum/nbOfMonth],
                    'parametres': [parametres]
                }), ignore_index=True)
    print("Ajout de :\n", classement.tail(1))

#######################################
# On enregistre nos nouvelles données
#######################################

print("Trié par le nombre de mois où les paramètres existent :")
classement=classement.sort_values(by=['nbOfMonth'], ascending=False)
classement.to_csv(path+"nbOfMonth-"+csvName, index=False)
print(classement)

classement=classement.sort_values(by=['nbOfMonth', 'pireFinalBalance'], ascending=False)
classement.to_csv(path+"pireFinalBalance-"+csvName, index=False)
print("Trié par la pireFinalBalance:")
print(classement)

classement=classement.sort_values(by=['finalBalanceMoyenne'], ascending=False)
if (float(classement['finalBalanceMoyenne'].iloc[0]) > bestValue ) :
    print(f"Nouvelle meilleure performance trouvée : {float(classement['finalBalanceMoyenne'].iloc[0])}")
    #On envoit une notification telegram si une meilleure performance est trouvée
    telegram_send.send(messages=[f"Etude sur timeframe 5 minutes en bull uniquement :\n\nNouvelle meilleure performance trouvée sur {float(classement['nbOfMonth'].iloc[0])} mois : {float(classement['finalBalanceMoyenne'].iloc[0])}, avec une valeure médiane de {float(classement['finalBalanceMediane'].iloc[0])}, un pire résultat de {float(classement['pireFinalBalance'].iloc[0])} et un meilleur de {float(classement['bestFinalBalance'].iloc[0])}\nParamètres à utiliser : {float(classement['parametres'].iloc[0])}"])
classement.to_csv(path+"balance-"+csvName, index=False)
print("Trié par finalBalanceMoyenne :")
print(classement)