import os, sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# MAX = 500*1024*1024    # 500Mb    - max chapter size

chunkSize = sys.argv[2]

inputFile = '/mnt/3e9410f0-3391-4122-8860-ba3a7997a266/szon.zip'

if chunkSize.endswith('k') or chunkSize.endswith('m') or chunkSize.endswith('g'):
    chunkSizeCount = int(chunkSize[:-1])
else:
    chunkSizeCount = int(chunkSize)

if chunkSize.endswith('k'):
    chunkSizeCount = chunkSizeCount*1024
elif chunkSize.endswith('m'):
    chunkSizeCount = chunkSizeCount*1024*1024
elif chunkSize.endswith('g'):
    chunkSizeCount = chunkSizeCount*1024*1024*1024

MAX = chunkSizeCount
BUF = 50*1024*1024*1024    # 50GB     - memory buffer size

def file_split(FILE, MAX):
    # Split file into pieces, every size is  MAX = 15*1024*1024 Byte
    chapters = 1
    uglybuf = ''
    with open(FILE, 'rb') as src:
        while True:
            tgt = open(FILE + '.%03d' % chapters, 'wb')
            written = 0
            while written < MAX:
                if len(uglybuf) > 0:
                    tgt.write(uglybuf)
                tgt.write(src.read(min(BUF, MAX - written)))
                written += min(BUF, MAX - written)
                uglybuf = src.read(1)
                if len(uglybuf) == 0:
                    break
            tgt.close()
            if len(uglybuf) == 0:
                break
            chapters += 1

if __name__ == '__main__':
    file_split(sys.argv[1], chunkSizeCount)