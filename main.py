
# calculates the punnet square calculations
def calculate(mom_genotype, dad_genotype):
    # separating the strings into arrays with individual strings in it
    mom = [*mom_genotype]
    dad = [*dad_genotype]

    genotypes_list = mom + dad

    one = genotypes_list[0]
    two = genotypes_list[1]
    three = genotypes_list[2]
    four = genotypes_list[3]

    genotypes_list = [one + three, two + three, one + four, two + four]
    print("List of genotypes: " + genotypes_list.__str__())


    #       A (1)      a (2)
    # a (3) Aa (1, 3) aa (2, 3)
    # a (4) Aa (1, 4) aa (2, 4)


# input the genotypes as individual strings separated by a comma
if __name__ == '__main__':
    mom, dad = input("Please enter two genotypes to calculate a punnett square with (in the form of \"Xx Xx\"): ").split()
    calculate(mom, dad)
