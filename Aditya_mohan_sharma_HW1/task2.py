
file1 = open('visited_link_file_q1_time_zone.txt', 'r')
file2 = open('visited_link_file_q1_electric_car.txt', 'r')
file3 = open('visited_link_file_q1_carbon_footprint.txt', 'r')

merged_file = open('merged_file_q2.txt', 'w+')
count = 0
for f1, f2, f3 in zip(file1, file2, file3):
	if(count < 1000):
	    merged_file.write(f1)
	    count += 1
	    merged_file.write(f2)
	    count += 1
	    merged_file.write(f3)
	    count += 1
	


file1.close()
file2.close()
file3.close()
merged_file.close()

print("merged file is saved as: merged_file_q2.txt in the same folder")