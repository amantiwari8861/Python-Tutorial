class User:
  @classmethod
  def from_id(cls, user_id):
    # Logic to create user from ID
    return cls(user_id, ...)  # Call the main constructor with retrieved data

  @classmethod
  def from_email(cls, email):
    # Logic to create user from email
    return cls(..., email)  # Call the main constructor with retrieved data

  def __init__(self, user_id, email):
    self.user_id = user_id
    self.email = email

# Assuming you have implemented the logic within the class methods
user1 = User.from_id(123)  # Create user from user ID 123
user2 = User.from_email("example@email.com")  # Create user from email

print(user1.email,user1.user_id)
print(user2.email,user2.user_id)
