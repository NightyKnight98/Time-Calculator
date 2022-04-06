def add_time(start, duration, day=None):


#getting elements of start time
  start1Pos = start.find(':')
  space = start.find(' ')
  start1 = start[:start1Pos]
  start2 = start[start1Pos + 1 : space]
  ampm = list(start[space + 1 :])
  if day :
      day = day[0].upper() + day[1:].lower()



#converting start string to int
  start1 = int(start1)
  start2 = int(start2)


#getting elements of duration time
  dur1Pos = duration.find(':')
  dur1 = duration[ : dur1Pos]
  dur2 = duration[dur1Pos + 1 : ]


#converting duration string to int
  dur1 = int(dur1)
  dur2 = int(dur2)



#Calculating new hour
  newHour = 0
  newHour = start1 + dur1
  if newHour > 12 :
     newHour = ((newHour % 12) - start1) + start1
        
#calculating new minute
  newMinute = 0
  newMinute = start2 + dur2
  if newMinute > 59 :
      newMinute = ((newMinute % 60) - start2) + start2
      newHour = newHour + 1
    
      if newHour > 12 :
          newHour = ((newHour % 12) - start1) + start1

#Getting new AM and PM
        
  minuteCheck = start2 + dur2
  hourCheck = start1 + dur1

  if minuteCheck > 59 :
      hourCheck = hourCheck + 1
    
  if hourCheck < 12 :
      newampm = ''
      newampm = ampm[0] + ampm[1]
    
  if hourCheck >= 12 and int(((hourCheck / 12)) % 2) == 1 :
      newampm = ''
      if ampm[0] == 'P' :
          newampm = 'AM'
      else :
          newampm = 'PM'

  if hourCheck > 12 and int(((hourCheck / 12)) % 2) == 0 :
      newampm = ''
      newampm = ampm[0] + ampm[1]


#Determine number of days
  totalDays = 0

  if start2 + dur2 > 59 :
      dur1 += 1
    
  totalDays = (dur1 - start1) / 24


  if (ampm[0] == 'A' and dur1 < 12  ) or (ampm[0] == 'A' and 24 - start1 > dur1) or   (ampm[0] == 'P' and 12 - start1 > dur1) :
      totalDays = 0
    

  if dur1 > 24 or (ampm[0] == 'A' and 24 - start1 <= dur1) or (ampm[0] == 'P' and 12   - start1 <= dur1) :
      totalDays = 1
      if dur1 > 24 :
          totalDays += int((dur1 - (12 - start1)) / 24)


#Formatting days
  weekdays = {1 : "Sunday", 2 : "Monday", 3 : "Tuesday", 4 : "Wednesday",
              5 : "Thursday", 6 : "Friday", 7 : "Saturday"}


  if totalDays == 0 :
      day = day

     
  if totalDays >= 1 and day :
      for i in weekdays :
          if day == weekdays[i] :   
              i = (i + totalDays) % 7
              break
      day = weekdays[i]


#Formatting Output


  if newHour == 0 :
      newHour = str("12")    
    
  if newMinute == 0 :
      newMinute = str("00")
        
  newHour = str(newHour)
  newMinute = str(newMinute)   



  if len(newMinute) == 1:
      newMinute = '0' + newMinute





  if totalDays < 1 and day:  
      print(newHour + ":" + newMinute + ' ' + newampm + ', ' + 
            day)
      return (newHour + ":" + newMinute + ' ' + newampm + ', ' + 
            day)
    
  if totalDays < 1 and not day:  
      print(newHour + ":" + newMinute + ' ' + newampm)
      return (newHour + ":" + newMinute + ' ' + newampm)
  if totalDays >= 1 and day :
      if totalDays == 1 :
          print(newHour + ":" + newMinute + ' ' + newampm + ', '
            + day + ' (next day)')
          return(newHour + ":" + newMinute + ' ' + newampm + ', '
            + day + ' (next day)')
      else :  
          print(newHour + ":" + newMinute + ' ' + newampm + ', '
            + day + ' (' + str(totalDays) + ' days later)')
          return (newHour + ":" + newMinute + ' ' + newampm + ', '
            + day + ' (' + str(totalDays) + ' days later)')
          
  if totalDays >= 1 and not day :
      if totalDays == 1 :
          print(newHour + ":" + newMinute + ' ' + newampm + ' '
             + '(next day)')
          return (newHour + ":" + newMinute + ' ' + newampm + ' '
             + '(next day)')
        
      else :
          print(newHour + ":" + newMinute + ' ' + newampm + ' '
             + '(' + str(totalDays) + ' days later)')
          return(newHour + ":" + newMinute + ' ' + newampm + ' '
             + '(' + str(totalDays) + ' days later)')
    



  