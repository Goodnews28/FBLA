import time
import random
from colorama import Fore, Back, Style
from ascii_art import get_art_for_stage

global income, net_worth, savings,  age, reflect
savings = 0
net_worth = 1000  # Starting balance
income = 0
age = 18 #Starting age

personality_traits = {
    "risk_taker": 0,
    "cautious": 0,
    "luxury_spender": 0,
    "frugal": 0,
    "career_focused": 0,
    "experience_seeker": 0
}

#Creates a typewriter effect for the text
def slowprint(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_choice(prompt, valid_choices):
    """Handles user input, allowing access to help and ensuring valid choices."""
    while True:
        choice = input(prompt).lower()
        if choice == "help":
            help()
        elif choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please enter a valid option.")

def initial_choice():
    global net_worth
    while True:
        slowprint(Fore.BLUE + "\nYou're 18, fresh out of high school, and the world is wide open before you. What's your next step?" + Style.RESET_ALL)
        print("1. Get a Job (Start earning immediately, but limited long-term growth)")
        print("2. Go to College (Invest in education for better future earnings, but take on debt")
        print("3. Start a Business (High risk, high reward, but requires upfront investment)\n")
        time.sleep(.5)
        choice = get_choice("Enter your choice (1-4): ", ["1", "2", "3", "4"])

        if choice == "1":
            personality_traits["career_focused"] += 1
            job, income = get_a_job()
            career = job
            net_worth += income
            return career, income
        elif choice == "2":
            personality_traits["cautious"] += 1
            personality_traits["career_focused"] += 1
            career, income = college()
            net_worth += income
            return  career, income
        elif choice == "3":
            personality_traits["risk_taker"] += 1
            net_worth, career, income = start_a_business()
            net_worth += income
            return net_worth, career, income
        elif choice.lower() == "stop":
            slowprint(
                Fore.BLUE + f"Game Over! Thanks for playing! Your final net worth is ${net_worth}." + Style.RESET_ALL)
            exit()
        else:
            print(Fore.RED + "Invalid input. Please enter 1, 2, or 3." + Style.RESET_ALL)
        
def get_a_job():
    global income, net_worth
    jobs = {
        "Retail Worker": 20000, "Fast Food Worker": 15000, "Office Assistant": 40000, "Factory Worker": 38000,
        "Service Worker": 28000,
        "Chef": 45000, "Waiter": 30000, "Dancer": 33000, "Police Officer": 52000, "Mechanic": 40000,
        "Receptionist": 35000
    }
    print("")
    job, income = random.choice(list(jobs.items()))
    slowprint(f"You land a job as a {job} and earn ${income} per year. The road ahead is uncertain, but it's a start!")
    return job, income

def college():
    global net_worth
    slowprint(
        "You enroll in college, ready to invest in your future. But tuition isn't cheap... \n")
    print("")
    print(Fore.BLUE + "Do you want to stay in-state or go out of state?" + Style.RESET_ALL)
    choice = get_choice(
        "1. In-state (Costs $100,000, more limitations) \n2. Out-of-state for $160,000 (Costs $160,000, more experiences) \n", ["1", "2"])
    if choice == "1":
        personality_traits["cautious"] += 1
        print("You choose an in-state school, saving money but limiting your networking potential.")
        net_worth -= 100000
        
    elif choice == "2":
        personality_traits["experience_seeker"] += 1
        print("You go out of state, expanding opportunities but accumulating more debt.")
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
    slowprint(f"After years of hard work, you graduate and land a job as a {job}, earning ${income} per year!")
    slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
    print("")
    return job, income

def start_a_business():
    global income, net_worth
    slowprint(
        "You take the bold leap into entrepreneurship! You invest in your idea, knowing the risk could pay off... or lead to failure.")
    income = random.randint(50000, 400000)
    net_worth -= 90000
    career = "Entrepreneur"
    print(f"Your business starts generating ${income} per year after you spent $90000 on it. The journey ahead will test your resilience.")
    slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
    return net_worth, career, income

def age_transition():
    """Handles transitioning through different life stages with financial decisions."""
    global net_worth, age, income
    while age <= 70:
        print("...")
        print(f"\n📅 You are now {age} years old.")
        print("Life moves fast! Every decision you make will shape your financial future.")

        if age < 25:
            # Age 18-25: Young adulthood, early career decisions
            #print("🌱 You're in your early years, full of energy and choices ahead.")
            get_art_for_stage("18-25")
            age18_25()
        elif age < 30:
            # Age 25-30: Settling down, career decisions
            #print("💼 Your career is taking shape. Time to make key decisions!")
            get_art_for_stage("25-30")
            age25_30()
        elif age < 40:
            # Age 30-40: Building wealth, career progression
            #print("🚀 This is a crucial period for wealth building and career progression.")
            get_art_for_stage("30-40")
            age30_40()
        elif age < 50:
            # Age 40-50: Midlife, focus on long-term goals
            #print("🔍 You're entering midlife, where long-term financial stability is essential.")
            get_art_for_stage("40-50")   
            age40_50()
        elif age < 70:
            # Age 50-70: Planning for retirement
            #print("🏡 Retirement planning is now a priority. Make wise choices!")
            get_art_for_stage("50-69")
            age50_69()
        else:
            # Age 70 and beyond: Retirement stage
            print("🎉 Congratulations! You've reached your golden years. Let's see how you've done.")
            return age70beyond()

        age += 5
        income += income * 5
        net_worth = random_events(age, net_worth)

def age18_25():
    global net_worth, age, income
    if age == 18:
        slowprint(Fore.BLUE + "🌱 Welcome to adulthood! Your future starts here. What will you prioritize?" + Style.RESET_ALL)
        print("1. Focus on career advancement and build a stable future")
        print("2. Enjoy your youth, travel, and socialize")
        print("3. Take a gap year to explore and find your passion")
        print("4. Start a side hustle and try to make extra money")
        choice = get_choice ("Enter your choice (1 - 4): ", ["1", "2", "3", "4"])
        print("")
        if choice == "1":
            # Career-focused path
            personality_traits["career_focused"] += 1
            personality_traits["cautious"] += 1
            print("You dedicate yourself to career growth, securing a strong financial foundation.")
            income_increase = random.randint(10000, 20000)
            net_worth += income_increase
            print(f"Your income grows by ${income_increase}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "2":
            # Socializing path
            personality_traits["experience_seeker"] += 1
            personality_traits["risk_taker"] += 1
            print("You embrace life, making unforgettable memories but also spending money.")
            expense = random.randint(1000, 5000)  # Spending on leisure
            net_worth -= expense
            print(f"You spent ${expense} on leisure and social experiences.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "3":
            # Gap year path
            personality_traits["experience_seeker"] += 1
            personality_traits["risk_taker"] += 1
            print("You take a gap year to explore new cultures and perspectives.")
            travel_cost = random.randint(5000, 10000)
            net_worth -= travel_cost
            print(f"Your adventures cost you ${travel_cost}, but you gained invaluable experiences.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "4":
            # Side hustle path
            personality_traits["career_focused"] += 1
            personality_traits["risk_taker"] += 1
            print("You dive into entrepreneurship, launching a side hustle.")
            sidehustle_income = random.randint(1000, 50000)
            net_worth += sidehustle_income
            print(f"Your hustle paid off! You earned ${sidehustle_income}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        else:
            slowprint(Fore.RED + "Invalid choice. Please enter 1 or 2." + Style.RESET_ALL)
            return age18_25()
        
    elif age == 23:
        slowprint(Fore.BLUE + "You're in your early 20s. Choose:" + Style.RESET_ALL)
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
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "2":
            # Transportation
            slowprint("Choosing transportation affects finances and lifestyle. Pick one:")
            print("1️. 🚗 Buy a car (High cost, high convenience)")
            print("2️. 🚙 Rent a car (Moderate cost, no ownership)")
            print("3️. 🚲 Buy a bike (Low cost, eco-friendly)")
            print("4️. 🚌 Use public transport (Cheapest option)")
            transport_choice = get_choice("Enter your choice (1-4): ", ["1", "2", "3", "4"])
            
            transport_costs = {"1": random.randint(10000, 50000), "2": random.randint(500, 2000), "3": random.randint(500, 2000), "4": random.randint(100, 500)}
            net_worth -= transport_costs[transport_choice]
            print(f"🚘 You spent ${transport_costs[transport_choice]} on transportation.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
        
        elif choice == "3":
            # Education
            personality_traits["career_focused"] += 1
            education_cost = random.randint(1000, 50000)
            net_worth -= education_cost
            salary_increase = random.randint(10000, 20000)
            income += salary_increase
            print(f"Investing in education cost ${education_cost}, but your salary increased by ${salary_increase}")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "4":
            # Cryptocurrency investment
            personality_traits["risk_taker"] += 1
            crypto_investment = random.randint(-10000, 10000)
            net_worth += crypto_investment
            print(f"Your crypto investment yielded ${crypto_investment}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        else:
            slowprint(Fore.RED + "Invalid choice. Please enter 1, 2, or 3." + Style.RESET_ALL)
            return age18_25()

    return financial_decisions()

def age25_30():
    global net_worth, age, savings, income
    if age == 28:
        slowprint(Fore.BLUE + "You are now settling into adulthood. Choose:" + Style.RESET_ALL)
        print("1. 🏘 Buy a house (Requires a down payment, but it could appreciate over time)")
        print("2. 🏡Rent a house(Less expensive, but no property appreciation")
        print("3. 👪 Start a family")
        print("4. 📋 Climb the career ladder (Could lead to salary increases, promotions)")
        choice = get_choice("Enter your choice (1-4): ", ["1", "2", "3", "4"])
        print("")
        if choice == "1":
            # House Ownership
            house_cost = random.randint(100000, 600000)
            net_worth -= house_cost
            print(f"You bought a house for ${house_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}\n Updated Savings: ${savings}" + Style.RESET_ALL)
            return
    
        elif choice == "2":
            # Renting
            personality_traits["frugal"] += 1
            print("Because you chose to rent and save money, you have more money to spend on luxuries.")
            rent_cost = random.randint(5000, 20000)
            net_worth -= rent_cost
            print(f"You rented a house for ${rent_cost}")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "3":
            # Start a family
            personality_traits["risk_taker"] += 1
            personality_traits["experience_seeker"] += 1
            slowprint("You started a family. Costs will increase but could provide stability.")
            print("1. Have a wedding")
            print("2. Have a child")
            print("3. Get a pet")
            print("4. Elope")
            family_choice = get_choice("Enter your choice (1-4): ", ["1", "2", "3"])
            if family_choice == "1":
                wedding_cost = random.randint(10000, 500000)
                net_worth -= wedding_cost
                print(f"You had a wedding and spent ${wedding_cost}.")
                slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
                return
            
            elif family_choice == "2":
                child_cost = random.randint(10000, 90000)
                net_worth -= child_cost
                print(f"You had a child and spent ${child_cost}.")
                slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
                return
            
            elif family_choice == "3":
                pet_cost = random.randint(1000, 5000)
                net_worth -= pet_cost
                print(f"You got a pet and spent ${pet_cost}.")
                slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
                return
            
            elif family_choice == "4":
                print("You chose to elope and saved money.")
                return

        elif choice == "4":
            # Career advancement
            personality_traits["career_focused"] += 1
            salary_increase = random.randint(10000, 20000)
            net_worth += salary_increase
            print(f"You focused on advancing your career and received a salary increase of ${salary_increase}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
    financial_decisions()
    # NOT DONE DO SOME CHOICES HERE


def age30_40():
    global net_worth, age
    if age == 33:
        slowprint(Fore.BLUE + "You're in your 30s, building your career and wealth. Choose:" + Style.RESET_ALL)
        print("1. Expand your investment portfolio (Stocks, real estate, bonds, mutual funds)")
        print("2. Focus on career advancement (Could lead to salary increases, promotions)")
        print("3. Purchase a vacation home")
        print("4. Focus on growing your family")
        choice = get_choice("Enter your choice (1-4): ", ["1", "2", "3", "4"])

        if choice == "1":
            personality_traits["risk_taker"] += 1
            investment = random.randint(10000, 70000)
            net_worth += investment
            print(f"You expanded your investment portfolio and gained ${investment}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "2":
            personality_traits["career_focused"] += 1
            salary_increase = random.randint(10000, 20000)
            net_worth += salary_increase
            print(f"You focused on career advancement and received a salary increase of ${salary_increase}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "3":
            personality_traits["luxury_spender"] += 1
            vacation_home_cost = random.randint(100000, 500000)
            net_worth -= vacation_home_cost
            print(f"You bought a vacation home and spent ${vacation_home_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "4":
            personality_traits["experience_seeker"] += 1
            personality_traits["risk_taker"] += 1
            family_expense = random.randint(10000, 50000)
            net_worth -= family_expense
            print(f"You focused on growing your family and spent ${family_expense}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        else:
            slowprint(Fore.RED + "Invalid choice. Please enter 1 or 2." + Style.RESET_ALL)
            return age30_40()

    elif age == 38:
        slowprint(Fore.BLUE + "You're in your late 30s. Choose:" + Style.RESET_ALL)
        print("1. Plan for retirement (Max out retirement savings, invest in 401k)")
        print("2. Invest in your health (Gym membership, healthy food)")
        print("3. Pay off your mortgage (Reduce debt, increase net worth)")
        print("4. Take a vacation (Relax and unwind)")
        choice = get_choice("Enter your choice (1-4): ", ["1", "2", "3", "4"])
        if choice == "1":
            personality_traits["cautious"] += 1
            slowprint("You chose to plan for retirement. How?")
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
                return

            elif choice == "2":
                retire_savings = random.randint(10000, 50000)
                net_worth += retire_savings
                print(f"You invested in 401k and added ${retire_savings}.")
                slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
                return

            elif choice == "3":
                retire_savings = random.randint(10000, 50000)
                net_worth += retire_savings
                print(f"You invested in Roth IRA and added ${retire_savings}.")
                slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
                return

            elif choice == "4":
                retire_savings = random.randint(10000, 50000)
                net_worth += retire_savings
                print(f"You invested in mutual funds and added ${retire_savings}.")
                slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
                return

            else:
                slowprint(Fore.RED + "Invalid choice. Please enter 1 or 2." + Style.RESET_ALL)
                return age30_40()

        elif choice == "2":
            personality_traits["experience_seeker"] += 1
            health_cost = random.randint(1000, 5000)
            net_worth -= health_cost
            print(f"You invested in your health and spent ${health_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "3":
            personality_traits["frugal"] += 1
            mortgage_payment = random.randint(10000, 50000)
            net_worth -= mortgage_payment
            print(f"You paid off your mortgage and spent ${mortgage_payment}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "4":
            personality_traits["experience_seeker"] += 1
            vacation_cost = random.randint(1000, 5000)
            net_worth -= vacation_cost
            print(f"You took a vacation and spent ${vacation_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        else:
            slowprint(Fore.RED + "Invalid choice. Please enter 1 or 2." + Style.RESET_ALL)
            return

    return financial_decisions()


def age40_50():
    global net_worth, age
    if age == 43:
        slowprint(Fore.BLUE + "Midlife! Options:" + Style.RESET_ALL)
        print("1. Expand investment portfolio (Could accumulate wealth over time")
        print("2. Take a career break (Risking reduced income, but sometimes needed for balance)")
        print("3. Buy a luxury asset")
        print("4. Aggressively save for retirement")
        choice = get_choice("Enter your choice (1-4): ", ["1", "2", "3", "4"])
        if choice == "1":
            personality_traits["risk_taker"] += 1
            personality_traits["career_focused"] += 1
            investment = random.randint(10000, 70000)
            net_worth += investment
            print(
                f"You chose to start a new investment portfolio. Your investments grow and you accumulate ${investment}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "2":
            personality_traits["experience_seeker"] += 1
            personality_traits["risk_taker"] += 1
            break_cost = random.randint(10000, 50000)
            net_worth -= break_cost
            print(f"You chose to take a career break.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "3":
            personality_traits["luxury_spender"] += 1
            luxury_asset_cost = random.randint(10000, 50000)
            net_worth -= luxury_asset_cost
            print(f"You bought a luxury asset and spent ${luxury_asset_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "4":
            personality_traits["cautious"] += 1
            retire_savings = random.randint(10000, 50000)
            net_worth += retire_savings
            print(f"You saved aggressively for retirement and added ${retire_savings}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        else:
            slowprint(Fore.RED + "Invalid choice. Please enter 1 or 2." + Style.RESET_ALL)
            return age40_50()
        # NOT DONE DO SOME CHOICES HERE
    elif age == 48:
        slowprint(Fore.BLUE + "You're in your late 40s. Options:" + Style.RESET_ALL)
        print("1. Focus on growing your wealth")
        print("2. Spend on experiences (Travel, hobbies)")
        print("3. Invest in real estate")
        print("4. Plan for retirement")
        choice = get_choice("Enter your choice (1-4): ", ["1", "2", "3", "4"])
        if choice == "1":
            personality_traits["career_focused"] += 1
            personality_traits["frugal"] += 1
            wealth_growth = random.randint(10000, 50000)
            net_worth += wealth_growth
            print(f"You focused on growing your wealth and gained ${wealth_growth}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "2":
            personality_traits["experience_seeker"] += 1
            experience_cost = random.randint(10000, 50000)
            net_worth -= experience_cost
            print(f"You spent on experiences and spent ${experience_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "3":
            personality_traits["frugal"] += 1
            real_estate_return = random.randint(10000, 100000)
            net_worth += real_estate_return
            print(f"You invested in real estate and earned ${real_estate_return}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "4":
            personality_traits["cautious"] += 1
            retire_savings = random.randint(10000, 50000)
            net_worth += retire_savings
            print(f"You planned for retirement and added ${retire_savings}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        else:
            slowprint(Fore.RED + "Invalid choice. Please enter 1 or 2." + Style.RESET_ALL)
            return
    return financial_decisions()


def age50_69():
    global net_worth, age, income
    if age == 53:
        slowprint(Fore.BLUE + "You're in your golden years! Options:" + Style.RESET_ALL)
        print("Planning for retirement. Choose:")
        print("1. Began diversifying your source of income")
        print("2. Travel the world (Spend your savings on adventures)")
        print("3. Downsize your home to free up capital")
        print("4. Plan for retirement (wills, trusts, charities)")
        choice = get_choice("Enter your choice (1-4): ", ["1", "2", "3", "4"])
        if choice == "1":
            personality_traits["career_focused"] += 1
            personality_traits["frugal"] += 1
            diverse_income = random.randint(10000, 50000)
            net_worth += diverse_income
            print(f"You diversified your income and gained ${diverse_income}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "2":
            personality_traits["experience_seeker"] += 1
            travel_cost = random.randint(10000, 50000)
            net_worth -= travel_cost
            print(f"You traveled the world and spent ${travel_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "3":
            personality_traits["frugal"] += 1
            home_downsize = random.randint(10000, 50000)
            net_worth += home_downsize
            print(f"You downsized your home and gained ${home_downsize}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "4":
            personality_traits["cautious"] += 1
            slowprint("You're getting reading for retirement. What is your legacy?")
            print("1. Write a will")
            print("2. Set up a trust")
            print("3. Donate to charity")
            print("4. Invest in your family")
            choice = input("Enter your choice (1-4): ")
            if choice == "1":
                will_cost = random.randint(1000, 5000)
                net_worth -= will_cost
                print(f"You wrote a will and spent ${will_cost}.")
                slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
                return

            elif choice == "2":
                trust_cost = random.randint(10000, 50000)
                net_worth -= trust_cost
                print(f"You set up a trust and spent ${trust_cost}.")
                slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
                return

            elif choice == "3":
                charity_cost = random.randint(1000, 5000)
                net_worth -= charity_cost
                print(f"You donated to charity and spent ${charity_cost}.")
                slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
                return

            elif choice == "4":
                family_investment = random.randint(10000, 500000)
                net_worth -= family_investment
                print(f"You invested in your family and spent ${family_investment}.")
                slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
                return

            else:
                slowprint(Fore.RED + "Invalid choice. Please enter 1 - 4." + Style.RESET_ALL)
                return
        else:
            slowprint(Fore.RED + "Invalid choice. Please enter 1 - 4." + Style.RESET_ALL)
            return age50_69()

    elif age == 58:
        slowprint(Fore.BLUE + "You're in your late 50s. Options:" + Style.RESET_ALL)
        print("1. Focus on growing your wealth")
        print("2. Spend on experiences (Travel, hobbies)")
        print("3. Take a family vacation")
        print("4. Plan for retirement")
        choice = get_choice("Enter your choice (1-4): ", ["1", "2", "3", "4"])

        if choice == "1":
            personality_traits["career_focused"] += 1
            wealth_growth = random.randint(10000, 50000)
            net_worth += wealth_growth
            print(f"You focused on growing your wealth and gained ${wealth_growth}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "2":
            personality_traits["experience_seeker"] += 1
            experience_cost = random.randint(10000, 50000)
            net_worth -= experience_cost
            print(f"You spent on experiences and spent ${experience_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "3":
            personality_traits["experience_seeker"] += 1
            vacation_cost = random.randint(1000, 5000)
            net_worth -= vacation_cost
            print(f"You took a family vacation and spent ${vacation_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "4":
            personality_traits["cautious"] += 1
            retire_savings = random.randint(10000, 50000)
            net_worth += retire_savings
            print(f"You planned for retirement and added ${retire_savings}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        else:
            slowprint(Fore.RED + "Invalid choice. Please enter 1 - 4." + Style.RESET_ALL)
            return

    elif age == 63:
        slowprint(Fore.BLUE + "In your 60s, you must make key decisions about late-life planning." + Style.RESET_ALL)
        print("1. Plan for retirement (Max out retirement savings, invest in 401k)")
        print("2. Work part-time (Stay active and earn extra income)")
        print("3. Trip around the globe (Spend your savings on adventures)")
        print("4. Move to a retirement friendly area ")
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
                return

            elif choice == "2":
                retire_savings = random.randint(10000, 80000)
                net_worth += retire_savings
                print(f"You invested in 401k and added ${retire_savings}.")
                slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
                return

            elif choice == "3":
                retire_savings = random.randint(10000, 50000)
                net_worth += retire_savings
                print(f"You invested in Roth IRA and added ${retire_savings}.")
                slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
                return

            elif choice == "4":
                retire_savings = random.randint(1000, 5000)
                net_worth += retire_savings
                print(f"You invested in mutual funds and added ${retire_savings}.")
                slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
                return

            else:
                slowprint(Fore.RED + "Invalid choice. Please enter 1 - 4." + Style.RESET_ALL)
                return age50_69()

        elif choice == "2":
            personality_traits["experience_seeker"] += 1
            income = (income / 2)
            net_worth += income
            print(f"You worked part-time and earned ${income}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "3":
            personality_traits["experience_seeker"] += 1
            travel_cost = random.randint(10000, 100000)
            net_worth -= travel_cost
            print(f"You traveled the world and spent ${travel_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "4":
            personality_traits["frugal"] += 1
            retirement_area_cost = random.randint(10000, 50000)
            net_worth -= retirement_area_cost
            print(f"You moved to a retirement-friendly area and spent ${retirement_area_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        else:
            slowprint(Fore.RED + "Invalid choice. Please enter 1 - 4." + Style.RESET_ALL)
            return

    elif age == 68:
        slowprint(Fore.BLUE + "You're in your late 60s. Options:" + Style.RESET_ALL)
        print("1. Fully retire (Enjoy your golden years)")
        print("2. Sell your assets (Downsize and free up capital)")
        print("3. Make a large donation (Support a cause you care about)")
        print("4. Manage healthcare costs (Invest in health insurance)")
        choice = get_choice("Enter your choice (1-4): ", ["1", "2", "3", "4"])

        if choice == "1":
            return age70beyond()

        elif choice == "2":
            personality_traits["frugal"] += 1
            asset_sell = random.randint(10000, 50000)
            net_worth += asset_sell
            print(f"You sold your assets and gained ${asset_sell}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "3":
            personality_traits["cautious"] += 1
            donation_cost = random.randint(1000, 5000)
            net_worth -= donation_cost
            print(f"You made a large donation and spent ${donation_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "4":
            personality_traits["cautious"] += 1
            health_insurance_cost = random.randint(1000, 5000)
            net_worth -= health_insurance_cost
            print(f"You invested in health insurance and spent ${health_insurance_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        else:
            slowprint(Fore.RED + "Invalid choice. Please enter 1 - 4." + Style.RESET_ALL)
            return
    return financial_decisions()


def age70beyond():
    slowprint("Congratulations! You have retired and are now in retirement.")
    print("1. 🏖️ Travel the world (Spend your savings on adventures)")
    print("2. 👨‍🏫 Volunteer (Give back to the community)")
    print("3. 🏡 Live a quiet life (Enjoy your years in peace)")
    print("4. 💰 Pass wealth down to family (Support future generations)")
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
    slowprint(
        "\nLet's pave your story and reflect on how your decisions/personality would have played out in the real world!")
    print("")

    if personality_traits["risk_taker"] > personality_traits["cautious"]:
        print("You are mostly a risk-taker! You embraced opportunities with high rewards but also high risks.")
        slowprint(
            Fore.BOLD + Fore.YELLOW + "This bold approach to finance is admired! However, make sure to prioritize financial stability as well, and balancing high-risk investments with stable assets (like bonds or index funds) might help secure this." + Style.RESET_ALL)

    else:
        print(
            "You are quite financially cautious! You prioritized stability and long-term security over risky opportunities.")
        slowprint(
            Fore.BOLD + Fore.YELLOW + "You were secure, but taking calculated risks—such as small investments or side businesses—might have helped you grow your wealth without jeopardizing security." + Style.RESET_ALL)
    print("")

    time.sleep(1)
    if personality_traits["luxury_spender"] > personality_traits["frugal"]:
        print("You tend to enjoy the finer things in life! You prioritized luxury and experiences over savings.")
        slowprint(
            Fore.BOLD + Fore.YELLOW + "While happiness is important, balancing spending with savings could improve financial security." + Style.RESET_ALL)

    else:
        print(
            "You are a bit frugal and financially disciplined. You made sure to secure a stable future through careful spending.")
        slowprint(
            Fore.BOLD + Fore.CYAN + "Your careful budgeting and disciplined saving have put you in a strong financial position! However, life isn’t just about accumulating wealth - spending on experiences, personal growth, or even calculated investments are necessary to make your life more fulfilling!" + Style.RESET_ALL)
    print("")
    time.sleep(1)

    if personality_traits["career_focused"] > personality_traits["experience_seeker"]:
        print("You are quite career-driven! You prioritized financial growth and professional success.")
        slowprint(
            Fore.BOLD + Fore.MAGENTA + "You worked hard to climb the career ladder, and it paid off! While income is key to financial success, making your money work for you through smart investments and passive income sources could have helped even more, and it is important to note that taking a break is also necessary!" + Style.RESET_ALL)
    else:
        print(
            "You love to value life experiences! You sought joy in travel, socializing, and meaningful moments over strict financial discipline.")
        slowprint(
            Fore.BOLD + Fore.MAGENTA + "While your memories are invaluable and great for your mental health, a bit more financial planning—like setting aside funds for the future or investing could have ensured long-term security while still allowing for adventure." + Style.RESET_ALL)

    print("")
    print(Fore.BOLD + "\nThank you for playing" + Fore.BLUE + " Head $tart" + Style.RESET_ALL + "!")
    exit()


def financial_decisions():
    global income, net_worth, savings, personality_traits
    print("")
    while True:
        slowprint(Fore.BLUE + "What would you like to do this year?" + Style.RESET_ALL)
        choice = input(
            "1. Save 50% of your income \n2. Invest in stocks \n3. Spend on luxury items \n4. Save for retirement" + Fore.RED + "\n5. Retire" + Style.RESET_ALL + "\n")
        print("")

        if choice == "1":
            savings += (income * 0.5)
            net_worth += (income * 0.5)  # Save half of income into savings
            personality_traits["cautious"] += 1
            personality_traits["frugal"] += 1
            print(f"You saved 50% of your income into savings. Savings: ${savings}.")

        elif choice == "2":
            invest_result = random.choice([100, 5000, 10000, 50000, 25000, 20000])
            net_worth += invest_result  # Net worth increases from investments
            personality_traits["risk_taker"] += 1
            print(f"You invested in stocks, and your investment resulted in ${invest_result}. Net worth: ${net_worth}.")

        elif choice == "3":
            luxury_result = random.choice([-10000, -5000, -1000, -2000])
            net_worth += luxury_result  # Spending on luxury decreases net worth
            personality_traits["luxury_spender"] += 1
            print(f"You spent ${abs(luxury_result)} on luxury items. Net worth: ${net_worth}.")

        elif choice == "4":
            retire_savings = random.choice([1000, 5000, 10000])
            net_worth += retire_savings  # Savings for retirement added to savings balance
            savings += retire_savings
            personality_traits["cautious"] += 1
            personality_traits["frugal"] += 1
            print(f"You saved for retirement, adding ${retire_savings} to savings. Savings: ${savings}.")

        elif choice == "5":
            print("You chose to retire!")
            return age70beyond()  # Proceed to retirement
        else:
            print(Fore.RED + "Invalid input. Please choose a valid option." + Style.RESET_ALL)
            break

def random_events(age, net_worth):
    events = [
        (Fore.GREEN + "🎉 You won a lottery!" + Fore.RESET, 50000),
        (Fore.GREEN + "🎊 You got a promotion!" + Fore.RESET, 20000),
        (Fore.RED + "💸 You had an unexpected medical expense." + Fore.RESET, -10000),
        (Fore.GREEN + "🎉 You received an inheritance." + Fore.RESET, 30000),
        (Fore.RED + "📉 You faced a job loss." + Fore.RESET, -20000)
        (Fore.RED + "😞 You had a car accident." + Fore.RESET, -15000),
        (Fore.GREEN + "🤑 Side business took off!" + Fore.RESET, 10000),
        (Fore.RED + "📉 Stock market crash! You lost some money" + Fore.RESET, -5000)
        (Fore.RED + "🏠 Unexpected home repair costs." + Fore.RESET, -8000),
        (Fore.RED + "📉 Economic recession! Your investments took a hit." + Fore.RESET, -12000),
    ]
    if random.random() < 0.2:
        event, amount = random.choice(events)
        net_worth += amount
        print(f"At age {age}: {event} (Net worth: ${net_worth})")

def help():
    print("")
    slowprint(Fore.GREEN + "\nWelcome to the Head $tart Help Menu!" + Style.RESET_ALL)
    print("This game is designed to teach you about making smart financial decisions.")
    print("You will start with a net worth of $100,000 and make choices that will affect your financial future.")
    print("Your goal is to retire with the highest net worth possible.")
    print("You will be presented with choices at different ages, and your decisions will impact your net worth.")
    print("Good luck!")

    slowprint(Fore.GREEN + "Need more help? Type 'yes' or 'no'" + Style.RESET_ALL)
    if input().lower() == "yes":
        print(Fore.GREEN + "\nHELP MENU:" + Style.RESET_ALL)
        print("1. How do financial choices affect my net worth?")
        print("2. How does the game work?")
        print("3. What are the different paths I can take?")
        print("4. Exit Help Menu")

        choice = input("Enter a number to learn more: ")
        if choice == "1":
            print(
                "Smart investments and career decisions increases our networth, while unnecessary expenses and bad luck decrease it.")
        elif choice == "2":
            print(
                "The game simulates financial growth through different life stages. You make decisions every 5 years, and random events can impact your wealth.")
        elif choice == "3":
            print(
                "You can choose different life paths like college, a job, or starting a business. Each path has unique financial opportunities and risks.")
        elif choice == "4":
            return
        else:
            print("Invalid choice. Please enter a valid number.")
            return help()

    elif input().lower() == "no":
        print(Fore.GREEN + "Good luck!" + Style.RESET_ALL)
        return main()

    main()


def main():
    global net_worth, age
    income, career = None, None
    print(
        Fore.BLUE + "Welcome to Head $tart!" + Style.RESET_ALL + "\nThis is a game designed to teach you about making smart financial decisions.\n")
    print("If you need help at any time, type 'help' to get to the help menu.")
    time.sleep(1)
    slowprint(Fore.BLUE + "What is your name?" + Style.RESET_ALL)
    name = input()
    time.sleep(.5)
    slowprint(f"Hello {name}! You are {age} years old, and have a starting net worth of ${net_worth}.")

    initial_choice()
    age_transition()

if __name__ == "__main__":
    main()
