import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering' , 'chennai' , 'campus'])
s = ser.map(lambda x: x[0].upper() + x[1:-1] + x[-1])
S = [str(x) for x in s]
ss = " "
x = ss.join(S)
print(x)
