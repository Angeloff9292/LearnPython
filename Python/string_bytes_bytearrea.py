import sys
print(sys.getdefaultencoding())
print(ord('A'))
print(chr(65))

s = "Hello!"
enc_ascii = s.encode('ascii')
enc_utf8 = s.encode('utf8')
enc_utf16 = s.encode('utf16')

print(type(enc_ascii))
print(enc_utf8)
print(enc_ascii)
print(enc_utf16)

print(len(enc_utf16))
print(len(enc_ascii))
print(len(enc_utf8))

print(b'string in bytes')
print('some_text'.encode('utf8'))

print(enc_ascii[0])
print(s[0])

