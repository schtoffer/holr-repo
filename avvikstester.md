# Resultat av avvikstest motorer
Når vi kjører liten motor på en gitt hastighet så opplever vi noen ganger at den faktiske hastigheten ikke alltid er lik hastigheten vi har oppgitt i programmet vårt. Dette kan være som resultat av mekanisk motstand, ujevn strømforsyning eller andre ytre forhold. Dette fører til avvik mellom programert hastighet og faktisk hastighet, og er noe som vi noen ganger må ta hensyn til i programmet vårt. Derfor har vi kjørt en test med hastighet på ulike nivå for å si noe om hva du kan forvente deg av avvik.

## Liten motor
Testen ble gjennomført med en liten Spike Prime motor. Motoren hadde et grått tannhjul montert direkte på akslingen. Det skulle med andre ord være svært lite ytre påvirkning som hindret motoreren. Motoren ble kjørt i 30 sekunder for hvert hastighetsintervall. Den laveste observerte faktiske motorhastigheten ble loggført og gjenspegles i tabellen under.

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

# Koden som er brukt for å gjennomføre testen
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