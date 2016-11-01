import dkim
import urllib2
import json
import datetime

url = "https://wikileaks.org/podesta-emails/get/"
results = {}
n = 23727
start = str(datetime.datetime.now())

while True:
    try:
        fetch = urllib2.urlopen(url +str(n)).read()
        email = dkim.DKIM(fetch)
        results[n] = email.verify()
        print("email", n, email.verify())
    except urllib2.URLError as url_error:
        break
    except dkim.DKIMException as dkim_error:
        results[n] = str(dkim_error)
        print("email", n, dkim_error)
    n += 1
with open("perm_results", "w") as f:
    f.write("This script started at %s \n" % start)
    f.write("completed at %s \n" % str(datetime.datetime.now()))
    json.dump(results, f)
