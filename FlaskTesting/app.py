from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

CharName = ""
history = "You stand at the edge of a vast desert. \n \nSandstorms whirl like miniature tornadoes. \n \n" + \
    	"Inside you see massive, monstrous shapes moving about. \n \n A withered hag waddles out in front of you \n \n"+ \
    	"EHEHEHEEEE, what is your name small boy???"

def hagFirst():
	toSay = CharName+", eh?? Well, " + CharName +", I hope you're not thinking of exploring... \nThe desert!! \n" + \
			"EHEHEHEHE many people more couragous and attractive than you have tried... \nAnd failed!!" + \
			"What makes you think you have what it takes " + CharName + "?? \nIf that is your real name??"
	return toSay

def hagSecond():
	toSay = "Well I guess you do have what it takes. \nGo away you win this time "+ CharName
	return toSay

def addToHist(string):
	global history
	history = history + "\n\n" + string

@app.route('/')
def start():
    return render_template('nameAsk.html')

@app.route('/', methods=['POST'])
def get_name():
    text = request.form['text']
    global CharName
    CharName = text
    if "jarek" in CharName.lower():
    	addToHist(">"+CharName)
    	return redirect(url_for('start_input'))
    else:
    	return "You are ripped apart by the hag"

@app.route('/input')
def start_input():
	addToHist(hagFirst())
	return render_template('input.html', response = history.split('\n'))

@app.route('/input', methods=['POST'])
def get_input():
    text = request.form['text']
    addToHist(">"+text)
    addToHist(hagSecond())
    return render_template('input.html', response = history.split('\n'))

if __name__ == '__main__':
   app.run(debug = True)