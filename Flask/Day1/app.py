from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def test():
    users = [
        {"username" : "traveler","name": "Alex"},
        {"username" : "photographer","name" : "Sam"},
        {"username" : "gourmet","name" : "Chris"}
        ]
    
    return render_template('day1.html',users=users)

if __name__ == "__main__":
    app.run(debug=True)
