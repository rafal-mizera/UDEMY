isAutomaticMode = True
is80PercentLight = False
isDirectLight = False
isRainy = False
turnLightsOn = isAutomaticMode and isDirectLight or isAutomaticMode and not is80PercentLight or isAutomaticMode and isRainy
print("Automatic mode:   ", isAutomaticMode)
print("Is the light good:", is80PercentLight)
print("Is sun low:       ", isDirectLight)
print("Is it rainy:      ", isRainy)
print("TURN LIGHTS ON:   ", turnLightsOn)

"""Wykładowca mówi studentom. Zaliczysz semestr jeżeli masz obecność co najmniej 80% i średnią >= 3.0 
lub zaliczyłeś pracę semestralną. Zbuduj wyrażenie w Python które stwierdzi czy student,
 który ma obecność 0.85, średnią 3.5 i nie zaliczył pracy semestralnej zda czy nie."""

averageOver3 = False
presenceOver80 = False
semestralWorkComplete = True

semesterComplete = averageOver3 and presenceOver80 or semestralWorkComplete
print(semesterComplete)


