
def PrintAnimal(*animals):

    bear = r'''
        /  \.-"""-./  \
        \    -   -    /
         |   o   o   |
         \  .-'"'-.  /
          '-\__Y__/-'
             `---`'''
    cat = r'''
        |\---/|
        | o_o |
         \_^_/'''

    bat = r'''
           /\                 /\
          / \'._   (\_/)   _.'/ \
         /_.''._'--('.')--'_.''._\
         | \_ / `;=/ " \=;` \ _/ |
          \/ `\__|`\___/`|__/`  \/
                  \(/|\)/       '''
    for animal in animals:
        if animal == 'cat':
            print(cat)
        elif animal == 'bear':
            print(bear)
        elif animal == 'bat':
            print(bat)
        else:
            print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animals)
            return False
    return True

if PrintAnimal("cat","bear","bat"):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')