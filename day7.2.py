print("Fake Fan Finder 👀.")
print("----------------")

name = input("Do you watch TV Series? ---> ")
if name == "yes":
    print("Hmm, answer these questions to identify as a true fan.")
    question = input("Do you watch Modern Family? --> ")

    if question == "no":
        print("What are you even doing not watching this gem. Highly recommended show!!")

    if question == "yes":
        print("Interesting....")
        print("I'll ask you, your favourite character in the show but there can be only one...HINT --> He is known as a great magician!!")

        fav = input("Whose's your favourite character in Modern Family --> ")

        if fav == "phill":
            print("Might be a lucky guess...")
            choose = input("Was Phill a divorcee or a full-time dad? --> ")

            if choose == "a full time dad":
                print("""Truee..He has been a father since his children 
                were born. And has been the best dad throughout the 
                season!""")

            elif choose == "a divorcee":
                print("""There, a fake fan, wanting to be known amongst the people. Sad. You should watch the show Modern Family. You won't regret it.""")

else:
    print("Ehhh...Boring person...😝")
