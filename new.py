# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))