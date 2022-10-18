from nsetools import Nse
from pprint import pprint
nse = Nse()
company = str(input("Enter the symbol of the company : "))
#data = nse.get_quote('zylog')
data = nse.get_quote(company)
print('=================================='+ data['companyName']+'\t'    + data['symbol']+'=================================================================')
print("Previous Day close (" , end="")
print(data['recordDate'] ,end="")
print(") : " ,end="")
print(data['previousClose'] , end="\t")
print("Trade Day : " ,end = "" )
print (data['secDate'])
print('================================== 52 week =================================================================')
print("52 week high : " , end = "")
print(data['high52'] , end = "\t")
print("52 week low : " , end = "")
print(data['low52'] )
print("Last close : " , end="")
print(data['previousClose'])

print('================================== Trade History =================================================================')
print("Sell \t\t  Qty \t\t\t    Buy \t Qty"  )
print("---- \t\t  --- \t\t\t    --- \t ---")
print(data['sellPrice1'] ,end="")
print(" \t ",end = "")
print(data['sellQuantity1'] , end = "")
print(" \t\t   " , end = "")
print(data['buyPrice1'] ,end="")
print(" \t ",end = "")
print(data['buyQuantity1'],end="\n")

print(data['sellPrice2'] ,end="")
print(" \t   ",end = "")
print(data['sellQuantity2'] , end = "")
print(" \t\t     " , end = "")
print(data['buyPrice2'] ,end="")
print(" \t ",end = "")
print(data['buyQuantity2'],end="\n")

print(data['sellPrice3'] ,end="")
print(" \t   ",end = "")
print(data['sellQuantity3'] , end = "")
print(" \t\t     " , end = "")
print(data['buyPrice3'] ,end="")
print(" \t ",end = "")
print(data['buyQuantity3'],end="\n")

print(data['sellPrice4'] ,end="")
print(" \t   ",end = "")
print(data['sellQuantity4'] , end = "")
print(" \t\t     " , end = "")
print(data['buyPrice4'] ,end="")
print(" \t ",end = "")
print(data['buyQuantity4'],end="\n")

print(data['sellPrice5'] ,end="")
print(" \t   ",end = "")
print(data['sellQuantity5'] , end = "")
print(" \t\t     " , end = "")
print(data['buyPrice5'] ,end="")
print(" \t ",end = "")
print(data['buyQuantity5'],end="\n")

print("Day open    : " , end = "")
print(data['open'] , end = "\n")
print("Day High    : " , end ="")
print(data['dayHigh'] , end = "\t\t")
print("            Day Low : " , end ="")
print(data['dayLow'] , end = "\n")
print('ClosePrice  : ' , end ="")
print(data['closePrice'],end = "\t")
print('              AveragePrice : ' , end ="")
print(data['averagePrice'],end = "\n")
print('TotalTradedVolume : ' , end ="")
print(data['totalTradedVolume'],end = "\n")


