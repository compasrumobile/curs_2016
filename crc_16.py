# coding: utf-8
import struct
# from array import array
#
# a = array('H', [1, 2, 3])

class Crc_16:

    def __init__(self):
        self.size = 256
        self.table = list(range(256))

        polynomial = 0xA6BC

        for i in range(self.size):
            value = 0
            temp = i
            for j in range(8):
                if ( ( ( value ^ temp ) & 0x0001 ) != 0 ):
                    value = ( ( value >> 1 ) ^ polynomial )
                else:
                    value >>= 1
                temp >>= 1
            self.table[i] = value

    def ComputeChecksum(self, bbytes):
        size = len(bbytes)
        crc = 0
        for i in range(size):
            index = ( crc ^ bbytes[i] )
            crc = ( ( crc >> 8 ) ^ self.table[index] )

        #crc = swap_endian<unsigned short>(crc ^ 0xffff);
        return crc ^ 0xffff

    def ComputeChecksumBytes(self, bbytes):
        num = self.ComputeChecksum(bbytes)
        return struct.pack('>H', num)


if __name__=='__main__':

    print(Crc_16().ComputeChecksum(b'Hello'))
    print(Crc_16().ComputeChecksumBytes(b'Hello'))

    #print( 1 ^ 1 )



