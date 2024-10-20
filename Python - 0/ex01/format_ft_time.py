import datetime as dt

x = dt.datetime.now()
print("Seconds since January 1, 1970: " + x.strftime("%s") +  " or " + "{:.2e}".format(float(x.strftime("%s"))) + " in scientific notation")
print(x.strftime("%b %d %Y"))
