from flask import Flask, render_template, request
import re
import linkGrabber
import ast


app = Flask(__name__,
            template_folder="template")

# Heyyy People, Hello World!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

@app.route('/')
def customer():
    return render_template('web.html')
a=[]

@app.route('/success', methods=['POST'])
def print_data():
    if request.method == 'POST':
        result = request.form
        # print(result)
        links = linkGrabber.Links(result['url'])
        gb = links.find('href', 'text', pretty=False)
        # gb= ast.literal_eval(str(gb))
        # print(type( gb))
        newlist= []
        for v in gb:
            newlist.append({"href":v["href"],"text":v["text"]})
        print(newlist)
        return render_template("result.html", result=result,gb=newlist)


if __name__ == '__main__':
    app.run(debug=True)
