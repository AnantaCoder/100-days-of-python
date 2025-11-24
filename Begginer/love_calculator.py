def calculate_love_score(name1, name2):
    # Convert names to lowercase
    n1 = name1.lower()
    n2 = name2.lower()

    combined = n1 + n2

    # Count TRUE letters
    t = combined.count("t")
    r = combined.count("r")
    u = combined.count("u")
    e = combined.count("e")
    true_total = t + r + u + e

    # Count LOVE letters
    l = combined.count("l")
    o = combined.count("o")
    v = combined.count("v")
    e2 = combined.count("e")
    love_total = l + o + v + e2

    # Create love score
    score = int(str(true_total) + str(love_total))

    print(f"{score}" + " is the love score ")

# Test call
calculate_love_score("Anirban Sarlar", "Snigdha Das")

