def get_update_rules(update, rule_dict):
    update_rules = {}
    for page in update:
        relevant_rules = []
        all_rules = rule_dict[page]
        for rule in all_rules:
            if rule in update:
                relevant_rules.append(rule)
        update_rules[page] = relevant_rules
    return update_rules


def check_page(page, page_rules):
    for rule in page_rules:
        if page >= rule:
            # print(page, 'should be less than', rule)
            return False
    return True


def check_update(update, update_rules):
    for page in update:
        page_idx = update.index(page)
        if any([rule in update_rules[page] for rule in update[:page_idx]]):
            return False
        # if check_page(page, update_rules[page]) == False:
        #     return False
    # print('unbroken')
    return True


data = open('day_5/input.txt').read().split('\n\n')

rule_dict = {}
for rule in data[0].split():
    rule = rule.split('|')
    left = int(rule[0])
    right = int(rule[1])
    if left in rule_dict:
        rule_dict[left].append(right)
    else:
        rule_dict[left] = [right]

all_updates = []
for update in data[1].split():
    all_updates.append([int(i) for i in update.split(',')])


## Task 1
all_correct_updates = []
for update in all_updates:
    update_rules = get_update_rules(update, rule_dict)
    if check_update(update, update_rules):
        # print('UNBROKEN')
        all_correct_updates.append(update)

midpoint_total = 0
for update in all_correct_updates:
    midpoint_total += update[int(len(update)/2)]
print(f'Task 1: {midpoint_total}') # 6384


