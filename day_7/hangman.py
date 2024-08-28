words = [
    "apple", "banana", "cherry", "date", "elderberry",
    "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "quince",
    "raspberry", "strawberry", "tangerine", "ugli", "voavanga",
    "watermelon", "xigua", "yuzu", "zucchini"
]

errors_list = [
"""
 +-----+
 |     |
 0     |
       |
       |
       |
==========
""",
"""
 +-----+
 |     |
 0     |
/      |
       |
       |
==========
""",
"""
 +-----+
 |     |
 0     |
/|     |
       |
       |
==========
""",
"""
 +-----+
 |     |
 0     |
/|\\    |
       |
       |
==========
""",
"""
 +-----+
 |     |
 0     |
/|\\    |
/      |
       |
==========
""",
"""
 +-----+
 |     |
 0     |
/|\\    |
/ \\    |
       |
========== 
"""
]