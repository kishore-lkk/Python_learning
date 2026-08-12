numbers = [1,2,3,4]
alphabets = ["a", "b", "c"]
main_dict = {}

for number in numbers:
    main_dict[number] = {}
    for character in alphabets:
        main_dict[number][character]
