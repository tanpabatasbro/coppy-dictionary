friend = {
    "cup": "ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasyep",
    "cuy":"cuy surucuy"
}
friends = friend
print(f"friend:{friend}\n")
print(f"friends :{friends}\n")

#copy dictionary
friends = friend.copy()

friend["cup"]="ucup si keren"
print(f"friend:{friend}\n")
print(f"friends :{friends}\n")

#pop dictionry
data_asyep = friends.pop("sep")
print(f"data asep = {data_asyep}\n")
print(f"friends = {friends}\n")

#pop item dictionary
data_akhir = friends.popitem()
print(f"data terakhir = {data_akhir}\n")
print(f"friends = {friends}\n")
