projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for name, project in zip(leaders,projects):
    print(f"The leader of {project} project is {name}")

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for name,(project,date) in zip(leaders,zip(projects,dates)):
    print(f"The leader of {project} project started on {date} is {name}")

for pos,(name,(project,date)) in enumerate(zip(leaders,zip(projects,dates))):
    print(f"NR: {pos}--------The leader of {project} project started on {date} is {name}")
