from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    posts = [
        {'Id': '0000001',
     
        'GroupId': '9999999',
        
        'Name': 'my name is Bora',
        
        'Data': 'YYYY,MM,DD HH,MM,SS',
        
        'User': 'nickname',
        
        'Type': ('String', 'String', 'post'),
                        
        'Content': ('first content block', 'sekond any content', 'id0000002')
                   
        }
    ]
    return render_template("index.html",
        title = 'index',        
        posts = posts)
