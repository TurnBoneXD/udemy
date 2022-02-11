def fotmat_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return
    name = f_name.title()
    surname = l_name.title()
    return f"{name} {surname}"

x = fotmat_name(input("Enter your first name : "),input("Enter your last name : "))
print(x)