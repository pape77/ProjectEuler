days = ['Monday','Tuesday','Wednesday', 'Thursday','Friday','Saturday','Sunday']

dayNum = [1,        2,          3,          4,          5,      6,          7]

def countMonday1st():
    actualDate = [1,1,1901,2]   #(1 jan 1901, Tuesday)
    count = 0
    for year in range(1901,2001):
        actualDate[2] = year
        for month in range(1,13):
            actualDate[1] = month
            actualDate[0] = 1
            if month in [1,3,5,7,8,10,12]:
                daysInMonth = 31
            elif month == 2:
                if year % 4 == 0 and (year %100 != 0 or year % 400 ==0):
                    daysInMonth = 29
                else:
                    daysInMonth = 28
            else:
                daysInMonth = 30
                
            for day in range(1,daysInMonth+1):
                if actualDate[3] == 7 and day == 1:
                    count+=1
                    print(actualDate)
                    actualDate[3] = 1
                    actualDate[0] = day
                elif actualDate[3] == 7:
                    actualDate[3] = 1
                    actualDate[0] = day
                else:
                    actualDate[3] += 1
                    actualDate[0] = day
                
    return count

print(countMonday1st())
                
                
            
            



        

