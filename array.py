#!/usr/bin/python

#
# Description: 
#   Spiral slice a space-separated symmetric array into a list
#

spiral = []
with open('array.txt','r') as a:
    for line in a:
        row = map(lambda x: x.rstrip(), line.split(' '))
        spiral.append(row)

print str(len(spiral)) + " by " + str(len(spiral[0]))

# note this implementation is destructive to the original; if that needs
#   preserved, copy it first
reformed = []
while (len(spiral) > 0):
    # chuck out the top of the list (easy part)
    reformed.append( spiral.pop(0) )
    # go down the right side
    for x in spiral:
        reformed.append( x.pop() )
    # pop off the bottom (reversing does in-place so we have to handle that)
    if (len(spiral) > 0):
        l = spiral.pop()
        l.reverse()
        reformed.append( l )
    # go up the left side
    if (len(spiral) > 0):
        for x in reversed(spiral):
            reformed.append( x.pop(0) )

# TODO: flatten list for prettier output and easier reuse
print reformed
