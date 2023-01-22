#  There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus or . The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.  For each game, you will get an array of clouds numbered if they are safe or if they must be avoided. 

# solution: if we can jump two, we do it, else we jump one

def jumpingOnClouds(c):
    # Write your code here
    n = len(c) 
    pos, jump = 0, 0
    
    while pos < n -1:
        if (pos + 2 < n) and (c[pos+2] == 0):
            jump += 1
            pos += 2
        elif (pos +1 < n) and (c[pos+1] == 0):
            jump += 1
            pos += 1
    return jump
