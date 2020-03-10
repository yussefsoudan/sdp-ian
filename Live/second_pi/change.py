import sys

new_status = str(sys.argv[1])
new_depart_time = str(sys.argv[2])

updateFile = './sdp-ian/ui/update.txt'
f = open(updateFile, "w+")

f.write('You flight has changed:' + '\n' + new_status + '\n ' + new_depart_time)

f.close()

