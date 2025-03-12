# Description: This file contains the main game logic for Head $tart, a financial simulation game.
import time
import random
from colorama import Fore, Back, Style
from ascii_art import get_art_for_stage

# Global variables for financial simulation
net_worth = 1000  # Starting balance
income = 0
age = 18  # Starting age

# Dictionary for personality traits to track user's decision patterns
personality_traits = {
    "risk_taker": 0,
    "cautious": 0,
    "luxury_spender": 0,
    "frugal": 0,
    "career_focused": 0,
    "experience_seeker": 0
}

#Creates a typewriter effect for text output
def slowprint(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Progress bar for net worth
def progress_bar(value, max_value, bar_length=30):
    percentage = int((value / max_value) * bar_length)
    bar = "█" * percentage + "-" * (bar_length - percentage)
    print(Fore.GREEN + f"\n📈 Financial Progress: [{bar}] ${value}" + Style.RESET_ALL)

# Display UI-styled menu with borders
def display_menu(title, options):
    border = "═" * (len(title) + 8)
    print(Fore.BLUE + f"\n╔{border}╗")
    print(f"║   {title}      ║")
    print(f"╚{border}╝" + Style.RESET_ALL)
    for index, option in enumerate(options, 1):
        print(Fore.CYAN + f"{index}. {option}" + Style.RESET_ALL)

def get_choice(prompt, valid_choices):
    """Handles user input, allowing access to help and ensuring valid choices."""
    while True:
        choice = input(prompt).lower()
        if choice == "help":
            help()
        elif choice in valid_choices:
            return choice
        else:
            print(Fore.RED + "⚠ Invalid choice. Please enter a valid option." + Style.RESET_ALL)

# Offers the player a set of starting choices (job, college, business)
def initial_choice():
    global net_worth, personality_traits
    while True:
        slowprint(Fore.BLUE + "\nYou're 18, fresh out of high school, and the world is wide open before you. What's your next step?" + Style.RESET_ALL)
        
        display_menu("Choose Your Path", [
            "🦺 Get a Job (Earn now, but limited growth)",
            "🎓 Go to College (Higher income, but debt)",
            "💼 Start a Business (Risky but high reward)"
        ])

        choice = get_choice("Enter your choice (1-3): ", ["1", "2", "3"])

        if choice == "1":
            personality_traits["career_focused"] += 1
            career, income = get_a_job()
            net_worth += income
            return career, income
        elif choice == "2":
            personality_traits["cautious"] += 1
            personality_traits["career_focused"] += 1
            career, income = college()
            net_worth += income
            return career, income
        elif choice == "3":
            personality_traits["risk_taker"] += 1
            net_worth, career, income = start_a_business()
            net_worth += income
            return net_worth, career, income
        elif choice.lower() == "stop":
            slowprint(Fore.BLUE + f"Game Over! Thanks for playing! Your final net worth is ${net_worth}." + Style.RESET_ALL)
            exit()
        else:
            print(Fore.RED + "Invalid input. Please enter 1, 2, or 3." + Style.RESET_ALL)

# Randomly assigns a job and sets the income
def get_a_job():
    global income, net_worth
    careers = {
        "Retail Worker": 20000, "Fast Food Worker": 15000, "Office Assistant": 40000, "Factory Worker": 38000,
        "Service Worker": 28000,
        "Chef": 45000, "Waiter": 30000, "Dancer": 33000, "Police Officer": 52000, "Mechanic": 40000,
        "Receptionist": 35000
    }
    career, income = random.choice(list(careers.items()))
    slowprint(f"\nYou land a job as a {career} and earn ${income} per year. The road ahead is uncertain, but it's a start!")
    slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}\n" + Style.RESET_ALL)
    progress_bar(net_worth, 100000)
    return career, income

