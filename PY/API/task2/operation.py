import requests

class APIClient:

    def getusers(self):

        try:
            response=requests.get("https://jsonplaceholder.typicode.com/users")

            response.raise_for_status()

            data=response.json()

            return data

        except Exception as e:
            print(e)

    def adduser(self):

        name=input("Enter user name")
        email=input("Enter user email")

        data={
            "name":name,
            "email":email,
        }

        try:

            res=requests.post("https://jsonplaceholder.typicode.com/posts",json=data)

            print(res.status_code)
        
        except Exception as e:
            print(e)
    
    def viewuser(self):
        try:
            response=requests.get("https://jsonplaceholder.typicode.com/users")

            response.raise_for_status()

            data=response.json()

            for user in data:

                print(f"{user['name']},{user['email']}")
        
        except Exception as e:

            print(e)
    def deleteuser(self):

        id=input("Enter ID you want to delete user")

        try:
            response=requests.delete(f'https://jsonplaceholder.typicode.com/posts/{id}')

            print(response.status_code)
        
        except Exception as e:

            print(e)

    def updateuser(self):       

        try:
            id=input("Enter ID you want to delete user")
            name=input("Enter user name")
            email=input("Enter user email")    

            data={
                "name":name,
                "email":email
            }
            response=requests.patch(f'https://jsonplaceholder.typicode.com/posts/{id}',json=data)

            print(response.status_code)
            
            if response.status_code==200:
                print("data updated")

        except Exception as e:
            print(e)


            
            