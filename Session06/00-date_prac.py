# date=input("please insert date:") 
# month=int(date[5:7]) 
# year=int(date[:4]) 
# day=int(date[8:]) 
# if month<12:     
#     day=1     
#     month=month+1     
#     # date=year,month,day     
#     date=f"{year}{"/"}{month}{"/"}{day}"     
#     print(date) 
# else:     
#     day=1     
#     month=1     
#     year=year+1     
#     date=f"{year}{"/"}{month}{"/"}{day}"     
#     print(date)

dt=input("ENTER YOUR DATE:::::>>>>") 
year=int(dt[:4]) 
month=int(dt[5:7]) 
day=int(dt[8:]) 
if month<12: 
    day="01" 
    month=month+1 
    print(year,month,day) 
else : 
    day="01" 
    month="01" 
    year=year+1 
    print(year,month,day)
