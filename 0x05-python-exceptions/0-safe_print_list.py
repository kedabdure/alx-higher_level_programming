def safe_print_list(my_list=[], x=0):
    try:
        for num in my_list[:x]:
            print("{}".format(num))
    except IndexError:
        pass

