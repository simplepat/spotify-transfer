import spotipy
import os

mp3_library_root_path = ''
output_file_name = ''

not_found = []
found = []

sp = spotipy.Spotify()

output = open(output_file_name, 'w')

for folder, subs, files in os.walk(unicode(mp3_library_root_path, 'utf-8')):
    for f in [f for f in files if f.endswith('.mp3')]:
		fn = f[:-4]

		if 'ft.' in fn:
			artist = fn.split(' ft. ')[0]
		elif 'feat.' in fn:
			artist = fn.split(' feat. ')[0]
		else:
			artist = fn.split(' - ')[0]

		if artist[:4] == 'The ':
			artist = artist[4:]
			
		artist.replace(' ', '+')
		title = fn.split(' - ')[1]
		title.replace(' ', '+')

		print artist, ' - ', title
		results = sp.search(q=title, type='track', limit='20')

		# limit in search: 10
		#j = 0
		#res_tracks = []
		#while not res_tracks and j <= 10:
		#    res_tracks = [i for i in results['tracks']['items'] if artist in i['artists'][j]['name']]
		#    j += 1

		res_size = len(results['tracks']['items'])

		fnd = False
		for i in results['tracks']['items']:
			if artist in i['artists'][0]['name']:
				print i['uri']
				output.write(i['uri'] + '\n')
				found.append(artist+' '+title)
				fnd = True
				break
			else:
				continue

		if not fnd:
			print 'Not found'
			not_found.append(artist+' '+title)

		#if res_tracks:
		#    print res_tracks[0]['uri']
		#    output.write(res_tracks[0]['uri'] + '\n')
		#    found.append(artist+' '+title)
		#else:
		#    print 'Not found'
		#    not_found.append(artist+' '+title)

output.close()
print 'Job done ! Found %i tracks over %i' %(len(found), len(found)+len(not_found))
