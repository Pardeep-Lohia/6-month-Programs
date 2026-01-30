# What is the average landed weight per landing for domestic US flights in July 1999?

# july 1999 -> domestic -> US flights -> landed weight/number of landings

import pandas as pd

df = pd.read_csv('Air.csv')
print(df)
print(df.info())
print(df.describe())


# usong activity period column
condition = (
    (df['GEO Summary'] == 'Domestic') &
    (df['GEO Region'] == 'US') &
    (df['Activity Period'] == 199907)
)

total_landed_weight, total_landings = (
    df.loc[condition, 'Total Landed Weight'].sum(),
    df.loc[condition, 'Landing Count'].sum()
)

average_landed_weight_per_landing = total_landed_weight / total_landings
print(average_landed_weight_per_landing)

# another approach using str split of Activity Period Start Date column

month = df['Activity Period Start Date'].str.split('/', expand=True)
condition_alt = (df['GEO Summary'] == 'Domestic') & (df['GEO Region'] == 'US') & (month[0] == '1999') & (month[1] == '07')
total_landed_weight_alt = df.loc[condition_alt, 'Total Landed Weight'].sum()
total_landings_alt = df.loc[condition_alt, 'Landing Count'].sum()
average_landed_weight_per_landing_alt = total_landed_weight_alt / total_landings_alt
print(average_landed_weight_per_landing_alt)