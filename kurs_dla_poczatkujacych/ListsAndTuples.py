marketing = ["loyality program","client promotion","market research"]
marketing.append("public relations")
print(marketing[2])
marketing.insert(2,"investor relations")
emailMarketing = marketing.copy()
emailMarketing.sort()
print(emailMarketing)
internalEmails = ['internal communication']
emailMarketing.extend(internalEmails)
emailMarketing = tuple(emailMarketing)
print(emailMarketing)