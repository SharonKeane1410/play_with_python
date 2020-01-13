import sys
import beyond_the_basics.reader as reader

r = reader.Reader(sys.argv[1])
try:
    print(r.read())
finally:
    r.close()