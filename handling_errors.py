def party_planner(cookies, people):
    leftovers = None
    num_each = None
    # TODO: Add a try-except block here to
    #       make sure no ZeroDivisionError occurs.
    while True:
        try:
            num_each = cookies // people
            leftovers = cookies % people
            break
        except ZeroDivisionError:
            print("Non-zero values for people, please!")
            people = int(raw_input("How many people are attending? "))



    return(num_each, leftovers)

# The main code block is below; do not edit this
lets_party = 'y'
while lets_party == 'y':

    cookies = int(raw_input("How many cookies are you baking? "))
    people = int(raw_input("How many people are attending? "))

    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    lets_party = raw_input("\nWould you like to party more? (y or n) ")
