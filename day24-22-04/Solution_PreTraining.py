def BobnBot(N, M, games, Q, queries):
    # Process each query
    results = []
    for query in queries:
        # Remove all -1 from the query
        processed_query = [x for x in query if x != -1]
        
        # Count games with the query as a prefix
        count = 0
        for game in games:
            if game[:len(processed_query)] == processed_query:
                count += 1
        
        # Add count to results
        results.append(count)
    
    return results

# ----------- Main Script ----------- #
# Input the size of games
size = input('Size of games (Example: 2 3) -> ')
try:
    m, n, *x = list(map(int, size.split()))
except:
    print("Invalid input")
    exit()

# ----------- Games ----------- #
games = []
print(f"Specify {m} games of length {n} -> values separated by space (Example: 1 3 3 -1)")
for _ in range(m):
    game = input("Game -> ")
    try:
        game = list(map(int, game.split()))[:n]
    except:
        game = [0 for _ in range(n)]
        print("Invalid input")
    games.append(game)

# ----------- Sequences ----------- #
q = int(input("Q -> "))
seqs = []
print(f"Specify {q} sequences -> values separated by space (Example: 1 3 3 -1)")
for _ in range(q):
    s = input("Sequence -> ")
    try:
        s = list(map(int, s.split()))
    except:
        s = [0 for _ in range(n)]
        print("Invalid input")
    seqs.append(s)

# ----------- Function Call and Output ----------- #
output = BobnBot(m, n, games, q, seqs)
print("Result ->", output)
def BobnBot(N, M, games, Q, queries):
    result = []
    for query in queries:
        # Remove all values after first -1 (including -1)
        prefix = []
        for val in query:
            if val == -1:
                break
            prefix.append(val)
 
        # Count games that start with this prefix
        count = 0
        for game in games:
            if game[:len(prefix)] == prefix:
                count += 1
        result.append(count)
    return result
 
 
# --------------------- INPUT HANDLING ------------------------ #
 
# Input size
size = input('Size of games (Example: 2 3) -> ')
try:
    m, n, *x = list(map(int, size.strip().split()))
except:
    print("Invalid input for size")
    exit()
 
# Input games
games = []
print(f"Enter {m} games, each with {n} values (Example: 1 3 3 -1):")
for _ in range(m):
    game_input = input("Game -> ")
    try:
        game = list(map(int, game_input.strip().split()))[:n]
    except:
        game = [0 for _ in range(n)]
        print("Invalid game input, using zeros.")
    games.append(game)
 
# Input queries
try:
    q = int(input("Number of queries (Q) -> "))
except:
    print("Invalid input for number of queries")
    exit()
 
queries = []
print(f"Enter {q} query sequences (Example: 1 3 3 -1):")
for _ in range(q):
    query_input = input("Sequence -> ")
    try:
        query = list(map(int, query_input.strip().split()))
    except:
        query = []
        print("Invalid query input, using empty query.")
    queries.append(query)
 
# ---------------------- PROCESS ---------------------- #
 
output = BobnBot(m, n, games, q, queries)
 
# ---------------------- OUTPUT ------------------------ #
 
print("\nGames:", games)
print("Queries:", queries)
print("Result ->", output)
