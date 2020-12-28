number_of_cards, upper_bound = list(map(int, input().split()))
cards = list(map(int, input().split()))

answer = -1

for i in range(number_of_cards):
    for j in range(i+1, number_of_cards):
        for k in range(j+1, number_of_cards):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= upper_bound:
                answer = max(answer, sum)

print(answer)