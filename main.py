def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count
        if amount == 0:
            break
    return result

def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    if dp[amount] == float('inf'):
        return {}
    
    result, current_amount = {}, amount
    for coin in reversed(coins):
        while current_amount >= coin and dp[current_amount] == dp[current_amount - coin] + 1:
            result[coin] = result.get(coin, 0) + 1
            current_amount -= coin

    return result

# Test the functions with an example amount
test_amount = 113
greedy_result = find_coins_greedy(test_amount)
dp_result = find_min_coins(test_amount)

greedy_result, dp_result
