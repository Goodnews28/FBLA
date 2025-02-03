import time
import random
from colorama import Fore, Back, Style

global income, net_worth, age
net_worth = 1000  # Starting balance
income = 0
age = 18 #Starting age

#Creates a typewriter effect for the text
def slowprint(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def college():
    global net_worth
    slowprint(
        "You chose to go to college. You have student loans to pay off, but you have an opportunity to get a better paying job. \n")
    print("")
    print(Fore.BLUE + "Do you want to stay in-state or go out of state?" + Style.RESET_ALL)
    choice = input(
        "1. In-state (Lower tuition costs, limited opportunities \n2. Out-of-state (Higher tuition costs, more opportunities) \n")
    if choice == "1":
        print("You chose to stay in-state. A better financial decision but you have limited opportunities")
        net_worth -= 100000
        
    elif choice == "2":
        print("You chose to go out of state. You have more opportunities but you have a higher tuition cost.")
        net_worth -= 160000

    else:
        print(Fore.RED + "Invalid input. Please enter 1 or 2." + Style.RESET_ALL)
        return net_worth
    
    slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}\n" + Style.RESET_ALL)
    career, income = collegejob()
    return career, income #Returns all necessary values for the main function to use


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
    slowprint(f"You got a job as a {job} and earn ${income} per year.")
    return job, income


def collegejob():
    global income, net_worth
    better_jobs = {
        "Doctor": 350000, "Lawyer": 140000, "Corporate Manager": 100000, "Actor": 80000, "Software Engineer": 130000,
        "Accountant": 79000, "Architect": 108000, "Engineer": 116000, "Astronaut": 152000, "Pilot": 215000,
        "Professor": 180000, "Veterinarian": 130000
    }
    job, income = random.choice(list(better_jobs.items()))
    slowprint(f"After graduating college, you got a job as a {job} and earn ${income} per year.")
    slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
    print("")
    return job, income


def start_a_business():
    global income, net_worth
    slowprint(
        "Congratulations! You have decided to start a business. The risks are high, but so is the reward.")
    income = random.randint(50000, 400000)
    net_worth -= 90000
    career = "Entrepreneur"
    print(f"You started a business and earn ${income} per year and spent on $90,000 starting up the business.")
    slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
    return net_worth, career, income


