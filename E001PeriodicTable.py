table = '''1 H 氢 Hydrogenium Hydrogen
2 He 氦 Helium Helium
3 Li 锂 Lithum Lithium
4 Be 铍 Beryllium Beryllium
5 B 硼 Borium Boron
6 C 碳 Carbonium Carbon
7 N 氮 Nitrogenium Nitrogen
8 O 氧 Oxygenium Oxygen
9 F 氟 Fluorum Fluorine
10 Ne 氖 Neonum Neon
11 Na 钠 Natrium Sodium
12 Mg 镁 Magnesium Magnesium
13 Al 铝 Aluminium Aluminium
14 Si 硅 Silicium Silicon
15 P 磷 Phosphyorum Phosphorus
16 S 硫 Sulphu Sulfur
17 Cl 氯 Chlorum Chlorine
18 Ar 氩 Argonum Argon
19 K 钾 Kalium Potassium
20 Ca 钙 Calcium Calcium
21 Sc 钪 Scandium Scandium
22 Ti 钛 Titanium Titanium
23 V 钒 Vanadium Vanadium
24 Cr 铬 Chromium Chromium
25 Mn 锰 Manganum Manganum
26 Fe 铁 Ferrum Iron
27 Co 钴 Cobaltum Cobalt
28 Ni 镍 Niccolum Nickel
29 Cu 铜 Cuprum Copper
30 Zn 锌 Zincum Zinc
31 Ga 镓 Gallium Gallium
32 Ge 锗 Germanium Germanium
33 As 砷 Arsenium Arsenic
34 Se 硒 Selenium Selenium
35 Br 溴 Bromium Bormine
36 Kr 氪 Kryptomum Krypton
37 Rb 铷 Rubidium Rubidium
38 Sr 锶 Strontium Strontium
39 Y 钇 Yttrium Yttrium
40 Zr 钴 Zirconium Zirconium
41 Nb 铌 Niobium Niobium
42 Mo 钼 Molybdanium Molybdanium
43 Tc 锝 Technetium Technetium
44 Ru 钌 Ruthenium Ruthenium
45 Rh 铑 Rhodium Rhodium
46 Pd 钯 Palladium Palladium
47 Ag 银 Argentum Silver
48 Cd 镉 Cadmium Cadmium
49 In 铟 Inlium Inlium
50 Sn 锡 Stannum Tin
51 Sb 锑 Stibium Antimony
52 Te 碲 Tellurum Tellurium
53 I 碘 Iodium Iodine
54 Xe 氙 Xenonum Xenon
55 Cs 铯 Caesium Caesium
56 Ba 钡 Baryum Barium
57 La 镧 Lanthanum Lanthanum
58 Ce 铈 Cerium Cerium
59 Pr 镨 Praseodymium Praseodymium
60 Nd 钕 Neodymium Neodymium
61 Pm 钷 Promethium Promethium
62 Sm 钐 Samarium Samarium
63 En 铕 Europinu Europinu
64 Gd 钆 Gadolinium Gadolinium
65 Tb 铽 Terbium Terbium
66 Dy 镝 Dysprosium Dysprosium
67 Ho 钬 Holmium Holmium
68 Er 铒 Erbium Erbium
69 Tm 铥 Thulium Thulium
70 Yb 镱 Ytterbium Ytterbium
71 Lu 镥 Lrtetium Lrtetium
72 Hf 铪 Hafnium Hafnium
73 Ta 钽 Tanatalum Tantalum
74 W 钨 Wolfram Tungsten
75 Re 铼 Rhenium Rhenium
76 Os 锇 Osmium Osmium
77 Ir 铱 Iridium I ridium
78 Pt 铂 Platinum Platinum
79 Au 金 Aurum Gold
80 Hg 汞 Hydrargyrum Mercury
81 Tl 铊 Thallium Thallium
82 Pb 铅 Plumbum Lead
83 Bi 铋 Bismuthum Bismuth
84 Po 钋 Polonium Polonium
85 At 砹 Astatium Astatium
86 Rn 氡 Radon Radon
87 Fr 钫 Franium Franium
88 Ra 镭 Radium Radium
89 Ac 锕 Actinium Actinium
90 Th 钍 Thorium Thorium
91 Pa 镤 Protactinium Protactinium
92 U 铀 Uranium Uranium
93 Np 镎 Neptunium Neptunium
94 Pu 钚 Plutonium Plutonium
95 Am 镅 Americium Americium
96 Cm 锔 Curkelium Curkelium
97 Bk 锫 Berkelium Berkelium
98 Cf 锎 Californium Californium
99 Es 镶 Einsteinium Einsteinium
100 Fm 镄 Fermim Fermim
101 Md 钔 Mendelevium Mendelevium
102 No 锘 Nobelium Nobelium
103 Lr 铹 Lawrencium Lawrencium
'''

