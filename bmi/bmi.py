weight = int(160)
height = int(67)

bmi = (weight / (height)**2) * 703
# convert to string with 2SD


def get_feedback(bmi):
    if bmi <= 18.4:
        return "underweight"
    elif bmi <= 24.9:
        return "normal"
    elif bmi <= 29.9:
        return "overweight"
    elif bmi <= 34.9:
        return "obese"


feedback = get_feedback(bmi)
bmi = "{:.2f}".format(bmi)


print(bmi)
print(feedback)
