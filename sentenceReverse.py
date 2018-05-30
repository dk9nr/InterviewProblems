def sr(s):
    final = ""
    lol=s.split()
    for word in lol[::-1]:
        final += word
        if word != lol[0]:
            final += " "
    print (final)









if __name__ == "__main__":
    lol= "This is the story of the boy who never became king."
    sr(lol)

        

