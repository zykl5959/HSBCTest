# Review 1
def add_to_list(value, my_list=None):
    # add_to_list with the default argument creates and modifies a new list
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

# Review 2
def format_greeting(name, age):
    # return"Hello, my name is {name} and I am {age} years old."
    # right way to format a string
    return "Hello, my name is {} and I am {} years old.".format(name, age);
 
# Review 3
class Counter:
    # We use count as a Class attribute not an instance attribute
    count = 0
 
    def __init__(self):
        # self.count += 1
        Counter.count += 1
 
    def get_count(self):
        # return self.count
        return Counter.count
 
# # Review 4
import threading
 
class SafeCounter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()  # Add a lock for synchronization
 
    def increment(self):
        #  Could have race Condition here
        with self.lock:  # Acquire the lock before accessing the shared resource
            self.count += 1
 
def worker(counter):
    for _ in range(10):
        counter.increment()
 
counter = SafeCounter()
threads = []
for _ in range(1000):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)
 
for t in threads:
    t.join()
 
# Review 5
def count_occurrences(lst):
    counts = {}
    for item in lst:
        if item in counts:
            # counts[item] =+ 1 is not correct gramma
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

if __name__ == "__main__":
    # print(add_to_list(1))  # Expected: [1]
    # print(add_to_list(2))  # Expected: [2]
    # print(add_to_list(3))  # Expected: [3]

    # print(format_greeting('12','3'));
    # c = Counter()
    # c2 = Counter()
    # print(c.get_count())
    # print(counter.count)
    # lst2 = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
    # print(count_occurrences(lst2))