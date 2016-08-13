# parsing the gps data from the castaway field test
# 
# generated from the arduino code that was made in a rush
# ( hence the need for post processing :P )
#
# frequency - 1s, 5s, 30s, 60s, 120s, 300s
# file 1 - simple:
# lat, lon
# file 2 - for a map:
# lat, lon, alt, heading dir
# file 3 - more info:
# date, time, sats, hdop, lat, lon, alt, speed, heading, heading dir
#
# by Erin RobotGrrl for Robot Missions
# http://robotmissions.org

f = open('CASTAWAY_GPS.txt', 'r')

frequency = 60
file1 = open('file1.csv', 'w')
file2 = open('file2.csv', 'w')
file3 = open('file3.csv', 'w')

file1.write("latitude, longitude\n")
file2.write("latitude, longitude, altitude, time\n")
file3.write("date, time, sats, hdop, latitude, longitude, altitude, speed, heading, heading dir\n")

linenum = 0

for line in f:
  if linenum < 3:
    print("skip")
  else:
    if (linenum-3)%frequency == 0:
        s = f.readline()
        splittystring = s.split(" ")

        datum = []
        for item in splittystring:
            if item == ' ' or item == '' or item == '\n':
                1+1
            else:
                datum.append(item)
        
        sats = datum[0]
        hdop = datum[1]
        lat = datum[2]
        lon = datum[3]
        fix_age = datum[4]
        date = datum[5]
        time = datum[6]
        date_age = datum[7]
        alt = datum[8]
        speed = datum[9]
        heading = datum[10]
        heading_dir = datum[11]

        file1.write("%s, %s\n" % (lat, lon))
        file2.write("%s, %s, %s, %s\n" % (lat, lon, alt, time))
        file3.write("%s, %s, %s, %s, %s, %s, %s, %s, %s, %s\n" % (date, time, sats, hdop, lat, lon, alt, speed, heading, heading_dir))

        print("%d sats %s" % (linenum, sats))

  linenum = linenum+1

  # if linenum > 27600:
  #   break

file1.close()
file2.close()
file3.close()
