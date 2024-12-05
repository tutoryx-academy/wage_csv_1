
wages_file = open('wage_reports/input.csv')
wages_file_lines = wages_file.readlines()

print(type(wages_file_lines))


for row in wages_file_lines[1:]:
    print(type(row))
    name, rate, hour = row.split(',')
    wage = float(rate) * float(hour) #TODO: HW apply calculate wage with condition 1.5 for more than 40 hours
    print(name, wage)
    
    #write outputs to a file
    wage_output = open('wage_reports/output.csv','w') #TODO: Find why just the last one is written in output, hint read docs for open func.
    str_output = name+','+str(wage)
    wage_output.write(str_output)