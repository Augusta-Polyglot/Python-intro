import sys,os,urllib,re,json

class HoneyPot_Analysis():
	def __init__(self, logFile):		
		self.Signatures=self.GetSignatures()
		self.Events=open(logFile,'r')
		self.Attacks=[]
		self.NewRequests=[]
	def GetSignatures(self):
		return {r'^/xmlrpc.php$':{'IsAttack':True,'Type':'DDOS','SubType':'Proxy','Details':'WordPress XML-RPC Pingback DDoS attack'},
			    r'^/CFIDE/administrator/$':{'IsAttack':True,'Type':'Directory Traversal','SubType':'Remote Shell','Details':'ColdFusion Remote File Disclosure of Password Hashes'},
			    r'^/HNAP1/$':{'IsAttack':True,'Type':'Router Exploitation','SubType':'Remote','Details':'Eplotaion of D-Link Home Network Administration Protocol'},
			    r'^/user/soapCaller.bs$':{'IsAttack':True,'Type':'Multiple','SubType':'Reconnaissance','Details':'Detection of Drupal Content Management System'},
			    r'/setup.php$':{'IsAttack':True,'Type':'Remote Code Injection','SubType':'None','Details':'phpMyAdmin Code Injection Vulnerability'},
				r'^/index.html$':{'IsAttack':False},
				r'^/robots.txt$':{'IsAttack':False}}
	def GetLocation(self,ip):
		data = json.loads(urllib.urlopen('http://freegeoip.net/json/%s'%(ip)).read())
		return {'Country':'Unknown' if data['country_name']=='' else data['country_name'],
				'City':'Unknown' if data['city']=='' else data['city'],
				'Lat':'Unknown' if data['latitude']=='' else data['latitude'],
				'Long':'Unknown' if data['longitude']=='' else data['longitude']}
	def SetAttack(self,data,attackData):
		location=self.GetLocation(data[4])
		attack=Attack()
		attack.Date=re.search(r'\d\d/\w{3}/\d{4}',data[1]).group()
		attack.Time=re.search(r'(\d\d:\d\d:\d\d)(\s)',data[1]).group(1)
		attack.IP=data[4]
		attack.AttackType=attackData['Type']
		attack.SubType=attackData['SubType']
		attack.AttackDetails=attackData['Details']
		attack.City=location['City']
		attack.Country=location['Country']
		attack.Latitude=location['Lat']
		attack.Longitude=location['Long']
		return attack
	def ANALYSIS_Attack(self,request):
		return next((self.Signatures[regex] for regex in self.Signatures if re.search(regex,request)), None)
	def SCAN(self):
		for event in self.Events:
			data=event.split('\t')
			attackData=self.ANALYSIS_Attack(data[10])
			if attackData==None:
				self.NewRequests.append(data[10])
			elif attackData['IsAttack']:
				self.Attacks.append(self.SetAttack(data,attackData))
	def SUMMARY(self):
		for attack in self.Attacks:
			print '-'*70
			print 'Attack: \t%s'%(attack.AttackDetails)
			print 'Type: \t\t%s'%(attack.AttackType)
			print 'Sub-Type: \t%s'%(attack.SubType)
			print 'IP: \t\t%s'%(attack.IP)
			print 'City: \t\t%s'%(attack.City)
			print 'Country: \t%s'%(attack.Country)
			print 'Lat/Long: \t%s/%s'%(attack.Latitude,attack.Longitude)
		print '-'*70
		print '\n'*2
		print '!!!    %i New Requests Found    !!!\n'%(len(self.NewRequests))
		for request in set(self.NewRequests):
			print request.replace('\n','')
class Attack():
	def __init__(self):
		self.Date=''
		self.Time=''
		self.IP=''
		self.AttackType=''
		self.SubType=''
		self.AttackDetails=''
		self.City=''
		self.Country=''
		self.Latitude=''
		self.Longitude=''

if __name__=="__main__":
	if len(sys.argv)>1:
		if os.path.isfile(sys.argv[1]):
			print "Honeypot Log Analysis"
			H_A=HoneyPot_Analysis(sys.argv[1])
			H_A.SCAN()
			H_A.SUMMARY()
		else:
			print 'Could Not Find File Specified'
	else:
		print 'PY_Log_Parser Requires path to log file'
		print 'Ex: python PY_Log_Parser.py Log.txt'