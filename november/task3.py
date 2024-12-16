entry = 'no updates'
logfile = open('logfile.txt','a')
def save_to_log(entry, logfile):
    logfile.write(entry)
    logfile.write('\n')

save_to_log(entry,logfile)