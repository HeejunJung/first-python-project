import Login_Function
import Database 

while True: #계정이 있을 경우
    if Login_Function.question():
        Login_Function.Login(Database.database_ID, Database.database_pwd, Database.database_nickname)
        break
    else:   #계정이 없을 경우
        Login_Function.make_ID(Database.database_ID, Database.database_nickname)
        Login_Function.make_pwd(Database.database_pwd)

