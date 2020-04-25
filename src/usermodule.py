from itertools import permutations,product
from collections import namedtuple

def add_dimension(old_values, new_dim_values, new_field_names):
    NewTuple = namedtuple('_', new_field_names)
    new_values = (NewTuple(*(x+(z,))) for x,z in product(old_values, new_dim_values))
    return new_values

def solution():
    locations = ['Vijayawada','Guntur','Mumbai','Pune','Hyderabad']
    temperatures = ['hot', 'cool', 'medium', 'verycool', 'veryhot']
    workshops = ['internet of things', 'distributed computing', 'machine learning', 'cyber security', 'artificial intelligence']
    works = ['wipro', 'IBM', 'google', 'zoho', 'tata']
    persons = ['meghana', 'nikhila', 'renuka', 'albert', 'jessy']

    location_permutations = permutations(locations)
    temperature_permutations = permutations(temperatures)
    workshop_permutations = permutations(workshops)
    work_permutations = permutations(works)
    person_permutations = permutations(persons)

  
    location_permutations = (x for x in location_permutations
            if x.index('Guntur')==0) 
    person_permutations = (x for x in person_permutations
            if x.index('renuka')-x.index('nikhila')==-1) 
    temperature_permutations = (x for x in temperature_permutations
            if x.index('verycool') == 2) 

    TwoTuple = namedtuple('_','location person')
    possible_solutions = (TwoTuple(x,z) for x,z in product(location_permutations, person_permutations))


    possible_solutions = (x for x in possible_solutions
            if x.location.index('Pune')==x.person.index('meghana')) 
    possible_solutions = (x for x in possible_solutions
            if abs(x.location.index('Guntur')-x.person.index('jessy')) == 1) 

    possible_solutions = add_dimension(possible_solutions, temperature_permutations,'location person temperature')

   
    possible_solutions = (x for x in possible_solutions
            if x.location.index('Vijayawada')==x.temperature.index('hot')) 
    possible_solutions = (x for x in possible_solutions
            if x.person.index('nikhila')==x.temperature.index('medium')) 

    possible_solutions = add_dimension(possible_solutions, work_permutations,'location person temperature work')

    
    possible_solutions = (x for x in possible_solutions
            if x.location.index('Hyderabad')==x.work.index('tata')) 
    possible_solutions = (x for x in possible_solutions
            if x.person.index('albert')==x.work.index('IBM')) 
    possible_solutions = (x for x in possible_solutions
            if x.temperature.index('cool')==x.work.index('google')) 

    possible_solutions = add_dimension(possible_solutions, workshop_permutations,'location person temperature work workshop')

    
    possible_solutions = (x for x in possible_solutions
            if x.location.index('Mumbai')==x.workshop.index('artificial intelligence')) 
    possible_solutions = (x for x in possible_solutions
            if x.work.index('zoho')==x.workshop.index('machine learning')) 
    possible_solutions = (x for x in possible_solutions
            if abs(x.work.index('wipro')-x.workshop.index('internet of things'))==1)
    possible_solutions = (x for x in possible_solutions
            if abs(x.work.index('IBM')-x.workshop.index('distributed computing'))==1) 

    possible_solutions = list(possible_solutions)
    if len(possible_solutions)==0:
        raise Exception('no solution found')

    if len(possible_solutions)>1:
        raise UserWarning('solution is not unique')

    sol = possible_solutions[0]
    while True:
        n=int(input("1.To find location of the workshop\n2.To find temperature of the location\n3.To find the person in the location to know about the details of the workshop conducted\n4.To find which workshop is conducted at a particular place\n5.Exit\nEnter your choice"))
        if n==1:
            n1=int(input("1.internet of things\n2.distributed computing\n3.machine learning\n4.cyber security\n5.artificial intelligence\n6.exit\nEnter your choice"))
            if(n1==1):
                print("The {} city conducts internet of things workshop.\n".format(sol.location[sol.workshop.index('internet of things')]))
            elif(n1==2):
                print("The {} city conducts distributed computing workshop.\n".format(sol.location[sol.workshop.index('distributed computing')]))
            elif(n1==3):
                print("The {} city conducts machine learning workshop.\n".format(sol.location[sol.workshop.index('machine learning')]))
            elif(n1==4):
                print("The {} city conducts cyber security workshop.\n".format(sol.location[sol.workshop.index('cyber security')]))
            elif(n1==5):
                print("The {} city conducts artificial intelligence workshop.\n".format(sol.location[sol.workshop.index('artificial intelligence')]))
            elif n1==6:
                print("EXITING")
                break
            else:
                print("Invalid option please Choose a valid option")
        elif n==2:
            n2=int(input("1.veryhot\n2.verycool\n3.hot\n4.cool\n5.medium\n6.exit\nEnter your choice"))
            if(n2==1):
                print("It is the {} where the temperature is very hot.\n".format(sol.location[sol.temperature.index('veryhot')]))
            elif(n2==2):
                print("It is the {} where the temperature is very cool.\n".format(sol.location[sol.temperature.index('verycool')]))
            elif(n2==3):
                print("It is the {} where the temperature is hot.\n".format(sol.location[sol.temperature.index('hot')]))
            elif(n2==4):
                print("It is the {} where the temperature is cool.\n".format(sol.location[sol.temperature.index('cool')]))
            elif(n2==5):
                print("It is the {} where the temperature is medium.\n".format(sol.location[sol.temperature.index('medium')]))
            elif n2==6:
                print("EXITING")
                break
            else:
                print("Invalid option please Choose a valid option")
        elif n==3:
            n3=int(input("1.Guntur\n2.Vijayawada\n3.Hyderabad\n4.Pune\n5.Mumbai\n6.exit\nEnter your choice"))
            if(n3==1):
                print("It is {} who knowns the details of the workshop conducted in Guntur.\n".format(sol.person[sol.location.index('Guntur')]))
            elif(n3==2):
                print("It is {} who knowns the details of the workshop conducted in Vijayawada.\n".format(sol.person[sol.location.index('Vijayawada')]))
            elif(n3==3):
                print("It is {} who knowns the details of the workshop conducted in Hyderabad.\n".format(sol.person[sol.location.index('Hyderabad')]))
            elif(n3==4):
                print("It is {} who knowns the details of the workshop conducted in Pune.\n".format(sol.person[sol.location.index('Pune')]))
            elif(n3==5):
                print("It is {} who knowns the details of the workshop conducted in Mumbai.\n".format(sol.person[sol.location.index('Mumbai')]))
            elif n3==6:
                print("EXITING")
                break
            else:
                print("Invalid option please Choose a valid option")
        elif n==4:
            n4=int(input("1.Guntur\n2.Vijayawada\n3.Hyderabad\n4.Pune\n5.Mumbai\n6.exit\nEnter your choice"))
            if(n4==1):
                print("It is {} the workshop conducted in Guntur.\n".format(sol.workshop[sol.location.index('Guntur')]))
            elif(n4==2):
                print("It is {} the workshop conducted in Vijayawada.\n".format(sol.workshop[sol.location.index('Vijayawada')]))
            elif(n4==3):
                print("It is {} the workshop conducted in Hyderabad.\n".format(sol.workshop[sol.location.index('Hyderabad')]))
            elif(n4==4):
                print("It is {} the workshop conducted in Pune.\n".format(sol.workshop[sol.location.index('Pune')]))
            elif(n4==5):
                print("It is {} the workshop conducted in Mumbai.\n".format(sol.workshop[sol.location.index('Mumbai')]))
            elif n4==6:
                print("EXITING")
                break
            else:
                print("Invalid option please Choose a valid option")
        elif n==5:
            print("EXITING")
            break
        else:
            print("Invalid option please Choose a valid option")
if __name__ == '__main__':
    solution()
