import two_state_ca.py
from matplotlib import pyplot as plt
rule_number = 110
length = 100
time = 100 

initialCondition = random_string(length)

field = spacetime_field(110, initialCondition, length)
spacetime_diagram(field, 10)
plt.savefig('rule110.pdf')