def college():
    global net_worth, personality_traits
    slowprint("You enroll in college, ready to invest in your future. But tuition isn't cheap... \n")
    print(Fore.BLUE + "\nDo you want to stay in-state or go out of state?" + Style.RESET_ALL)
    choice = get_choice( "1. In-state (Costs $100,000, more limitations) \n2. Out-of-state (Costs $160,000, more experiences) \n", ["1", "2"])
    if choice == "1":
        personality_traits["cautious"] += 1
        print("You choose an in-state school, saving money but limiting your networking potential.")
        net_worth -= 100000
        
    elif choice == "2":
        personality_traits["experience_seeker"] += 1
        print("*You go out of state, expanding opportunities but accumulating more debt.*")
        net_worth -= 160000

    else:
        print(Fore.RED + "Invalid input. Please enter 1 or 2." + Style.RESET_ALL)
        return net_worth
    
    slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}\n" + Style.RESET_ALL)
    career, income = collegejob()
    return career, income #Returns all necessary values for the main function to use

def collegejob():
    global income, net_worth
    better_jobs = {
        "Doctor": 350000, "Lawyer": 140000, "Corporate Manager": 100000, "Actor": 80000, "Software Engineer": 130000,
        "Accountant": 79000, "Architect": 108000, "Engineer": 116000, "Astronaut": 152000, "Pilot": 215000,
        "Professor": 180000, "Veterinarian": 130000
    }
    job, income = random.choice(list(better_jobs.items()))
    net_worth += income
    slowprint(f"After years of hard work, you graduate and land a job as a {job}, earning ${income} per year!")
    slowprint("*A job after college will usually be more lucrative than without college!*")
    slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
    print("")
    return job, income

def start_a_business():
    global income, net_worth
    slowprint(
        "You take the bold leap into entrepreneurship! You invest in your idea, knowing the risk could pay off... or lead to failure.")
    income = random.randint(50000, 400000)
    net_worth -= 90000
    net_worth += income
    career = "Entrepreneur"
    print(f"Your business starts generating ${income} per year after you spent $90000 on it. The journey ahead will test your resilience.")
    slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
    return net_worth, career, income

def add():
    global age, income, net_worth
    age += 9
    income += income * 9
    net_worth = random_events(age, net_worth)

def age_transition():
    """Handles transitioning through different life stages with financial decisions."""
    global net_worth, age, income
    if age != 18:
        print("...")
        print(f"\n📅 Age: {age} .")
    if age == 18:
        print("Life moves fast! Every decision you make will shape your financial future.")
    
     # The function calls the different stages of age transition (18-27, 28-37, etc.)
    for stage in range(18, 68, 10):
        get_art_for_stage(f"{stage}-{stage+9}")
        if stage == 18:
            age18_27()
        elif stage == 28:
            age28_37()
        elif stage == 38:
            age38_47()
        elif stage == 48:
            age48_57()
        elif stage == 58:
            age58_67()
        
        add()

    print("🎉 Congratulations! You've reached your golden years. Let's see how you've done.")
    return age68beyond()

def age18_27():
    global net_worth, age, income, personality_traits
    slowprint(Fore.BLUE + "Welcome to adulthood! Your future starts here. What will you prioritize?" + Style.RESET_ALL)
    print("1. 💰 Invest in stocks (High risk, high reward)")
    print("2. 🚙 Decide on your primary mode of transportation")
    print("3. 🎓 Further your education for career growth")
    print("4. 💸 Invest in cryptocurrency (High risk, high reward)")
    
    choice = get_choice("Enter your choice (1-4): ", ["1", "2", "3", "4"])
    print("")
    if choice == "1":
        # Stock investment
        personality_traits["risk_taker"] += 1
        stock_investment = random.randint(1000, 10000)
        net_worth += stock_investment
        print(f"Smart move! Your stock investments earned you ${stock_investment}.")
        print("*Investing in stocks early helps your money grow over time through compounding, but you are neglecting important personal spendings such as transportation*")
        slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
    
    elif choice == "2":
        # Transportation
        print("*Good on you for getting started on what's a necessity!*")
        slowprint(Fore.BLUE + "\nChoosing transportation affects finances and lifestyle. Pick one:" + Style.RESET_ALL)
        print("1️. 🚗 Buy a car (High cost, high convenience)")
        print("2️. 🚙 Rent a car (Moderate cost, no ownership)")
        print("3️. 🚲 Buy a bike (Low cost, eco-friendly)")
        print("4️. 🚌 Use public transport (Cheapest option)")
        transport_choice = get_choice("Enter your choice (1-4): ", ["1", "2", "3", "4"])
        
        transport_costs = {"1": random.randint(10000, 50000), "2": random.randint(500, 2000), "3": random.randint(500, 2000), "4": random.randint(100, 500)}
        net_worth -= transport_costs[transport_choice]
        print(f"🚘 You spent ${transport_costs[transport_choice]} on transportation. This will definetely pay off in the long run though!")
        slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
    
    elif choice == "3":
        # Education
        personality_traits["career_focused"] += 1
        education_cost = random.randint(1000, 50000)
        net_worth -= education_cost
        salary_increase = random.randint(10000, 20000)
        income += salary_increase
        print(f"Investing in education cost ${education_cost}, but your salary increased by ${salary_increase}")
        slowprint("*It's great that you realize that the learning doesn't stop after 18 years old. There's always place for promotions and growth!*")
        slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
    
    elif choice == "4":
        # Cryptocurrency investment
        personality_traits["risk_taker"] += 1
        crypto_investment = random.randint(-10000, 10000)
        net_worth += crypto_investment
        print(f"Your crypto investment yielded ${crypto_investment}.")
        slowprint("This is a great and modern investment, and it will provide you wonders for the future! Make sure to take charge of life's necessities like transportation, however.*")
        slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
    else:
        slowprint(Fore.RED + "Invalid choice. Please enter 1, 2, or 3." + Style.RESET_ALL)
        return age18_27()

    financial_decisions()

