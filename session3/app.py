# Python Validation
# age = 0 => 70
# def validate_age(age):
#     if isinstance(age,int) and 0 <= age <= 70:
#         return True
#     else:
#         return False

# print(validate_age(-10))
# print(validate_age(1.5))
# print(validate_age("bj"))
# print(validate_age(5))
# print(validate_age(75))

# def validate_username(username):
#     if(username.isalnum() and 3 <= len(username) <= 50 ):
#         return True
#     return False

# Regex  
# import re
# def validate_email(email):
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     print(re.match(pattern, email))
#     return re.match(pattern, email) is not None

# print(validate_email("aaa"))

# import json

# json_data = '{"name":"marwa", "age":"40"}'
# data = json.loads(json_data)
# print(json_data["name"])
# try:
#     data = json.loads(json_data)
#     if "name" in data and isinstance(data["name"], str):
#         print("valid")
#     else: 
#         print("invalid")
# except json.JSONDecodeError:
#     print("invalid json")




# def validate_username(username):
#     if(username.isalnum() and 3 <= len(username) <= 50 ) or (username.isdigit()):
#             return True
#     return False

# validate_username("123")

# pydantic
# pip install pydantic email-validator

# from pydantic import BaseModel, ValidationError, EmailStr

# class Post(BaseModel):
#     id: int
#     content: str
#     email: EmailStr

# try:
#     p = Post(id=1, content="text", email="@a.com")
#     print("tmam")
# except ValidationError as err:
#     print(err.json())

# from pydantic import BaseModel, ValidationError, EmailStr, Field, field_validator
# from typing import List, Optional
# class Address(BaseModel):
#     floornum: str
#     streetname: str
#     zipcode: str = Field(..., pattern=r'^\d{5}$')
# class User(BaseModel):
#     name : str = Field(..., min_length=3, max_length=20)
#     email: EmailStr
#     age: int = Field(..., ge=14, le=70)
#     status: bool = True
#     skills: List[str] = []
#     address: Optional[Address] = None
#     @field_validator('name')
#     @classmethod
#     def name_with_capital(cls, value):
#         if not value[0].isupper():
#             raise ValueError("Name must start with capital letter")
#         return value
# try:
#     userData = User(
#         name= "Marwa", email="a@a.com", age=15, status=True, skills=[])
#     print("done")
# except Exception as err:
#     print(err)

# class User:
#     name = None
#     age = 0
#     def show(self):
#         print(self.name, self.age)

# marwa = User()
# marwa.name="marwa"
# marwa.age=40
# marwa.show()

# class User:
#     def __init__(self, name = None, age = 0):
#         self.name = name
#         self.age = age
#     def show(self):
#         print(self.name, self.age)

# user1 = User("marwa", 40)
# user2 = User("abc", 30)
# user3 = User()
# user1.show()
# user2.show()
# user3.show()


# class User:
#     def __init__(self, name, age):
#         self.name =name
#         self.age = age
#     def show(self):
#         print(self.name, self.age)

# class Student(User):
#     def __init__(self,name, age, grades):
#         super().__init__(name,age)
#         self.grades =grades
#     def show(self):
#         super().show()
#         print(self.grades)
#     @staticmethod
#     def p():
#         print("test")

# s = Student("marwa",40, [])
# s.show()
# Student.p()

# pip install requests
import requests
# url = "https://jsonplacehoder.typicode.com/users"
# try:
#     res = requests.get(url)
#     # print(res.status_code)
#     # print(res.text)
#     result = res.json()
#     print(result)
# except requests.exceptions.RequestException as err:
#     print(err)

# if input > 10 or < 1  print invalid number
# call url = "https://jsonplacehoder.typicode.com/users/{numbr}"

# import api_req
# url = "https://jsonplaceholder.typicode.com/posts"

# response = api_req.getApiData(url)
# print(response)

# payload = {
#     "title": 'foo',
#     "body": 'bar',
#     "userId": 1,
#   }

# headers = {
#     "Content-Type": "application/json"
# }
# api_req.postApiData(url, payload, headers)

# import json
# json_data = '{"name":"marwa", "age":40}'
# data = json.loads(json_data)

# j_str = json.dumps(data, indent=10)
# print(j_str)
# with open("x.json", "r") as file:
#     data = json.load(file)
#     j = json.dump(data)
#     print(j)

# with open("f.json", "w") as file:
#     json.dump(data, file, indent=5)


#pycryptodome
# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes

# key = get_random_bytes(16)
# cipher = AES.new(key, AES.MODE_EAX)
# nonce = cipher.nonce

# d = b"marwa"
# ciphertxt, tag = cipher.encrypt_and_digest(d)
# print(ciphertxt)
# cipher_dec = AES.new(key, AES.MODE_EAX, nonce=nonce)
# plainData = cipher_dec.decrypt_and_verify(ciphertxt, tag)
# print(plainData)
# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes

# key = get_random_bytes(16)
# cipher = AES.new(key, AES.MODE_EAX)
# nonce = cipher.nonce

# d = b"marwa"
# ciphertext, tag = cipher.encrypt_and_digest(d)
# print(ciphertext)

# cipher_dec = AES.new(key, AES.MODE_EAX, nonce=nonce)
# plainData = cipher_dec.decrypt_and_verify(ciphertext, tag)
# print(plainData)


# paramiko
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(
    hostname="",
    username="",
    password="",
    port=22
)

# stdin, stdout, stderr = ssh.exec_command('ls -l /home')
# print(stdout.read().decode())

sftp = ssh.open_sftp()
sftp.put("file_path", "remote_path")
sftp.get("remotePath", "localpath")
sftp.close()
ssh.close()