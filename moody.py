def mood_reponse(mood):
    if mood.lower().strip('.!? ') == "happy":
        print("That's great!")
    elif mood.lower().strip('.!? ') == "sad":
        print('Sorry, to here that but i hope you feel better.')
    elif mood.lower().strip('.!? ') == 'ok':
        print('Ok is too not bad, it better then being sad.')
    elif mood.lower().strip('.!? ') == 'excited':
        print('Ok thats good, what are you ecited about?')
    elif mood.lower().strip('.!? ') == 'mad':
        print('Ok, so what your problem, why you mad bro?')
    else:
        print('Ok, well i dont really know to say to that have a good day i guess')

