# global-seismic-forecasting



## About

In 2020 I was astonished by a seemingly groundbreaking discovery published in [Nature](https://www.nature.com/articles/s41598-020-67860-3) on the correlation between large earthquakes and solar activity of high significance (null hypothesis rejected with probability of being wrong < 0.00001). To imagine some of the highest energy seismic events on Earth being tied to solar activity in any capacity is quite surprising and, to me, required further investigation. 

The researchers found that when densities of protons from incoming solar wind pass a threshold that large magnitude Earthquakes occur within a timeshift of a day. The values for solar wind proton density were recorded by the Solar and Heliospheric Observatory's proton monitor which began transmitting data in 1996. It makes sense it would take so long for seismologists and geophysicists to find this connection given that humanity has just recently been able to consistently measure properties of ionized gases from the sun at the L1 Lagrange point relative to the frequency of high magnitude earthquakes on earth. Therefore, the relevant datasets have just matured enough to find such a correlation. 

My software takes this finding a step further by training a machine learning model to predict time of  occurance of high-magnitude earthquakes as a function of proton density using both SOHO's proton monitor data since 1996 and the Global Catalog of Calibrated Earthquake Locations (GCCEL) comprising all earthquake records since the 1960s. Since these datasets are quite large, I chose to distribute the storage and computing of data accross several laptops in my homemade computer cluster using Apache Hadoop and Spark. 
