# Complete the breakingRecords function below.
# code by Vertika Dhingra.
def breakingRecords(scores):
    M2=[]
    N2=[]
    for i in range(len(scores)):
        M1=list((max(scores[i],scores[x])) for x in range(len(scores)) if x<=i)
        M2.append(M1)
        N1=list((min(scores[i],scores[x])) for x in range(len(scores)) if x<=i)
        N2.append(N1)

    Highest_Score = [max(M2[x]) for x in range(len(M2))]
    Lowest_Score = [min(N2[x]) for x in range(len(N2))]

    best_record=0
    for i in range(len(Highest_Score)-1):
        if Highest_Score[i]<Highest_Score[i+1]:
            best_record+=1

    worst_record=0
    for i in range(len(Lowest_Score)-1):
        if Lowest_Score[i]>Lowest_Score[i+1]:
            worst_record+=1

    return best_record,worst_record
        



    
   

