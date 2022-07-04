import csv
from optparse import check_choice

def write_into_csv(info_list):
    with open('student_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["NAME","AGE","CONTACT_NO","EMAIL_ID"])

        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True

    while(condition):
        student_info = input("Enter Student information ( NAME AGE CONTACT_NO EMAIL_ID ) : ")
        
        #Split
        student_info_list = student_info.split(' ')
        
        print("\nThe Entered information is -> \nNAME :{}\nAGE :{}\nCONTACT_NO :{}\nEMAIL_ID :{}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

        choise_check = input("Is written information correct ? ( Yes / No )")
        if check_choice == "Yes":
            write_into_csv(student_info_list)
            
            condition_check = input("Enter ( YES / NO ) if you want to enter information of another student ")
            if condition_check == 'YES':
               condition = True
            elif condition_check == 'NO':
                condition = False  
                print("<--------Thank You -------->")

        elif check_choice == "No":
            print("\nPlease Re-Enter the values !!!")        
        