def age28_37():
    global net_worth, age, income, personality_traits
    slowprint(Fore.BLUE + "You are now settling into adulthood. Choose:" + Style.RESET_ALL)
    print("1. 🏘  Buy a house (Requires a down payment, but it could appreciate over time)")
    print("2. 🏡 Rent a house (Less expensive, but no property appreciation)")
    print("3. 👪 Start a family")
    print("4. 📋 Climb the career ladder (Could lead to salary increases, promotions)")
    choice = get_choice("Enter your choice (1-4): ", ["1", "2", "3", "4"])
    print("")
    if choice == "1":
        # House Ownership
        house_cost = random.randint(100000, 600000)
        net_worth -= house_cost
        print(f"You bought a house for ${house_cost}.")
        slowprint("*Buying a house provides stability, builds equity, and can be a valuable long-term investment!*")
        slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)

    elif choice == "2":
        # Renting
        personality_traits["frugal"] += 1
        print("Because you chose to rent and save money, you have more money to spend on luxuries.")
        rent_cost = random.randint(5000, 20000)
        net_worth -= rent_cost
        print(f"You rented a house for ${rent_cost}")
        slowprint("*Renting a house offers flexibility, lower upfront costs, and fewer maintenance responsibilities.*")
        slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
    
    elif choice == "3":
        # Start a family
        personality_traits["risk_taker"] += 1
        personality_traits["experience_seeker"] += 1
        slowprint("You started a family! Costs will increase but could provide stability.")
        slowprint("*It is great that you realize that in the real world, many of your expenses will go towards things like this. Be prepared*")
        print("1. Have a wedding")
        print("2. Have a child")
        print("3. Get a pet")
        print("4. Elope")
        family_choice = get_choice("Enter your choice (1-4): ", ["1", "2", "3"])
        if family_choice == "1":
            wedding_cost = random.randint(10000, 500000)
            net_worth -= wedding_cost
            print(f"You had a wedding and spent ${wedding_cost}. I heard it was fun!")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
        
        elif family_choice == "2":
            child_cost = random.randint(10000, 90000)
            net_worth -= child_cost
            print(f"You had a child and spent ${child_cost}. Treasure these years!")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
        
        elif family_choice == "3":
            pet_cost = random.randint(1000, 5000)
            net_worth -= pet_cost
            print(f"You got a pet and spent ${pet_cost}. What will you name it?")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            
        elif family_choice == "4":
            print("You chose to elope and saved money. Not a bad decision!")


    elif choice == "4":
        # Career advancement
        personality_traits["career_focused"] += 1
        salary_increase = random.randint(10000, 20000)
        net_worth += salary_increase
        print(f"You focused on advancing your career and received a salary increase of ${salary_increase}.")
        slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
    financial_decisions()

