import countryflag
def FlagViewer(country):
  countries=[country]
  flags = countryflag.getflag(countries)
  print(flags)