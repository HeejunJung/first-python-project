#우주선 발사 기록 장치입니다.
#원하는 시간을 입력해주시면 자동으로 카운트다운 시작합니다.
number = 0
while True:
    number = number + 1
    ask = input('프로젝트를 가동하시겠습니까?(Y/N): ')
    #대답이 Y일경우 
    if ask == 'Y':
        print(f'우주선 이륙 프로젝트 {number}차')
        time = input("원하시는 시간을 입력해주세요ex)2시간40분 ->02시간40분00초: ") #최대 99시간99분9초
        if '시간' in time: #'시간'으로만 표시했을 경우
            if len(time) < 5:
                hour = int(time[0:2])
                time_sum = hour*60*60
            else:
                hour = int(time[0:2]) #[start:end] -> start오프셋부터 end-1오프셋까지
                min = int(time[4:6])
                second = int(time[7:9]) 
                hour_second = hour*60*60 #시간->초 변환
                min_second = min*60 #분->초 변환
                time_sum = hour_second + min_second + second
        elif '분' in time:
            if len(time) < 4: #'분'으로만 표시했을 경우
                min = int(time[0:2])
                time_sum = min*60
            else:
                min = int(time[0:2])
                second = int(time[3:5]) 
                min_second = min*60 #분->초 변환
                time_sum = min_second + second
        elif '초' in time:
            second = int(time[0:2])
            time_sum = second
        else:
            print("삐빅 숫자 형식이 맞지 않습니다. 시스템을 종료합니다.")
            

        #카운트다운
        while time_sum > -1:
            print(f'출발하기 {time_sum}초 전')
            time_sum = time_sum - 1
            print("이륙!!")
            

    #대답이 N일경우    
    elif ask == 'N':
        print("프로젝트를 종료합니다.")
        break;
    #예외
    else:
        print("형식이 맞지않습니다. 프로젝트를 종료합니다.")
        break;
