import requests
import urllib.parse as up

def download_file(url):
	local_filename = 'download.mp4'
	r = requests.get(url, stream=True)
	with open(local_filename, 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024):
			if chunk:
				f.write(chunk)
	return (local_filename)

link = 'xk0h_DkEyYE'
a = requests.get('http://youtube.com/get_video_info?video_id='+link)
parsed = up.parse_qs(a.text)
if (parsed['status'] == ['fail']):
    print("Can't Download Video")
    print(parsed['reason'][0])
else:
	parsed =  parsed['url_encoded_fmt_stream_map']
	new = str(parsed).split(',')
	#for i in new:  See all the video quality available
	#		print (i)
	#		print ("\n")

	ed = up.parse_qs(new[0]) #create dictionary of the given URL
	#print (ed)

	for i in ed: #get all dictionary elements
		if 'url' in i:
			download_file (ed[i][0]) #in multidimensional list get first that is link url

