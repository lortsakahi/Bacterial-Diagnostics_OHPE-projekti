patients={}
resistance_risk=["Pseudomonas", "Enterobacter", "Pneumoniae"]
'''This is the dictionary for all patients diagnosed.'''
from datetime import datetime, timedelta

def gramPlus():
    '''
    This function will be called if user wants to get clean cultivation analysis.
    If the gram staining result was gram(+), this function will ask if the bacteria growth has any katalase activity.
    No katalase activity has two different diagnosis possibilities, either Aureus or Saprophyticus based on koagulase enzyme activity.
    In case there is katalase activity, the program asks which type of hemolysis can be detected on the plate.
    In case of alpha-hemolysis, the final diagnosis depends on whether the bacteria is resistant to optokine.
    If the bacteria was beta-hemolytic, the diagnosis refers straight to Pyogenes infection.
    The diagnosis result will be saved into the Patients-dictionary under the key asked line 120 preceding diagnosis1() function.
    '''
    kat=str(input("Result of catalase test (T/F): "))
    if kat=="T":
        koag=str(input("Result of coagulase test (T/F): "))
        if koag=="T":
            bac="Aureus"
            patients[pat]=bac
            print("Your patient has Staphylococcus aureus infection if any of the following symptoms are present:\nred/irritated skin, joint pain, fever.")
        elif koag=="F":
            bac="Saprophyticus"
            patients[pat]=bac
            print("Your patient has Staphylococcus saprophyticus infection\nwhich causes urinary tract infections.")
    elif kat=="F":
        hem=str(input("Describe the type of hemolysis on the plate (alpha/beta): "))
        if hem=="alpha":
            opt=str(input("The bacteria is susceptible to optocine (T/F): "))
            if opt=="T":
                bac="Pneumoniae"
                patients[pat]=bac
                print("Your patient has Streptococcus pneumoniae infection that causes\nrespiratory track symptoms.")
            elif opt=="F":
                bac="Viridans"
                patients[pat]=bac
                print("Your patient has Streptococcus viridans infection that causes\npneumonia and possibly meningitis.")
        if hem=="beta":
            bac="Pyogenes"
            patients[pat]=bac
            print("Your patient has Streptococcu pyogenes infection,\nwhich usually manifest itself thourgh either fasciitis/cellulitis or Strep Throat.")

def gramNeg():
    '''
    This function will be called if user wants to get clean cultivation analysis.
    If the gram staining result was gram(-), this function will ask if the growth is oxidase active.
    Positive oxidase activity has a specific diagnosis.
    In case the growth is not oxidase active, the final diagnosis is based on the morfology of the bacterial colonies.
    Fluorescent colonies and non-fluorescent have separate diagnosis.
    The diagnosis result will be saved into the Patients-dictionary under the key asked in line 120 preceding diagnosis1() function.
    '''
    ox=str(input("Result of oxidase test (T/F): "))
    if ox=="T":
        bac="Enterobacter"
        patients[pat]=bac
        print("Your patient has salmonellosis if any of the symptoms are present:\nfever, stomach ache and diarrhea. Otherwise your patient is healthy.")
    elif ox=="F":
        morf=str(input("The colonies are fluorescent (T/F): "))
        if morf=="T":
            bac="Pseudomonas"
            patients[pat]=bac
            print("Your patient has Pseudomonas infection.\nHowever, it rarely shows any symptoms in healthy people.")
        elif morf=="F":
            bac="Haemophilus"
            patients[pat]=bac
            print("Your patient has Haemophilus infection (ear/eye/sinus infections, pneumonia.")

def diagnosis1():
    '''
    For clarity see Picture nro. 1.
    This function forms the basis for clean culture diagnosis criteria.
    The result of gram staining leans the diagnosis toward different types of bacteria.
    The following diagnosis functions gramPlus() and gramNeg() are called respectively.
    '''
    try:
        gram=str(input("Result of Gram staining (+/-): "))
        if gram=="+":
            gramPlus()
        if gram=="-":
            gramNeg()
    except ValueError:
        print("Please insert answers according to the instructions.")
    except UnboundLocalError:
        print("Please insert answers according to the instructions.")

