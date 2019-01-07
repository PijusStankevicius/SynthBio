import pandas as pd
import statsmodels as sm
import statistics
import numpy as np
import scipy 
from scipy.stats import chisquare
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 

data = pd.read_csv("bacteria.csv")
data = data.iloc[:,1:]

#Central tendencies
pd.value_counts(data.y)
pd.value_counts(data.ap)
pd.value_counts(data.hilo)
pd.value_counts(data.trt)
week = pd.value_counts(data.week)
id = pd.value_counts(data.ID)
idp = pd.DataFrame(id)

statistics.mode(data.y)
statistics.mode(data.ap)
statistics.mode(data.hilo)
statistics.mode(data.trt)
statistics.mode(data.week)
statistics.mode(data.ID) #Unikalios modos neturi

statistics.median(data.week)
q75, q25 = np.percentile(data.week, [75 ,25])
iqr = q75 - q25     #week kintamojo IQR

idp.index.values
idpx = pd.DataFrame(idp.index.values)

for i in range(len(idp)):
    idpx.iloc[i,1] = idp.iloc[i,0]


plt.clf() #Clears figure
objects = idpx.iloc[:,0]
y_pos = np.arange(len(objects))
performance = idp.iloc[:,0]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Pasikartojimų kiekis')
plt.title('Kintamojo dažnis')
 
plt.show()

#Chi square
a = data[data.ap == 'a']
a = a[a.week == 11]  #kurie gavo antibiotika
ay = sum(a.y == 'y')      #kiek turejo bakterija ir gavo antibio
an = sum(a.y == 'n')      # gavo antibiotika, bet neturejo bakterijos

p = data[data.ap == 'p']
p = p[p.week == 11]  
py = sum(p.y == 'y')      
pn = sum(p.y == 'n')

antibio = pd.DataFrame()
antibio[0,0] = ay
antibio[1,0] = py


chisquare([93,31,84,12],[100,24,77,19])
chisquare([16,8,16,4],[17,7,15,6])
