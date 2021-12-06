def average(array):
    _average=0
    for i in array:
        _average=_average+i
    return  _average/len(array)

def distributed(array):
    result=0
    for i in array:
        _distributed=(i-average(array))**2
        result+=_distributed
        print(result)
    return result/len(array)
    
array=[14.5, 13.8, 15.6, 12.3, 14.4, 13.7]
print(distributed(array))
