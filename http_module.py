import requests 

url = "https://api.criminalip.io/v1/ip/hosting"
api_key = ""

ip_address = input("Enter an IP Address ")
num_domains = int(input("Enter the number of domains to display: " ))


headers ={
    "x-api-key": "Zv0mWe845aolF4snKfU6rAyPOi7rq0RUuzAkAgQDdB9gdcIVx6V9FdQryOCG"
}

params = {
    "ip": ip_address,
    "full" :"false"
}

response = requests.get(url,headers= headers, params= params)

if response.status_code == 200:
    data            = response.json()
    is_hosting      = data["is_hosting"]
    hosting_info    = data["hosting_info"]

    if is_hosting:
        as_name = hosting_info["as_name_include_hosting_or_cloud"]
        domains = hosting_info["domain_exist_more_than_5"]

        print(f"this ip is hosting with {as_name} AS.")

        if domains:
            print(f"The following {num_domains} domains are 이 아이피들과 연관있습니다.")
            for domain in domains[:num_domains]:
                print(domain["domain"])
        else:
            print("No domains are associated with this IP.")
    else:
        print("이 아이피는 호스팅자료가 없습니다.")

else:
    print(f"에러 발생 : {response.status_code}")



