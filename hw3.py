import data

#Part 1
#Takes in a list of CountyDemographics objects and returns
#the total population of all counties as an int
def population_total(demos:list[data.CountyDemographics]) -> int:
    pop = 0
    for x in demos:
        pop += x.population['2014 Population']

    return pop


#Part 2
#Takes in a list of CountyDemographics objects and a string
#representing a state and filters the given list to include
#only demographics from the given state
def filter_by_state(demos:list[data.CountyDemographics], state:str) -> list[data.CountyDemographics]:
    return [x for x in demos if x.state == state]


#Part 3
#Takes in a list of CountyDemographics objects and a string
#representing an education level and filters population based on
#given parameters
def population_by_education(demos:list[data.CountyDemographics], filter:str) -> float:
    pop = 0
    for x in demos:
        if filter not in x.education:
            continue
        pop += (x.population['2014 Population'] * (x.education[filter]/100))
    
    return pop

#Takes in a list of CountyDemographics objects and a string
#representing an ethnicity and filters population based on
#given parameters
def population_by_ethnicity(demos:list[data.CountyDemographics], filter:str) -> float:
    pop = 0
    for x in demos:
        if filter not in x.ethnicities:
            continue
        pop += (x.population['2014 Population'] * (x.ethnicities[filter]/100))
    
    return pop

#Takes in a list of CountyDemographics objects and returns
#the total population of people living below the poverty level
def population_below_poverty_level(demos:list[data.CountyDemographics]) -> float:
    pop = 0
    for x in demos:
        pop += (x.population['2014 Population'] * (x.income['Persons Below Poverty Level']/100))
    
    return pop


#Part 4
#Takes in a list of CountyDemographics objects and a string
#representing an education level and returns a filtered population 
#as a percentage based on the given parameters
def percent_by_education(demos:list[data.CountyDemographics], filter:str) -> float:
    if population_total(demos) != 0:
        return population_by_education(demos, filter)/population_total(demos)
    else:
        return 0.00

#Takes in a list of CountyDemographics objects and a string
#representing an ethnicity and returns a filtered population 
#as a percentage based on the given parameters
def percent_by_ethnicity(demos:list[data.CountyDemographics], filter:str) -> float:
    if population_total(demos) != 0:
        return population_by_ethnicity(demos, filter)/population_total(demos)
    else:
        return 0

#Takes in a list of CountyDemographics objects and returns the percentage
#of the total population living below the poverty level
def percent_below_poverty_level(demos:list[data.CountyDemographics]) -> float:
    if population_total(demos) != 0:
        return population_below_poverty_level(demos)/population_total(demos)
    else:
        return 0


#Part 5
#Takes in a list of CountyDemographics objects and a string
#representing an education level and returns a filtered list of
#CountyDemographics that are above the given threshold value
def education_greater_than(demos:list[data.CountyDemographics], filter:str, threshold:float) -> list[data.CountyDemographics]:
    if threshold < 0 or threshold > 100:
        #print('Please input a number between 0 and 100')
        return
    return [x for x in demos if x.education[filter] > threshold]

#Takes in a list of CountyDemographics objects and a string
#representing an education level and returns a filtered list of
#CountyDemographics that are below the given threshold value
def education_less_than(demos:list[data.CountyDemographics], filter:str, threshold:float) -> list[data.CountyDemographics]:
    if threshold < 0 or threshold > 100:
        #print('Please input a number between 0 and 100')
        return
    return [x for x in demos if x.education[filter] < threshold]

#Takes in a list of CountyDemographics objects and a string
#representing an ethnicity and returns a filtered list of
#CountyDemographics that are above the given threshold value
def ethnicity_greater_than(demos:list[data.CountyDemographics], filter:str, threshold:float) -> list[data.CountyDemographics]:
    if threshold < 0 or threshold > 100:
        #print('Please input a number between 0 and 100')
        return
    return [x for x in demos if x.ethnicities[filter] > threshold]

#Takes in a list of CountyDemographics objects and a string
#representing an ethnicity and returns a filtered list of
#CountyDemographics that are below the given threshold value
def ethnicity_less_than(demos:list[data.CountyDemographics], filter:str, threshold:float) -> list[data.CountyDemographics]:
    if threshold < 0 or threshold > 100:
        #print('Please input a number between 0 and 100')
        return
    return [x for x in demos if x.ethnicities[filter] < threshold]


#Takes in a list of CountyDemographics objects and returns a filtered list of
#CountyDemographics that are above the given threshold value based on the
#the percentage of people living below the poverty level
def below_poverty_level_greater_than(demos:list[data.CountyDemographics], threshold:float) -> list[data.CountyDemographics]:
    if threshold < 0 or threshold > 100:
        #print('Please input a number between 0 and 100')
        return
    return [x for x in demos if x.income['Persons Below Poverty Level'] > threshold]

#Takes in a list of CountyDemographics objects and returns a filtered list of
#CountyDemographics that are below the given threshold value based on the
#the percentage of people living below the poverty level
def below_poverty_level_less_than(demos:list[data.CountyDemographics], threshold:float) -> list[data.CountyDemographics]:
    if threshold < 0 or threshold > 100:
        #print('Please input a number between 0 and 100')
        return
    return [x for x in demos if x.income['Persons Below Poverty Level'] < threshold]