def diagnosis2(patients: dict):
    '''
    This function estimates the risk for bacterial resistance by counting the mean for Disch experiment diameter.
    In this experiment, an antibiotic disk is  placed on the growth plate.
    The more bacteria has diminished around the disc during incubation, the less resistant the bacteria are.
    The limit is set to 18 mm in this function. S refers to susceptible bacteria and R to resistant accoringly to the SIR-classification.
    For some species there is no resistance data available an therefore they are automaticly classified as susceptible.

    :param patients: the data is taken from the diagnosis-library patients.
    '''
    limit=18
    nro=int(input("Please give the number of the patient: "))
    if patients[nro]=="Pyogenes":
        bentz=int(input("Bentzylepenicilline Disc diameter (mm): "))
        amox=int(input("Amoxicilline Disc diameter (mm): "))
        res=((bentz+amox)/2)
        if res<limit:
            print("No resistance detected (S).")
        else:
            print("There is a resistance risk (R).")
    elif patients[nro]=="Enterobacter":
        sulf=int(input("Sulfatrimetoprime Disc diameter (mm): "))
        norf=int(input("Norfloxacine Disc diameter (mm): "))
        trim=int(input("Trimetoprime Disc diameter (mm): "))
        res=((sulf+norf+trim)/3)
        if res<limit:
            print("No resistance detected (S).")
        else:
            print("There is a resistance risk (R).")
    elif patients[nro]=="Pneumoniae":
        ery=int(input("Erytromycine Disc diameter (mm): "))
        klin=int(input("Klindamysine Disc diameter (mm): "))
        res=((ery+klin)/2)
        if res<limit:
            print("No resistance detected (S).")
        else:
            print("There is a resistance risk (R).")
    elif patients[nro]=="Pseudomonas" or patients[nro]=="Haemophilus" or patients[nro]=="Aureus" or patients[nro]=="Saprophyticus" or patients[nro]=="Viridans":
        print("No resistance detected with these species (S).")

def diagnosis3(resistance_risk: list):
    '''
    This function counts the number of resistant patients and adds the count to the patients-dictionary.
    The resistant bacteria are searched from the resistance_risk list defined inside this function.

    :param resistance_risk: list of the risky bacterial species
    '''
    n=0
    for patient in patients:
        if patient in resistance_risk:
            n+=1
    patients["Resistant patients"]=n
    return n

def end():
    '''
    This function will be called if the user wants to close down the program.
    The function saves the made diagnosis into the Patients.py file with the information of the diagnosis date.
    '''
    with open("C:\Users\lohik\ohpe-projekti-Karin-Lohi\src\Patients.py", "w") as t:
        from datetime import datetime, timedelta
        tanaan=datetime.now()
        t.write(tanaan.strftime("%Y %m %d %H %M"))
        for key, value in patients.items(): 
            t.write('%s:%s\n' % (key, value))

while True:
    '''
    This is the main program view, where the user will start and were they will return after each function.
    The user will get to choose the diagnosis method, which each call for different functions defined above.
    This program is created in a while-loop, which is breaked after the user chooses number 0.
    The while-loop includes some try-error possibilities in case the user inserts non-numerical answer.
    '''
    try:
        print("Welcome to the Automated Bacterial diagnostics program!\n")
        print("Here are your options:\n0 Diagnosis ready, please exit the program\n1 Pure culture conclusions\n2 Bacterial resistance analysis\n3 Bacterial resistance in current patients\n4 See the list of the patients\n")
        val=int(input("Please select your preferred method of diagnosis: "))
        
        if val==0:
            end()
            break
        
        elif val==1:
            pat=int(input("Please give the number of the patient: "))
            diagnosis1()
        
        elif val==2:
            diagnosis2()
        
        elif val==3:
            diagnosis3()

        elif val==4:
            print(patients)

    except ValueError:
        print("Please choose an existing diagnostics alternative between number 0 and 5!")
    except TypeError:
        print("Please type in your choice of diagnostic method in numeral format!")

print("Thank you for trusting our services! Hopefully we'll see you soon again.")
