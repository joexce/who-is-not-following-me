# Load followers & following data
followers = open("followers.txt", "r")
following = open("following.txt", "r")

# Get username from text
def get_user_name(users):
    # Username variabel
    username = []

    # Idexing variabel
    index = 0

    for res in users:
        spaceSplitter1 = res.split(" ")
        # We will seperate space and only have islower char
        if(len(spaceSplitter1) == 1 and res[0].isupper() != True ):
            # Remove trailing newline and insert into array
            username.insert(index, res.rstrip("\n"))
        index += 1
    return username


whosNotFollBack = set(get_user_name(following)).difference(set(get_user_name(followers)))

print(whosNotFollBack)
