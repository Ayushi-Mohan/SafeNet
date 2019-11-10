import platform
import socket
import os

def blockSites(urls, b, ec, e, g, il, m, n, s):
	'''Needs to be run when user logs in.'''

	OS = platform.system()

	host_file = None

	if OS == 'Windows':
		host_file = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
	elif OS == 'Darwin':
		host_file = 'etc/hosts'
	else:
		host_file = '/etc/hosts'

	block = []
	redirect = {}
	for i in range(8):
		if urls[i] == 'TRUE':
			if i == 0:
				for j in range(len(b)):
					block.append(b[j].url)
			elif i == 1:
				for j in range(len(ec)):
					block.append(ec[j].url)
			elif i == 2:
				for j in range(len(e)):
					block.append(e[j].url)
			elif i == 3:
				for j in range(len(g)):
					block.append(g[j].url)
			elif i == 4:
				for j in range(len(il)):
					block.append(il[j].url)
			elif i == 5:
				for j in range(len(m)):
					block.append(m[j].url)
			elif i == 6:
				for j in range(len(n)):
					block.append(n[j].url)
			else:
				for j in range(len(s)):
					block.append(s[j].url)
		elif urls[i] == 'NULL':
			pass
		else:
			ip = socket.gethostbyname(urls[i])
			if i == 0:
				for j in range(len(b)):
					redirect[b[j]] = ip
			elif i == 1:
				for j in range(len(ec)):
					redirect[ec[j]] = ip
			elif i == 2:
				for j in range(len(e)):
					redirect[e[j]] = ip
			elif i == 3:
				for j in range(len(g)):
					redirect[g[j]] = ip
			elif i == 4:
				for j in range(len(il)):
					redirect[il[j]] = ip
			elif i == 5:
				for j in range(len(m)):
					redirect[m[j]] = ip
			elif i == 6:
				for j in range(len(n)):
					redirect[n[j]] = ip
			else:
				for j in range(len(s)):
					redirect[s[j]] = ip
	for i in range(8, len(urls) - 1, 2):
		if urls[i + 1] == 'NULL':
			block.append(urls[i])
		else:
			ip = socket.gethostbyname(urls[i + 1])
			redirect[urls[i]] = ip

	with open(host_file, 'rt') as file:
		content = file.read()
		with open('/tmp/etc_hosts.tmp', 'wt') as outf:
			outf.write(content)
			for website in block:
				if website in content:
					pass
				else:
					outf.write('\n127.0.0.1 ' + website)
			for website, ip in redirect.items():
				outf.write('\n' + ip + ' ' + website)

	os.system('sudo /home/murali/pymvh.sh')

def unblockSites(urls):
	'''Needs to be run when the user logs out.'''

	OS = platform.system()

	host_file = None

	if OS == 'Windows':
		host_file = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
	elif OS == 'Darwin':
		host_file = 'etc/hosts'
	else:
		host_file = '/etc/hosts'

	with open(host_file, 'r+') as file:
		content = file.readlines()
		file.seek(0)
		for line in content:
			if not any(website in line for website in urls):
				file.write(line)
			file.truncate()

def updateBlockedSites(old_urls, new_urls, b, ec, e, g, il, m, n, s):
	'''Needs to be run when user hits "Submit" on checkbox page.'''
	if old_urls:
		unblockSites(old_urls)
	blockSites(new_urls, b, ec, e, g, il, m, n, s)