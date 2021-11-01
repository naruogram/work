import math
sample=[40/100,30/100,30/100]
sample2=[80/100,10/100,10/100]
sample_sam=0;
sample_sam2=0;
for i in sample:
    sample_sam+=-i*math.log(i,2)
print(sample_sam)
for k in sample2:
    sample_sam2=-k*math.log(k,2)
print(sample_sam2)
print(sample_sam>sample_sam2)
# 上記の結果から平均情報量が小さくなり、予測が簡単なことがわかる