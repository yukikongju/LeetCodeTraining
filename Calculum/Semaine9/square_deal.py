# Solution: test all 


def solve(r1, r2, r3):
    # test all cases by inversing width and height
    t1 = helper(r1, r2, r3)
    t2 = helper(r1[::-1], r2, r3)
    t3 = helper(r1, r2[::-1], r3)
    t4 = helper(r1, r2, r3[::-1])
    t5 = helper(r1[::-1], r2[::-1], r3)
    t6 = helper(r1[::-1], r2, r3[::-1])
    t7 = helper(r1, r2[::-1], r3[::-1])
    t8 = helper(r1[::-1], r2[::-1], r3[::-1])

    return t1 or t2 or t3 or t4 or t5 or t6 or t7 or t8

def helper(r1, r2, r3):
    # stack all rectangles
    if (r1[0] == r2[0] == r3[0]) and (r1[0] == r1[1] + r2[1] + r3[1]):
        return True

    # stack 1 and 2 the same way; 3 the other way
    if (r1[0] == r2[0]) and (r1[1] + r2[1] == r3[1]) and (r1[0] + r3[0] == r3[1]):
        return True

    # stack 1 and 3 the same way; 2 the other way
    if (r1[0] == r3[0]) and (r1[1] + r3[1] == r2[1]) and (r1[0] + r2[0] == r2[1]):
        return True


    # stack 2 and 3 the same way; 1 the other way
    if (r2[0] == r3[0]) and (r2[1] + r3[1] == r1[1]) and (r2[0] + r1[0] == r1[1]):
        return True

    return False


#  -------------------------------------------------------------------------

def test_sample1(): # Sol: True
    r1, r2, r3 = [7, 3], [7, 1], [7, 3]
    print(solve(r1, r2, r3))
    

def test_sample2(): # Sol: True
    r1, r2, r3 = [9, 2], [7, 4], [7, 5]
    print(solve(r1, r2, r3))


def test_sample3(): # Sol: False
    r1, r2, r3 = [3, 1], [3, 2], [3, 3]
    print(solve(r1, r2, r3))

#  -------------------------------------------------------------------------

def main():
    test_sample1()
    test_sample2()
    test_sample3()
    
if __name__ == "__main__":
    main()
