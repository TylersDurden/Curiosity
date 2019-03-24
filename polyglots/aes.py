from Crypto.Cipher import AES
import transformer
import base64
import os, sys


BLOCK_SIZE = 16

PADDING = '{'

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

iv = '#tH15iS4S3CReT!?'   # IV must be 16 bytes
secret = 'a+&sdfgra1235asda#45612A'
print len(secret)

# create a cipher object using the random secret
cipher = AES.new(secret,AES.MODE_CFB,iv)


if '-encrypt' in sys.argv and os.path.exists(sys.argv[2]):
    encrypted_file = '0x'+sys.argv[2].split('.')[0].upper()+'.txt'
    print 'ENCRYPTING ' + sys.argv[2] + '->' + encrypted_file
    # Get the file data
    data = transformer.breakdown_file(sys.argv[2], BLOCK_SIZE)
    encrypted_data = list()
    for line in data.values():
        ln = ''
        for element in line:
            ln += element
        encrypted_data.append(EncodeAES(cipher, ln))
    for enc_line in encrypted_data:
        open(encrypted_file, 'a').write(enc_line)
