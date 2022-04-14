from statistics import mean,median,mode,variance
import pandas as pd
ls = [12,16,24,24,32,72,45,24]
stdDev = pd.Series(ls)

lsMean = mean(ls)
lsMedian = median(ls)
lsMode = mode(ls)
range1 = max(ls) - min(ls); 
stdeviation = stdDev.std(axis=0,skipna=True)

print(f"mean: {lsMean}")
print(f"median: {lsMedian}")
print(f"mode: {lsMode}")
print(f"range1: {range1}")
print(f"stdeviation: {stdeviation}")
print(f"Variance of sample set is {variance(stdDev)}")
