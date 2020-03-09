import sys
new_status = str(sys.argv[1])
<<<<<<< HEAD

updateFile = '../../ui/update.txt'
with open(updateFile, 'w') as filetowrite:
    filetowrite.write('You flight has changed:' + ' ' + new_status)
=======
new_depart_time = str(sys.argv[2])
print('You flight has changed:' + ' ' + new_status + ' ' + new_depart_time)
>>>>>>> ddc79e1ddf43ad73e0714fd51c0e854c85d0a122
