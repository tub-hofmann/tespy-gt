import pandas as pd
import matplotlib.pyplot as plt

# data import
df_eta = pd.read_csv('../data/eta.csv', header=0, index_col=0)
df_swk = pd.read_csv('../data/swk.csv', header=0, index_col=0)

# select values to plot
fig, eta_swk = plt.subplots()

for i in range(5):
    eta_swk.plot(df_swk.iloc[:,i], df_eta.iloc[:,i], color='blue')
    eta_swk.plot(df_swk.iloc[i], df_eta.iloc[i], color='red')

eta_swk.plot(df_swk.iloc[:,5],df_eta.iloc[:,5], color='blue', label='p_r = constant')
eta_swk.plot(df_swk.iloc[5], df_eta.iloc[5], color='red', label='T_inlet = constant')

# legend
eta_swk.set(xlabel='specific work [kJ/kg]', ylabel='efficiency [%]', title='parameter analysis')

# final plot
plt.legend()
plt.show()




