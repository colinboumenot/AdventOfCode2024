text = open('Input/Day22.txt').read()

def get_2000(secret):
    modulo = 16777216
    answer = []
    for _ in range(2000):
        secret = (secret ^ (secret * 64)) % modulo
        secret = (secret ^ (secret // 32)) % modulo
        secret = (secret ^ (secret * 2048)) % modulo
        answer.append(secret)
    return answer

def changes(price):
    return [price[x+1] - price[x] for x in range(len(price) - 1)]
def scores(price, change):
    answer = {}
    for x in range(len(change) - 3):
        pattern = (change[x], change[x+1], change[x+2], change[x+3])
        if pattern not in answer:
            answer[pattern] = price[x+4]
    return answer

secrets = [int(x) for x in text.splitlines()]
result = 0
answer = {}
for line in secrets:
    result += get_2000(line)[-1]
    prices = get_2000(line)
    prices = [x % 10 for x in prices]
    change = changes(prices)
    score = scores(prices, change)
    for k, v in score.items():
        if k not in answer:
            answer[k] = v
        else:
            answer[k] += v

print(result)
print(max(answer.values()))