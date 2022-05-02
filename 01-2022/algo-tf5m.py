################################################################

import subprocess
import pandas as pd
import sys, getopt
import sys
import telegram_send
import configparser

##########################
#   VALEUR PAR DEFAUT
##########################

cfg = configparser.ConfigParser()
cfg.read('mois.cfg')
fichierEnregistrement="backtest.csv"

argumentList = sys.argv[1:]
try:
    substring = ".csv"

    if substring in sys.argv[1]:
        fichierEnregistrement=sys.argv[1]
        print("Enregistrement des données dans : ", fichierEnregistrement)
        print("Si des données étaient déjà présente dans le fichier, elles ont été supprimées\n")
        classement = pd.DataFrame([])
        try :
            classement = pd.read_csv(fichierEnregistrement)
        except :
            print(f"Le fichier {fichierEnregistrement} n'existe pas, nous allons le créer.")
    else:
        print("Vous devez spécifier un fichier .csv\npython3 algorithme.py <nom-du-fichier.csv>")
        exit()
except :
    print("Vous devez specifier un nom de fichier csv :\npython3 algorithme.py <nom-du-fichier.csv>")
    exit()

dateAnnee=str(cfg['DATE']['annee']) #1
dateMois=str(cfg['DATE']['mois']) #2
dateJour='01' #3
startingBalance = 1000 #4

# maxPositions
#entre 2 et 3 avec un pas de 1
maxPositionsdefault = 2 
maxPositionsmin = 2
maxPositionsmax = 3
maxPositionspas = 1
maxPositionsuse = 'true' #pour utiliser ce paramètre ou non
maxPositions = maxPositionsdefault

# parametrePVO2default
#Pour le moment l'algo précedent n'a pas dépassé le -2
#entre -10 et 10 avec un pas de 5
parametrePVO2default = -20
parametrePVO2min = -5
parametrePVO2max = 10
parametrePVO2pas = 5 #default 5
parametrePVO2use = 'true' #pour utiliser ce paramètre ou non
parametrePVO2 = parametrePVO2default

# parametrePERF
#Compliqué de savoir ça ossille entre 30 et 10
#entre 20 et 35 avec un pas de 5
parametrePERFdefault = 30
parametrePERFmin = 0
parametrePERFmax = 30
parametrePERFpas = 10
parametrePERFuse = 'true' #pour utiliser ce paramètre ou non
parametrePERF = parametrePERFdefault

# parametreTRIX_HISTO
#entre -0.2 et 0.2 avec un pas de 0.1
parametreTRIX_HISTOdefault = -10.0
parametreTRIX_HISTOmin = -10.0
parametreTRIX_HISTOmax = 0.0
parametreTRIX_HISTOpas = 10.0
parametreTRIX_HISTOuse = 'true'
parametreTRIX_HISTO = parametreTRIX_HISTOdefault

# parametrePVO
#On a les meilleurs perfs entre 8,9 et 10
#entre 5 et 15 avec un pas de 2
parametrePVOdefault = 9
parametrePVOmin = 0
parametrePVOmax = 20
parametrePVOpas = 5 #default 2
parametrePVOuse = 'true'
parametrePVO = parametrePVOdefault


#parametreBOL_BANDwindowdev
#entre 1.8 et 3.0 avec un pas 0.4
parametreBOL_BANDwindowdevdefault = 1.6
parametreBOL_BANDwindowdevmin = 1.2
parametreBOL_BANDwindowdevmax = 2.8
parametreBOL_BANDwindowdevpas = 0.4 #default 0.4
parametreBOL_BANDwindowdevuse = 'true'
parametreBOL_BANDwindowdev = parametreBOL_BANDwindowdevdefault

#parametreBOL_BANDwindow
#entre 15 et 35 avec un pas de 2
parametreBOL_BANDwindowdefault = 25
parametreBOL_BANDwindowmin = 20
parametreBOL_BANDwindowmax = 40
parametreBOL_BANDwindowpas = 10
parametreBOL_BANDwindowuse = 'true'
parametreBOL_BANDwindow = parametreBOL_BANDwindowdefault

