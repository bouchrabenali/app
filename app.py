def hello_world():
 prefix_google = """
 <!-- Google tag (gtag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=G-QJR28CP9SP"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', 'G-QJR28CP9SP');
</script>
 """
 return prefix_google + "Hello World"



 
from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello, World!'
 
if __name__ == '__main__':
    app.run()



