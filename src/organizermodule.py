workshops=['internetofthings','machinelearning','distributedcomputing','cybersecurity']
locations=['guntur','vijayawada','hyderabad','mumbai','nizamabad','tadepalli','pune']

neighbors={}

neighbors['guntur']=['tadepalli','hyderabad','vijayawada']
neighbors['vijayawada']=['hyderabad','guntur']
neighbors['hyderabad']=['nizamabad','pune','guntur','vijayawada']
neighbors['mumbai']=['pune']
neighbors['nizamabad']=['hyderabad']
neighbors['tadepalli']=['guntur','vijayawada']
neighbors['pune']=['mumbai']

workshops_locations={}

def neighbour_workshop(location,workshop):
    for neighbour in neighbors.get(location):
        workshoplocation_of_neighbour=workshops_locations.get(neighbour)
        if workshoplocation_of_neighbour==workshop:
            return False
    return True

def getting_workshop_location(location):
    for workshop in workshops:
        if(neighbour_workshop(location,workshop)):
            return workshop


def main():
    for location in locations:
        workshops_locations[location]=getting_workshop_location(location)
    print(workshops_locations)

main()
