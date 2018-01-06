import requests
import urlparse

def download_file(url):
	local_filename = 'download.mp4'
	r = requests.get(url, stream=True)
	with open(local_filename, 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024):
			if chunk:
				f.write(chunk)
	return (local_filename)

a = requests.get('http://youtube.com/get_video_info?video_id=hS5CfP8n_js')
parsed = urlparse.parse_qs(a.text)
parsed =  parsed['url_encoded_fmt_stream_map']
new = str(parsed).split(',')
#for i in new:  See all the video quality available
#		print (i)
#		print ("\n")

ed = urlparse.parse_qs(new[0]) #create dictionary of the given URL
#print (ed)
for i in ed: #get all dictionary elements
	if 'url' in i:
		download_file (ed[i][0])

