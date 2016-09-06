import time
import webbrowser

default_url = "https://www.youtube.com/watch?v=0R1Nf4MS9hM"

print "Hello World !"
print "It's an exciting day, isn't it ?."
print "How many sessions do you plan to work today  :"
sessions = int(raw_input())
sess_no =1
while(sess_no<=sessions):
	print "Session " + str(sess_no) + "  began at " + time.ctime()
	print "Do you want to add your custom URL or use : \n" + default_url + "\n" + "Answer with a Y/N"
	if raw_input() ==  "Y":
		print "Insert your URL here  : "
		default_url = raw_input()

	print "How long do you want each session to be : (in hours)"
	limit = float(raw_input())
	limit*=3600
	time.sleep(limit)
	webbrowser.open(default_url)
	sess_no+=1
print "Hope you achieved your goal, Keep up the good work"