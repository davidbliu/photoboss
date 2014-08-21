# PhotoBoss
PBL's own photo manager

# Overview

# Design Plan

technology choices:
amazon s3


Three stages: 
1. sync local filesystem with amazon s3
2. web application for filtering images (chairs do this)
3. sync amazon filtered results with facebook/wordpress/whatever



# Getting Started

# Motivation/Benefits of Reorganization
*remove facebook dependency
* facebook is autocreated from our filesystem
* back up in two places: imgur and facebook
* main data store in s3
* never change
	* facebook api and imgur api probably change errday (jk but often enough for concern)
* why imgur?
	* its an intermediate layer between filesystem and facebook
	* indirection
	* one example where this is good: chairs can scrub through images and final-filter. 
		* perhaps peer filtering
		* __idea:__ _ALL_ images stored on imgur and a subset of the better ones on facebook