import data #changes were made to the repr method to make display less cluttered
from build_data import get_data as allDemographics
import hw3 as df #Demographic Functions

from os.path import exists
from colorPrint import prGreen, prRed, prCyan, prPurple #Custom library to implement easy functions to use color with print() function


class EXIT(Exception): pass

full_data = allDemographics()
counties = full_data

valid_fields = {"Education": ["Bachelor's Degree or Higher", "High School or Higher"],
                "Ethnicities": ["American Indian and Alaska Native Alone", "Asian Alone", "Black Alone", "Hispanic or Latino", "Native Hawaiian and Other Pacific Islander Alone", "Two or More Races", "White Alone", "White Alone, not Hispanic or Latino"],
                "Income": ["Persons Below Poverty Level"]}

def field_error(f:str, cat:str):
    #Function to report field category errors to reduce clutter
    prRed("Error: {} is not a valid category of {}".format(cat, f))
    return

def check_args(length:int, proper_length:int, usage:str) -> bool:
    #function to change whether or not the correct amount
    # of arguments were given for a specific function
    if length < proper_length:
        prRed("Error: Not enough arguments")
        prRed("Command Usage: " + usage)
        return False
    if length > proper_length:
        prRed("Error: Too many arguments")
        prRed("Command Usage: " + usage)
        return False
    else:
        return True

