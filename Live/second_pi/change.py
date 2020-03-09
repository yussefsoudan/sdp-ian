import sys
new_status = str(sys.argv[1])

updateFile = '../../ui/update.txt'
with open(updateFile, 'w') as filetowrite:
    filetowrite.write('You flight has changed:' + ' ' + new_status)
