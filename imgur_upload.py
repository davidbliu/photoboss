import os
import yaml

#
# load variables from config file
#
data = yaml.load(open('config.yaml', 'r'))
LOCAL_PHOTO_PATH = data['local_photo_path']
IMGUR_CLIENT_ID = data['imgur_client_id']
IMGUR_CLIENT_SECRET = data['imgur_client_secret']


"""
UPLOAD images from local filesystem onto PBL's imgur account
	- track image dumps on ht portfolio
TODO
	- back up images on s3
"""
def upload_images(image_dir):
	print 'uploading images to imgur...'
	print '\tclient id '+IMGUR_CLIENT_ID
	print '\tclient secret '+IMGUR_CLIENT_SECRET

	# get all files on local filesystem

	# create albums in imgur based on directory structure

	# upload images. change local filesystem for restart? (transfer/transferred)



if __name__ == '__main__':
	print 'syncing local filesystem with PBL photo archives...'
	upload_images(LOCAL_PHOTO_PATH)

