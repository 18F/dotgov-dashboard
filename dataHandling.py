import pandas as pd

path="/Users/JohnTindel/Documents/Work/Data Library/"

scan = pd.read_csv(path+"inspect.csv")
marchDoms = pd.read_csv(path+"marchDom.csv")

liveComp = scan[['Domain', 'Live']]
liveCompSub = marchDoms[['Domain Name', 'Status']]
liveCompSub.columns = ['Domain', 'marchStatus']
liveComp.Domain = liveCompSub.Domain.str.upper()
liveComp = pd.merge(liveComp, liveCompSub, on='Domain', how='outer')
liveComp.aprilStatus = 'Empty'
discrepancies1 = liveComp[liveComp.Live==False]
discrepancies1 = discrepancies1[discrepancies1.marchStatus=="ACTIVE"]
discrepancies2 = liveComp[liveComp.marchStatus!="ACTIVE"]
discrepancies2 = discrepancies2[discrepancies2.Live==True]
discrepancies3 = liveComp[liveComp.Live!=False]
discrepancies3 = discrepancies3[discrepancies3.Live!=True]
discrepancies = discrepancies1.append(discrepancies2.append(discrepancies3))

agency = marchDoms[['Domain Name', 'Agency']]
agency.columns = ['Domain', 'Agency']
agency.Domain = agency.Domain.str.lower()
scanSub = pd.merge(scan, agency, on='Domain', how='outer')
scanSub = scanSub[scanSub.Agency!='Non-Federal Agency']

long = pd.melt(scanSub, id_vars=['Agency', 'Domain'])
long = long[long.variable!='Canonical']
long = long[long.variable!='Redirect To']
long = long[long.variable!='HSTS Header']
long = long.fillna(False)

pivot = pd.pivot_table(long, rows=['Agency', 'variable'], columns=['value'], aggfunc='count')
pivot.columns = [['True', 'False']]
pivot.to_csv(path+"temp.csv")
pivot=pd.read_csv(path+"temp.csv")
pivotOne = pivot[['Agency', 'variable', 'True']]
pivotOne['binary'] = "Yes"
pivotTwo = pivot[['Agency', 'variable', 'False']]
pivotTwo['binary'] = "No"
pivotOne.columns=['Agency', 'variable', 'value', 'binary']
pivotTwo.columns=['Agency', 'variable', 'value', 'binary']
pivotFinal = pivotOne.append(pivotTwo)
pivotFinal = pivotFinal.fillna(0)
pivotFinal.to_csv(path+'output.csv')
