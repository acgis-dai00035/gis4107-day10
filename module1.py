#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dai
#
# Created:     15/11/2019
# Copyright:   (c) Dai 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
##x = 17
##y = 7
##print float(x)/y
##def kmll(x,y):
##    pass
##class Person:
##  def __init__(self, name, age):
##    self.name = name
##    self.age = age
##
##  def myfunc(self):
##    print("Hello my name is " + self.name)
##
##p1 = Person("John", 36)
##p1.myfunc()
print ' </Placemark>\n</Document>\n</kml>'
name = 'qwe'
longitude = 74
latitude = 45
wateroffice_link='qwewqeqwe'
print ' <Placemark>\n  <name>' + name + '</name>\n  <description>\n' +'   '+ wateroffice_link + '\n  </description>\n  <Point>\n' +'   <coordinates>'+ str(longitude) +','+str(latitude) + '</coordinates>\n  </Point>'