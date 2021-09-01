hitsTitles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
hitsTitles.append('CHILD IN TIME')
hitsTitles.append('AGAIN')
hitsTitles.insert(2,'HOTEL CALIFORNIA')
hitsTitles.insert(0,'THE SOUND OF SILENCE')
print(hitsTitles.index('HOTEL CALIFORNIA'))
hitsTitles.remove('HOTEL CALIFORNIA')
hitsTitles[0] = 'ENJOY THE SILENCE'
titlesToRead = hitsTitles.copy()
titlesToRead.reverse()
titlesToRead.sort()
print(titlesToRead.pop(0))
print(titlesToRead.pop(1))
print(hitsTitles)
print(titlesToRead)

additionalSongs = ['NOTHING COMPARES 2 U','WISH YOU WERE HERE']
hitsTitles.extend(additionalSongs)
print(hitsTitles)
print(hitsTitles.count('WISH YOU WERE HERE'))
print(hitsTitles.count('RIDERS ON THE STORM'))
hitsTitles.clear()
print(hitsTitles)