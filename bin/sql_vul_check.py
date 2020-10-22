import requests

def find_error_based_sql(list_of_links):
    print("[+] Checking the above list for Error Based SQL INJECTION")
    flag = 1
    for i in list_of_links:
        initial = "'"
        first = requests.post(i+initial)

        if "mysql" in first.text.lower():
            print("\033[93m[+] Injectable MySQL detected -> \033[0m"+str(i))
            flag = 0
        elif "native client" in first.text.lower():
            print("\033[93m[+] Injectable MSSQL detected -> \033[0m"+str(i))
            flag = 0
        elif "syntax error" in first.text.lower():
            print("\033[93m[+] Injectable PostGRES detected -> \033[0m"+str(i))
            flag = 0
        elif "ORA" in first.text.lower():
            print("\033[93m[+] Injectable Oracle detected -> \033[0m"+str(i))
            flag = 0

    if flag is 1:
        print("\n[-] No Error Based SQL Vulnerability Found.")
