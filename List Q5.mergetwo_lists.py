# 5.Merge two lists of friends into one and remove any duplicate names.
# Defining two lists of friends
friends_list1 = ['John', 'Theo', 'Janvier', 'Bertine']
friends_list2 = ['Bertine', 'Peace', 'Peter', 'John']

# Merging the lists and removing duplicates by converting to a set
merged_friends_list = list(set(friends_list1 + friends_list2))

# Displaying the merged list
print(merged_friends_list)