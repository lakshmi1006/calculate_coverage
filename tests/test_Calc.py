from Calc import calc, add_me
def test_calc():
    calc()
    print("hello")

def test_add_me():
    check_val = add_me(1,100)
    assert check_val == 1000
    #check_val = add_me(0,100,4)
    #assert check_val == 1000
    check_val = add_me(2,11,0)
    assert check_val == 121
    check_val = add_me(3,140,5)
    assert check_val == 14
    check_val = add_me(10,2)
    assert check_val == 200
test_add_me()
test_calc()
