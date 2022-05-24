from sys import stdin

input = stdin.readline

n = int(input().strip())
roads = list(map(int, input().split()))
price = list(map(int, input().split()))
won = 0
tank = 0

for i in range(n-1):
    # print(f'\n{i}번째')
    if roads[i] <= tank:
        tank -= roads[i]
        # print(f'기름 충분, 정상주행중. 남은 기름: {tank}')
    else:
        for j in range(i, len(price)):
            # print(f'최저가 찾는중... {price[j]} < {price[i]}?')
            if price[j] < price[i]:
                low_price_index = j
                break

        # print(f'주행해야 할 km = 넣어야 할 기름: {sum(roads[i:j])}')
        km = sum(roads[i:j])
        won += (km * price[i])
        tank += (km - roads[i])

print(won)