rotors = ['ekmflgdqvzntowyhxuspaibrcj','ajdksiruxblhwtmcqgznpyfvoe','bdfhjlcprtxvznyeiwgakmusqo',
          'esovpzjayquirhxlnftgkdcmwb','vzbrgityupsdnhlxawmjqofeck ']
rotorscheck = ['q','e','v','j','z']
reflectors = ['yruhqsldpxngokmiebfzcwvjat','fvpjiaoyedrzxwgctkuqsbnmhl']
c_rot = []
a = 0
def shift (a,b):
    shifted = ''
    for i in range (len(a)):
        shifted = shifted + chr((ord(a[i]) - 97 + b)%26 + 97)
    shifted = shifted [26-b:] + shifted[0:26-b]
    return shifted
print('input 1 rotor (1-5)')
a = int(input())
if (not(isinstance(a, int))) or (a < 1) or (a>8):
    print('Wrong input');
    exit();
c_rot.append(a-1)
print('input 2 rotor(1-5)')
a = int(input())
if (not(isinstance(a, int))) or (a < 1) or (a>8):
    print('Wrong input');
    exit();
c_rot.append(a-1)
print('input 3 rotor(1-5)')
a = int(input())
if (not(isinstance(a, int))) or (a < 1) or (a>8):
    print('Wrong input');
    exit();
c_rot.append(a-1)
a = ''
print('input reflector (B or C)')
a = str(input())
if (a != 'B' and a != 'C' and a != 'b' and a != 'c'):
    print('Wrong input')
    exit()
if (a == 'B' or a == 'b'):
    c_ref = 0
else:
    c_ref = 1
r1 = ''
r2 = ''
r3 = ''
print('input 1 ring setting a-z')
r1 = str(input())
rotors[c_rot[0]] = shift((rotors[c_rot[0]]), (ord(r1)-97))
print('input 2 ring setting a-z')
r2 = str(input())
rotors[c_rot[1]] = shift((rotors[c_rot[1]]), (ord(r2)-97))

print('input 3 ring setting a-z')
r3 = str(input())
rotors[c_rot[2]] = shift((rotors[c_rot[2]]), (ord(r3)-97))
print(rotors[c_rot[0]],rotors[c_rot[1]],rotors[c_rot[2]])
print('input initial position 1 ring a-z')
r1 = str(input())
print('input initial position 2 ring a-z')
r2 = str(input())
print('input initial position 3 ring a-z')
r3 = str(input())
print ('Enter message:')
s = ''
ans = ''
s = str(input())
s = s.lower()
wwwww = False
#_________________________________________________________________________
for i in range (len(s)):
    
    
    letter = s[i]
    if letter == ' ':
        ans = ans + ' '
        continue
    wwwww = False
    if r3 == rotorscheck [c_rot[2]]:
        wwwww = True
    r3 = chr ((ord (r3) - 97 + 1)%26 + 97)
    if wwwww:
        wwwww = False
        if (r2 == rotorscheck [c_rot[1]]):
            wwwww = True
        r2 = chr((ord(r2) - 97 + 1)%26 + 97)
        if wwwww == True:
            wwwww = False
            r1 = chr ((ord (r1) - 97 + 1)%26 + 97)
    else:
        if r2 == rotorscheck [c_rot[1]]:
            r2 = chr((ord (r2) - 97 + 1)%26 + 97)
            r1 = chr((ord(r1) - 97 + 1)%26 + 97)

    
    
    print(r1,r2,r3)
    letter = chr((ord(letter)-97 + ord(r3) - 97)%26+97)
    letter = rotors[c_rot[2]][ord(letter)-97]
    letter = chr((ord(letter)-97-(ord(r3)-97))%26+97)
    print('3rd wheel', letter)
    letter = chr((ord(letter)-97 + ord(r2) - 97)%26+97)
    letter = rotors[c_rot[1]][ord(letter)-97]
    letter = chr((ord(letter)-97-(ord(r2)-97))%26+97)
    print('2nd wheel',letter)
    letter = chr((ord(letter)-97 + ord(r1) - 97)%26+97)
    letter = rotors[c_rot[0]][ord(letter)-97]
    letter = chr((ord(letter)-97-(ord(r1)-97))%26+97)
    print('1st wheel', letter)
    letter = reflectors[c_ref][ord(letter) - 97]
    print('after reflector',letter)
    #_______________________________________________________
    letter = chr((ord(letter)-97 + ord(r1) - 97)%26+97)
    pos = rotors[c_rot[0]].index(letter)
    letter = chr((pos - (ord(r1)-97) )%26 + 97)
    print('1st wheel',letter)
    letter = chr((ord(letter)-97 + ord(r2) - 97)%26+97)
    pos = rotors[c_rot[1]].index(letter)
    letter = chr((pos - (ord(r2)-97) )%26 + 97)
    print('2st wheel',letter)
    letter = chr((ord(letter)-97 + ord(r3) - 97)%26+97)
    pos = rotors[c_rot[2]].index(letter)
    letter = chr((pos - (ord(r3)-97) )%26 + 97)
    print('3st wheel',letter)
    ans = ans + letter
    print('_______________________________________________')
print()
print(ans)
