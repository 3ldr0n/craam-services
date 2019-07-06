import tarfile
import urllib.request

for year in range(1998, 2018):
    filename = "{}_events.tar.gz".format(year)
    url = ("ftp://ftp.swpc.noaa.gov/pub/warehouse/{}/{}"
           .format(year, filename))
    with urllib.request.urlopen(url) as r:
        print("Downloading {} data".format(year))
        with open(filename, "wb") as fp:
            fp.write(r.read())
    tar = tarfile.open(filename)
    tar.extractall()
    tar.close()
