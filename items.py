from converter import *

rom_name = 'EarthBound Beginnings (ITA).nes'

f = open(rom_name,'rb')
rom = f.read()
f.close()

f = open('items.txt','r',encoding='utf-8')
strings = [line[:-1] for line in f.readlines()]
f.close()

f = open('items_en.txt','r',encoding='utf-8')
strings_en = [line[:-1] for line in f.readlines()]
f.close()

for n in range(len(strings)):
        if strings[n] == '':
                strings[n] = strings_en[n]

strings_len = [0]
for n in range(1,len(strings)):
	strings_len.append(len(strings[n-1]) + strings_len[n-1])
strings = deconvert(''.join(strings))

t = [0, 1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 34, 35, 35, 35, 35, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 45, 45, 45, 45, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 55, 56, 57, 58, 58, 59, 60, 60, 61, 62, 63, 64, 65, 65, 65, 66, 67, 68, 69, 70, 71, 71, 71, 71, 71, 72, 72, 73, 74, 75, 76, 77, 78, 78, 79, 80, 80, 81, 82, 83, 84, 85, 86, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 96, 97, 98, 99, 100, 101, 102, 103, 0, 0, 0, 0, 0, 0, 0, 0, 99, 100, 101, 104, 104, 104, 100, 101, 99, 101, 99, 100, 88, 89, 90, 91, 92, 93, 94, 94, 94, 94, 94, 95, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 105, 106, 107, 107, 107, 107, 107, 107, 108, 109, 110, 111, 112, 112, 112, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 122, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 150, 150, 150, 150, 150, 150, 0, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 221, 222, 223, 223, 223, 224, 225, 225, 225, 226, 227, 228, 228, 228, 228, 228, 229, 230, 231, 231, 232, 232, 233, 234, 235, 236, 237, 238, 238, 239, 240, 241, 241, 241, 242, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 255, 256, 257, 258, 259, 260, 261, 157, 156, 155, 154, 153, 152, 151, 150]

def to_pointer(pos):
    return (pos+0x8000-0x10).to_bytes(2,'little')

def from_pointer(pnt):
    return int.from_bytes(pnt,'little')-0x8000+0x10

pointer_pos = [
    [0x01810,0x01dd0,0xb8,0x08],
    [0x01e10,0x02000,0x3e,0x08],
    [0x2c028,0x2cf50,0x7a,0x20],
    [0x3c62e,0x3c63e,0x08,0x02]
]


strings_start = 0x10
strings_end = 0xc10

pointers = []
for a in pointer_pos:
    for i in range(a[2]):
        pointers.append(a[0]+i*a[3])

if len(strings) <= strings_end:
    rom = rom[:strings_start] + strings + b'\x00'*(strings_end-strings_start-len(strings)) + rom[strings_end:]
    for n in range(len(pointers)):
        rom = rom[:pointers[n]] + to_pointer((sum(len(i) for i in strings[:t[n]]))+strings_start) + rom[pointers[n] + 2:]
else:
    print('Error!')

f = open(rom_name,'wb')
f.write(rom)
f.close()
