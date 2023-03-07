class CountyDemographics:
    # Initialize a new CountyDemographics object.
    # input: the county's age demographics data as a dictionary
    # input: the county's name as a string
    # input: the county's education demographics data as a dictionary
    # input: the county's ethnicities demographics data as a dictionary
    # input: the county's income demographics data as a dictionary
    # input: the county's population demographics data as a dictionary
    # input: the county's state as a string
    def __init__(self,
                  age: dict[str,float],
                  county: str,
                  education: dict[str,float],
                  ethnicities: dict[str,float],
                  income: dict[str,float],
                  population: dict[str,float],
                  state: str):
        self.age = age
        self.county = county
        self.education = education
        self.ethnicities = ethnicities
        self.income = income
        self.population = population
        self.state = state


    def format_property(self, prop):
        new = ''
        for x in prop:
            new += '\n\t\t'
            new += str(x)
            new += ': '
            new += str(prop[x])
        return new

    # Provide a developer-friendly string representation of the object.
    # input: CountyDemographics for which a string representation is desired. 
    # output: string representation
    def __repr__(self):
        return '\033[92m County: {}, {}\033[00m \n\t\033[1m Age Demographics:\033[0m{} \n\t\033[1m Education Demographics:\033[0m{} \n\t\033[1m Ethnicity Demographics:\033[0m{} \n\t\033[1m Income Demographics:\033[0m{} \n\t\033[1m Population:\033[0m{}\n'.format(
                self.county,
                self.state,
                self.format_property(self.age),
                self.format_property(self.education),
                self.format_property(self.ethnicities),
                self.format_property(self.income),
                self.format_property(self.population),
            )
