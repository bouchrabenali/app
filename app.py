from flask import Flask
from flask import render_template, request, Response
import requests 
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
from io import BytesIO
app= Flask(__name__,template_folder = 'templateTP')

 
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



@app.route('/logger')
def logger():
    # Log message in Python (server-side)
    app.logger.info("This is a log message in Python")

    # Log message for the browser (client-side)
    browser_log = """
    <script>
        console.log('This is a browser log message');
    </script>
    """
    
    return "Logger Page" + browser_log
 

@app.route('/textbox', methods=['GET', 'POST'])
def display_message():
    user_message = None  # Par défaut, le message est vide
    if request.method == 'POST':
        user_message = request.form.get('message', '')  # Récupère le message soumis par l'utilisateur

    return render_template('templateTP.html', user_message=user_message)

@app.route("/make_google_request", methods=["GET"])

def make_google_request():

    try:
        # Make a request to Google
        response = requests.get("https://www.google.com/") 
        # Check if the request was successful
        if response.status_code == 200:
            return response.cookies.get_dict()
        else:
            return "Google request failed with status code: " + str(response.status_code)
    except Exception as e:
        return "An error occurred: " + str(e)
    

@app.route("/make_google_request2", methods=["GET"])

def make_google_request2():

    try:
        # Make a request to Google
        response = requests.get("https://analytics.google.com/analytics/web/#/p408254187/reports/intelligenthome")
        # Check if the request was successful
        if response.status_code == 200:
            return response.cookies.get_dict()
        else:
            return "Google request failed with status code: " + str(response.status_code)
    except Exception as e:
        return "An error occurred: " + str(e)
    
@app.route('/google_analytics_report', methods=['GET', 'POST'])
def google_analytics_report():
    if request.method == 'POST':
        print('hello, POST method')
        try:
            req2 = requests.get("https://analytics.google.com/analytics/web/#/p408254187/reports/intelligenthome")
            status_code = req2.status_code
            response_text = req2.text

 

            return render_template('google_analytics_report.html', status_code=status_code, response_text=response_text)
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render_template('google_analytics_report.html', error_message=error_message)
    else:
        return render_template('google_analytics_report.html', status_code=None, response_text=None)
    
    
@app.route('/google_trends', methods=['GET'])
def google_trends():
    # Create a pytrends client
    pytrends = TrendReq(hl='fr-FR', tz=0, geo='FR') # geo='FR' is used to specify that the data is from France
   
    # Define your keywords and timeframe
    keywords = ['Football', 'rugby']
    timeframe = 'today 3-m'  # my time frame is the last 3 months
    # Get Google Trends data
    pytrends.build_payload(keywords, timeframe=timeframe)
    interest_over_time_df = pytrends.interest_over_time()
    data = interest_over_time_df.to_json(orient='split')
    return data


@app.route('/google_trends_chart', methods=['GET'])
def google_trends_chart():
    pytrends = TrendReq(hl='fr-FR', tz=0, geo='FR') # geo='FR' is used to specify that the data is from France
    keywords = ['Football', 'rugby']
    timeframe = 'today 3-m'
    pytrends.build_payload(keywords, timeframe=timeframe)
    interest_over_time_df = pytrends.interest_over_time()
    interest_over_time_df.to_csv('football-rugby.csv')
    # Generate a line chart
    plt.figure()
    interest_over_time_df.plot(title='Google Trends', legend=True)
    
    # Save the chart as an image in memory
    chart_image = BytesIO()
    plt.savefig(chart_image, format='png')
    chart_image.seek(0)

    return Response(chart_image, content_type='image/png')



    

if __name__ == '__main__':
    app.run(debug=True)


url = "https://analytics.google.com/analytics/web/#/p408254187/reports/intelligenthome"
# Effectuer une requête GET
response = requests.get(url)
# Extraire le statut de la réponse et le contenu de la réponse
status_code = response.status_code
response_text = response.text
# Afficher le statut de la réponse et le contenu de la réponse
print(f"Status Code: {status_code}")
print(f"Response Text: {response_text}")





