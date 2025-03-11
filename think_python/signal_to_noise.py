"Simple signal to noise ratio"
import math
SIGNAL_POWER = 9
NOISE_POWER = 10
RATIO = SIGNAL_POWER / NOISE_POWER
decibels = 10* math.log10(RATIO)
print(decibels)
