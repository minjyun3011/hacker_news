import requests


def search_address(zipcode):
    response = requests.get(f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}")

# print(response)
# print(response.text)
    if response.status_code == 200:
        address_info = response.json()["results"][0]
        pref_name = address_info["address1"]
        city_name = address_info["address2"]
        town_name = address_info["address3"]
     
        address = f"{pref_name}{city_name}{town_name}"
        return address
    else:
        print("郵便番号検索に失敗しました")


if __name__ == "__main__":
    zipcode = input("郵便番号を入力してください > ")
    result = search_address(zipcode)
    if result:
        print(result)


   