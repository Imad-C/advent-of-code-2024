def check_consistent_direction(list_):
    # is list increasing or decreasing?
    if list_[0] < list_[1]:
        increasing = True
    elif list_[0] > list_[1]:
        increasing = False
    else: 
        return False

    # check direction is consistent
    for i, item in enumerate(list_):
        # dont want to test last element
        if i == len(list_) - 1:
            break

        if increasing:
            if item > list_[i+1]:
                return False
        else: # then decreasing
            if item < list_[i+1]:
                return False

    return True


def check_constrained_difference(list_):
    for i, item in enumerate(list_):
        # dont want to test first element
        if i == 0:
            continue

        # is difference between constraints
        difference = abs(item - list_[i-1])
        if (difference < 1) or (difference > 3):
            return False
        
    return True


# get all reports
all_reports = []
with open("day_2/input.txt", "r") as f:
    for line in f:
        report = line.strip('\n').split(' ')
        report = [int(level) for level in report]
        all_reports.append(report)
 

## Task 1: assess each report for saftey
safe_reports = 0
for report in all_reports:
    safe = True # default is safe, will check below

    safe = check_consistent_direction(report) and\
        check_constrained_difference(report)

    # add to tally if still safe
    if safe: 
        safe_reports += 1

print(f'Task 1: {safe_reports}') # 585

## Task 2: with saftey dampener
# generate a list of lists 
# of all possible combinations for each report
all_reports_combos = []
for report in all_reports:
    report_combo = []
    for i in range(0, len(report)):
        report_combo.append(report[:i]+report[i+1:])

    all_reports_combos.append(report_combo)


safe_reports = 0
# loop through all combos for each report
for report_combo in all_reports_combos:
    combo_safe = False # will assume no combo is safe, prove otherwise below
    for report in report_combo:
        # (same process as for Task 1)
        safe = True # default is safe, will check below

        safe = check_consistent_direction(report) and\
            check_constrained_difference(report)
        
        if safe: 
            combo_safe = True
            break # no need to test all combos if one is already safe

    # add to tally if at least one in the combo is safe
    if combo_safe == True:
        safe_reports += 1

print(f'Task 2: {safe_reports}') # 626