from flask import Flask
 
app = Flask(__name__)

@app.route('/')

def hello_world():
 prefix_google = """
 <!-- Google tag (gtag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=G-QLDTKG8PY4"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', 'G-QLDTKG8PY4');
</script>
 """
 return prefix_google + "Hello World"



@app.route('/')
def root():
    return 'Hello, World!'
 
#if __name__ == '__main__':
    #app.run()



