# code by Vertika Dhingra.
# 5/15 test cases passed.
def minion_game(string):
    # your code goes here
    S = string
    len_s = len(S)
    Vowels = 'AEIOU'

    Vowels_S = set([v for v in S if v in Vowels])

    kevin_score = []
    stuart_score = []
    for e, i in enumerate(S):
        if i in Vowels_S:
            for r in range(0, len_s+1):
                kevin_score.append(S[e:e+r])
        elif i not in Vowels_S:
            for m in range(0, len_s+1):
                stuart_score.append(S[e:e+m])

    kevin_score_unique = set(kevin_score)
    stuart_score_unique = set(stuart_score)
    kevin_score_unique.remove('')
    stuart_score_unique.remove('')

    kevin_score_unique_list = list(kevin_score_unique)
    stuart_score_unique_list = list(stuart_score_unique)

    Final_Score_kevin = 0
    for x in kevin_score_unique_list:
        Final_Score_kevin += sum(1 for i in range(len(S))
                                 if S.startswith(x, i))

    Final_Score_stuart = 0
    for x in stuart_score_unique_list:
        Final_Score_stuart += sum(1 for i in range(len(S))
                                  if S.startswith(x, i))

    if Final_Score_kevin > Final_Score_stuart:
        print('Kevin', Final_Score_kevin)
    elif Final_Score_kevin < Final_Score_stuart:
        print('Stuart', Final_Score_stuart)
    elif Final_Score_stuart == Final_Score_kevin:
        print('Draw')
