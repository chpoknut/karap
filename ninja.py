def func1(arg1, arg2):
    var33 = var5(arg1, arg2)
    var34 = func8()
    var38 = func9(var34, arg1)
    var43 = func11(var34, arg2)
    var44 = ((var43 + arg1) + 1435543863) | arg1
    if arg2 < var38:
        var45 = arg1 & 986 & arg2 & var44
    else:
        var45 = (var33 - arg1 - var43) | var33
    var46 = arg2 - (var44 ^ arg1) - var34
    var47 = ((var33 + 1997267405) ^ 832) | var43
    var48 = var44 + ((var44 - var33) - arg2)
    var49 = arg1 | (var48 ^ var33) + var38
    var50 = var34 - arg2 & (var33 - var38)
    var51 = (var48 - (var43 - var44)) | 487
    var52 = (var49 - var43) - arg1 ^ arg2
    var53 = (var48 - arg2) & (-804677847 & var50)
    var54 = (var38 & var44) + (var47 + var50)
    var55 = (var46 | var49) | var38 | var43
    var56 = var48 | var55
    var57 = 862 | var38 | var52 ^ var52
    var58 = ((var38 | var43) & var44) - var56
    var59 = var46 ^ var47 & var48 ^ var44
    var60 = var44 | ((var51 ^ 500) + var33)
    var61 = 510670021 ^ var47
    result = ((var59 - arg1 + 1059651517 | (arg2 ^ var50 & (var38 & (var46 ^ var54)))) | var34) + var52
    return result
def func11(arg39, arg40):
    var41 = 0
    for var42 in xrange(11):
        var41 += (arg39 | var41) & 9
    return var41
def func8():
    func6()
    result = len(range(4))
    func7()
    return result
def func7():
    global len
    del len
def func6():
    global len
    len = lambda x : 4
def func4(arg6, arg7):
    var12 = func5(arg6, arg7)
    var13 = (arg7 + var12) ^ arg7 - -1662745462
    var14 = (arg7 ^ var12) & (-896 - -1881047480)
    var15 = -214 & -879
    var16 = ((-465 - var14) ^ 748086954) ^ arg7
    var17 = arg6 - -1044788285
    var18 = arg6 | var17 - var12 + var16
    var19 = (-193 & var18) & 1836765422 & -352374503
    var20 = (var19 ^ var17 + var17) + var17
    var21 = arg6 - var20
    var22 = var15 - (var15 - var12) - var12
    if var16 < var19:
        var23 = -1721849058 & var15
    else:
        var23 = var15 & (var17 | 153) & var13
    var24 = arg6 ^ var12 & var14 & arg6
    var25 = var16 ^ var21 + var13
    var26 = -828 & var12 & var18
    if var15 < var15:
        var27 = var26 | (var16 ^ arg6 + var13)
    else:
        var27 = var22 ^ var16
    var28 = arg6 ^ var15
    var29 = var25 | (var22 ^ (var15 + 566))
    var30 = var22 ^ var13
    var31 = ((var28 | var17) ^ var21) ^ arg7
    var32 = arg7 + (var31 - var30 | var20)
    result = var22 + var21 | var15 | arg6 + var28 | var16
    return result
def func5(arg8, arg9):
    var10 = 0
    for var11 in xrange(4):
        var10 += var10 - 8 + arg8
    return var10
def func3():
    closure = [1]
    def func2(arg3, arg4):
        closure[0] += func4(arg3, arg4)
        return closure[0]
    func = func2
    return func
var5 = func3()
def func9(arg35, arg36):
    def func10(acc, rest):
        var37 = 5 ^ 4
        if acc == 0:
            return var37
        else:
            result = func10(acc - 1, var37)
            return result
    result = func10(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 12'
    print 'arg_number: 62'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
