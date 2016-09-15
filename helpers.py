alpha = 'abcdefghijklmnopqrstuvwxyz'
a_cap=str(alpha.upper())
def alphabet_position(letter):
    pl = 0
    for alet in letter:
        alpha_pl=alpha.find(alet)
        cap_pl=a_cap.find(alet)
    #then do the if statements
    if alpha_pl>0:
        pl=pl+alpha_pl
    if cap_pl>=pl:
        pl=pl+cap_pl
    return pl

#letter=input("What letter?")
#print("This is your value: ", alphabet_position(letter))

def rotate_character(char, rot):
    pos=0

#char is lowercase
    if char.islower():
        pos=alpha.find(char)
        new_pos=pos + rot
        return alpha[new_pos % 26]

#uppercase
    elif char.isupper():
        pos=a_cap.find(char)
        new_pos=pos+rot
        return a_cap[new_pos % 26]

    else:
         return char
