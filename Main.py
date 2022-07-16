from math import sin, radians
from time import sleep
import random
from rich import print as rprint
def wave():
	for a in range(-180, 180):
		s = round( float( "{:.02f}".format( sin( radians(a) ) * 100 ) ) ) // 2
		colors =  [
"green"         ,			
"yellow"        ,
"blue"          ,
"magenta"       ,
"cyan"          ,
"white"         ,
"bright_black"  ,
"bright_red"    ,
"bright_green"  ,
"bright_yellow" ,
"bright_blue"   ,
"bright_magenta",
"bright_cyan"   ,
"bright_white"  ,
"grey0"         ,
"navy_blue"     ,
"dark_blue"     ,
"blue3"         ,
"blue1"         ,
"dark_green"    ,
"deep_sky_blue4",
"dodger_blue3"   ,    
"dodger_blue2"   ,    
"green4"         ,    
"spring_green4"  ,    
"turquoise4"     ,    
"deep_sky_blue3" ,    
"dodger_blue1"   ,    
"dark_cyan"      ,    
"light_sea_green",    
"deep_sky_blue2" ,    
"deep_sky_blue1" ,    
"green3"         ,    
"spring_green3"   ,   
"cyan3"           ,   
"dark_turquoise"  ,   
"turquoise2"       ,  
"green1"             ,
"spring_green2"      ,
"spring_green1"      ,
"medium_spring_green",
"cyan2"              ,
"cyan1"              ,
"purple4"            ,
"purple3"            ,
"blue_violet"        ,
"grey37"             ,
"medium_purple4"     ,
"slate_blue3"        ,
"royal_blue1"        ,
"chartreuse4"        ,
"pale_turquoise4"    ,
"steel_blue"         ,
"steel_blue3"        ,
"cornflower_blue"    ,
"dark_sea_green4"    ,
"cadet_blue"         ,
"sky_blue3"          ,
"chartreuse3"]
		color = random.choice(colors)
		rprint( (s + 50) * f" [{color}]"+"*\n")
		sleep(0.01)

while True:

	wave()
