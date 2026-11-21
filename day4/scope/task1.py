count = 0

def track_call():
    global count
    count += 1
    print(f"Function called {count} times")

track_call()
track_call()
track_call()
track_call()
print("Final count:", count)