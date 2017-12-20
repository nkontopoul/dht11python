import subprocess
import re
import sys
import time
 
###############################################################
###################  Begin DHT function  ######################
###############################################################
 
def DHT_read(pin):
 
    # read the sensor for Temperature on Pin 4 for ten times     
    #define lists:
    temp_list=[]
    hum_list=[]
 
    #define the number of times toread the sensor
    read_count=10
 
    #set counters to zero
    i=0
    sensor_error=0
 
    #begin the loop for reading the sensor
    while i<read_count:
 
        #run DHT driver to read data from sensor
        output = subprocess.check_output(["sudo","./Adafruit_DHT", "11", str(pin)]);
        #to see output: print output, "\n"
 
        #get the temperature out of the 'output' string
        matches = re.search("Temp =\s+([0-9.]+)", output)
 
        #check for an error
        if (not matches):
            time.sleep(1)
            #print "error detected"
            sensor_error=sensor_error+1
            continue
 
        temp = (float(matches.group(1)))*9.0 / 5.0 + 32
        #to see temp: print temp, "\n\n"
 
        #add to temp list
        temp_list.append(temp)
        i=i+1
 
        #calculate humidity
        humidity = float(matches.group(1))
 
        #add to humidity list
        hum_list.append(humidity)
 
    #calculate temp average
    sum_temp=0
    w= len(temp_list)
 
    while w > 0:
        sum_temp=sum_temp+temp_list[w-1]
        w=w-1
 
    temp_avg=sum_temp / len(temp_list)
 
    #calculate temp average
    sum_hum=0
    w= len(hum_list)
 
    while w > 0:
        sum_hum=sum_hum+hum_list[w-1]
        w=w-1
 
    hum_avg=sum_hum / len(hum_list)
 
    #print "Λίστα θερμοκρασίας" , temp_list
    #print "Μέση θερμοκρασία = " , temp_avg , "\n"
    #print "Λίστα Υγρασίας" , hum_list
    #print "Μέση υγρασία = " , hum_avg , "\n"
    #print "Αριθμός σφαλμάτων" , sensor_error
 
    return temp_avg, hum_avg
 
##################################################
##################### END DHT_read Function  #######
##################################################
 
temperature , humidity = DHT_read(4)
print temperature , humidity