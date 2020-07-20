from covid import Covid

c = Covid()
try:
    cntry = input("Enter Country Name :").strip()
    country_name = cntry.lower()
    country_info = c.get_status_by_country_name(country_name)

    count = 0
    for key in country_info:
        if count>1 and count<6:
            print(key, "cases =>", country_info[key])
        count+=1
except:
    print("Check the correct COUNTRY NAME from the given list-\n")
    for st in c.list_countries():
        print(st["name"])