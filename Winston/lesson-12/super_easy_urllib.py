import urllib.request as request
import urllib.parse as parse
import urllib.error as error

contents = request.urlopen('http://data.pr4e.org/romeo.txt')
for line in contents:
    print(line.decode().strip())