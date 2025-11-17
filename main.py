from pyscript import display
# DS2
Science = {'James', 'John', 'Smith', 'Doe'}
Math = {'John', 'Smith', 'Sean', 'LeBron'}

one_club = (Science | Math)
both_club = (Science & Math)
sci = (Science)
math = (Math)
only_club = (Science ^ Math)

display(f'These students are all in at least one club {one_club}', target='output')
display(f'These students belong to both clubs {both_club}', target='output')
display(f'These students belong to science club {sci}', target='output')
display(f'These students belong to math club {Math}', target='output')
display(f'These students belong to only one club {only_club}', target='output')