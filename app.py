from flask import Flask, redirect, url_for, request, render_template
import hashlib 
from difflib import SequenceMatcher
app = Flask(__name__)
 
 

 
 
@app.route('/hash_file', methods=['POST', 'GET'])
def hash_file(fileName1, fileName2):
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    with open(fileName1, "rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h1.update(chunk)

    with open(fileName2, "rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h2.update(chunk)

    return h1.hexdigest(),h2.hexdigest()
    
def compare(file1,file2):
    if request.method == "POST":
       # getting input with name = fname in HTML form
       firstname = request.form.get("file1")
       # getting input with name = lname in HTML form
       lastname = request.form.get("file2")
    
    msg1,msg2 = hash_file("file1","file2")
    print(msg1+"\t"+msg2)
    print((SequenceMatcher(None,msg1,msg2).ratio())*100)


    return render_template("app.html")
    
    
 
 
if __name__ == '__main__':
    app.run(debug=True)