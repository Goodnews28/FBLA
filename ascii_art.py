import time
#Track displayed art to avoid repetition
displayed_art = set()
def get_art_for_stage(stage):
    """Return ASCII art for different game stages"""
    art = {
        "18-27": """
    🎓 Early Life
    +---------+
    |         |
    | FUTURE  |
    | AHEAD   |
    |         |
    +---------+
    """,

        "28-37": """
    🏠 Major Decisions
    +---------------------------+
    |             `'::::.       |
    |         _____A_           |
    |        /      /\          |
    |     __/__/\__/  \___      |
    | ---/__|" '' "| /___/\---- |
    |   |''|"'||'"| |' '||      |
    |   """""""""""""""""""     | 
    +---------------------------+
    """,
        "38-47": """
    👴 Crucial Period for Wealth
   ____________________________
  |  LEVEL UP!                 |
  |  Age: [ 30 → 40 ]          |
  |  XP: ██████████ 99%        |
  |  Skills:                   |
  |  - Wisdom       ✔️         |
  |  - Experience   ✔️         |
  |  - Responsibility ✔️       |
  |  - Fun Still Allowed ✔️    |
  |_____________________________|

    """,

        "48-57": """
    💼 Mid-Life
        /\  
       /  \      "The View is Great at 40-50"
      /    \      
     /      \    But There's More to Climb...  
    /        \  
   /__________\  
  /            \  
 /              \  
/________________\  

    """,
        "58-67": """
    👨👩 Golden Years
      ~~~~~      ☀      ~~~~~
    ~~~~~~~~    ~~~~~~    ~~~~~~~~
  ~~~~~~~~~~  ~~~~~~~~  ~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  "Golden Years: Time to Shine"
    """
    }

    if stage not in displayed_art:
        print(art.get(stage, ""))
        displayed_art.add(stage)  # Mark this stage as displayed
        time.sleep(1)  # Small delay to make it visible
