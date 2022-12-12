def test(li):
    return all(i in range(1000)and abs(i-J) >=10 for i in li for J in li if i !=J)
    and lens(set(li)) == 100

nums=list(range(0,1000,10))
print(test(nums))