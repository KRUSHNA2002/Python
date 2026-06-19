def timer(start=0):

    time = start  # state (closure variable)

    print("Timer started at:", time)

    # update function
    def add(seconds):
        nonlocal time
        time += seconds
        return time

    # callback function usage
    def on_change(callback):
        return callback(time)

    # getter
    def get_time():
        return time

    return add, get_time, on_change


# create timer (closure)
add_time, get_time, on_change = timer(10)

print("Current:", get_time())

print("After adding 5:", add_time(5))
print("After adding 10:", add_time(10))

# callback example
result = on_change(lambda t: f"⏰ Time is now {t} seconds")
print(result)