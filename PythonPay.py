try:
    hours = raw_input("Enter hours: ")
    h = float(hours)
    rate = raw_input("Enter Rate: ")
    r = float(rate)
except: print "Please enter a number"

#print rate, hours
if h <=40:
    pay = r * h
else:
    pay = r * 40 + (r * 1.5*(h-40))
print 'Total pay= '
print pay
