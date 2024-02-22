
question = ['are', 'you','awake','for','this']
answer = question
answer[0] = answer[3]
answer[1] = answer[4]
answer[4] = answer[2]
answer[2]= 'I'
answer[3] = 'am'
print(answer)
