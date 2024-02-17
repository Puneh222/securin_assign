#ProblemStatement:TheDoomedDiceChallenge;

# Part - a = Doomed dice challenge;

#To Find total combinations;
dice_a=[1,2,3,4,5,6]
dice_b=[1,2,3,4,5,6]

total_combinations = len(dice_a) * len(dice_b)
print("Total combinations possible are ", total_combinations)


# 2. Distribution of Possible Combinations
dis_poss_comb = [[0]*6 for i in range(6)]
for i1 in range(1,(len(dice_a)+1)):
    for i2 in range (1,(len(dice_b)+1)):
        total = i1+i2
        dis_poss_comb[i1 - 1][i2- 1] = total

# to display all possible combinations
for i3 in range(1, 7):
    for i4 in range(1, 7):
        total1 = i3 + i4
        print(f"DieA={i3}, DieB={i4}, Sum={total1}")
        
#to display all the possible sum of the combinations in a row 
for row in dis_poss_comb:
    print(row)




#3.. Probability of Sums
j=min(min(dis_poss_comb))
k=max(max(dis_poss_comb))

for m in range(j,k+1):
    s=sum(row.count(m) for row in dis_poss_comb)
    prob = s/total_combinations
    print("the probability of",m, "for",s ,"times is", prob)






