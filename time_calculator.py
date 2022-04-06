def add_time(start, duration, day=None):

#getting elements of start time
  startHourPosition = start.find(':')
  space = start.find(' ')
  startHour = start[:startHourPosition]
  startMinute = start[startHourPosition + 1 : space]
  am_pm = list(start[space + 1 :])
  if day :
      day = day[0].upper() + day[1:].lower()


#converting start string to int
  startHour = int(startHour)
  startMinute = int(startMinute)

#getting elements of duration time
  durationHourPosition = duration.find(':')
  durationHour = duration[ : durationHourPosition]
  durationMinute = duration[durationHourPosition + 1 : ]

#converting duration string to int
  durationHour = int(durationHour)
  durationMinute = int(durationMinute)

#Calculating new hour
  newHour = 0
  newHour = startHour + durationHour
  if newHour > 12 :
     newHour = ((newHour % 12) - startHour) + startHour
        
#calculating new minute
  newMinute = 0
  newMinute = startMinute + durationMinute
  if newMinute > 59 :
      newMinute = ((newMinute % 60) - startMinute) + startMinute
      newHour = newHour + 1
    
      if newHour > 12 :
          newHour = ((newHour % 12) - startHour) + startHour

#Getting new AM and PM      
  minuteCheck = startMinute + durationMinute
  hourCheck = startHour + durationHour

  if minuteCheck > 59 :
      hourCheck = hourCheck + 1
    
  if hourCheck < 12 :
      new_am_pm = ''
      new_am_pm = am_pm[0] + am_pm[1]
    
  if hourCheck >= 12 and int(((hourCheck / 12)) % 2) == 1 :
      new_am_pm = ''
      if am_pm[0] == 'P' :
          new_am_pm = 'AM'
      else :
          new_am_pm = 'PM'

  if hourCheck > 12 and int(((hourCheck / 12)) % 2) == 0 :
      new_am_pm = ''
      new_am_pm = am_pm[0] + am_pm[1]


#Determine number of days
  totalDays = 0

  if startMinute + durationMinute > 59 :
      durationHour += 1
    
  totalDays = (durationHour - startHour) / 24


  if (am_pm[0] == 'A' and durationHour < 12  ) or (am_pm[0] == 'A' and 24 - startHour > durationHour) or   (am_pm[0] == 'P' and 12 - startHour > durationHour) :
      totalDays = 0
    
  if durationHour > 24 or (am_pm[0] == 'A' and 24 - startHour <= durationHour) or (am_pm[0] == 'P' and 12   - startHour <= durationHour) :
      totalDays = 1
      if durationHour > 24 :
          totalDays += int((durationHour - (12 - startHour)) / 24)


#Formatting and calculating days
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

  #Returning New Time
  if totalDays < 1 and day:  
      return (newHour + ":" + newMinute + ' ' + new_am_pm + ', ' + 
            day)
    
  if totalDays < 1 and not day:  
      return (newHour + ":" + newMinute + ' ' + new_am_pm)
    
  if totalDays >= 1 and day :
      if totalDays == 1 :
          return(newHour + ":" + newMinute + ' ' + new_am_pm + ', '
            + day + ' (next day)')
      else :  
          return(newHour + ":" + newMinute + ' ' + new_am_pm + ', '
            + day + ' (' + str(totalDays) + ' days later)')  
        
  if totalDays >= 1 and not day :
      if totalDays == 1 :
          return(newHour + ":" + newMinute + ' ' + new_am_pm + ' '
             + '(next day)')      
      else :
          return(newHour + ":" + newMinute + ' ' + new_am_pm + ' '
             + '(' + str(totalDays) + ' days later)')
    