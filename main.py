#All financial deposits/withdrawls due to certain choices are based on real-life scenarios
import time
import random
from colorama import Fore, Back, Style

global income, net_worth, savings,  age
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

def initial_choice(): #Allows them to choose between a job/college/business
    global net_worth
    while True:
        slowprint(Fore.BLUE + "\nFresh out of high school. What's next?" + Style.RESET_ALL)
        print("1. Get a Job (Immediate Income, but lower long-term income and limited growth)")
        print("2. Go to College (Leads to student loans, delayed income, but higher long-term earnings)")
        print("3. Start a Business (High risk, high reward)\n")
        time.sleep(.5)
        choice = input("Enter your choice (1-3) (or 'stop' to exit): ")

        if choice == "1":
            #Job
            personality_traits["career_focused"] += 1 #Gives points to certain personality traits based on their choices for a reflection at the end of the game
            job, income = get_a_job()
            career = job
            return career, income
        elif choice == "2":
            #College
            personality_traits["cautious"] += 1
            personality_traits["career_focused"] += 1
            career, income = college()
            return  career, income
        elif choice == "3":
            #Entrepreneur
            personality_traits["risk_taker"] += 1
            net_worth, career, income = start_a_business()
            return net_worth, career, income
        elif choice.lower() == "stop":
            slowprint(
                Fore.BLUE + f"Game Over! Thanks for playing! Your final net worth is ${net_worth}." + Style.RESET_ALL)
            exit()
        else:
            print(Fore.RED + "Invalid input. Please enter 1, 2, or 3." + Style.RESET_ALL)
        

def get_a_job():
    global income, net_worth
    #Jobs that usually don't require post-secondary education
    jobs = {
        "Retail Worker": 20000, "Fast Food Worker": 15000, "Office Assistant": 40000, "Factory Worker": 38000,
        "Service Worker": 28000,
        "Chef": 45000, "Waiter": 30000, "Dancer": 33000, "Police Officer": 52000, "Mechanic": 40000,
        "Receptionist": 35000
    }
    print("")
    job, income = random.choice(list(jobs.items())) #Ensures the experience and story is entertaining and unpredictable for the user each time
    slowprint(f"You got a job as a {job} and earn ${income} per year.")
    net_worth += income
    slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
    print("")
    return job, income

def college():
    global net_worth
    slowprint(
        "You chose to go to college. You have student loans to pay off, but you have an opportunity to get a better paying job. \n")
    print("")
    print(Fore.BLUE + "Do you want to stay in-state or go out of state?" + Style.RESET_ALL)
    choice = input(
        "1. In-state for $100,000 (Lower tuition costs, limited opportunities \n2. Out-of-state for $160,000 (Higher tuition costs, more opportunities) \n")
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

def collegejob():
    global income, net_worth
    better_jobs = {
        "Doctor": 350000, "Lawyer": 140000, "Corporate Manager": 100000, "Actor": 80000, "Software Engineer": 130000,
        "Accountant": 79000, "Architect": 108000, "Engineer": 116000, "Astronaut": 152000, "Pilot": 215000,
        "Professor": 180000, "Veterinarian": 130000
    }
    job, income = random.choice(list(better_jobs.items()))
    slowprint(f"After graduating college, you got a job as a {job} and earn ${income} per year.")
    net_worth += income
    slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
    print("")
    return job, income

def start_a_business():
    global income, net_worth
    slowprint(
        "Congratulations! You have decided to start a business. The risks are high, but so is the reward.") #Gives background on the potential choice to help educate the user
    income = random.randint(50000, 400000)
    net_worth -= 90000
    career = "Entrepreneur"
    print(f"You started a business and earn ${income} per year and spent on $90,000 starting up the business.")
    net_worth += income
    slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
    print("")
    return net_worth, career, income

