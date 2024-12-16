def seconds_to_time(time):
    if time>359999:
        return None
    else:
        if time >= 3600: 
            hours = time//3600
            hours_in_seconds = hours*3600
            minutes = (time - hours_in_seconds)//60
            minutes_in_seconds = minutes*60
            seconds = time - hours_in_seconds - minutes_in_seconds
            if hours<10:
                hours = '0'+str(hours)
            if minutes<10:
                minutes ='0'+str(minutes)
            if seconds<10:
                seconds = '0'+str(seconds)
            return(str(hours)+':'+str(minutes)+':'+str(seconds))
        else:
            minutes = time//60
            minutes_in_seconds = minutes*60
            seconds = time - minutes_in_seconds
            if minutes<10:
                minutes = '0' + str(minutes)
            if seconds<10:
                seconds = '0' + str(seconds)
            return(str(minutes)+':'+str(seconds))


print(seconds_to_time(3600))
    



