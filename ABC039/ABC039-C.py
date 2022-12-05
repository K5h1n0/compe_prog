s = input()
kenban = "WBWBWWBWBWBW"
s = s[:12]
l = []
l.append(kenban)
for i in range(len(kenban)-1):
    kenban = kenban[1:] + kenban[0]
    if kenban[0] == "W":
        l.append(kenban)
name = ["Do","Re","Mi","Fa","So","La","Si"]
for i in range(len(l)):
    if s == l[i]:
        print(name[i])
        exit()