#parametreMACD
#entre 10 et 30 avec un pas de 2
parametreMACDdefault = 20
parametreMACDmin = 10
parametreMACDmax = 40
parametreMACDpas = 10
parametreMACDuse = 'false'
parametreMACD = parametreMACDdefault

#parametreEMA13D
#entre 250 et 400 avec un pas de 50
parametreEMA13Ddefault = 312
parametreEMA13Dmin = 250
parametreEMA13Dmax = 400
parametreEMA13Dpas = 50
parametreEMA13Duse = 'false'
parametreEMA13D = parametreEMA13Ddefault

#parametreEMA9D
#entre 150 et 350 avec un pas de 50
parametreEMA9Ddefault = 216
parametreEMA9Dmin = 150
parametreEMA9Dmax = 350
parametreEMA9Dpas = 50
parametreEMA9Duse = 'false'
parametreEMA9D = parametreEMA9Ddefault

#parametreEMA10
#entre 8 et 14 avec un aps de 2
parametreEMA10default = 10
parametreEMA10min = 8
parametreEMA10max = 14
parametreEMA10pas = 2
parametreEMA10use = 'false'
parametreEMA10 = parametreEMA10default

#parametreEMA50
#entre 40 et 60 avec un pas de 2
parametreEMA50default = 50
parametreEMA50min = 40
parametreEMA50max = 60
parametreEMA50pas = 2
parametreEMA50use = 'false'
parametreEMA50 = parametreEMA50default

#parametreEMA45
#entre 40 et 50 avec un aps de 2
parametreEMA45default = 45
parametreEMA45min = 40
parametreEMA45max = 50
parametreEMA45pas = 2
parametreEMA45use = 'false'
parametreEMA45 = parametreEMA45default

bestFinalBalance = 0

i=0

