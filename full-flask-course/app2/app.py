from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("likes", type=int, help="Likes of the video", required=True)
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)

videos = {}

def aborter_if_vid_doesnt_exist(video_id):
    if video_id not in videos: 
        abort(404, 'video does not exist')

class Video(Resource):
    def get(self, video_id):
        aborter_if_vid_doesnt_exist(video_id)
        return videos[video_id]
    
    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201


api.add_resource(Video, '/video/<string:video_id>')
                                                                                      

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='127.0.0.1')    