def age38_47():
    global net_worth, age, personality_traits
    slowprint(Fore.BLUE + "Halfaway there! You're almost 40! Choose:" + Style.RESET_ALL)
    print("1.🧾 Plan for retirement (Max out retirement savings, invest in 401k)")
    print("2.🥗 Invest in your health (Gym membership, healthy food)")
    print("3.💵 Pay off your mortgage (Reduce debt, increase net worth)")
    print("4.🌴 Take a vacation (Relax and unwind)")
    choice = get_choice("Enter your choice (1-4): ", ["1", "2", "3", "4"])
    if choice == "1":
        personality_traits["cautious"] += 1
        slowprint(Fore.BLUE + "\nYou chose to plan for retirement. It's a great idea to start doing this early on in your career. How?" + Style.RESET_ALL)
        print("1. Max out retirement savings")
        print("2. Invest in 401k")
        print("3. Invest in Roth IRA")
        print("4. Invest in mutual funds")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            retire_savings = random.randint(10000, 50000)
            net_worth += retire_savings
            print(f"You maxed out retirement savings and added ${retire_savings}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)

        elif choice == "2":
            retire_savings = random.randint(10000, 50000)
            net_worth += retire_savings
            print(f"You invested in 401k and added ${retire_savings}.")
            slowprint("*A 401(k) is a retirement savings plan offered by employers that allows employees to contribute a portion of their salary*")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)

        elif choice == "3":
            retire_savings = random.randint(10000, 50000)
            net_worth += retire_savings
            print(f"You invested in Roth IRA and added ${retire_savings}.")
            slowprint("*A Roth IRA is a retirement savings account where you contribute after-tax income*")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)

        elif choice == "4":
            retire_savings = random.randint(10000, 50000)
            net_worth += retire_savings
            print(f"You invested in mutual funds and added ${retire_savings}.")
            slowprint("*Mutual funds pool money from many investors to buy a mix of stocks or bonds, managed by experts.*")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        else:
            slowprint(Fore.RED + "Invalid choice. Please enter 1 or 2." + Style.RESET_ALL)
            return age38_47()

    elif choice == "2":
        personality_traits["experience_seeker"] += 1
        health_cost = random.randint(1000, 5000)
        net_worth -= health_cost
        print(f"You invested in your health and spent ${health_cost}. You're better off both healthy and financially aware!")
        slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)

    elif choice == "3":
        personality_traits["frugal"] += 1
        mortgage_payment = random.randint(10000, 50000)
        net_worth -= mortgage_payment
        print(f"You paid off your mortgage and spent ${mortgage_payment}.")
        slowprint("*Paying off your mortgage means less debt and more financial freedom.*")
        slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)

    elif choice == "4":
        personality_traits["experience_seeker"] += 1
        vacation_cost = random.randint(1000, 5000)
        net_worth -= vacation_cost
        print(f"You took a vacation and spent ${vacation_cost}.")
        slowprint("*A vacation gives you a break from routine, helps reduce stress, and allows you to relax or explore new places.*")
        slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)

    else:
        slowprint(Fore.RED + "Invalid choice. Please enter 1 or 2." + Style.RESET_ALL)
        return

    financial_decisions()