def financial_decisions():
    global income, net_worth
    print("")
    while True:
        slowprint(Fore.BLUE + "What would like to do this year?" + Style.RESET_ALL)
        choice = input(
            "1. Save 50% of your income \n2. Invest in stocks \n3. Spend on luxury items \n4. Save for retirement" + Fore.RED + "\n5. Retire" + Style.RESET_ALL +"\n")
        print("")
        if choice == "1":
            net_worth += (income * 0.5)
            print("You saved 50% of your income.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            break

        elif choice == "2":
            invest_result = random.choice([100, 5000, 10000, 50000, 25000, 20000])
            net_worth += invest_result
            print(f"You invested in stocks, and your investment resulted in ${invest_result}")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            break

        elif choice == "3":
            luxury_result = random.choice(
                [-10000, -5000, -1000, -2000, -3000, -4000, -5000, -6000, -7000, -8000, -9000, -10000])
            net_worth += luxury_result
            print(f"You spent ${luxury_result} on luxury items.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            break

        elif choice == "4":
            retire_savings = random.choice([10000, 5000, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])
            net_worth += retire_savings
            print(f"You saved for retirement and earned ${retire_savings}.")
            slowprint(Fore.GREEN + f"Updated net worth: {net_worth}" + Style.RESET_ALL)
            break
    
        elif choice == "5":
            print("You chose to retire!")
            return age70beyond()
        else:
            print(Fore.RED + "Invalid input. Please enter a number between 1 and 5." + Style.RESET_ALL)


def age_transition():
    """Handles transitioning through different life stages with financial decisions."""
    global net_worth
    global age
    while age <= 70:
        print("...")
        print(f"\nCurrent Age: {age}")
        if age < 25:
            # Age 18-25: Young adulthood, early career decisions
            age_effect = age18_25()
        elif age < 30:
            # Age 25-30: Settling down, career decisions
            age_effect = age25_30()
        elif age < 40:
            # Age 30-40: Building wealth, career progression
            age_effect = age30_40()
        elif age < 50:
            # Age 40-50: Midlife, focus on long-term goals
            age_effect = age40_50()
        elif age < 70:
            # Age 50-70: Planning for retirement
            age_effect = age50_69()
        else:
            # Age 70 and beyond: Retirement stage
            return age70beyond()

        age += 5


def age18_25():
    global net_worth, age
    if age == 18:
        slowprint(Fore.BLUE + "You're navigating early adulthood. Would you like to:" + Style.RESET_ALL)
        print("1. Focus on career advancement")
        print("2. Enjoy your youth with vacations and socializing")
        choice = input("Enter your choice (1 or 2): ")
        print("")
        if choice == "1":
            # Career-focused path
            print("You chose to focus on career advancement. Your career progresses well!")
            income_increase = random.randint(10000, 20000)
            net_worth += income_increase
            print(f"You gained ${income_increase} in income.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            financial_decisions()

        elif choice == "2":
            # Socializing path
            print("You chose to enjoy your youth. While you had fun, you spent money on vacations and social activities.")
            expense = random.randint(1000, 5000)  # Spending on leisure
            net_worth -= expense
            print(f"You spent ${expense} on leisure. Your new net worth is ${net_worth}.")
            financial_decisions()

        else:
            slowprint(Fore.RED + "Invalid choice. Please enter 1 or 2." + Style.RESET_ALL)
            return age18_25()

    financial_decisions()
    # NOT DONE DO SOME CHOICES HERE


def age25_30():
    global net_worth, age
    if age == 28:
        slowprint(Fore.BLUE + "You are now settling into adulthood. Choose:" + Style.RESET_ALL)
        print("1. Buy a house (Requires a down payment, but it could appreciate over time)")
        print("2. Rent and save money(Less expensive, but no property appreciation")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            house_cost = random.randint(100000, 600000)
            net_worth -= house_cost
            print(f"You bought a house for ${house_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            financial_decisions()
    
        elif choice == "2":
            print("Because you chose to rent and save money, you have more money to spend on luxuries.")
            rent_cost = random.randint(5000, 20000)
            net_worth -= rent_cost
            print(f"You rented a house for ${rent_cost}")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            financial_decisions()
    financial_decisions()
    # NOT DONE DO SOME CHOICES HERE


def age30_40():
    global net_worth,age
    if age == 33:
        slowprint(Fore.BLUE + "You're in your 30s, building your career and wealth. Choose:" + Style.RESET_ALL)
        print("1. Invest in real estate (A long-term investment with potential appreciation)")
        print("2. Focus on career advancement (Could lead to salary increases, promotions)")
        print("3. Start a family (Costs will increase but could provide stability)")
        choice = input("Enter your choice (1-3): ")
    
        if choice == "1":
            # Real estate investment
            real_estate_investment = random.randint(20000, 100000)
            net_worth += real_estate_investment
            print(f"You invested in real estate and gained ${real_estate_investment}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            financial_decisions()

        elif choice == "2":
            # Focus on career
            salary_increase = random.randint(10000, 25000)
            net_worth += salary_increase
            print(
                f"You focused on advancing your career and received a salary increase of ${salary_increase}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            financial_decisions()

        elif choice == "3":
            # Start a family
            family_costs = random.randint(20000, 50000)
            net_worth -= family_costs
            print(f"You started a family and incurred ${abs(family_costs)} in costs.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            financial_decisions()

        else:
            slowprint(Fore.RED + "Invalid choice. Please enter 1, 2, or 3." + Style.RESET_ALL)
            return age30_40()
        
    financial_decisions()


def age40_50():
    global net_worth, age
    if age == 43:
        slowprint(Fore.BLUE + "Midlife! Options:" + Style.RESET_ALL)
        print("1. Start a new investment portfolio (Could accumulate wealth over time")
        print("2. Take a career break (Risking reduced income, but sometimes needed for balance)")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            investment = random.randint(10000, 70000)
            net_worth += investment
            print(
                f"You chose to start a new investment portfolio. Your investments grow and you accumulate ${investment}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            financial_decisions()
            return investment
        elif choice == "2":
            break_cost = random.randint(10000, 50000)
            net_worth -= break_cost
            print(f"You chose to take a career break.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            financial_decisions()
            return break_cost
        else:
            slowprint(Fore.RED + "Invalid choice. Please enter 1 or 2." + Style.RESET_ALL)
            return age40_50()
        # NOT DONE DO SOME CHOICES HERE
    financial_decisions()


def age50_69():
    global net_worth, age
    if age == 43:
        slowprint(Fore.BLUE + "You're in your golden years! Options:" + Style.RESET_ALL)
        print("Planning for retirement. Choose:")
        print("1. Max out retirement savings(Secure a comfortable retirement, but it will reduce current savings)")
        print("2. Travel the world (Spend your savings on adventures)")
        print("3. Invest in real estate")
        choice = input("Enter your choice (1 - 3): ")
        if choice == "1":
            retire_savings = random.randint(10000, 50000)
            net_worth += retire_savings
            print(
                f"You chose to max out retirement savings by adding ${retire_savings}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            financial_decisions()
            return retire_savings
        elif choice == "2":
            travel_cost = random.randint(10000, 50000)
            net_worth -= travel_cost
            print(f"You chose to travel the world and spent {travel_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            financial_decisions()
            return travel_cost
    
        elif choice == "3":
            real_estate_return = random.randint(10000, 100000)
            net_worth += real_estate_return
            print(f"Your investment earned you ${real_estate_return}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            financial_decisions()
            return real_estate_return
        else:
            slowprint(Fore.RED + "Invalid choice. Please enter 1 or 2." + Style.RESET_ALL)
            return age50_69()
        # NOT DONE DO SOME CHOICES HERE


def age70beyond():
    slowprint("Congratulations! You have retired and are now in retirement.")
    slowprint(Fore.GREEN + f"YOUR FINAL NET WORTH ${net_worth}!!!" + Style.RESET_ALL)
    print("Thank you for playing!" + Fore.BLUE + " Head $tart" + Style.RESET_ALL)
    exit()


def initial_choice():
    global net_worth
    while True:
        slowprint(Fore.BLUE + "\nFresh out of high school. What's next?" + Style.RESET_ALL)
        print("1. Get a Job (Immediate Income, but lower long-term income and limited growth)")
        print("2. Go to College (Leads to student loans, delayed income, but higher long-term earnings)")
        print("3. Start a Business (High risk, high reward)\n")
        time.sleep(.5)
        choice = input("Enter your choice (1-3) (or 'stop' to exit): ")

        if choice == "1":
            job, income = get_a_job()
            net_worth += income
            career = job
            return career, income
        elif choice == "2":
            career, income = college()
            net_worth += income
            return  career, income
        elif choice == "3":
            net_worth, career, income = start_a_business()
            net_worth += income
            return net_worth, career, income
        elif choice.lower() == "stop":
            slowprint(
                Fore.BLUE + f"Game Over! Thanks for playing! Your final net worth is ${net_worth}." + Style.RESET_ALL)
            exit()
        else:
            print(Fore.RED + "Invalid input. Please enter 1, 2, or 3." + Style.RESET_ALL)


def main():
    global net_worth, age
    income, career = None, None
    print(
        Fore.BLUE + "Welcome to Head $tart!" + Style.RESET_ALL + "\nThis is a game designed to teach you about making smart financial decisions.\n")
    time.sleep(1)
    slowprint(Fore.BLUE + "What is your name?" + Style.RESET_ALL)
    name = input()
    time.sleep(.5)
    slowprint(f"Hello {name}! You are {age} years old, and have a starting net worth of ${net_worth}.")
    

    initial_choice()
    

    #if isinstance(financial_effect, int):
        #net_worth += financial_effect

    age_transition()


if __name__ == "__main__":
    main()
