import pandas as pd
import plotly as pt

kaz2014_f = pd.read_excel('kaz2014.xlsx')
kaz2015_f = pd.read_excel('kaz2015.xlsx')
kaz2016_f = pd.read_excel('kaz2016.xlsx')
kaz2017_f = pd.read_excel('kaz2017.xlsx')

uzb2014_f = pd.read_excel('uzb2014.xlsx')
uzb2015_f = pd.read_excel('uzb2015.xlsx')
uzb2016_f = pd.read_excel('uzb2016.xlsx')
uzb2017_f = pd.read_excel('uzb2017.xlsx')

tjk2014_f = pd.read_excel('tjk2014.xlsx')
tjk2015_f = pd.read_excel('tjk2015.xlsx')
tjk2016_f = pd.read_excel('tjk2016.xlsx')
tjk2017_f = pd.read_excel('tjk2017.xlsx')

kgz2014_f = pd.read_excel('kgz2014.xlsx')
kgz2015_f = pd.read_excel('kgz2015.xlsx')
kgz2016_f = pd.read_excel('kgz2016.xlsx')
kgz2017_f = pd.read_excel('kgz2017.xlsx')

kaz2014 =(kaz2014_f['Prob_Mod_Sev'] * kaz2014_f['wt']).sum() / kaz2014_f['wt'].sum()
kaz2015 =(kaz2015_f['Prob_Mod_Sev'] * kaz2015_f['wt']).sum() / kaz2015_f['wt'].sum()
kaz2016 =(kaz2016_f['Prob_Mod_Sev'] * kaz2016_f['wt']).sum() / kaz2016_f['wt'].sum()
kaz2017 =(kaz2017_f['Prob_Mod_Sev'] * kaz2017_f['wt']).sum() / kaz2017_f['wt'].sum()
kz = [kaz2014, kaz2015, kaz2016, kaz2017]

uzb2014 =(uzb2014_f['Prob_Mod_Sev'] * uzb2014_f['wt']).sum() / uzb2014_f['wt'].sum()
uzb2015 =(uzb2015_f['Prob_Mod_Sev'] * uzb2015_f['wt']).sum() / uzb2015_f['wt'].sum()
uzb2016 =(uzb2016_f['Prob_Mod_Sev'] * uzb2016_f['wt']).sum() / uzb2016_f['wt'].sum()
uzb2017 =(uzb2017_f['Prob_Mod_Sev'] * uzb2017_f['wt']).sum() / uzb2017_f['wt'].sum()
uz = [uzb2014, uzb2015, uzb2016, uzb2017]

tjk2014 =(tjk2014_f['Prob_Mod_Sev'] * tjk2014_f['wt']).sum() / tjk2014_f['wt'].sum()
tjk2015 =(tjk2015_f['Prob_Mod_Sev'] * tjk2015_f['wt']).sum() / tjk2015_f['wt'].sum()
tjk2016 =(tjk2016_f['Prob_Mod_Sev'] * tjk2016_f['wt']).sum() / tjk2016_f['wt'].sum()
tjk2017 =(tjk2017_f['Prob_Mod_Sev'] * tjk2017_f['wt']).sum() / tjk2017_f['wt'].sum()
tj = [tjk2014, tjk2015, tjk2016, tjk2017]

kgz2014 =(kgz2014_f['Prob_Mod_Sev'] * kgz2014_f['wt']).sum() / kgz2014_f['wt'].sum()
kgz2015 =(kgz2015_f['Prob_Mod_Sev'] * kgz2015_f['wt']).sum() / kgz2015_f['wt'].sum()
kgz2016 =(kgz2016_f['Prob_Mod_Sev'] * kgz2016_f['wt']).sum() / kgz2016_f['wt'].sum()
kgz2017 =(kgz2017_f['Prob_Mod_Sev'] * kgz2017_f['wt']).sum() / kgz2017_f['wt'].sum()
kg = [kgz2014, kgz2015, kgz2016, kgz2017]

years = range(2014, 2018)
plt.figure(figsize=(10, 6))
plt.plot(years, kz, marker='o', linestyle='-', label='Казахстан')
plt.plot(years, uz, marker='o', linestyle='-', label='Узбекистан')
plt.plot(years, tj, marker='o', linestyle='-', label='Таджикистан')
plt.plot(years, kg, marker='o', linestyle='-', label='Кыргызстан')
plt.title('Центральная Азия')
plt.xticks(years)
plt.yticks(np.arange(0, 0.3, 0.05))
plt.legend()
plt.grid(True)
plt.show()