def age48_57():
    global net_worth, age, personality_traits
    slowprint(Fore.BLUE + "Midlife! Options:" + Style.RESET_ALL)
    print("1.🧐 Expand investment portfolio (Could accumulate wealth over time")
    print("2.🌴 Take a career break (Risking reduced income, but sometimes needed for balance)")
    print("3.🚢 Buy a luxury asset")
    print("4.💰 Aggressively save for retirement")
    choice = get_choice("Enter your choice (1-4): ", ["1", "2", "3", "4"])
    if choice == "1":
        personality_traits["risk_taker"] += 1
        personality_traits["career_focused"] += 1
        investment = random.randint(10000, 70000)
        net_worth += investment
        print(
            f"You chose to start a new investment portfolio. Your investments grow and you accumulate ${investment}.")
        slowprint("*An investment portfolio helps spread risk and grow your money over time.*")
        slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)

    elif choice == "2":
        personality_traits["experience_seeker"] += 1
        personality_traits["risk_taker"] += 1
        break_cost = random.randint(10000, 50000)
        net_worth -= break_cost
        print(f"You chose to take a career break. Take the time off and enjoy!")
        slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)

    elif choice == "3":
        personality_traits["luxury_spender"] += 1
        luxury_asset_cost = random.randint(10000, 50000)
        net_worth -= luxury_asset_cost
        print(f"You bought a luxury asset and spent ${luxury_asset_cost}.")
        slowprint("*It's always important to consider your happiness first. Just work won't do any good!*")
        slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)

    elif choice == "4":
        personality_traits["cautious"] += 1
        retire_savings = random.randint(10000, 50000)
        net_worth += retire_savings
        print(f"You saved aggressively for retirement and added ${retire_savings}. Look at you go!")
        slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)

    else:
        slowprint(Fore.RED + "Invalid choice. Please enter 1 or 2." + Style.RESET_ALL)
        return age48_57()

    financial_decisions()