def age_transition(): #Ensures the story is carried through different lifestages
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
    global net_worth, age, income
    if age == 18:
        slowprint(Fore.BLUE + "You're navigating early adulthood. Would you like to:" + Style.RESET_ALL)
        print("1. Focus on career advancement")
        print("2. Enjoy your youth with vacations and socializing")
        print("3. Take a gap year & Explore the world")
        print("4. Start a sidehustle")
        choice = input("Enter your choice (1 - 4): ")
        print("")
        if choice == "1":
            # Career-focused path
            personality_traits["career_focused"] += 1
            personality_traits["cautious"] += 1
            print("You chose to focus on career advancement. Your career progresses well!")
            income_increase = random.randint(10000, 20000)
            net_worth += income_increase
            print(f"You gained ${income_increase} in income.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        elif choice == "2":
            # Socializing path
            personality_traits["experience_seeker"] += 1
            personality_traits["risk_taker"] += 1
            print("You chose to enjoy your youth. While you had fun, you spent money on vacations and social activities.")
            expense = random.randint(1000, 5000)  # Spending on leisure
            net_worth -= expense
            print(f"You spent ${expense} on leisure.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL) #Returns the net worth after every decision the user makes to continue interactivity
            return
        
        elif choice == "3":
            # Gap year path
            personality_traits["experience_seeker"] += 1
            personality_traits["risk_taker"] += 1
            print("You chose to take a gap year and explore the world. You spent money on travel and experiences.")
            travel_cost = random.randint(5000, 10000)
            net_worth -= travel_cost
            print(f"You spent ${travel_cost} on travel.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "4":
            # Side hustle path
            personality_traits["career_focused"] += 1
            personality_traits["risk_taker"] += 1
            print("You chose to start a side hustle. Your side business was successful and you earned extra income.")
            sidehustle_income = random.randint(1000, 50000)
            net_worth += sidehustle_income
            print(f"Your side hustle earned you ${sidehustle_income}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return

        else:
            slowprint(Fore.RED + "Invalid choice. Please enter 1 or 2." + Style.RESET_ALL)
            return age18_25()
        
    elif age == 23:
        slowprint(Fore.BLUE + "You're in your early 20s. Choose:" + Style.RESET_ALL)
        print("1. Invest in stocks (High risk, high reward)")
        print("2. Sort out your transportation (Car, bike, public transport)")
        print("3. Further your education (Certifications, courses)")
        print("4. Invest in cryptocurrency (High risk, high reward)")
        choice = input("Enter your choice (1-4): ")
        print("")
        if choice == "1":
            # Stock investment
            personality_traits["risk_taker"] += 1
            stock_investment = random.randint(1000, 10000)
            net_worth += stock_investment
            print(f"You invested in stocks and gained ${stock_investment}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "2":
            # Transportation
            slowprint("What's your mode of transportation?")
            print("1. Buy a Car (Costs more but provides convenience)")
            print("2.Rent a Car (Cheaper, but no ownership)")
            print("2. Bike (Eco-friendly, cheaper)")
            print("3. Public Transport (Cheapest option)")
            choice = input("Enter your choice (1-4): ")
            if choice == "1":
                car_cost = random.randint(10000, 50000)
                net_worth -= car_cost
                print(f"You bought a car and spent ${car_cost}.")
                slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
                return
            
            elif choice == "2":
                rent_car_cost = random.randint(500, 2000)
                net_worth -= rent_car_cost
                print(f"You rented a car and spent ${rent_car_cost}.")
                slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
                return
            
            elif choice == "3":
                bike_cost = random.randint(500, 2000)
                net_worth -= bike_cost
                print(f"You bought a bike and spent ${bike_cost}.")
                slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
                return
            
            elif choice == "4":
                public_transport_cost = random.randint(100, 500)
                net_worth -= public_transport_cost
                print(f"You used public transport and spent ${public_transport_cost}.")
                slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
                return
            return
        
        elif choice == "3":
            # Education
            personality_traits["career_focused"] += 1
            education_cost = random.randint(1000, 50000)
            net_worth -= education_cost
            salary_increase = random.randint(10000, 20000)
            income += salary_increase
            print(f"You furthered your education and spent ${education_cost}, but you now earn ${salary_increase} more.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "4":
            # Cryptocurrency investment
            personality_traits["risk_taker"] += 1
            crypto_investment = random.randint(100, 10000)
            net_worth += crypto_investment
            print(f"You invested in cryptocurrency and gained ${crypto_investment}.")
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
        print("1. Buy a house (Requires a down payment, but it could appreciate over time)")
        print("2. Rent a house(Less expensive, but no property appreciation")
        print("3. Start a family")
        print("4. Climb the career ladder (Could lead to salary increases, promotions)")
        choice = input("Enter your choice (1 - 4 ): ")
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
            family_choice = input("Enter your choice (1-3): ")
            if family_choice == "1":
                #Have a wedding
                wedding_cost = random.randint(10000, 500000)
                net_worth -= wedding_cost
                print(f"You had a wedding and spent ${wedding_cost}.")
                slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
                return
            
            elif family_choice == "2":
                #Have a child
                child_cost = random.randint(10000, 90000)
                net_worth -= child_cost
                print(f"You had a child and spent ${child_cost}.")
                slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
                return
            
            elif family_choice == "3":
                #Get a pet
                pet_cost = random.randint(1000, 5000)
                net_worth -= pet_cost
                print(f"You got a pet and spent ${pet_cost}.")
                slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
                return
            
            elif family_choice == "4":
                #Elope
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

def age30_40():
    global net_worth,age
    if age == 33:
        slowprint(Fore.BLUE + "You're in your 30s, building your career and wealth. Choose:" + Style.RESET_ALL)
        print("1. Expand your investment portfolio (Stocks, real estate, bonds, mutual funds)")
        print("2. Focus on career advancement (Could lead to salary increases, promotions)")
        print("3. Purchase a vacation home")
        print("4. Focus on growing your family")
        choice = input("Enter your choice (1-4): ")
    
        if choice == "1":
            #Expanding investment portfolio
            personality_traits["risk_taker"] += 1
            investment = random.randint(10000, 70000)
            net_worth += investment
            print(f"You expanded your investment portfolio and gained ${investment}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "2":
            #Focusing on career advancement
            personality_traits["career_focused"] += 1
            salary_increase = random.randint(10000, 20000)
            net_worth += salary_increase
            print(f"You focused on career advancement and received a salary increase of ${salary_increase}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "3":
            #Purchasing a vacation home
            personality_traits["luxury_spender"] += 1
            vacation_home_cost = random.randint(100000, 500000)
            net_worth -= vacation_home_cost
            print(f"You bought a vacation home and spent ${vacation_home_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "4":
            #Growing family
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
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            #Retirement planning
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
            #Investments in health
            personality_traits["experience_seeker"] += 1
            health_cost = random.randint(1000, 5000)
            net_worth -= health_cost
            print(f"You invested in your health and spent ${health_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "3":
            #Paying off mortgage
            personality_traits["frugal"] += 1
            mortgage_payment = random.randint(10000, 50000)
            net_worth -= mortgage_payment
            print(f"You paid off your mortgage and spent ${mortgage_payment}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "4":
            #Vacation
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
        print("4. Further save for retirement")
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            #Investment portfolio
            personality_traits["risk_taker"] += 1
            personality_traits["career_focused"] += 1
            investment = random.randint(10000, 70000)
            net_worth += investment
            print(
                f"You chose to start a new investment portfolio. Your investments grow and you accumulate ${investment}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "2":
            #Career break
            personality_traits["experience_seeker"] += 1
            personality_traits["risk_taker"] += 1
            break_cost = random.randint(10000, 50000)
            net_worth -= break_cost
            print(f"You chose to take a career break.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "3":
            #Luxury asset
            personality_traits["luxury_spender"] += 1
            luxury_asset_cost = random.randint(10000, 50000)
            net_worth -= luxury_asset_cost
            print(f"You bought a luxury asset and spent ${luxury_asset_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "4":
            #Retirement saving
            personality_traits["cautious"] += 1
            retire_savings = random.randint(10000, 50000)
            net_worth += retire_savings
            print(f"You saved extensively for retirement and added ${retire_savings}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        else:
            slowprint(Fore.RED + "Invalid choice. Please enter 1 or 2." + Style.RESET_ALL)
            return age40_50()
    elif age == 48:
        slowprint(Fore.BLUE + "You're in your late 40s. Options:" + Style.RESET_ALL)
        print("1. Focus on growing your wealth")
        print("2. Spend on experiences (Travel, hobbies)")
        print("3. Invest in real estate")
        print("4. Plan for retirement")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            #Growing wealth
            personality_traits["career_focused"] += 1
            personality_traits["frugal"] += 1
            wealth_growth = random.randint(10000, 50000)
            net_worth += wealth_growth
            print(f"You focused on growing your wealth and gained ${wealth_growth}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "2":
            #Experience spending
            personality_traits["experience_seeker"] += 1
            experience_cost = random.randint(10000, 50000)
            net_worth -= experience_cost
            print(f"You spent on experiences and spent ${experience_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "3":
            #Real estate
            personality_traits["frugal"] += 1
            real_estate_return = random.randint(10000, 100000)
            net_worth += real_estate_return
            print(f"You invested in real estate and earned ${real_estate_return}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "4":
            #Retirement planning
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
        print("4. Wills, trusts, charities")
        choice = input("Enter your choice (1 - 4): ")
        if choice == "1":
            #Diversifying income
            personality_traits["career_focused"] += 1
            personality_traits["frugal"] += 1
            diverse_income = random.randint(10000, 50000)
            net_worth += diverse_income
            print(f"You diversified your income and gained ${diverse_income}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "2":
            #Travelling world
            personality_traits["experience_seeker"] += 1
            travel_cost = random.randint(10000, 50000)
            net_worth -= travel_cost
            print(f"You traveled the world and spent ${travel_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "3":
            #Downsizing home
            personality_traits["frugal"] += 1
            home_downsize = random.randint(10000, 50000)
            net_worth += home_downsize
            print(f"You downsized your home and gained ${home_downsize}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "4":
            #Wills, trusts, charities
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
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            #Growing wealth
            personality_traits["career_focused"] += 1
            wealth_growth = random.randint(10000, 50000)
            net_worth += wealth_growth
            print(f"You focused on growing your wealth and gained ${wealth_growth}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "2":
            #Experience spending
            personality_traits["experience_seeker"] += 1
            experience_cost = random.randint(10000, 50000)
            net_worth -= experience_cost
            print(f"You spent on experiences and spent ${experience_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "3":
            #Family vacation
            personality_traits["experience_seeker"] += 1
            vacation_cost = random.randint(1000, 5000)
            net_worth -= vacation_cost
            print(f"You took a family vacation and spent ${vacation_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "4":
            #Retirement planning
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
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            #Retirement planning
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
            #Part-time job
            personality_traits["experience_seeker"] += 1
            income = (income / 2)
            net_worth += income
            print(f"You worked part-time and earned ${income}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "3":
            #Travelling
            personality_traits["experience_seeker"] += 1
            travel_cost = random.randint(10000, 100000)
            net_worth -= travel_cost
            print(f"You traveled the world and spent ${travel_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "4":
            #Moving
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
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            #Retire
            return age70beyond()
        
        elif choice == "2":
            #Selling assets
            personality_traits["frugal"] += 1
            asset_sell = random.randint(10000, 50000)
            net_worth += asset_sell
            print(f"You sold your assets and gained ${asset_sell}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "3":
            #Making donation
            personality_traits["cautious"] += 1
            donation_cost = random.randint(1000, 5000)
            net_worth -= donation_cost
            print(f"You made a large donation and spent ${donation_cost}.")
            slowprint(Fore.GREEN + f"Updated net worth: ${net_worth}" + Style.RESET_ALL)
            return
        
        elif choice == "4":
            #Health insurance
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
    print("1. Travel the world (Spend your savings on adventures)")
    print("2. Volunteer (Give back to the community)")
    print("3. Live a quiet life (Enjoy your years in peace)")
    print("4. Pass wealth down to family (Support future generations)")
    slowprint(Fore.GREEN + f"YOUR FINAL NET WORTH: ${net_worth}!!!" + Style.RESET_ALL)
    
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        #Travel
        personality_traits["experience_seeker"] += 1
        print("You chose to travel the world. Enjoy your adventures!")
    
    elif choice == "2":
        #Volunteer
        personality_traits["experience_seeker"] += 1
        print("You chose to volunteer. Giving back is a great way to spend your time!")
    
    elif choice == "3":
        #Quiet life
        personality_traits["frugal"] += 1
        print("You chose to live a quiet life. Enjoy your peaceful years!")
    
    elif choice == "4":
        #Support future generations
        personality_traits["cautious"] += 1
        print("You chose to pass wealth down to your family. Support future generations!")
    else:
        slowprint(Fore.RED + "Invalid choice. Please enter 1 - 4." + Style.RESET_ALL)
        return
    
    # Personality Summary
    slowprint("\nLet's pave your story and reflect on how your decisions/personality would have played out in the real world!")
    print("")
    
    if personality_traits["risk_taker"] > personality_traits["cautious"]:
        print("You are mostly a risk-taker! You embraced opportunities with high rewards but also high risks.")
        slowprint(Fore.BOLD + Fore.YELLOW + "This bold approach to finance is admired! However, make sure to prioritize financial stability as well, and balancing high-risk investments with stable assets (like bonds or index funds) might help secure this." + Style.RESET_ALL)
    
    else:
        print("You are quite financially cautious! You prioritized stability and long-term security over risky opportunities.")
        slowprint(Fore.BOLD + Fore.YELLOW + "You were secure, but taking calculated risks—such as small investments or side businesses—might have helped you grow your wealth without jeopardizing security." + Style.RESET_ALL)
    print("")
    
    time.sleep(1)
    if personality_traits["luxury_spender"] > personality_traits["frugal"]:
        print("You tend to enjoy the finer things in life! You prioritized luxury and experiences over savings.")
        slowprint(Fore.BOLD + Fore.YELLOW + "While happiness is important, balancing spending with savings could improve financial security." + Style.RESET_ALL)
        
    else:
        print("You are a bit frugal and financially disciplined. You made sure to secure a stable future through careful spending.")
        slowprint(Fore.BOLD +Fore.CYAN + "Your careful budgeting and disciplined saving have put you in a strong financial position! However, life isn’t just about accumulating wealth - spending on experiences, personal growth, or even calculated investments are neccessary to make your life more fulfilling!" + Style.RESET_ALL)
    print("")
    time.sleep(1)
    
    if personality_traits["career_focused"] > personality_traits["experience_seeker"]:
        print("You are quite career-driven! You prioritized financial growth and professional success.")
        slowprint(Fore.BOLD + Fore.MAGENTA + "You worked hard to climb the career ladder, and it paid off! While income is key to financial success, making your money work for you through smart investments and passive income sources could have helped even more, and it is important to note that taking a break is also necessary!" + Style.RESET_ALL)
    else:
        print("You love to value life experiences! You sought joy in travel, socializing, and meaningful moments over strict financial discipline.")
        slowprint(Fore.BOLD + Fore.MAGENTA + "While your memories are invaluable and great for your mental health, a bit more financial planning—like setting aside funds for the future or investing could have ensured long-term security while still allowing for adventure." + Style.RESET_ALL)
    
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
            #Save income
            savings += (income * 0.5)
            net_worth += (income * 0.5)  # Save half of income into savings
            personality_traits["cautious"] += 1
            personality_traits["frugal"] += 1
            print(f"You saved 50% of your income into savings. Savings: ${savings}.")
        
        elif choice == "2":
            #Stocks
            invest_result = random.choice([100, 5000, 10000, 50000, 25000, 20000])
            net_worth += invest_result  # Net worth increases from investments
            personality_traits["risk_taker"] += 1
            print(f"You invested in stocks, and your investment resulted in ${invest_result}. Net worth: ${net_worth}.")
        
        elif choice == "3":
            #Spend on luxury items
            luxury_result = random.choice([-10000, -5000, -1000, -2000])
            net_worth += luxury_result  # Spending on luxury decreases net worth
            personality_traits["luxury_spender"] += 1
            print(f"You spent ${abs(luxury_result)} on luxury items. Net worth: ${net_worth}.")
        
        elif choice == "4":
            #Retirement savings
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
