import sys
import pandas as pd

#sys.argv = ['solar_wind_parse.py',datafile.txt, 'a' for append / 'w' for overwrite]

solar_wind_file = open(sys.argv[1],"r",encoding="utf8")
solar_wind_data = solar_wind_file.read()
solar_wind_file.close()

data_start = solar_wind_data.find("CRN(E)") + 7     #skip the headers
solar_wind_records = solar_wind_data[data_start:len(solar_wind_data)].splitlines()

#initialize datetime and proton density lists
datetime_records = [None]*len(solar_wind_records)
proton_density_records = [None]*len(solar_wind_records)

#gather data into lists from file
for line in range(len(solar_wind_records)):
    datetime_records[line] = solar_wind_records[line][0:22]
    proton_density_records[line] = float(solar_wind_records[line][32:38])

data_dict = {'Datetime':datetime_records,'Proton_Density':proton_density_records}
df = pd.DataFrame(data_dict)

df.to_csv("proton_density.csv",index=False,mode=sys.argv[2])

