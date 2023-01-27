from django.contrib.auth.models import User
uname = input('User name is ? :')
uemail = input('User email is ? ?')
upassword = input('User password is ? :')
user = User.objects.create_user(uname, uemail, upassword)

# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
# user.last_name = 'Lennon'
user.save()