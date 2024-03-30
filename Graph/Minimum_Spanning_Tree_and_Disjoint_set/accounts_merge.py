from disjoint_set_by_rank import *


def accounts_merge(accounts):
    n = len(accounts)
    hash_map = dict()
    disjoint = Disjoint(n)

    for i, (name, *emails) in enumerate(accounts):
        for email in emails:

            if email in hash_map:
                disjoint.union_by_rank(hash_map[email], i)
            else:
                hash_map[email] = i

    print(hash_map)
    combined_accounts = [[] for _ in range(n)]

    for email, index in hash_map.items():
        ultimate_parent_index = disjoint.find_uparent(index)

        combined_accounts[ultimate_parent_index].append(email)

    result = []
    for i in range(len(combined_accounts)):

        if len(combined_accounts[i]) == 0:
            continue

        name = [accounts[i][0]]
        sorted_emails = sorted(combined_accounts[i])

        name.extend(sorted_emails)
        result.append(name)

    print(result)
    return result


accounts = [["John", "j1@com", "j2@com", "j3@com"],
            ["John", "j4@com"],
            ["Raj", "r1@com", "r2@com"],
            ["John", "j1@com", "j5@com"],
            ["Raj", "r2@com", "r3@com"],
            ["Mary", "m1@com"]]

accounts_merge(accounts)
