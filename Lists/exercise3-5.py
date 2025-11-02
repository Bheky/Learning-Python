# Exercise focused on replacing one of the guest on the list

guest_list = ['tadiwa moyo', 'debby mcfarlane', 'nyasha gore']
# print(guest_list)

guest = guest_list[0].title()
print(f"{guest}, you are cordially invited to a 6pm dinner.")

guest = guest_list[1].title()
print(f"{guest}, you are cordially invited to a 6pm dinner.")

guest = guest_list[2].title()
print(f"{guest}, you are cordially invited to a 6pm dinner.")

# One guest cannot make it need to be replaced asap
print(f"{guest_list[2].title()}, will not make it tonight.")


# Modifying the list to add a new guest
guest_list = ['tadiwa moyo', 'debby mcfarlane', 'nyasha gore']
del(guest_list[2])
guest_list.insert(2, "garnett magidi")

# Sending out second set of invitation messages
guest = guest_list[0].title()
print(f"{guest}, you are cordially invited to a 6pm dinner.")

guest = guest_list[1].title()
print(f"{guest}, you are cordially invited to a 6pm dinner.")

guest = guest_list[2].title()
print(f"{guest}, you are cordially invited to a 6pm dinner.")