table_rest = '''104号以后的元素发现的晚，因此没有拉丁文名称。。。但有英文的。。。
104 Rf 钅卢 Rutherfordium
105 Db 钅杜 Dubnium
106 Sg 钅喜 Seaborgium
107 Bh 钅波 Bohriium
108 Hs 钅黑 Hassium
109 Mt 钅麦 Meitnerium
110 Uun
111 Uuu
112 Uub'''

#
# Split the table by lines
#

table_lines = table.split("\n")
print(table_lines)


#
# Split the table by spaces
#

for i in range(len(table_lines)):
    table_lines[i] = table_lines[i].split(" ")

print(table_lines)


def SpacesForLineUp(str):
    return " " * (16 - len(str))


#
# Output The Table
#

def OutputThisElement(input, element):
    result = input

    # Add Number
    result += "%3d" % int(element[0])
    result += "  "

    # Add Symbol
    if len(element[1]) == 1:
        result += element[1]
        result += "   "
    else:
        result += element[1]
        result += "  "

    # Add Chinese Name
    result += element[2]
    result += "  "

    # Add Latin/English Name
    if element[4][0].lower() == element[1][0].lower():
        # Names the same , Use English
        result += element[4]
        result += "\n"
    else:
        result += element[3]
        result += SpacesForLineUp(element[3])
        result += "(Latin)"
        result += "\n"

    return result

def TableSearch(table, chinese_name):
    for i in range(len(table)):
        if table[i][2] == chinese_name:
            return table[i]
    raise ValueError("Can not find the fitting element in the table.")
    return None

def AddEmptyLine(input):
    return input + "\n"

#
# Start Outputting
#

outs = ""

for i in range(0, 5):
    outs = OutputThisElement(outs, table_lines[i])
outs = AddEmptyLine(outs)

for i in range(5, 10):
    outs = OutputThisElement(outs, table_lines[i])
outs = AddEmptyLine(outs)

for i in range(10, 15):
    outs = OutputThisElement(outs, table_lines[i])
outs = AddEmptyLine(outs)

for i in range(15, 20):
    outs = OutputThisElement(outs, table_lines[i])
outs = AddEmptyLine(outs)

outs = OutputThisElement(outs, TableSearch(table_lines, "金"))
outs = OutputThisElement(outs, TableSearch(table_lines, "银"))
outs = OutputThisElement(outs, TableSearch(table_lines, "铜"))
outs = OutputThisElement(outs, TableSearch(table_lines, "铁"))
outs = OutputThisElement(outs, TableSearch(table_lines, "锌"))
outs = AddEmptyLine(outs)

outs = OutputThisElement(outs, TableSearch(table_lines, "钡"))
outs = OutputThisElement(outs, TableSearch(table_lines, "铂"))
outs = OutputThisElement(outs, TableSearch(table_lines, "锰"))
outs = OutputThisElement(outs, TableSearch(table_lines, "汞"))
outs = OutputThisElement(outs, TableSearch(table_lines, "碘"))
outs = AddEmptyLine(outs)

print(outs)

with open("PeriodicTable.txt", "wb") as f:
    f.write(outs.encode(encoding="utf-8"))
