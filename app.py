from flask import Flask, render_template, request

form_site = Flask(__name__)

@form_site.route("/", methods=['POST', 'GET'])
def root():
    print request
    print request.method
    print request.headers
#    print request.args
    print request.form
    return render_template('temp.html')

if __name__ == '__main__':
    form_site.debug = True
    form_site.run()
    
