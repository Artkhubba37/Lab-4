def backpack(ves, cena, vmest, items):
    n = len(cena)
    dp = [[0] * (vmest + 1) for _ in range(n + 1)]
    carry = [[[] for _ in range(vmest + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, vmest + 1):
            if ves[i-1] > w:
                dp[i][w] = dp[i-1][w]
                carry[i][w] = carry[i-1][w]
            else:
                if cena[i-1] + dp[i-1][w-ves[i-1]] > dp[i-1][w]:
                    dp[i][w] = cena[i-1] + dp[i-1][w-ves[i-1]]
                    carry[i][w] = carry[i-1][w-ves[i-1]] + [items[i-1]]
                else:
                    dp[i][w] = dp[i-1][w]
                    carry[i][w] = carry[i-1][w]

    return dp[n][vmest], carry[n][vmest]

def remaining_value(cena, items, result_items):
    remaining_items = [item for item in items if item not in result_items]
    remaining_val = sum([cena[items.index(item)] for item in remaining_items])
    return remaining_val

# Пример использования
items=['r','p','a','m','k','x','t','f','d','s','c']
ves = [3,2,2,2,1,3,1,1,1,2,2]
cena = [25,15,15,20,15,20,25,15,10,20,20]
vmest=8
result_value, result_items = backpack(ves, cena, vmest, items)
remaining_val = remaining_value(cena, items, result_items)
result_value=result_value+15-remaining_val
result_items+='i'
print("Максимальная стоимость предметов в рюкзаке:", result_value)
print("Были взяты следующие предметы:", result_items)