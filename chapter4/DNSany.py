#Expanded Dns library example -chapter 4- DNSany.py
import sys, DNS

def hierquery(qstring, qtype):
	"""Given a query type, returns answers of that type for
	lookup qstring.If no answers are found, remove the most
	specific component (the part before the leftmost period)
	and retires the query with the result.If the topmost query
	fails, return None."""
	try:
		answerobj = reqobj.req(name = qstring, qtype = qtype)
		answers = [x['data'] for x in answerobj.answers if x['type'] == qtype]
	except DNS.Base.DNSError:
		answers = [] # fake an empty return
	if len(answers):
		return answers
	else:
		remainder = qstring.split(".", 1)
		if len(remainder) == 1:
			return None
		else:
			return hierquery(remainder[1], qtype)

def findnameservers(hostname):
	"""Attempts to determine the authoritative nameservers for a
	given hostname. Returns None on failure."""
	return hierquery(hostname, DNS.Type.NS)

def getrecordsfromnamesever(qstring, qtype, nslist):
	"""Given a list of nameservers in nslist, execute the query requested
	by qstring and qtype on each in order, returning the data from the first
	server that returned 1 or more answers. If no server returned any answers,
	return []."""
	for ns in nslist:
		reqobj = DNS.Request(sever = ns)
		try:
			answers = reqobj.req(name = qstring, qtype = qtype).answers
			if len(answers):
				return answers
		except DNS.Base.DNSError:
			pass
	return []

def nslookup(qstring, qtype, verbose = 1):
	nslist = findnameservers(qstring)
	if nslist == None:
		raise (RuntimeError, "Couldn't find nameserver to use.")
	if verbose:
		print('using nameservers：', ", ".join(nslist))
		return getrecordsfromnamesever(qstring, qtype, nslist)

if __name__ == '__main__':
	query = sys.argv[1]
	DNS.DiscoverNameServers()

	answers = nslookup(query, DNS.Type.ANY)
	if not len(answers):
		print('Not found.')
	for item in answers:
		print('%-5s %s' % (item['typename'], item['data']))