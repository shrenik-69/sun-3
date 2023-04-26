import pandas as pd

data = pd.read_csv('dwarf_stars.csv')
data = data.dropna()
data.Mass = data.Mass.str.replace('[^a-zA-Z0-9]','').astype('float')
data['Radius'] = data['Radius']*0.102763
data['Mass'] = data['Mass']*0.000954588

data.to_csv('updated_dwarf_stars.csv')