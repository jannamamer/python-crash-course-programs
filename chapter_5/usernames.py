current_users = ['joanna', 'christine', 'janna', 'mamer', 'python']
new_users = ['joanna', 'JANNA', 'dela cruz', 'manez', 'rootcon']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Please enter a new username.")
    else:
        print("Username is available.")