def eval_command(com:str, demos:list[data.CountyDemographics]):
    #Main function to evaluate the opfile commands
    #Matches first argument to active commands
    global counties
    args = com.split(':')
    match args[0]:
        case "display":
            #Syntax: display
            #Print the county information for each county to the terminal
            if not check_args(len(args), 1, "display"):
                return

            for x in demos:
                print(x)

            prPurple('Successfully printed {} entries!'.format(len(demos)))

        case "filter-state":
            #Syntax: filter-state:<state abbreviation>
            #Reduce the collection of counties to those with matching state abbreviation 
            #If no county's state matches the abbreviation, then the resulting collection will be empty
            if not check_args(len(args), 2, "filter-state:<state abbreviation>"):
                return
            
            counties = df.filter_by_state(demos, args[1])
            prPurple("Now only showing counties located in {}".format(args[1]))
            prPurple("Total entries remaining: {}".format(len(counties)))

        case "filter-gt":
            #Syntax: filter-gt:<field>:<number>
            #Reduce the collection of entries to those for which the value in the 
            # specified <field> is greater-than the specified <number>
            if not check_args(len(args), 3, "filter-gt:<field>:<number>"):
                return
            
            fields = args[1].split('.')

            if len(fields) != 2:
                prRed("{} is not a valid argument for this command".format(args[1]))
                return

            try:
                thr = float(args[2])
                if thr > 100 or thr < 0:
                    prRed("Error: You must provide a third argument that is a number between 0 and 100")
                    return
            except:
                prRed("Error: You must provide a third argument that is a number between 0 and 100")
                return

            match fields[0]:
                case 'Education':
                    if fields[1] not in valid_fields[fields[0]]:
                        field_error(fields[0], fields[1])
                        return
                    counties = df.education_greater_than(demos, fields[1], thr)
                case 'Ethnicities':
                    if fields[1] not in valid_fields[fields[0]]:
                        field_error(fields[0], fields[1])
                        return
                    counties = df.ethnicity_greater_than(demos, fields[1], thr)
                case 'Income':
                    if fields[1] not in valid_fields[fields[0]]:
                        field_error(fields[0], fields[1])
                        return
                    counties = df.below_poverty_level_greater_than(demos, thr)
                case _:
                    prRed("Error: {} is not a valid field for this Command".format(args[1]))
                    return
                
            prPurple("Successfully filtered countries by {}, {} higher than {}%".format(fields[0], fields[1], thr))

        case "filter-lt":
            #Syntax: filter-lt:<field>:<number>
            #Reduce the collection of entries to those for which the value in the 
            # specified <field> is less-than the specified <number>
            if not check_args(len(args), 3, "filter-lt:<field>:<number>"):
                return

            fields = args[1].split('.')

            if len(fields) != 2:
                prRed("{} is not a valid argument for this command".format(args[1]))
                return

            try:
                thr = float(args[2])
                if thr > 100 or thr < 0:
                    prRed("Error: You must provide a third argument that is a number between 0 and 100")
                    return
            except:
                prRed("Error: You must provide a third argument that is a number between 0 and 100")
                return

            match fields[0]:
                case 'Education':
                    if fields[1] not in valid_fields[fields[0]]:
                        field_error(fields[0], fields[1])
                        return
                    counties = df.education_less_than(demos, fields[1], thr)
                case 'Ethnicities':
                    if fields[1] not in valid_fields[fields[0]]:
                        field_error(fields[0], fields[1])
                        return
                    counties = df.ethnicity_less_than(demos, fields[1], thr)
                case 'Income':
                    if fields[1] not in valid_fields[fields[0]]:
                        field_error(fields[0], fields[1])
                        return
                    counties = df.below_poverty_level_less_than(demos, thr)
                case _:
                    prRed("Error: {} is not a valid field for this Command".format(args[1]))
                    return
                
            prPurple("Successfully filtered countries by {}, {} less than {}%".format(fields[0], fields[1], thr))

        case "population-total":
            #Syntax: population-total
            #Print (to the terminal) the total 2014 population across all current counties (not per county)
            if not check_args(len(args), 1, "population-total"):
                return
            
            pop = df.population_total(counties)
            prPurple("2014 Population: {}".format(pop))

        case "population":
            #Syntax: population:<field>
            #Compute the total 2014 sub-population across all current counties (not per county). 
            #The specified <field> is expected to be a percentage of the population for each entry, 
            # so this computation requires computing the sub-population by entry.
            if not check_args(len(args), 2, "population:<field>"):
                return
            
            fields = args[1].split('.')
            match fields[0]:
                case 'Education':
                    if fields[1] not in valid_fields[fields[0]]:
                        field_error(fields[0], fields[1])
                        return
                    pop = df.population_by_education(demos, fields[1])
                case 'Ethnicities':
                    if fields[1] not in valid_fields[fields[0]]:
                        field_error(fields[0], fields[1])
                        return
                    pop = df.population_by_ethnicity(demos, fields[1])
                case 'Income':
                    if fields[1] not in valid_fields[fields[0]]:
                        field_error(fields[0], fields[1])
                        return
                    pop = df.population_below_poverty_level(demos)
                case _:
                    prRed("Error: {} is not a valid field for this Command".format(args[1]))
                    return

            prPurple("2014 {} Population: {}".format(fields[1], round(pop, 2)))

        case "percent":
            #Syntax: percent:<field>
            #Print the percentage of the total population within the sub-population specified by <field>
            if not check_args(len(args), 2, "percent:<field>"):
                return
            
            fields = args[1].split('.')
            match fields[0]:
                case 'Education':
                    if fields[1] not in valid_fields[fields[0]]:
                        field_error(fields[0], fields[1])
                        return
                    per = df.percent_by_education(demos, fields[1])
                case 'Ethnicities':
                    if fields[1] not in valid_fields[fields[0]]:
                        field_error(fields[0], fields[1])
                        return
                    per = df.percent_by_ethnicity(demos, fields[1])
                case 'Income':
                    if fields[1] not in valid_fields[fields[0]]:
                        field_error(fields[0], fields[1])
                        return
                    per = df.percent_below_poverty_level(demos)
                case _:
                    prRed("Error: {} is not a valid field for this Command".format(args[1]))
                    return

            prPurple("2014 {} Population Percentage: {}%".format(fields[1], round(per*100, 2)))

        case "clear-filters":
            #reset current counties to full data set
            counties = full_data
            prPurple("Filters reset, now showing all countries")

        case "exit":
            #Raise exception to break out of debug loop
            prCyan("Exiting debug mode")
            raise EXIT
        
        case _:
            prRed("Error: '{}' is not a valid command".format(com))

if __name__ == '__main__':
    
    opFile = 'inputs/' + input('Select OP File: ')

    if opFile.strip("inputs/") == 'debug': #Debug mode to test and try functions individually
        prCyan("Now entering Debug Mode")
        while True:
            try:
                In = input('Enter Command: ') 
                eval_command(In, counties)
            except EXIT:
                break

    else:
        if exists(opFile):
            #If the specified opfile exists, evaluate the file commands line by line
            with open(opFile, 'r') as op:
                for command in op:
                    eval_command(command.strip('\n'), counties)

        else:
            prRed("Error: No such opfile exists\n Make sure the specified opfile is located in the 'inputs' folder")