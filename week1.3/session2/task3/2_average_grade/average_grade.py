# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]

iteration = 0
averages = []
with open("student_data.csv", "r") as f:
    # iterate througheach line in file
    for line in f:
        if iteration == 0:
                iteration += 1
        else:
            # calc average grades
            total = int(line.split(",")[2]) + int(line.split(",")[3]) + int(line.split(",")[4])
            average = total / 3
            averages.append(f"{line.split(",")[1]}: {average:.2f}")

# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3


# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f

with open("report.txt", "w") as outfile:
    for grade in averages:
        outfile.write(f"{grade}\n")        
