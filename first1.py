# 1
# IDENTIFY ADMIN

user_id = ['kunal', 'nihal', 'avadhoot', 'admin', 'abhijeet']

for user_id in user_id:
    if user_id == 'admin':
        print(f"Hello! {user_id.title()}, would you like see status report?")
    else:
        print(f"Hello! {user_id.title()}, thank you for logging in again.")
        
