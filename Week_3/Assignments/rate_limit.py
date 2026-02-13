def rate_limit(max_api_calls):
    def decorator(func):
        count = 0
        def wrapper(*args, **kwargs):
            nonlocal count
            if count >= max_api_calls:
                raise Exception("Rate limit exceeded. Please try again later.")
            count += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator 


@rate_limit(6)
def api_call():
    print("API call executed successfully...")

if __name__ == "__main__":
    for _ in range(8):
        try:
            api_call()
        except Exception as e:
            print(f"Error occurred: {e}")