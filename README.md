# motion2csv
Recording Motion with skeleton coordinates using MS Kinect v2

# Using
1. Build, 
2. Start program, 
3. Let Kinect record the human's motion.
-> Then Formatted csv file will be written.

# Output
The CSV File recorded contains below information.

1. Time, 
2. nFrame, 
3. relativeTime, 
4. bodyIndex(str), 
5. bodyIndex, 
6. X, 
7. Y, 
8. Z, 
9. state 

### Description for each information
1. **Time** : Absolute time when the frame is recorded 
- hh_mm_ss
2. **nFrame** : The number of frame recorded
3. **relativeTime** : Relative time, The unit time is 1 milisecond.
4. **bodyIndex(str)** : Joint type (string)
5. **bodyIndex** :  Joint type(integer)
6. **X, Y, Z** : The coordinates of the joint.
7. **state** : The state of the joint's record(integer). the meaning of values are below.  
      : TrackingState_NotTracked	= 0,  
      : TrackingState_Inferred	= 1,  
      : TrackingState_Tracked	= 2	  

# Example  

# Function description
void CBodyBasics::DrawBody  
: Actually, Most of processes are in this function. Recording motion, Writing csv, etc...
You should look into this function. Further descriptions are written in code. 

# TODO
1. Let absoulte time contains milisecond.  
2. Test with actual kinect device.  
