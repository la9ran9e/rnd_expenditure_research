import wbdata
from datetime import datetime
data_date = (datetime(2000, 1, 1), datetime(2018, 1, 1))
df = wbdata.api.get_dataframe({'NY.GDP.PCAP.PP.KD': 'GDP per Capita',
                               "GB.XPD.RSDV.GD.ZS": "R&D Expenditures"
                               },
                              data_date=data_date
                              )

df.to_csv('../get_data_dataset.csv', index=True)

print(df)
