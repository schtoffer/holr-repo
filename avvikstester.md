# Resultat av avvikstest motorer
Når vi kjører liten motor på hastighet = x, opplever vi noen ganger at faktisk_hastighet != hastighet. Dette kan være som resultat av motstand i mekanikken i motoren, eller strømforsyning. Altså noe med motoren å gjøre. Denne form for avvik må vi noen ganger ta hensyn til i koden vår. Derfor har vi kjørt en test med hastighet på ulike nivå for å si noe om hva du kan forvente deg av avvik.

## Liten motor
| Hastighet | Laveste observerte hastighet | Numerisk avvik | %-vis avvik |
|---|---|---|---|
| 20 | 18 | -2 | -10.0% |
| 30 | 27 | -3 | -10.0% |
| 40 | 37 | -3 | -7.5% |
| 50 | 47 | -3 | -6.00002% |
| 60 | 56 | -4 | -6.66668% |
| 70 | 66 | -4 | -5.7143% |
| 80 | 76 | -4 | -5.00002% |
| 90 | 85 | -5 | -5.55556% |
| 100 | 95 | -5 | -5.00002% | 

## Stor motor (med hjul montert på)
| Hastighet | Laveste observerte faktiske hastighet | Numerisk avvik    | %-vis avvik   |
| ---       | ---                                   | ---               | ---           |
| 10        | 8                                     | -2                | -20%          |
| 20        | 17                                    | -3                | -15%          |
| 30        | 26                                    | -4                | -13,4%          |
| 40        | 35                                    | -5                | -12,5%         |
| 50        | 44                                    | -6                | -12%           |
| 60        | 53                                    | -7                | -11,7%        |
| 70        | 62                                    | -8                | -11,4%        |
| 80        | 71                                    | -9                | -11,3%        |
| 90        | 83                                    | -8                | -8,9%         |
| 100       | 87                                    | -13               | -13%          |

# Test av ny jobb (beta)


# Koden som er brukt for å gjennomføre denne testen
```
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import equal_to, greater_than, greater_than_or_equal_to
from math import *

#Objecter
hub = PrimeHub()
motorFront = Motor('D')
timer = Timer()
f = open('tabell.txt','w')
f.write("| Hastighet | Laveste observerte hastighet | Numerisk avvik | %-vis avvik |")
f.write("\n|---|---|---|---|")
f.close()
f = open('tabell.txt','a')

#f = open('tabell.txt','r')
#print(f.read())

#Variabler
speed = 10
observationTime = 10
lastSpeed = speed
obsSpeed = []
obsNumericDiff = []
obsPrecentDiff = []

#Program

while speed <= 100:

    motorFront.start(speed)
    wait_until(motorFront.get_speed, greater_than_or_equal_to, speed-2)
    actualSpeed = motorFront.get_speed()

    timer.reset()
    while timer.now() < observationTime:
        actualSpeed = motorFront.get_speed()

        if actualSpeed < lastSpeed:
            
            prosentvisAvvik = (actualSpeed / speed - 1) * 100
            #numeriskAvvik = speed - actualSpeed
            obsSpeed.append(actualSpeed)
            obsNumericDiff.append(actualSpeed - speed)
            obsPrecentDiff.append(prosentvisAvvik)
            lastSpeed = actualSpeed

        '''if timer.now() >= observationTime:
            # then break out of the while loop
            break'''

    f.write("\n| " + str(speed) + " | " + str(obsSpeed.pop()) + " | " + str(obsNumericDiff.pop()) + " | " + str(obsPrecentDiff.pop()) + "% | ")
    speed += 10
    lastSpeed = speed

motorFront.stop()
f.close()
f = open('tabell.txt','r')
print(f.read())


#print("Vi ber om hastighet på " + str(speed) +", men vi får hastighet: " + str(actualSpeed) + ". Dette er et numerisk avvik på " + str(numeriskAvvik) +", og et %-vis avvik på " + str(prosentvisAvvik))
            
f.close()
f = open('tabell.txt','r')
print(f.read())
```