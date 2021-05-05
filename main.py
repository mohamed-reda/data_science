users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Initialize the dict with an empty list for each user id:
friendships = {user["id"]: [] for user in users}

# friendships = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
# And loop over the friendship pairs to populate it:
for i, j in friendship_pairs:
    # print("i: ", i, ", j: ", j, type(friendships[i]))

    friendships[i].append(j)

    # Add j as a friend of user i
    friendships[j].append(i)  # Add i as a friend of user j

print(friendships)


def number_of_friends(user):
    """How many friends does _user_ have?"""
    # user_id = user["id"]
    friend_ids = friendships[user["id"]]
    return len(friend_ids)


total_connections = sum(number_of_friends(user) for user in users)
print(total_connections)

num_users = len(users) # length of the users list
avg_connections = total_connections / num_users
print(avg_connections)




