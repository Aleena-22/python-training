def secret_time_machine(s, k):
    s = list(s)
    result = ["IMPOSSIBLE"]
    def is_valid(a, b):
        return abs(int(a) - int(b)) >= 3
 
    def dfs(s, swaps_left):
        if swaps_left == 0:
            current = ''.join(s)
            if result[0] == "IMPOSSIBLE" or current > result[0]:
                result[0] = current
            return
 
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n):
                if is_valid(s[i], s[j]):
                    s[i], s[j] = s[j], s[i]
                    dfs(s, swaps_left - 1)
                    s[i], s[j] = s[j], s[i]
 
    dfs(s, k)
    return result[0]
 
print(secret_time_machine('2731', 2))
print(secret_time_machine('2731', 1))
print(secret_time_machine('2731', 0))
print(secret_time_machine('555', 1))