def age58_67():
    global personality_traits, net_worth
    slowprint(Fore.BLUE + "In your late 50s, you must make key decisions about late-life planning." + Style.RESET_ALL)
    print("1.💲 Plan for retirement (Max out retirement savings, invest in 401k)")
    print("2.💪 Work part-time (Stay active and earn extra income)")
    print("3.🌍 Trip around the globe (Spend your savings on adventures)")
    print("4.🏠 Move to a retirement friendly area ")
    choice = get_choice("Enter your choice (1-4): ", ["1", "2", "3", "4"])
    if choice == "1":
        personality_traits["cautious"] += 1
        slowprint(Fore.BLUE + "You chose to plan for retirement. How?" + Style.RESET_ALL)
        print("1. Max out retirement savings")
        print("2. Invest in 401k")
        print("3. Invest in Roth IRA")
        print("4. Invest in mutual funds")
        choice = get_choice("Enter your choice (1-4): ", ["1", "2", "3", "4"])
        if choice == "1":
            retire_savings = random.randint(10000, 50000)
            net_worth += retire_savings
            print(f"You maxed out retirement savings and added ${retire_savings}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)

        elif choice == "2":
            retire_savings = random.randint(10000, 80000)
            net_worth += retire_savings
            print(f"You invested in 401k and added ${retire_savings}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)

        elif choice == "3":
            retire_savings = random.randint(10000, 50000)
            net_worth += retire_savings
            print(f"You invested in Roth IRA and added ${retire_savings}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)

        elif choice == "4":
            retire_savings = random.randint(1000, 5000)
            net_worth += retire_savings
            print(f"You invested in mutual funds and added ${retire_savings}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)

        else:
            slowprint(Fore.RED + "Invalid choice. Please enter 1 - 4." + Style.RESET_ALL)
            return age58_67()

    elif choice == "2":
        personality_traits["experience_seeker"] += 1
        income = 40000
        net_worth += income
        print(f"You worked part-time and earned ${income}.")
        slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)

    elif choice == "3":
        personality_traits["experience_seeker"] += 1
        travel_cost = random.randint(10000, 100000)
        net_worth -= travel_cost
        print(f"You traveled the world and spent ${travel_cost}.")
        slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)

    elif choice == "4":
        personality_traits["frugal"] += 1
        retirement_area_cost = random.randint(10000, 50000)
        net_worth -= retirement_area_cost
        print(f"You moved to a retirement-friendly area and spent ${retirement_area_cost}.")
        slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)

    else:
        slowprint(Fore.RED + "Invalid choice. Please enter 1 - 4." + Style.RESET_ALL)
        return

    financial_decisions()


def age68beyond():
    slowprint("Congratulations! You have retired and are now in retirement.")
    print("1.🏖️ Travel the world (Spend your savings on adventures)")
    print("2.👨‍🏫 Volunteer (Give back to the community)")
    print("3.🏡 Live a quiet life (Enjoy your years in peace)")
    print("4.💰 Pass wealth down to family (Support future generations)")
    slowprint(Fore.GREEN + f"YOUR FINAL NET WORTH: ${net_worth}!!!" + Style.RESET_ALL)

    choice = get_choice("Enter your choice (1-4): ", ["1", "2", "3", "4"])
    if choice == "1":
        personality_traits["experience_seeker"] += 1
        print("You chose to travel the world.🛫 Enjoy your adventures!")

    elif choice == "2":
        personality_traits["experience_seeker"] += 1
        print("You chose to volunteer. Giving back is a great way to spend your time!")

    elif choice == "3":
        personality_traits["frugal"] += 1
        print("You chose to live a quiet life. Enjoy your peaceful years! 🏡")

    elif choice == "4":
        # Support future generations
        personality_traits["cautious"] += 1
        print("You chose to pass wealth down to your family. Support future generations! 💰💸")
    else:
        slowprint(Fore.RED + "Invalid choice. Please enter 1 - 4." + Style.RESET_ALL)
        return

    # Personality Summary
    slowprint(Fore.BLUE +
        "\nLet's pave your story and reflect on how your decisions/personality would have played out in the real world!" + Style.RESET_ALL)
    print("")

    if personality_traits["risk_taker"] > personality_traits["cautious"]:
        print("You are mostly a risk-taker! You embraced opportunities with high rewards but also high risks.")
        slowprint(Fore.YELLOW + "This bold approach to finance is admired! However, make sure to prioritize financial stability as well, and balancing high-risk investments with stable assets (like bonds or index funds) might help secure this." + Style.RESET_ALL)

    else:
        print(
            "You are quite financially cautious! You prioritized stability and long-term security over risky opportunities.")
        slowprint(Fore.YELLOW + "You were secure, but taking calculated risks—such as small investments or side businesses—might have helped you grow your wealth without jeopardizing security." + Style.RESET_ALL)
    print("")

    time.sleep(1)
    if personality_traits["luxury_spender"] > personality_traits["frugal"]:
        print("You tend to enjoy the finer things in life! You prioritized luxury and experiences over savings.")
        slowprint(Fore.YELLOW + "While happiness is important, balancing spending with savings could improve financial security." + Style.RESET_ALL)

    else:
        print(
            "You are a bit frugal and financially disciplined. You made sure to secure a stable future through careful spending.")
        slowprint(Fore.CYAN + "Your careful budgeting and disciplined saving have put you in a strong financial position! However, life isn’t just about accumulating wealth - spending on experiences, personal growth, or even calculated investments are necessary to make your life more fulfilling!" + Style.RESET_ALL)
    print("")
    time.sleep(1)

    if personality_traits["career_focused"] > personality_traits["experience_seeker"]:
        print("You are quite career-driven! You prioritized financial growth and professional success.")
        slowprint(Fore.MAGENTA + "You worked hard to climb the career ladder, and it paid off! While income is key to financial success, making your money work for you through smart investments and passive income sources could have helped even more, and it is important to note that taking a break is also necessary!" + Style.RESET_ALL)
    else:
        print(
            "You love to value life experiences! You sought joy in travel, socializing, and meaningful moments over strict financial discipline.")
        slowprint(Fore.MAGENTA + "While your memories are invaluable and great for your mental health, a bit more financial planning—like setting aside funds for the future or investing could have ensured long-term security while still allowing for adventure." + Style.RESET_ALL)

    print("")
    print("\nThank you for playing" + Fore.BLUE + " Head $tart" + Style.RESET_ALL + "!")
    exit()

#Function to simulate financial decisions (saving, investing, spending, etc.)
def financial_decisions():
    global income, net_worth, personality_traits
    slowprint(Fore.BLUE + "\nWhat would you like to do this time?" + Style.RESET_ALL)
    
    display_menu("Financial Decisions", [
        "💰 Save 50% of your income",
        "📈 Invest in stocks",
        "🛍️ Spend on luxury items",
        "🏡 Save for retirement",
        "👴 Retire"
    ])

    choice = get_choice("Enter your choice (1-5): \n", ["1", "2", "3", "4", "5"])
    if choice == "1":
        net_worth += (income * 0.5)  # Save half of income into savings
        personality_traits["cautious"] += 1
        personality_traits["frugal"] += 1
        print(Fore.GREEN + f"💾 You saved 50% of your income." + Style.RESET_ALL)

    elif choice == "2":
        invest_result = random.choice([100, 5000, 10000, 50000, 25000, 20000])
        net_worth += invest_result  # Net worth increases from investments
        personality_traits["risk_taker"] += 1
        print(Fore.GREEN + f"📈 Your stock investment returned ${invest_result}." + Style.RESET_ALL)

    elif choice == "3":
        luxury_result = random.choice([-10000, -5000, -1000, -2000])
        net_worth += luxury_result  # Spending on luxury decreases net worth
        personality_traits["luxury_spender"] += 1
        print(Fore.RED + f"🛍️ You spent ${abs(luxury_result)} on luxury. Net worth: ${net_worth}" + Style.RESET_ALL)

    elif choice == "4":
        retire_savings = random.choice([1000, 5000, 10000])
        net_worth += retire_savings  # Savings for retirement added to savings balance
        personality_traits["cautious"] += 1
        personality_traits["frugal"] += 1
        print(Fore.GREEN + f"🏡 You saved for retirement, adding ${retire_savings}." + Style.RESET_ALL)


    elif choice == "5":
        print("You chose to retire!")
        return age68beyond()  # Proceed to retirement
    else:
        print(Fore.RED + "Invalid input. Please choose a valid option." + Style.RESET_ALL)

def random_events(age, net_worth):
    events = [
        (Fore.GREEN + "🎉 You won a lottery!" + Fore.RESET, 50000),
        (Fore.GREEN + "🎊 You got a promotion!" + Fore.RESET, 20000),
        (Fore.RED + "💸 You had an unexpected medical expense." + Fore.RESET, -10000),
        (Fore.GREEN + "🎉 You received an inheritance." + Fore.RESET, 30000),
        (Fore.RED + "📉 You faced a job loss." + Fore.RESET, -20000),
        (Fore.RED + "😞 You had a car accident." + Fore.RESET, -15000),
        (Fore.GREEN + "🤑 Side business took off!" + Fore.RESET, 10000),
        (Fore.RED + "📉 Stock market crash! You lost some money" + Fore.RESET, -5000),
        (Fore.RED + "🏠 Unexpected home repair costs." + Fore.RESET, -8000),
        (Fore.RED + "📉 Economic recession! Your investments took a hit." + Fore.RESET, -12000),
    ]
    if random.random() < 0.3:
        event, amount = random.choice(events)
        net_worth += amount
        slowprint(Fore.BLUE + f"At age {age}: {event} (Net worth: ${net_worth})" + Style.RESET_ALL)  
    return net_worth

#Provides help menu for the player
def help():
    global age
    display_menu("Help Menu", [
    "🧐 How do financial choices affect net worth?",
    "📜 How does the game work?",
    "🚀 What different paths can I take?",
    "❌ Exit Help Menu",
    "🔄 Restart the game"
])

    choice = input(Fore.BLUE + "\nEnter a number to learn more: \n" + Style.RESET_ALL)
    if choice == "1":
        print("💡 Smart investments increase net worth, while unnecessary spending decreases it.")
        time.sleep(1)
        help()
    elif choice == "2":
       print("🎲 The game simulates financial decisions. Every few years, you make choices that impact your future.")
       time.sleep(1)
       help()
    elif choice == "3":
        print("🛤️ You can pursue a career, start a business, or invest in different opportunities!")
        time.sleep(1)
        help()
    elif choice == "4":
        print("Going back to where you left off!")
        age_transition()
    elif choice == "5":
        main()
    else:
        print("Invalid choice. Please enter a valid number.")
        return help()

def main():
    global net_worth, age
    print(Fore.BLUE + "\n🌟 Welcome to *Head $tart*! Learn about financial decisions while having fun!" + Style.RESET_ALL)
    print("If you need help at any time, type 'help' to get to the help menu.\n")
    time.sleep(1)
    slowprint(Fore.BLUE + "What is your name?" + Style.RESET_ALL)
    name = input()
    time.sleep(.5)
    print(f"\n👋 Hello {name}! You are {age} years old and have a starting net worth of ${net_worth}.")
    initial_choice()
    age_transition()

if __name__ == "__main__":
    main()