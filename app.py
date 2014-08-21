import argparse
import atexit
import sys
import urlparse
import yaml
from flask import Flask, request, jsonify, render_template
import urllib2
import socket
import os
import shutil
import subprocess
import json
import ast


import facebook_manager
data = yaml.load(open('config.yaml', 'r'))
LOCAL_PHOTO_PATH = data['local_photo_path']
FACEBOOK_ID = data['facebook_app_id']
FACEBOOK_SECRET = data['facebook_app_secret']


app = Flask(__name__)

@app.route('/callback', methods=['GET', 'POST']) 
def fb_callback():
    print 'callback engaged'
    fb_response = request.form.get('fb_response')
    oauth_token = request.args['oauth_token']
    print oauth_token
    #
    # sync local filesystem
    #
    print 'syncing local filesystem...'
    facebook_manager.sync_local_filesystem(oauth_token, 'asdf')
    return jsonify('done good good')


@app.route('/', methods=['GET', 'POST'])
def root():
    print 'rendering auth page...'
    return render_template('fb_auth.html', facebook_app_id = FACEBOOK_ID)

if __name__ == '__main__':
    print 'hi my name is david'

    # host = socket.gethostbyname(socket.gethostname())
    host='localhost'

    print 'running your app'
    app.run(port=5000, host=host)