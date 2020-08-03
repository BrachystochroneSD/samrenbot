from flask import Flask, request, Response

follower_file = open('follow_alert.txt', 'w')
app = Flask(__name__)

@app.route('/TwitchAlert', methods=['GET','POST'])
def respond():
    if request.method == 'GET':
        hubchall = request.args.get('hub.challenge')
        return Response(response=hubchall, status=200, content_type="text/plain")
    elif request.method == 'POST':
        data = request.get_json(force=True)
        new_follow = data['data'][0]['from_name']
        print(new_follow, end="", file=follower_file)
        return Response(status=200)
