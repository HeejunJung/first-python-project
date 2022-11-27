# members = ['egoing', 'k8805', 'leezche']
# for memeber in members do 
#     if memebers == input_id
#         puts('Hello!, '+members)
#         exit
#     end
# end
# puts("Who are you?")

puts("아이디를 입력해주세요: ")
input_id = gets.chomp()

def login(id)
    members = ['egoing', 'k8805', 'leezche']
    for member in members do
        if member == id
             return true #리턴이 작동하면 밑은 작동x
        end
    end
    return false
end

if login(input_id)
    puts("안녕하세요 " +input_id +"님")
else
    puts(input_id + "님 누구세요")
end
