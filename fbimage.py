import binascii
import Image

img = Image.open('') # put file name here
pixdata = img.load()
bitlist = []
bitstring = ""

print "STARTED"

def make_hex(data):
    return size_hex(hex(data[2]).strip('0x')) \
            + size_hex(hex(data[1]).strip('0x')) \
            + size_hex(hex(data[0]).strip('0x')) \
            + "ff"


def size_hex(data):
    if len(data) == 1: return "0"+data
    elif data == '': return "00"
    else: return data

for y in xrange(img.size[1]):
    for x in xrange(img.size[0]):
        bitlist.append(make_hex(pixdata[x,y]))
    for x in xrange(1024-img.size[0]):
        bitlist.append('00000000')

print "RENDERING IMAGE"
bytes = binascii.a2b_hex(''.join(bitlist))
while True:
    bitout = open('/dev/fb0', 'wb')
    bitout.write(bytes)
    bitout.close()

