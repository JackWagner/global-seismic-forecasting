import time
import re 
import sys
import pandas as pd


#Open and read Global Catalog of Calibrated Earthquake Locations (GCCEL) data file
gccel_file = open(str(sys.argv[1]),"r",encoding="utf8")
gccel_data = gccel_file.read()


print(str(sys.argv[1]),"opened")
time.sleep(2)

gccel_file.close()

#Regex for array of records
records = re.split("STOP",gccel_data)
num_of_records = len(records)

print("Number of Records: ", str(num_of_records), "\n")

#column-oriented storage of event, hypocenter and magnitude records
#initializing arrays with zeros
event_record = [None]*num_of_records             #Event ID 5:121

hypocenter_datetime_record = [None]*num_of_records   #Datetime Y=5:8, M=10:11, D=13:14, H=16:17, m=19:20, s 22:26

hypocenter_latitude_record = [None]*num_of_records   #Latitude 35:42
hypocenter_longitude_record = [None]*num_of_records  #Longitude 44:52

hypocenter_clusterID_record = [None]*num_of_records  #ClusterID 104:121

magnitude_surface_record = [None]*num_of_records     #Magnitude 5:8, Scale=MS at 10:14
magnitude_body_record = [None]*num_of_records        #Magnitude 5:8, Scale=mb at 10:14
magnitude_richter_record = [None]*num_of_records     #Magnitude 5:8, Scale=ML at 10:14
magnitude_moment_record = [None]*num_of_records      #Magnitude 5:8, Scale=MW at 10:14

if(len(sys.argv) == 2 or (int(sys.argv[2]) == 0 and int(sys.argv[3]) == 0)):
    record_range = range(num_of_records)
else:
    record_range = range(int(sys.argv[2]),int(sys.argv[3]))
print(str(records[1].count("\n")))
for i in record_range: 
    temp_records = records[i].splitlines()
    
    for j in range(len(temp_records)):
        line_num = i*records[1].count("\n")+j+1 
        if (temp_records[j][0:2] == "E "):
            #print("\n\n  Event:     ", temp_records[j][4:101])
            event_record[i] = temp_records[j][4:101]
        
        if (temp_records[j][0:2] == "H "):
            
            hypocenter_datetime_record[i] = temp_records[j][4:26]
            hypocenter_latitude_record[i] = float(temp_records[j][34:42])
            hypocenter_longitude_record[i] = float(temp_records[j][43:52])
            hypocenter_clusterID_record[i] = temp_records[j][103:121].strip()

            #print("  Datetime:     ", temp_records[j][4:26])
            #print("  Latitude/Longitude:    ", temp_records[j][34:42]," / ",temp_records[j][43:52])
            #print("  ClusterID:    ",temp_records[j][103:121])

        if (temp_records[j][0:2] == "M "):
            
            if (temp_records[j][9:11] == "MS"):
                magnitude_surface_record[i] = float(temp_records[j][4:8])
                #print("  Surface Magnitude:    ", temp_records[j][4:8])
            
            if (temp_records[j][9:11] == "mb"):
                magnitude_body_record[i] = float(temp_records[j][4:8])
                #print("  Body Magnitude:    ", temp_records[j][4:8])
            
            if (temp_records[j][9:11] == "ML"):
                magnitude_richter_record[i] = float(temp_records[j][4:8])
                #print("  Richter Magnitude:   ", temp_records[j][4:8])
            
            if (temp_records[j][9:11] == "MW" or temp_records[j][9:11] == "Mw"):
                magnitude_moment_record[i] = float(temp_records[j][4:8])
                #print("  Moment Magnitude:   ", temp_records[j][4:8])


data = { 'ClusterID' : hypocenter_clusterID_record, 'Datetime' : hypocenter_datetime_record,
         'Latitude' : hypocenter_latitude_record, 'Longitude' : hypocenter_longitude_record,
         'Surface Magnitude' : magnitude_surface_record, 'Body Magnitude' : magnitude_body_record,
         'Richter Magnitude' : magnitude_richter_record, 'Moment Magnitude' : magnitude_moment_record }

earthquake_df = pd.DataFrame(data)

earthquake_df.to_csv("earthquakes.csv",index=False,mode='w')



