# Høvik og Lier Robotics
Høvik og Lier Robotics er et aktivitetstilbud for barn og unge i alderen 10 - 16 år, bosatt i Lier kommune.

## Resultat av avvikstest motorer
Når vi kjører liten motor på hastighet = x, opplever vi noen ganger at faktisk_hastighet != hastighet. Dette kan være som resultat av motstand i mekanikken i motoren, eller strømforsyning. Altså noe med motoren å gjøre. Denne form for avvik må vi noen ganger ta hensyn til i koden vår. Derfor har vi kjørt en test med hastighet på ulike nivå for å si noe om hva du kan forvente deg av avvik.

### Liten motor
| hastighet | laveste observerte faktiske hastighet | numerisk avvik    | %-vis avvik   |
| ---       | ---                                   | ---               | ---           |
| 10        | 8                                     | -2                | -20%          |
| 20        | 17                                    | -3                | -15%          |
| 30        | 27                                    | -3                | -10%          |
| 40        | 37                                    | -3                | -7,5%         |
| 50        | 46                                    | -4                | -8%           |
| 60        | 56                                    | -4                | -6,7%         |
| 70        | 66                                    | -4                | -5,7%         |
| 80        | 75                                    | -5                | -6,3%        |
| 90        | 85                                    | -5                | -5,6%         |
| 100       | 92                                    | -8                | -8%           |

### Stor motor (med hjul montert på)
| hastighet | laveste observerte faktiske hastighet | numerisk avvik    | %-vis avvik   |
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

## Koden som er brukt for å gjennomføre denne testen
```
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import equal_to, greater_than
from math import *

hub = PrimeHub()
motorFront = Motor('A')

speed = 40

motorFront.start(speed)
wait_until(motorFront.get_speed, equal_to, speed-2)

actualSpeed = motorFront.get_speed()
print(actualSpeed)

lastSpeed = speed

while True:
    actualSpeed = motorFront.get_speed()

    if actualSpeed < lastSpeed:
        prosentvisAvvik = (actualSpeed / speed - 1) * 100
        numeriskAvvik = speed - actualSpeed
        print("Vi ber om hastighet på " + str(speed) +", men vi får hastighet: " + str(actualSpeed) + ". Dette er et numerisk avvik på " + str(numeriskAvvik) +", og et %-vis avvik på " + str(prosentvisAvvik))
        lastSpeed = actualSpeed
```