#================================================================================================================
#   FONCTION QUI LANCE LE BACKTEST AVEC LES PARAMETRES D'ENTREES ET ENREGISTRE LE RESULTAT DANS UN FICHIER CSV
#================================================================================================================
def launch_backtest():
    
    print(f"Lancement du backtest avec les paramètres : {dateAnnee} {dateMois} {dateJour} {startingBalance} {maxPositions} {parametrePVO2} {parametrePERF} {parametreTRIX_HISTO} {parametrePVO} {parametreBOL_BANDwindowdev} {parametreBOL_BANDwindow} {parametreMACD} {parametreEMA13D} {parametreEMA9D} {parametreEMA10} {parametreEMA50} {parametreEMA45}")
    global i
    global classement
    i=i+1
    pourcent=round(100*i/count,4)
    print(f"Avancement total d'execution : {i}/{count} ({pourcent}%)")
    if ((classement['maxPositions'] == maxPositions) & (classement['parametrePVO2'] == parametrePVO2) & (classement['parametrePERF'] == parametrePERF) & (classement['parametreTRIX_HISTO'] == parametreTRIX_HISTO) & (classement['parametrePVO'] == parametrePVO) & (classement['parametreBOL_BANDwindowdev'] == parametreBOL_BANDwindowdev) & (classement['parametreBOL_BANDwindow'] == parametreBOL_BANDwindow) & (classement['parametreMACD'] == parametreMACD) & (classement['parametreEMA13D'] == parametreEMA13D) & (classement['parametreEMA9D'] == parametreEMA9D) & (classement['parametreEMA10'] == parametreEMA10) & (classement['parametreEMA50'] == parametreEMA50) & (classement['parametreEMA45'] == parametreEMA45)).any() :
        print(f"Données {dateAnnee} {dateMois} {dateJour} {startingBalance} {maxPositions} {parametrePVO2} {parametrePERF} {parametreTRIX_HISTO} {parametrePVO} {parametreBOL_BANDwindowdev} {parametreBOL_BANDwindow} {parametreMACD} {parametreEMA13D} {parametreEMA9D} {parametreEMA10} {parametreEMA50} {parametreEMA45} déjà présentes dans le classement")
    else :
        cmd = (f"python3 -W ignore _backtest-for-bear-only.py {dateAnnee} {dateMois} {dateJour} {startingBalance} {maxPositions} {parametrePVO2} {parametrePERF} {parametreTRIX_HISTO} {parametrePVO} {parametreBOL_BANDwindowdev} {parametreBOL_BANDwindow} {parametreMACD} {parametreEMA13D} {parametreEMA9D} {parametreEMA10} {parametreEMA50} {parametreEMA45}")
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate() 
        result=out.decode('utf-8')
        if result=='':
            result=1000
            dates=str("0")
            finalBalance=float(0)
            perfVSUSD=float(0)
            holdPercentage=float(0)
            vsHoldPercentage=float(0)
            bestTrade=float(0)
            worstTrade=float(0)
            drawDown=float(0)
            taxes=float(0)
            totalTrades=float(0)
            totalGoodTrades=float(0)
            totalBadTrades=float(0)
            winRateRatio=float(0)
            tradesPerformance=float(0)
            averagePercentagePositivTrades=float(0)
            averagePercentageNegativTrades=float(0)
        else:
            separatedResult=result.split('\n')
            y=1
            for line in separatedResult:
                if y==1 :
                    dates=str(line)
                if y==2 :
                    finalBalance=float(line)
                if y==3 :
                    perfVSUSD=float(line)
                if y==4 :
                    holdPercentage=float(line)
                if y==5 :
                    vsHoldPercentage=float(line)
                if y==6 :
                    bestTrade=float(line)
                if y==7 :
                    worstTrade=float(line)
                if y==8 :
                    drawDown=float(line)
                if y==9 :
                    taxes=float(line)
                if y==10 :
                    totalTrades=float(line)
                if y==11 :
                    totalGoodTrades=float(line)
                if y==12 :
                    totalBadTrades=float(line)
                if y==13 :
                    winRateRatio=float(line)
                if y==14 :
                    tradesPerformance=float(line)
                if y==15 :
                    averagePercentagePositivTrades=float(line)
                if y==16 :
                    averagePercentageNegativTrades=float(line)
                y=y+1
        classement = classement.append(pd.DataFrame({
                    'dates' : [dates],
                    'finalBalance' : [finalBalance],
                    'perfVSUSD' : [perfVSUSD],
                    'holdPercentage' : [holdPercentage],
                    'vsHoldPercentage' : [vsHoldPercentage],
                    'bestTrade' : [bestTrade],
                    'worstTrade' : [worstTrade],
                    'drawDown' : [drawDown],
                    'taxes' : [taxes],
                    'totalTrades' : [totalTrades],
                    'totalGoodTrades' : [totalGoodTrades],
                    'totalBadTrades' : [totalBadTrades],
                    'winRateRatio' : [winRateRatio],
                    'tradesPerformance' : [tradesPerformance],
                    'averagePercentagePositivTrades' : [averagePercentagePositivTrades],
                    'averagePercentageNegativTrades' : [averagePercentageNegativTrades],
                    'startingBalance': [startingBalance],
                    'maxPositions': [maxPositions],
                    'parametrePVO2': [parametrePVO2],
                    'parametrePERF': [parametrePERF],
                    'parametreTRIX_HISTO': [parametreTRIX_HISTO],
                    'parametrePVO': [parametrePVO],
                    'parametreBOL_BANDwindowdev': [parametreBOL_BANDwindowdev],
                    'parametreBOL_BANDwindow': [parametreBOL_BANDwindow],
                    'parametreMACD': [parametreMACD],
                    'parametreEMA13D': [parametreEMA13D],
                    'parametreEMA9D': [parametreEMA9D],
                    'parametreEMA10': [parametreEMA10],
                    'parametreEMA50': [parametreEMA50],
                    'parametreEMA9D': [parametreEMA9D],
                    'parametreEMA45': [parametreEMA45]}), ignore_index=True)
                    
        classement.dates = classement.dates.astype(str)
        classement.finalBalance = classement.finalBalance.astype(float)
        classement.perfVSUSD = classement.perfVSUSD.astype(float)
        classement.holdPercentage = classement.holdPercentage.astype(float)
        classement.vsHoldPercentage = classement.vsHoldPercentage.astype(float)
        classement.bestTrade = classement.bestTrade.astype(float)
        classement.worstTrade = classement.worstTrade.astype(float)
        classement.drawDown = classement.drawDown.astype(float)
        classement.taxes = classement.taxes.astype(float)
        classement.totalTrades = classement.totalTrades.astype(float)
        classement.totalGoodTrades = classement.totalGoodTrades.astype(float)
        classement.totalBadTrades = classement.totalBadTrades.astype(float)
        classement.winRateRatio = classement.winRateRatio.astype(float)
        classement.tradesPerformance = classement.tradesPerformance.astype(float)
        classement.averagePercentagePositivTrades = classement.averagePercentagePositivTrades.astype(float)
        classement.averagePercentageNegativTrades = classement.averagePercentageNegativTrades.astype(float)
        

        classement.to_csv(fichierEnregistrement)
    return True

