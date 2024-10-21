
import statistics
def display_main_menu():
    print("Enter some numbers separated by commas(e.g.5,67,32)")


def get_user_input():
    input_num= input()
    number= input_num.split(",")
    num_list = [float(string) for string in number]
    return num_list

def calc_average(num_list):
    avg= sum(num_list)/len(num_list)
    print("Avg Temp is:", avg)

def calc_min_max_temperature(num_list):
    min_max_list=[min(num_list),max(num_list)]
    print(min_max_list)

def sort_temp(num_list):
    num_list.sort()
    print("Sorted order is",num_list)

def calculate_median_temp(num_list):
    median = statistics.median(num_list)
    print("The median is:", median)

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    calc_average(num_list)
    calc_min_max_temperature(num_list)
    sort_temp(num_list)
    calculate_median_temp(num_list)

if __name__=="__main__":
    main()