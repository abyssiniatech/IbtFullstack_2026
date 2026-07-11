# telebirr tip calculator
# step1 store a bill total (ETB)  and number of people in variable
# step2 write a funtion  split_bill(total,people,tip_rate=0.10)
# step3 use it compute the per-person amount ,tip include
# step4 loop over  a list of names and print each person's share 

# solve the problem by using the above steps
def split_bill(total, people, tip_rate=0.10):
    total_with_tip = total + (total * tip_rate)
    return total_with_tip / people

bill_total = 1000  # ETB
num_people = 5
tip_percentage = 0.15  # 15%

names = ["Aster", "Biniyam", "Chala", "Dawit", "Eleni"]

for name in names:
    share = split_bill(bill_total, num_people, tip_percentage)
    print(f"{name} should pay: {share:.2f} ETB")
    
