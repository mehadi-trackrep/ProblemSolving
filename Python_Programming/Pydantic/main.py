from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

user_attr = {
    'name': 'John Doe',
    'email': 'john.doe@goava.com',
    'account_id': '1'
}

user = User(**user_attr)
print(user.account_id)

# user = User(name='John Doe', email='john.doe@gmail.com', account_id='str')
# print(user.account_id)

user = User(name='John Doe', email='john.doe@google.com', account_id='12')
print(user.account_id)
