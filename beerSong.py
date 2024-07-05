def beer_song():
    beer_num = 99
    word = "bottles"

    while beer_num > 0:
        if beer_num == 1:
            word = "bottle"

        print(f"{beer_num} {word} of beer on the wall,")
        print(f"{beer_num} {word} of beer.")
        print("Take one down.")
        print("Pass it around.")
        beer_num -= 1

        if beer_num > 0:
            print(f"{beer_num} {word} of beer on the wall.")
        else:
            print("No more bottles of beer on the wall.")
        print()

beer_song()
