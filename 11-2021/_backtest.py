################################################################
import sys, getopt
import sys
sys.path.append( '../utilities' )
from data_engine import DataEngine
from backtesting import Backtesting
import pandas as pd
import ta
import others as o1
import ccxt
import json
f = open('../database/pair_list.json',)
pairJson = json.load(f)
f.close()
#import pandas_ta as pda
from custom_indicators import CustomIndocators as ci
import numpy as np
from datetime import datetime, timedelta
import configparser

#pairs qu'on utilise
pairList = pairJson['all']
#timeframe utilisée
timeframe = '5m'
#date de début du backtest
startDate = "2022-01-01T00:00:00"
dateDebut='2022-01-01'
#date de fin du backtest
dateFin='2022-02-01'

cfg = configparser.ConfigParser()
cfg.read('mois.cfg')

# -- Starting value --
startingBalance = 1000
makerFee = 0.0007
takerFee = 0.0007

# -- Rules --
StopLossActivation = False
takeProfitActivation = False
showLog = False
Risque = False
DCA = False

# -- Hyper parameters --
SlPct = 0.007
TpPct = 0.007
maxPositions = 2


################################################################
# Exemple de paramètres d'entrées nécessaire à la stratégie

argumentList = sys.argv[1:]
try:
    test=sys.argv[17]
    if(sys.argv[1]!='default'):
        dateAnnee=str(sys.argv[1])
    if(sys.argv[2]!='default'):
        dateMois=str(sys.argv[2])
    if(sys.argv[3]!='default'):
        dateJour=str(sys.argv[3])
    if(sys.argv[4]!='default'):
        startingBalance=float(sys.argv[4])
    if(sys.argv[5]!='default'):
        maxPositions=int(sys.argv[5])
    if(sys.argv[6]!='default'):
        parametrePVO2=int(sys.argv[6])
    if(sys.argv[7]!='default'):
        parametrePERF=int(sys.argv[7])
    if(sys.argv[8]!='default'):
        parametreTRIX_HISTO=float(sys.argv[8])
    if(sys.argv[9]!='default'):
        parametrePVO=int(sys.argv[9])
    if(sys.argv[10]!='default'):
        parametreBOL_BANDwindowdev=float(sys.argv[10])
    if(sys.argv[11]!='default'):
        parametreBOL_BANDwindow=int(sys.argv[11])
    if(sys.argv[12]!='default'):
        parametreMACD=int(sys.argv[12])
    if(sys.argv[13]!='default'):
        parametreEMA13D=int(sys.argv[13])
    if(sys.argv[14]!='default'):
        parametreEMA9D=int(sys.argv[14])
    if(sys.argv[15]!='default'):
        parametreEMA10=int(sys.argv[15])
    if(sys.argv[16]!='default'):
        parametreEMA50=int(sys.argv[16])
    if(sys.argv[17]!='default'):
        parametreEMA45=(sys.argv[17])
except :
    print("Utilisez ces arguments :",
            "dateAnnee",        #1
            "dateMois",         #2
            "dateJour",         #3
            "startingBalance",  #4
            "maxPositions",     #5
            "parametrePVO2",    #6 
            "parametrePERF",    #7
            "parametreTRIX_HISTO",#8
            "parametrePVO",     #9
            "parametreBOL_BANDwindowdev",#10
            "parametreBOL_BANDwindow",#11
            "parametreMACD",    #12
            "parametreEMA13D",  #13
            "parametreEMA9D",   #14
            "parametreEMA10",   #15
            "parametreEMA50",   #16
            "parametreEMA45"    #17
            )

################################################################
################################################################
################################################################

# METTRE ICI LE CODE DE VOTRE BACKTEST
# VOUS POUVEZ CREER VOTRE PROPRE CODE EN VOUS INSPIRANT DES BACKTESTS PROPOSES PAR CRYPTO ROBOTS ici :
# https://github.com/CryptoRobotFr/cBot-Project/tree/main/backtest


################################################################
################################################################
################################################################
if (sum(walletUsdArray) + usd) != startingBalance :
    BTobject = Backtesting()
    #fonction créée dans /utilities/backtesting.py qui permet de print dans l'ordre : dates, finalBalance, etc...
    BTobject.multi_spot_backtest_print(dfTrades=dfTrades, dfTest=dfTestList[0], pairList=pairList, timeframe=timeframe)

#newDf = BTobject.multi_spot_backtest_analys(dfTrades=dfTrades, dfTest=dfTestList[0], pairList=pairList, timeframe=timeframe)
