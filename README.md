# Høvik og Lier Robotics
Høvik og Lier Robotics er et aktivitetstilbud for barn og unge i alderen 10 - 16 år, bosatt i Lier kommune.

## Resultat av avvikstest liten motor
Når vi kjører liten motor på hastighet = x, opplever vi noen ganger at faktisk_hastighet != hastighet. Dette kan være som resultat av motstand i mekanikken i motoren, eller strømforsyning. Altså noe med motoren å gjøre. Denne form for avvik må vi noen ganger ta hensyn til i koden vår. Derfor har vi kjørt en test med hastighet på ulike nivå for å si noe om hva du kan forvente deg av avvik.

| hastighet | laveste observerte faktiske hastighet | numerisk avvik    | %-vis avvik   |
| ---       | ---                                   | ---               | ---           |
| 10        | 8                                     | 2                 | -20%          |
| 20        | 17                                    | 3                 | -15%          |
| 30        | 27                                    | 3                 | -10%          |
| 40        | 37                                    | 3                 | -7,5%         |
| 50        | 46                                    | 4                 | -8%           |
| 60        | 56                                    | 4                 | -6,7%         |
| 70        | 66                                    | 4                 | -5,7%         |
| 80        | 75                                    | 5                 | -6,25%        |
| 90        | 85                                    | 5                 | -5,6%         |
| 100       | 92                                    | 8                 | -8%           |

### Koden som er brukt for å gjennomføre denne testen
```
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import equal_to, greater_than
from math import *

hub = PrimeHub()
motorFront = Motor('D')

speed = 100

motorFront.start(speed)
wait_until(motorFront.get_speed, equal_to, speed-2)

actualSpeed = motorFront.get_speed()
print(actualSpeed)

lastSpeed = speed

while True:
    actualSpeed = motorFront.get_speed()

    if actualSpeed < lastSpeed:
        print("Vi ber om hastighet på", speed,", men vi får hastighet:", actualSpeed, ". Dette er et avvik på", ((actualSpeed/speed)-1)*100),"%"
        lastSpeed = actualSpeed
```