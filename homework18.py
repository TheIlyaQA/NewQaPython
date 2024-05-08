test_design_writers = [1, 3, 5]
test_scripters = [2, 3, 4, 6, 7, 8]
reviewers = [1, 2, 3, 9, 10]
out_of_office_today = [2, 5, 6, 1]

all_team = sorted(set(test_design_writers + test_scripters + reviewers + out_of_office_today))
print(f'all testers in the team -> {all_team}')

only_write_scripts = sorted(set(test_scripters) - set(test_design_writers) - set(reviewers))
print(f'testers who can only write scripts -> {only_write_scripts}')

at_work_today = sorted(set(test_design_writers + test_scripters + reviewers) - set(out_of_office_today))
print(f'testers who are at work today -> {at_work_today}')

could_write_and_review_today = sorted(set(reviewers).intersection(set(test_design_writers)) - set(out_of_office_today))
print(f'testers who could write and review scripts, and are at work today -> {could_write_and_review_today}')