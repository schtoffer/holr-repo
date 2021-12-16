# Resultat av avvikstest motorer
Når vi kjører liten motor på hastighet = x, opplever vi noen ganger at faktisk_hastighet != hastighet. Dette kan være som resultat av motstand i mekanikken i motoren, eller strømforsyning. Altså noe med motoren å gjøre. Denne form for avvik må vi noen ganger ta hensyn til i koden vår. Derfor har vi kjørt en test med hastighet på ulike nivå for å si noe om hva du kan forvente deg av avvik.

## Liten motor
| Hastighet | Laveste observerte hastighet | Numerisk avvik | %-vis avvik |
|---|---|---|---|
| 10 | 8 | -2 | -20.0% | 
| 20 | 17 | -3 | -15.0% | 
| 30 | 26 | -4 | -13.3333% | 
| 40 | 37 | -3 | -7.5% | 
| 50 | 46 | -4 | -8.00002% | 
| 60 | 56 | -4 | -6.66668% | 
| 70 | 66 | -4 | -5.7143% | 
| 80 | 75 | -5 | -6.25% | 
| 90 | 84 | -6 | -6.66668% | 
| 100 | 95 | -5 | -5.00002% | 


# Test av ny jobb (beta)


# Koden som er brukt for å gjennomføre denne testen
```
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import equal_to, greater_than, greater_than_or_equal_to
from math import *

#Objects
hub = PrimeHub()
motorFront = Motor('D')
timer = Timer()

#Variables
speed = 10
increments = 10
observationTime = 30
lastSpeed = speed
obsSpeed = []
obsNumericDiff = []
obsPrecentDiff = []

## RUN PROGRAM

# Initionalize log-file
f = open('tabell.txt','w')
f.write("| Hastighet | Laveste observerte hastighet | Numerisk avvik | %-vis avvik |")
f.write("\n|---|---|---|---|")
f.close()
f = open('tabell.txt','a')

# Run tests

while speed <= 100:

    motorFront.start(speed)
    wait_until(motorFront.get_speed, greater_than_or_equal_to, speed-2)
    actualSpeed = motorFront.get_speed()

    timer.reset()
    while timer.now() < observationTime:
        actualSpeed = motorFront.get_speed()

        if actualSpeed < lastSpeed:
            
            prosentvisAvvik = (actualSpeed / speed - 1) * 100
            obsSpeed.append(actualSpeed)
            obsNumericDiff.append(actualSpeed - speed)
            obsPrecentDiff.append(prosentvisAvvik)
            lastSpeed = actualSpeed

    # Add observations to the log file
    f.write("\n| " + str(speed) + " | " + str(obsSpeed.pop()) + " | " + str(obsNumericDiff.pop()) + " | " + str(obsPrecentDiff.pop()) + "% | ")
    speed += increments
    lastSpeed = speed

motorFront.stop()
f.close()
f = open('tabell.txt','r')
print(f.read())
```