rom_name = 'EarthBound Beginnings (ita).nes'

f = open(rom_name,'rb')
rom = f.read()
f.close()

f = open('table2.tbl','r',encoding='utf-8')
table = [line[:-1] for line in f.readlines()]
f.close()

chars = {}
inv_chars = {}

for line in table:
    if line[0] != '#':
        chars[int('0x'+line[:2],16)] = line[3:]
        inv_chars[line[3:]] = int('0x'+line[:2],16)

def convert(text):
    r = ''
    for i in text:
        if i in chars:
            r += chars[i]
        else:
            r += '\\'
    return r

def deconvert(text):
    r = b''
    for i in text:
        if i in inv_chars:
            r += inv_chars[i].to_bytes(1,'big')
        else:
            r += b'\xff'
    return r

#print(convert(rom)[0x71c0d:0x71e0d])
#print(deconvert('NO NAME'))
#print(hex(convert(rom).find('apà',0)))
