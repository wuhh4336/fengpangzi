import base64, zlib
flag = 'eJxLy0lMrw6NTzPMS4n3TVWsBQAz4wXi'
print zlib.decompress(flag.decode('base64'))
