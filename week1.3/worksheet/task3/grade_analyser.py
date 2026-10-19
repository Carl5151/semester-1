# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file
file = input("Enter file name: ")
students = []

# open the file
with open(f'{file}', 'r') as f:
# read in the data, and for each student calculate their average grade and classification
    data = f.readlines()
    clean = []
    # retrieve only values
    for line in data[1:]:
        clean.append(line.strip().split(','))
    # formating data
    for grades in clean:
        format = [grades[0]]
        # calculating average
        sum = 0
        modules = 0
        for grade in range(1, len(grades)):
            try:
                sum += int(grades[grade])
                modules += 1
            except:
                break
        average = sum / modules
        format.append(f"{average:.2f}")
        # determining classification
        if average < 40:
            format.append('F')
        elif average < 50:
            format.append('3')
        elif average < 60:
            format.append('2:2')
        elif average < 70:
            format.append('2:1')
        else:
            format.append('1')
        # store formatted student grade
        students.append(format)

# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}

# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'
with open(f'{file}_out.csv', 'w') as outfile:
    for student in students:
        outfile.write(f"{student[0]},{student[1]},{student[2]}\n")

# You can compare your output files with the 4 example files in example_outfiles folder
