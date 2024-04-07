def towers(disks, source, helper, destination):
    # Last step to complete execution
    if (disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        return

    # Recursive call
    towers(disks - 1, source, destination, helper)
    print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
    towers(disks - 1, helper, source, destination)

disks = int(input('Enter the number of disks that need to be arranged: '))
'''
Source: A
Helper: B
Destination: C
'''
towers(disks, 'A', 'B', 'C')
