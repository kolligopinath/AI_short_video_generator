from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from AI_short_video_generator.AI_short_video_generator import generate_video

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    text_input = ''
    if request.method == 'POST':
        text_input = request.form['input_text']
        # You can process the text_input here as needed
    return render_template('index.html', input_text=text_input)


@app.route('/process', methods=['POST'])
def process():
    text_input = request.form['input_text']
    video_dir = ''
    # "Mother and Childs Colorful Tale.mp4"
    video_file = generate_video(text_input)
    return send_from_directory(video_dir, video_file, as_attachment=True, mimetype='video/mp4')


if __name__ == '__main__':
    app.run(debug=True)
