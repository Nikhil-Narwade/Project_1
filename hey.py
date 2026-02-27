# hey.py - me learning python finally!

print("=" * 50)
print("          PYTHON FOR BEGINNERS")
print("=" * 50)

# just variables nothing fancy
my_name = "Sarah"
my_age = 22
my_height = 5.6
like_coding = True

print(f"\nhi i'm {my_name}")
print(f"i'm {my_age} years old")
print(f"i'm {my_height} feet tall")
print(f"do i like coding? {like_coding}")

# let's do some math
print("\n" + "-" * 30)
print("MATH TIME")
print("-" * 30)

x = 20
y = 6

print(f"x = {x}, y = {y}")
print(f"x + y = {x + y}")
print(f"x - y = {x - y}")
print(f"x * y = {x * y}")
print(f"x / y = {x / y}")
print(f"x // y = {x // y}")  # no decimals
print(f"x % y = {x % y}")    # remainder
print(f"x squared = {x ** 2}")

# lists are cool
print("\n" + "-" * 30)
print("LISTS ARE FUN")
print("-" * 30)

games = ["minecraft", "valorant", "fifa", "gta"]
print(f"my games: {games}")
print(f"first game: {games[0]}")
print(f"last game: {games[-1]}")
print(f"first two: {games[:2]}")

games.append("cod")
print(f"after adding cod: {games}")

games.remove("fifa")
print(f"after removing fifa: {games}")

# loops
print("\n" + "-" * 30)
print("LOOPS")
print("-" * 30)

print("counting to 5:")
for i in range(1, 6):
    print(f"  number {i}")

print("\nmy favorite games:")
for game in games:
    print(f"  i play {game}")

# while loop
print("\n" + "-" * 30)
print("WHILE LOOP")
print("-" * 30)

count = 3
print("launch in:")
while count > 0:
    print(f"  {count}...")
    count -= 1
print("  go! 🚀")

# if else stuff
print("\n" + "-" * 30)
print("IF ELSE")
print("-" * 30)

temp = 28

if temp > 30:
    print("damn it's hot")
elif temp > 20:
    print("perfect weather")
elif temp > 10:
    print("kinda chilly")
else:
    print("freezing out here")

# functions
print("\n" + "-" * 30)
print("FUNCTIONS")
print("-" * 30)

def say_hi(name):
    return f"hey {name}, welcome!"

def add(a, b):
    return a + b

def is_odd(num):
    return num % 2 == 1

print(say_hi("sam"))
print(f"10 + 5 = {add(10, 5)}")
print(f"is 7 odd? {is_odd(7)}")
print(f"is 8 odd? {is_odd(8)}")

# dictionaries (like objects)
print("\n" + "-" * 30)
print("DICTIONARIES")
print("-" * 30)

me = {
    "name": "sarah",
    "age": 22,
    "city": "mumbai",
    "hobbies": ["gaming", "reading", "music"]
}

print(f"about me: {me}")
print(f"my name: {me['name']}")
print(f"my age: {me['age']}")
print(f"my city: {me['city']}")
print(f"my hobbies: {', '.join(me['hobbies'])}")

# strings stuff
print("\n" + "-" * 30)
print("STRINGS")
print("-" * 30)

msg = "  python is pretty cool  "
print(f"original: '{msg}'")
print(f"uppercase: '{msg.upper()}'")
print(f"lowercase: '{msg.lower()}'")
print(f"no spaces: '{msg.strip()}'")
print(f"length: {len(msg)}")
print(f"has 'cool'? {'cool' in msg}")

# writing files
print("\n" + "-" * 30)
print("FILES")
print("-" * 30)

# write to file
with open("test.txt", "w") as f:
    f.write("learning python today\n")
    f.write("it's actually fun\n")
    f.write("making progress!")

print("saved to test.txt")

# read from file
try:
    with open("test.txt", "r") as f:
        content = f.read()
        print("\nfile says:")
        print(content)
except:
    print("couldn't read file")

# list comprehension (shortcut)
print("\n" + "-" * 30)
print("LIST COMPREHENSION")
print("-" * 30)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [n * n for n in nums]
even_nums = [n for n in nums if n % 2 == 0]

print(f"numbers: {nums}")
print(f"squares: {squares}")
print(f"evens only: {even_nums}")

# error handling
print("\n" + "-" * 30)
print("ERROR HANDLING")
print("-" * 30)

def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "oops can't divide by zero!"
    except:
        return "something went wrong"

print(f"15 / 3 = {safe_divide(15, 3)}")
print(f"15 / 0 = {safe_divide(15, 0)}")

print("\n" + "=" * 50)
print("       KEEP CODING FAM!       ")
print("=" * 50)
