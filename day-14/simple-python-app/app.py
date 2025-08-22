from flask import Flask

#build app new1, update pipeline role policy
#still did not work

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()



