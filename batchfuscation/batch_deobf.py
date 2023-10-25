# Table
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

# Get batchfuscation content
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