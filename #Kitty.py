# Cute Cat
import random

print(r"""
  /\_/\
 ( o.o )
 > ^ <
"meow?"
""")

kitties = [
    r"""
 /\_/\
( ^.^ )
(") (")
"Meow meow!"
""",
    r"""
   /\_/\
  ( -.- )
   > ^ <
"meow..."
""",
    r"""
 /\_/\
( ^_^ )
 > ^ <
"meow!"
""",
    r"""
 /\   /\
{  o_o  }
 >     <
"meow?"
""",
    r"""
 /\_/\
( o.o ) 
 > ^ <
"Meow! ♥"
"""
]

while True:
    _ = input("...")
    if _.lower() == "bad kitty":
        print("meow!!")
        break
    print(random.choice(kitties))