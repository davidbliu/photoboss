import os
import yaml

# facebook imports
import facebook
from facepy import utils
#
# load variables from config file
#
data = yaml.load(open('config.yaml', 'r'))
LOCAL_PHOTO_PATH = data['local_photo_path']
FACEBOOK_ID = data['facebook_app_id']
FACEBOOK_SECRET = data['facebook_app_secret']


"""
UPLOAD images from local filesystem onto PBL's imgur account
	- track image dumps on ht portfolio
TODO
	- back up images on s3
"""
def upload_images(oauth_access_token, image_dir):
	print 'uploading images to facebook...'

	graph = facebook.GraphAPI(oauth_access_token)
	print graph
	print graph.__dict__
	profile = graph.get_object("me")
	# friends = graph.get_connections("me", "friends")
	# graph.put_object("me", "feed", message="I am writing on my wall!")
	# get all files on local filesystem

	# create albums in imgur based on directory structure

	# upload images. change local filesystem for restart? (transfer/transferred)


def sync_local_filesystem(oauth_access_token, image_dir):
	print 'syncing local filesystem'
	graph = facebook.GraphAPI(oauth_access_token)
	profile = graph.get_object('me')
	print graph
	print profile

def upload_local_image(oauth_access_token, image_path):
	print 'uploading local image...'

def get_fb_access_token():
	
	app_id = FACEBOOK_ID # must be integer
	app_secret = FACEBOOK_SECRET 
	oath_access_token = utils.get_application_access_token(app_id, app_secret)
	print 'this is your access token:'
	print '\t'+ str(oath_access_token)
	return oath_access_token

if __name__ == '__main__':
	print 'syncing local filesystem with PBL photo archives...'
	# upload_images(LOCAL_PHOTO_PATH)
	# token = get_fb_access_token()
	# upload_images(token, 'asdf')

	token = 'CAAKkkP6DGKcBAICCRcNqnuiO6XgV8ILrG9CDqW0F8bWGVAHaZAjXuredb5sAVZCudxTTiG3FAZCdcUPEuszOcZB5rsdpghZAaTTuHnAN7oYUu9auiZBm6qsSzRQFxCHJKJLSiMG5U1nKf3jT9mn6FXc0lRcQVEfKMDaliiYOrKKNhhZAcu83sHoywShX5fMeZCZBSR74psqTZA7VETD6dakUUb'
	sample_image_path = '/home/david/Desktop/theseus.jpg'
	sync_local_filesystem(token, 'asdf')