texto = 'PETER –HI, EXCUSE-ME, WHAT ́S YOUR NAME?ALICE –HELLO, I AM ALICE.PETER –NICE TO MEET YOU ALICE, MY NAME IS PETER.ALICE –NICE TO MEET YOU PETER.PETER –SO, I AM FROM NEW YORK, AND I AM ALITTLE LOST HERE. CAN YOU HELP ME?ALICE –SURE. WHAT DO YOU NEED?PETER –I WANT A GOOD PLACE TO HAVE LUNCH. ISTHERE A GOOD RESTAURANT AROUND?ALICE –YES, THERE ARE SOME GREAT RESTAURANTSIN THIS NEIGHBORHOOD.PETER –OH, THAT ́S AMAZING!ALICE –WHAT KIND OF FOOD DO YOU LIKE?PETER –I LIKE ALMOST ALL KINDS OF FOOD, BUT MY FAVORITES ARE ITALIAN AND JAPANESE FOOD.ALICE –WELL, THERE IS A VERY GOOD ITALIAN RESTAURANT JUST A FEW BLOCKS AWAY.PETER –OK.ALICE –AND THERE IS ALSO A FANTASCTIC JAPANESERESTAURANT THAT IS NOT VERY FAR AS WELL.PETER –RIGHT. WHERE IS THE JAPANESERESTAURANT?ALICE –IT ́S ON TRAFALGAR ST. NEXT TO A BANK AND JUST ACROSS THE MOVIE THEATER.PETER –I THINK I KNOW THIS MOVIE THEATER. IT ́SBETWEEN A PUB AND A PLOWER SHOP, RIGHT?ALICE –YES! THAT ́S IT.PETER –GREAT! BUT HOW CAN I GET THERE FROMHERE?ALICE –WELL IT ́S VERY EASY. FIRST, GO DOWN THISSTREET FOR 5 BLOCKS, THEN YOU TURN LEFTAT THE TRAFFIC LIGHT.PETER –OK...ALICE –NOW, GO AHEAD FOR TWO BLOCKS AND TURN RIGHT AT VIRGINIAN AVENUE. PETER –FINE...ALICE –ON VIRGINIAN AVENUE GO AHEAD FORTHREE BLOCKS, THE RESTAURANT IS ON YOUR LEFT JUST PAST THE DRUGSTORE.PETER –WELL, IT LOOKS SIMPLE.ALICE –AND IT IS. VERY EASY. YOU CAN ́T MISS IT!PETER –THANK YOU VERY MUCH ALICE...  WELL,MAYBE YOU COULD GO HAVE LUNCH WITHME. WHAT DO YOU SAY?ALICE –SORRY PETER, I CAN ́T. I AM WAITING FOR MYBOYFRIEND.PETER –OH, I AM SORRY!ALICE –IT ́S OK. I HOPE YOU LIKE THE RESTAURANT.GOOD BYE PETER!PETER –BYE BYE, AND... THANKS AGAIN!'


separado = texto.split('PETER –')


falas_peter = []
falas_alice = []
for x in separado:
    corte = x.split('ALICE –')
    falas_peter.append(corte[0])
    try:
        falas_alice.append(corte[1])
    except:
        pass

falas_peter = falas_peter[1:]




for posx, x in enumerate(falas_peter):
    # print(f'PETER: {falas_peter[posx]}')
    try:
        print(f'ALICE: {falas_alice[posx]}')
    except:
        pass
    print()