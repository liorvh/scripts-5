#!/usr/bin/env python

import os, sys
from hashlib import sha256

path= str(sys.argv[1])

print 'file "{}"'.format(url)
f = open(path,"rb")
checksum = sha256(f.read()).hexdigest()
print 'sha256 "{}"'.format(checksum)
f.close()
print
