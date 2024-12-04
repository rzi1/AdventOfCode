forms = [str(x).replace("\n",  " ") for x in open("Inputs/d6").read().split("\n\n")]

answers = 0
p2_answers = 0
for form in forms:
    individuals_arr = form.split(" ")
    individuals = (set(individual) for individual in individuals_arr)
    id1 = next(individuals)
    p2_answers += len(id1.intersection(*individuals))
    form = form.replace(" ","")
    answers += len(set(form))

print(answers)
print(p2_answers)