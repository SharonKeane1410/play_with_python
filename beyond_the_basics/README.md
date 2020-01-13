PyDev console: starting.
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
import sys
sys.path.append('C:\\Users\\Sharon\\PycharmProjects\\play_with_python\\beyond_the_basics')
sys.path.append('C:\\Users\\Sharon\\PycharmProjects\\play_with_python\\beyond_the_basics\\reader')
sys.path.append('C:\\Users\\Sharon\\PycharmProjects\\play_with_python\\beyond_the_basics\\compressed')
import beyond_the_basics.reader
reader is being imported..
import beyond_the_basics.reader.compressed
import beyond_the_basics.reader.compressed.bzipped
import beyond_the_basics.reader.compressed.gzipped
import beyond_the_basics.reader.reader
r = beyond_the_basics.reader.Reader('beyond_the_basics/reader/compressed/test.bz2')

