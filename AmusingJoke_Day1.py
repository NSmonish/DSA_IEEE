guestName = list(input("Enter guest's name: "))
residenceName = list(input("Enter residence's name: "))
disorderedName = list(input("Enter jumbled name found: "))

combined = guestName + residenceName   #combining guest and residence name into single list.
combined.sort()                        #sorting it alphabetically.
disorderedName.sort()                  #sorting the jumbled name as a list.

if combined==disorderedName:           #comparing both list to find if they are the same and print "YES" or "NO".
    print("YES")
else:
    print("NO")
