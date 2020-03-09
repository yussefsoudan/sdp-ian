import sys
new_status = str(sys.argv[1])
new_depart_time = str(sys.argv[2])
updateFile = '../../ui/update.txt'
with open(updateFile, 'w') as filetowrite:
    filetowrite.write('You flight has changed:' + ' ' + new_status + ' ' + new_depart_time)
