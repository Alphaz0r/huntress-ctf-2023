# Batchfuscation
# I was reading a report on past Trickbot malware, and I found this sample that looks a lot like their code! Can you make any sense of it?

A file is included with the challenge

---

Let's download the file!

I won't show it here because it's very very long, but you can find it in this directory.

We know it's a batch file. Let's make a small analysis.

# File analysis

> TL;DR Every single character is placed in a variable and they just wrote the code with a succession of variables.

`Line 2 -> 224` are just variable, after deobfuscating them all I could create a little python dictonnary I could use to write a little python script to deobfuscate the file.


```py

# Dictionnary
variables_dict = {
    'kquqjy' : 't',
    'zvipzis' : 'i',
    'uqcqswo' : 'x',
    'ltevposie' : 'e',
    'kmgnxdhqb' : ' ',
    'naikpbo' : 'd',
    'wzirk' : 'm',
    'rbiky' : 'c',
    'jeuudks' : 'a',
    'xeegh' : '/',
    'mbbzmk' : '=',
    'grfxdh' : ' ',
    'bdevq' : 'set',
    'grtoy': 'a',
    'kbhoesxh': 'b',
    'fxflckau': 'c',
    'pxesvvz': 'd',
    'aeawgno': 'e',
    'vdqvoyxss': 'f',
    'mljmage': 'g',
    'dtqahrd': 'h',
    'xrghxw': 'i',
    'rvrcd': 'j',
    'cxqemy': 'k',
    'djkxbuskp': 'l',
    'auuhztfa': 'm',
    'znvbyce': 'n',
    'exoypdqzg': 'o',
    'upogfi': 'p',
    'xulqq': 'q',
    'jxiczrrc': 'r',
    'qihgjzq': 's',
    'ldawonn': 't',
    'edefpb': 'u',
    'giknplvpv': 'v',
    'fbvra': 'w',
    'klerqtt': 'x',
    'puufauef': 'y',
    'lhuzd': 'z',
    'iwwna': 'A',
    'ilajhm': 'B',
    'hzsouxmm': 'C',
    'dqutqsgb': 'D',
    'jkkvc': 'E',
    'ioexkmd': 'F',
    'jmcpbpld': 'G',
    'udpmq': 'H',
    'rbijdi': 'I',
    'qzpkv': 'J',
    'ikedxdamk': 'K',
    'stcjm': 'L',
    'majmn': 'M',
    'utjscfnmq': 'N',
    'bpxroxnqg': 'O',
    'hrleb': 'P',
    'wzprdlp': 'Q',
    'fikmapqe': 'R',
    'lwuwiovpd': 'S',
    'lftuiqz': 'T',
    'vogsuisdx': 'U',
    'bsslmcgic': 'V',
    'oyyfmilg': 'W',
    'lhniwqwff': 'X',
    'nvfosjl': 'Y',
    'ajexk': 'Z',
    'flopojsse': '0',
    'tqjmbt': '1',
    'wpwjwymw': '2',
    'wxkugd': '3',
    'fxqik': '4',
    'zygcfg': '5',
    'remydays': '6',
    'ztvra': '7',
    'yqdie': '8',
    'lzyqwgi': '9',
    'koimdqluu': '{',
    'tleci': '}',
    'vgysuv': '+',
    'xpjaysvii': ':',
    'nvsna': '*',
    'vrzatob': '=',
    'orutn': '.',
    'hmjhafbu': '_'
}

# Get batchfuscation file content
with open('./batchfuscation' , 'r') as file:
    string = file.read()


# Find / replace
for var, charac in variables_dict.items():
    var='%'+var+'%'
    string = string.replace(var, charac)
    
# Write output to another file
with open('./batchfusaction_deobf', 'w') as output:
    output.write(string)

print("Glory to snek")
```

Once the file has been deobfuscated, I see that most of the lines are just beginning with `rem` which means the line is ignored by the program.

Searching for "flag" inside the file I could find interesting lines.

`:: set flag_character34=d`

After getting them all I had to replace every character in order and got the flag.

flag{acad67e3d0b5bf31ac6639360db9d19a}



