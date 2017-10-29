import turtle as t
import random

t.shape("turtle")                       #turtle 모양 나타남
t.color("green")                        #초록색으로 그리기
t.pensize(3)                            #펜사이즈는 3
t.speed(0)                              #스피드는 제일 빠르게
t.up()
t.goto(-250,-250)                       #네모난 틀 만들기
t.down()
t.goto(250,-250)
t.goto(250,250)
t.goto(-250,250)
t.goto(-250,-250)
t.up()

t.goto(0,0)

t.lt(random.randint(0,180))             #각도는 랜덤하게 돌려준다


while True:                             #트루일때까지 무한반복
    t.fd(5)                             #5씩 앞으로 간다
    x=t.xcor()                          #x좌표를 나타내준다.
    y=t.ycor()                          #y좌표를 나타내준다.
    
    a=t.heading()                       #지금 바라보는 각도를 a로 지정해다.
    
    if x>250:                           #오른쪽 벽에 거북이가 맞는다면
        if a<90:                        #90도보다 작은 각도로 맞는다면
            t.lt(180-2*a)
        else:                           #그렇지 않다면
            t.rt(180+2*a)

    if x<-250:                          #왼쪽 벽에 거북이가 맞는다면
        if a<180:                       #180도보다 작은 각도로 맞는다면
            t.rt(2*a-180)
        else:                           #그렇지 않다면
            t.lt(180-2*a)

    if y>250:                           #위쪽 벽에 거북이가 맞는다면
        if a<90:                        #90도보다 작은 각도로 맞는다면
            t.rt(2*a)
        else:                           #그렇지 않다면
            t.lt(-2*a)
        
    if y<-250:                          #아래쪽 벽에 거북이가 맞는다면
        if a>270:                       #270도보다 큰 각도로 맞는다면
            t.lt(720-2*a)
        else:                           #그렇지 않다면
            t.rt(720+2*a)


    
        