#========================================================================
#   SUCCESSION DE BOUCLE QUI VA FAIRE VARIER TOUS NOS PARAMETRES 1 PAR 1
#========================================================================

count=0
for j in range(2):
    #maxPositions
    if maxPositionsuse=='true':
        maxPositions = maxPositionsmin
    else:
        maxPositions = maxPositionsdefault
        maxPositionsmin = maxPositions
        maxPositionsmax = maxPositions
    while maxPositions <= maxPositionsmax:

        #parametrePVO2
        if parametrePVO2use=='true':
            parametrePVO2 = parametrePVO2min
        else:
            parametrePVO2 = parametrePVO2default
            parametrePVO2min = parametrePVO2
            parametrePVO2max = parametrePVO2
        while parametrePVO2 <= parametrePVO2max:
        
            #parametrePERF
            if parametrePERFuse=='true':
                parametrePERF = parametrePERFmin
            else:
                parametrePERF = parametrePERFdefault
                parametrePERFmin = parametrePERF
                parametrePERFmax = parametrePERF
            while parametrePERF <= parametrePERFmax:
                
                #parametreTRIX_HISTO
                if parametreTRIX_HISTOuse=='true':
                    parametreTRIX_HISTO = parametreTRIX_HISTOmin
                else:
                    parametreTRIX_HISTO = parametreTRIX_HISTOdefault
                    parametreTRIX_HISTOmin = parametreTRIX_HISTO
                    parametreTRIX_HISTOmax = parametreTRIX_HISTO
                while parametreTRIX_HISTO <= parametreTRIX_HISTOmax:
                    
                    #parametrePVO
                    if parametrePVOuse=='true':
                        parametrePVO = parametrePVOmin
                    else:
                        parametrePVO = parametrePVOdefault
                        parametrePVOmin = parametrePVO
                        parametrePVOmax = parametrePVO
                    while parametrePVO <= parametrePVOmax:
                        
                        #parametreBOL_BANDwindowdev
                        if parametreBOL_BANDwindowdevuse=='true':
                            parametreBOL_BANDwindowdev = parametreBOL_BANDwindowdevmin
                        else:
                            parametreBOL_BANDwindowdev = parametreBOL_BANDwindowdevdefault
                            parametreBOL_BANDwindowdevmin = parametreBOL_BANDwindowdev
                            parametreBOL_BANDwindowdevmax = parametreBOL_BANDwindowdev
                        while parametreBOL_BANDwindowdev <= parametreBOL_BANDwindowdevmax:
                        
                            #parametreBOL_BANDwindow
                            if parametreBOL_BANDwindowuse=='true':
                                parametreBOL_BANDwindow = parametreBOL_BANDwindowmin
                            else:
                                parametreBOL_BANDwindow = parametreBOL_BANDwindowdefault
                                parametreBOL_BANDwindowmin = parametreBOL_BANDwindow
                                parametreBOL_BANDwindowmax = parametreBOL_BANDwindow
                            while parametreBOL_BANDwindow <= parametreBOL_BANDwindowmax:
                            
                                #parametreMACD
                                if parametreMACDuse=='true':
                                    parametreMACD = parametreMACDmin
                                else:
                                    parametreMACD = parametreMACDdefault
                                    parametreMACDmin = parametreMACD
                                    parametreMACDmax = parametreMACD
                                while parametreMACD <= parametreMACDmax:
                                    
                                    #parametreEMA13D
                                    if parametreEMA13Duse=='true':
                                        parametreEMA13D = parametreEMA13Dmin
                                    else:
                                        parametreEMA13D = parametreEMA13Ddefault
                                        parametreEMA13Dmin = parametreEMA13D
                                        parametreEMA13Dmax = parametreEMA13D
                                    while parametreEMA13D <= parametreEMA13Dmax:
                   
                                        #parametreEMA9D
                                        if parametreEMA9Duse=='true':
                                            parametreEMA9D = parametreEMA9Dmin
                                        else:
                                            parametreEMA9D = parametreEMA9Ddefault
                                            parametreEMA9Dmin = parametreEMA9D
                                            parametreEMA9Dmax = parametreEMA9D
                                        while parametreEMA9D <= parametreEMA9Dmax:
                                        
                                            #parametreEMA10
                                            if parametreEMA10use=='true':
                                                parametreEMA10 = parametreEMA10min
                                            else:
                                                parametreEMA10 = parametreEMA10default
                                                parametreEMA10min = parametreEMA10
                                                parametreEMA10max = parametreEMA10
                                            while parametreEMA10 <= parametreEMA10max:
                                                
                                                #parametreEMA50
                                                if parametreEMA50use=='true':
                                                    parametreEMA50 = parametreEMA50min
                                                else:
                                                    parametreEMA50 = parametreEMA50default
                                                    parametreEMA50min = parametreEMA50
                                                    parametreEMA50max = parametreEMA50
                                                while parametreEMA50 <= parametreEMA50max:
                                                        
                                                    #parametreEMA45
                                                    if parametreEMA45use=='true':
                                                        parametreEMA45 = parametreEMA45min
                                                    else:
                                                        parametreEMA45 = parametreEMA45default
                                                        parametreEMA45min = parametreEMA45
                                                        parametreEMA45max = parametreEMA45
                                                    while parametreEMA45 <= parametreEMA45max:
                                                        if j==1:
                                                            launch_backtest()
                                                        else :
                                                            count=count+1
                                                        parametreEMA45=parametreEMA45+parametreEMA45pas
                                                    parametreEMA50=parametreEMA50+parametreEMA50pas
                                                parametreEMA10=parametreEMA10+parametreEMA10pas
                                            parametreEMA9D=parametreEMA9D+parametreEMA9Dpas
                                        parametreEMA13D=parametreEMA13D+parametreEMA13Dpas
                                    parametreMACD=parametreMACD+parametreMACDpas
                                parametreBOL_BANDwindow=parametreBOL_BANDwindow+parametreBOL_BANDwindowpas
                            parametreBOL_BANDwindowdev=round(parametreBOL_BANDwindowdev+parametreBOL_BANDwindowdevpas,4)
                        parametrePVO=parametrePVO+parametrePVOpas
                    parametreTRIX_HISTO=round(parametreTRIX_HISTO+parametreTRIX_HISTOpas,4)
                parametrePERF=parametrePERF+parametrePERFpas
            parametrePVO2=parametrePVO2+parametrePVO2pas
        maxPositions=maxPositions+maxPositionspas
    
#==================================================================================
#   ENREGISTREMENT FINALE (AU CAS OU MAIS NORMALEMENT LE FICHIER SERA DEJA REMPLI
#==================================================================================

print(classement.head())
classement.to_csv(fichierEnregistrement)
telegram_send.send(messages=[f"Votre algorithme d'études en timeframe 5 minutes a enregistré toutes les données dans {fichierEnregistrement} pour le mois de {str(cfg['DATE']['mois'])} {str(cfg['DATE']['date'])}"])
