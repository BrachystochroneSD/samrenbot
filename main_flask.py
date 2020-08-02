from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/TwitchAlert', methods=['GET','POST'])
def respond():
    if request.method == 'GET':
        hubchall = request.args.get('hub.challenge')
        return Response(response=hubchall, status=200, content_type="text/plain")
    elif request.method == 'POST':
        data = request.get_json(force=True)
        print(data['data'][0]['from_name'])
        return Response(status=200)
