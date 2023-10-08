import pandas as pd

df = pd.read_csv('pulse-subdomains.csv')
df.to_csv('subdomains_modified.csv', columns=['Domain'], header=False, index=False)
