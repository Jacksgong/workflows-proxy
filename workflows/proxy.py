__author__ = 'jacksgong'

import sys
import os
from workflow import Workflow, ICON_WEB, web

def main(wf):

	params = wf.args[0]

	echo_qq = 'http://txp-01.tencent.com/proxy.pac'
	echo_off = 'off'
	echo_pre = 'networksetup -setautoproxyurl Wi-Fi ' 
	echo_diy_pre = 'http://192.168.'
	echo_diy_end = ':2516'

	if params.startswith('q') :
		wf.add_item(echo_qq,'switch to Tencent proxy',arg =echo_qq,uid=0,valid=True, icon = './qq-proxy.png')
	elif params.startswith('o') : 
		wf.add_item(echo_off,'off wifi proxy',arg = echo_off, uid = 0, valid= True, icon = './off.png')
	elif params.startswith('s') :
		status  = os.popen('networksetup -getautoproxyurl wi-fi').read()
		statusList = status.splitlines()
		ip = statusList[0]
		enable = statusList[1]
			
		wf.add_item(ip,enable, arg =('current status: '+ status),uid = 0) 
	else:
		diy = echo_diy_pre + params + echo_diy_end
		wf.add_item(diy,'switch to ' + diy + ' proxy', arg =diy, uid = 0, valid = True, icon = './others-proxy.png')
	

	wf.send_feedback()

if __name__ == '__main__':
	wf = Workflow()
	sys.exit(wf.run(main))
