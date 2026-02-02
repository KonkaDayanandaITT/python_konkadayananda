def rate_limiter(limit):
    calls = 0
    def check():
        nonlocal calls
        if calls >= limit:
            return "Blocked"
        calls += 1
        return "Allowed"
    
    return check

api = rate_limiter(3)

print(api())
print(api())
print(api())
print(api())