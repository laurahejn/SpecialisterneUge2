import os

#first we have our data
local_parent = os.getcwd()
relative_data = r'Data\app_log (logfil analyse) - random.txt'
data_path = os.path.join(local_parent, relative_data)

#Then we sort our original datafile so that we may compare to the result of our code
sorted_log = []
type_log = []
with open(data_path, 'r') as datafile: 
    for line in datafile:
        line_list = line.split()
        log_type = line_list[2]
        if log_type not in type_log:
            type_log.append(log_type)
            sorted_log.append([line])
        else:
            sorted_log[type_log.index(log_type)].append(line)

#Comparision of result of code in opg2.py and the control above
for log_type in type_log:
    res_list = []
    file_placement = r'Delopgave_2\res\{}.txt'.format(log_type)
    res_path = os.path.join(os.getcwd(), file_placement)
    #first we test that the file exists
    assert os.path.exists(res_path), 'The file does not exists for logs of the type {}'.format(log_type)
    #and it is non-empty
    assert os.path.getsize(res_path) > 0, 'The file corresponding to {} is empty.'.format(log_type)
    with open(res_path, 'r') as res_log:
        for line in res_log:
            res_list.append(line)
    control_log = sorted_log[type_log.index(log_type)]
    #check that the numbers of logs is the same in the control and the result
    assert len(res_list) == len(control_log), 'The resulting log does not contain what it is supposed to.'
    #check that each entry corresponds
    for i in range(len(res_list)):
        assert res_list[i] == control_log[i], 'The log for {} differes at index {}'.format(log_type, i)
