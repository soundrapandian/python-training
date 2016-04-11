def count_value(item):
    return item[1]
input_file = None
try:
    input_file = open('votes.txt')
    vote_count_dict = {}
    voter_list = []
    for line in input_file:
        color = line.split('-')[1].strip().lower()
        voter = line.split('-')[0].strip().lower()
        if voter not in voter_list:
            voter_list.append(voter)
            if color in vote_count_dict.keys():
                vote_count_dict[color] += 1
            else:
                vote_count_dict[color] = 1
    vote_count_list = list(vote_count_dict.items())
    vote_count_list.sort(key=count_value, reverse=True)
    print (vote_count_list[0][0])
    print (vote_count_list)
except Exception as e:
    print (str(e))
finally:
    if input_file:
        input_file.close()