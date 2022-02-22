
solar_wind_nineties: solar_wind_parse.py solarwind/1996.txt solarwind/1997.txt solarwind/1998.txt solarwind/1999.txt
	python3 solar_wind_parse.py solarwind/1996.txt w
	python3 solar_wind_parse.py solarwind/1997.txt a
	python3 solar_wind_parse.py solarwind/1998.txt a
	python3 solar_wind_parse.py solarwind/1999.txt a
	
solar_wind_aughts: solar_wind_parse.py solarwind/2000.txt solarwind/2001.txt solarwind/2002.txt solarwind/2003.txt solarwind/2004.txt solarwind/2005.txt solarwind/2006.txt solarwind/2007.txt solarwind/2008.txt solarwind/2009.txt
	python3 solar_wind_parse.py solarwind/2000.txt a
	python3 solar_wind_parse.py solarwind/2001.txt a
	python3 solar_wind_parse.py solarwind/2002.txt a
	python3 solar_wind_parse.py solarwind/2003.txt a
	python3 solar_wind_parse.py solarwind/2004.txt a
	python3 solar_wind_parse.py solarwind/2005.txt a
	python3 solar_wind_parse.py solarwind/2006.txt a
	python3 solar_wind_parse.py solarwind/2007.txt a
	python3 solar_wind_parse.py solarwind/2008.txt a
	python3 solar_wind_parse.py solarwind/2009.txt a

solar_wind_tens: solar_wind_parse.py solarwind/2010.txt solarwind/2011.txt solarwind/2012.txt solarwind/2013.txt solarwind/2014.txt solarwind/2015.txt solarwind/2016.txt solarwind/2017.txt solarwind/2018.txt solarwind/2019.txt
	python3 solar_wind_parse.py solarwind/2010.txt a
	python3 solar_wind_parse.py solarwind/2011.txt a
	python3 solar_wind_parse.py solarwind/2012.txt a
	python3 solar_wind_parse.py solarwind/2013.txt a
	python3 solar_wind_parse.py solarwind/2014.txt a
	python3 solar_wind_parse.py solarwind/2015.txt a
	python3 solar_wind_parse.py solarwind/2016.txt a
	python3 solar_wind_parse.py solarwind/2017.txt a
	python3 solar_wind_parse.py solarwind/2018.txt a
	python3 solar_wind_parse.py solarwind/2019.txt a

solar_wind_twenties: solar_wind_parse.py solarwind/2020.txt solarwind/2021.txt
	python3 solar_wind_parse.py solarwind/2020.txt a
	python3 solar_wind_parse.py solarwind/2021.txt a

earthquakes: gccel_parse.py all_gccel.dat
	python3 gccel_parse.py all_gccel.dat 0 0

run:
	make clean
	make solar_wind_nineties
	make solar_wind_aughts
	make solar_wind_tens
	make solar_wind_twenties
	make earthquakes

clean:
	del earthquakes.csv
	del proton_density.csv
