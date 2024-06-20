guestName = list(input())
residenceName = list(input())
disorderedName = list(input())

combined = guestName + residenceName   #combining guest and residence name into single list.
combined.sort()                        #sorting it alphabetically.
disorderedName.sort()                  #sorting the jumbled name as a list.

if combined==disorderedName:           #comparing both list to find if they are the same and print "YES" or "NO".
    print("YES")
else:
    print("NO")
