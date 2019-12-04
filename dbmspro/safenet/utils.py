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
					redirect[b[j].url] = ip
			elif i == 1:
				for j in range(len(ec)):
					redirect[ec[j].url] = ip
			elif i == 2:
				for j in range(len(e)):
					redirect[e[j].url] = ip
			elif i == 3:
				for j in range(len(g)):
					redirect[g[j].url] = ip
			elif i == 4:
				for j in range(len(il)):
					redirect[il[j].url] = ip
			elif i == 5:
				for j in range(len(m)):
					redirect[m[j].url] = ip
			elif i == 6:
				for j in range(len(n)):
					redirect[n[j].url] = ip
			else:
				for j in range(len(s)):
					redirect[s[j].url] = ip
	for i in range(8, len(urls) - 1, 2):
		if urls[i] != 'NULL':
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
				outf.write('\n' + str(ip) + ' ' + website)

	if OS == 'Windows':
		pass
	elif OS == 'Darwin':
		os.system('sudo mv /tmp/etc_hosts.tmp etc/hosts')
	else:
		os.system('sudo mv /tmp/etc_hosts.tmp /etc/hosts')

def unblockSites():
	'''Needs to be run when the user logs out.'''

	OS = platform.system()

	host_file = None
	copy_file = None

	os.system('sudo cp ../etc_hosts /etc/hosts')


def updateBlockedSites(new_urls, b, ec, e, g, il, m, n, s):
	'''Needs to be run when user hits "Submit" on checkbox page.'''
	unblockSites()
	blockSites(new_urls, b, ec, e, g, il, m, n, s)
