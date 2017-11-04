#!/usr/bin/env python 3.1
from __future__ import print_function
import subprocess
import os
import datetime
import time
import csv
import fileinput
import commands
import re
from datetime import date, timedelta
def whiteinfine():
        cycle_file_w=open('/opt/JOBAlert_New/utk/files/cyc.txt', "w")
        return_code = subprocess.call("ps x |grep -v grep| grep -e /bin/.*sh   | awk '{print $6,$7,$8,$9}' > /tmp/tt  && sed -e 's/^/nohup /g' -e 's/$/\&/g'  /tmp/tt", shell=True, stdout=cycle_file_w)
        if os.stat("/opt/JOBAlert_New/utk/files/cycle.txt").st_size==0:
               cycle_file_write=open('/opt/JOBAlert_New/utk/files/cycle.txt', "w")
               cycle_file_write.write("null \n")
               cycle_file_write.close()
        cycle_file_r=open('/opt/JOBAlert_New/utk/files/cyc.txt', "r")
        for i, lines in enumerate(cycle_file_r.readlines()):
                cycle_file_read=open('/opt/JOBAlert_New/utk/files/cycle.txt', "r")
                for liness in cycle_file_read.readlines():
                        if lines == liness:
                                flagee=1
                                break
                        else:
                                flagee=0
                if flagee == 0:
                        cycle_file_append = open('/opt/JOBAlert_New/utk/files/cycle.txt', "a")
                        cycle_file_append.write(lines)
####################################
	log_file_w=open('/opt/JOBAlert_New/utk/files/logfile', "w")
	log_file1 = subprocess.call("ps aux | grep java | grep -v 'grep'", shell=True, stdout=log_file_w)
	if os.stat("/opt/JOBAlert_New/utk/files/logfille").st_size==0:
		cycle_file_write=open('/opt/JOBAlert_New/utk/files/logfille', "w")
		cycle_file_write.write("null \n")
		cycle_file_write.close()
	log_file_r = open('/opt/JOBAlert_New/utk/files/logfile', "r")
	log_file_read = open('/opt/JOBAlert_New/utk/files/logfille', "r")
	for i, lines in enumerate(log_file_r.readlines()):
		prid=(lines.split()[1])
		scnam=(lines.split()[-1])
		for liness in log_file_read.readlines():
			if scnam in liness:
				flagel=1
	                	break
			else:
				flagel=0
		if flagel == 0:
			log_file_append = open('/opt/JOBAlert_New/utk/files/logfille', "a")
			log_file_append.write(lines)
		else:
			scnam=scnam.split('/')[-1]
			subprocess.call(["sed -i '/"+scnam+"/d' /opt/JOBAlert_New/utk/files/logfille"], shell=True)
			#proc.wait()
                        log_file_append = open('/opt/JOBAlert_New/utk/files/logfille', "a")
                        log_file_append.write(lines)
def processoncycle():
	logfile_for_process1='/opt/JOBAlert_New/utk/logs/logfileprocess'+time.strftime('%d%m%y')
	logfile_for_process=open(logfile_for_process1,"a")
        cycle_file_read=open('/opt/JOBAlert_New/utk/files/cycle.txt', "r")
        initlin={}
        datelog={}
        for  line in cycle_file_read.readlines():
                if line == 'null \n':
                        pass
                else:
                        myWords = [x for x in line.split()]
                        myWords = len(myWords)
                        if myWords==4 :
                                modfile=(line.split(' ')[2])
				if len(modfile)==1 or len(modfile)==2 or len(modfile)==3:
					modfile=(line.split('/')[-1])
					modfile=modfile.split('.sh')[0]
				else:
					modfile=modfile
                                script_name=(line.split(' ')[1])
                                log_file2=[]
                                log_file_r=open('/opt/JOBAlert_New/utk/files/logfille', "r")
                                for logline in log_file_r.readlines():
                                        if modfile in logline:
                                                log_file2=logline.split()
	                                        log_file3=log_file2[-1]
        	                                process_id=log_file2[1]
                	                        break
                        	        else:
                                	        pass
                                        	log_file3="utkarsh"
                                if os.path.isfile(log_file3) :
                                        modtime=os.path.getmtime(log_file3)
                                        logfile_open=open(log_file3, "r")
                                        initlin[modfile] = sum(1 for line in open(log_file3))
                                        initlin[modfile] = initlin[modfile] - 2
                                        datelog[modfile] = (line.split(' ')[4])
                                        previoustime = date.today() - timedelta(1)
                                        previoustime = previoustime.strftime('%d-%m-%Y')
                                        currentsystime = time.strftime('%d-%m-%Y')
                                        timedifferenc=time.time()-modtime
                                        timedifferenc=int(timedifferenc)
					if timedifferenc > 1020:
						pidp=commands.getoutput("tail -5 "+log_file3)
						if 'Process Completed Successfully' in pidp:
                                                        logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Process "+modfile+" completed sucessufully \n")
							filemoddate=time.strftime('%d-%m-%Y', time.gmtime(os.path.getmtime(log_file3)))
                                                        pidpp=commands.getoutput("tail -20 "+log_file3)
                                                       # subprocess.call(["/usr/local/bin/sendEmail -t utkarsh.srivastava@timesgroup.com -f utkarsh.srivastava@timesgroupe.com -l /var/log/sendEmail -u 'Process Completed' -m 'Hi Sir ,\n\n\nProcess  "+modfile+" completed \n\n This will restart for next shedule date, Please verify. \n\n\n\n "+pidpp+"\n\n\n\n Regards,\nUtkarsh Srivastava'"], shell=True)
							if filemoddate==currentsystime:
								pass
							else:
								if any(c in script_name for c in ("NoJobAlertMailer")):
									if (time.strftime('%H')=='09'):
										subprocess.call(['cd /opt/JOBAlert_New/;'+line], shell=True)
										subprocess.call(["sed -i '/"+modfile+"/d' /opt/JOBAlert_New/utk/files/logfille"], shell=True)
			                                                        logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Process  "+modfile+" Started\n")
										whiteinfine()
								elif any(c in script_name for c in ("NoStageMailer","UnsuccessOnLine","ActivationMailer")):
									if (time.strftime('%H')=='01'):
										subprocess.call(['cd /opt/JOBAlert_New/;'+line], shell=True)
										subprocess.call(["sed -i '/"+modfile+"/d' /opt/JOBAlert_New/utk/files/logfille"], shell=True)
                                                                                logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Process "+modfile+" Started\n")
										whiteinfine()
								elif any(c in script_name for c in ("JunkResumeMailer")):
									regx = re.compile('22:3.')
									if (time.strftime('%H:%M')==''.join(map(str, regx.findall(s)[0]))):
										subprocess.call(['cd /opt/JOBAlert_New/;'+line], shell=True)
                                                                                subprocess.call(["sed -i '/"+modfile+"/d' /opt/JOBAlert_New/utk/files/logfille"], shell=True)
                                                                                logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Process  "+modfile+" Started\n")
                                                                                whiteinfine()
								elif any(c in script_name for c in ("Stage7Registration")):
									if (time.strftime('%H')=='02'):
										subprocess.call(['cd /opt/JOBAlert_New/;'+line], shell=True)
                                                                                subprocess.call(["sed -i '/"+modfile+"/d' /opt/JOBAlert_New/utk/files/logfille"], shell=True)
                                                                                logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Process  "+modfile+" Started\n")
                                                                                whiteinfine()
								elif any(c in script_name for c in ("BirthDayWishMailer")):
									if (time.strftime('%H')=='06'):
										subprocess.call(['cd /opt/JOBAlert_New/;'+line], shell=True)
                                                                                subprocess.call(["sed -i '/"+modfile+"/d' /opt/JOBAlert_New/utk/files/logfille"], shell=True)
                                                                                logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Process  "+modfile+" Started\n")
                                                                                whiteinfine()
								else:
									subprocess.call(['cd /opt/JOBAlert_New/;'+line], shell=True)
	                                                                subprocess.call(["sed -i '/"+modfile+"/d' /opt/JOBAlert_New/utk/files/logfille"], shell=True)
        	                                                        whiteinfine()
                                                                        logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Process  "+modfile+" Started\n")
					    	else:    
                                                	logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Process  "+modfile+" Running\n")
						        #pidp=commands.getoutput("ps aux | grep "+modfile+" | grep -v 'grep' | awk '{print $2}'")
						        if process_id != '':
						            subprocess.call(['kill -9 '+process_id+'; kill -9 '+process_id], shell=True)
						        subprocess.call(['cd /opt/JOBAlert_New/;'+line], shell=True)
                                                        subprocess.call(["sed -i '/"+modfile+"/d' /opt/JOBAlert_New/utk/files/logfille"], shell=True)
                                                        pidpp=commands.getoutput("tail -30 "+log_file3)
                                                        subprocess.call(["/usr/local/bin/sendEmail -t utkarsh.srivastava@timesgroup.com -f utkarsh.srivastava@timesgroupe.com -l /var/log/sendEmail -u 'Error In Process' -m 'Hi Sir ,\n\n\nThere is error in "+line+"\n\n\n Process have restarted, please find error details \n\n\n\n "+pidpp+"\n\n\n\n Regards,\nUtkarsh Srivastava'"], shell=True)
                                                        logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Error in Process "+modfile+"\n")
                                                        whiteinfine()
					else:
						tm=time.strftime('%d-%m-%y %H:%M')
                                        	logfile_for_process.write(tm+" Process "+modfile+" log running\n")
                                else:
                                        pass

                        elif myWords==3 :
                                script_name=(line.split('/')[-1])
                                script_name=(script_name.split('.sh')[0])
                                log_file2=[]
                                log_file_r=open('/opt/JOBAlert_New/utk/files/logfille', "r")
                                for logline in log_file_r.readlines():
                                        if script_name in logline:
                                                log_file2=logline.split()
                                                log_file3=log_file2[-1]
                                                process_id=log_file2[1]
                                                break
                                        else:
                                                pass
                                                log_file3="utkarsh"
                                if os.path.isfile(log_file3) :
                                        modtime=os.path.getmtime(log_file3)
                                        currentsystime = time.strftime('%d-%m-%Y')
                                        logfile_open=open(log_file3, "r")
                                        initlin[script_name] = sum(1 for line in open(log_file3))
                                        initlin[script_name] = initlin[script_name] - 10
                                        previoustime = date.today() - timedelta(1)
                                        previoustime = previoustime.strftime('%d-%m-%Y')
                                        timedifferenc=time.time()-modtime
                                        timedifferenc=int(timedifferenc)
					if timedifferenc > 1020:
						pidp=commands.getoutput("tail -5 "+log_file3)
						if 'Process Completed Successfully' in pidp:
                                                        logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Process "+script_name+" Completed Sucessfully\n")
							filemoddate=time.strftime('%d-%m-%Y', time.gmtime(os.path.getmtime(log_file3)))
                                                        pidpp=commands.getoutput("tail -20 "+log_file3)
                                                        #subprocess.call(["/usr/local/bin/sendEmail -t utkarsh.srivastava@timesgroup.com -f utkarsh.srivastava@timesgroupe.com -l /var/log/sendEmail -u 'Process Completed' -m 'Hi Sir ,\n\n\nProcess "+script_name+" completed\n\n This will restart for next shedule date, Please verify. \n\n\n\n "+pidpp+"\n\n\n\n Regards,\nUtkarsh Srivastava'"], shell=True)
							if filemoddate==currentsystime:
								pass
							else:
								if any(c in script_name for c in ("AutoRefreshJobBatch","RssFeedCompanyBatch")):
									if (time.strftime('%H')=='01'):
										subprocess.call(['cd /opt/JOBAlert_New/;'+line], shell=True)
                                                                                subprocess.call(["sed -i '/"+script_name+"/d' /opt/JOBAlert_New/utk/files/logfille"], shell=True)
                                                                                logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Process "+script_name+" Started\n")
                                                                                whiteinfine()
								elif any(c in script_name for c in ("CorporateDashboardBatch")):
									if (time.strftime('%H')=='13' and time.strftime('%d')=='01'):
										subprocess.call(['cd /opt/JOBAlert_New/;'+line], shell=True)
                                                                             	sbprocess.call(["sed -i '/"+script_name+"/d' /opt/JOBAlert_New/utk/files/logfille"], shell=True)
                                                                                logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Process "+script_name+" Started\n")
                                                                                whiteinfine()
								else:
									subprocess.call(['cd /opt/JOBAlert_New/;'+line], shell=True)
        	                                                        subprocess.call(["sed -i '/"+script_name+"/d' /opt/JOBAlert_New/utk/files/logfille"], shell=True)
                                                                        logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Process "+script_name+" Started\n")
                	                                                whiteinfine()
						else:                    
                                                	logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Error in Process "+script_name+"\n")
							#pidp=commands.getoutput("ps aux | grep "+script_name+" | grep -v 'grep' | awk '{print $2}'")
							if process_id != '':
								subprocess.call(['kill -9 '+process_id+'; kill -9 '+process_id], shell=True)
							subprocess.call(['cd /opt/JOBAlert_New/;'+line], shell=True)
                                                        subprocess.call(["sed -i '/"+script_name+"/d' /opt/JOBAlert_New/utk/files/logfille"], shell=True)
                                                        pidpp=commands.getoutput("tail -30 "+log_file3)
                                                        subprocess.call(["/usr/local/bin/sendEmail -t utkarsh.srivastava@timesgroup.com -f utkarsh.srivastava@timesgroupe.com -l /var/log/sendEmail -u 'Error in Process' -m 'Hi Sir ,\n\n\nThere is error in "+line+"\n\n\n Process have restarted, please find error details \n\n\n\n "+pidpp+"\n\n\n\n Regards,\nUtkarsh Srivastava'"], shell=True)
                                                        logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+"Error in Process "+script_name+"\n")
                                                        whiteinfine()
					else:
                                        	logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Process "+script_name+" Running\n")
                                else:
                                        pass
                        elif myWords==5 :
                                modfile=(line.split(' ')[2])
                                script_name=(line.split(' ')[1])
				initlin={}
				datelog={}
				log_file2=[]
                                log_file_r=open('/opt/JOBAlert_New/utk/files/logfille', "r")
                                for logline in log_file_r.readlines():
                                	if modfile in logline:
                                        	log_file2=logline.split()
                                                log_file3=log_file2[-1]
                                                process_id=log_file2[1]
                                                break
                                        else:
                                                pass
                                                log_file3="utkarsh"
                                if os.path.isfile(log_file3):
                                        modtime=os.path.getmtime(log_file3)
                                        logfile_open=open(log_file3, "r")
                                        initlin[modfile] = sum(1 for line in open(log_file3))
                                        initlin[modfile] = initlin[modfile] - 10
                                        datelog[modfile] = (line.split(' ')[3])
                                        currentsystime = time.strftime('%d-%m-%Y')
                                        previoustime = date.today() - timedelta(1)
                                        previoustime = previoustime.strftime('%d-%m-%Y')
                                        timedifferenc=time.time()-modtime
                                        timedifferenc=int(timedifferenc)
					if timedifferenc > 1020:
						pidp=commands.getoutput("tail -5 "+log_file3)
						if 'Process Completed Successfully' in pidp:
                                                        logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Process "+modfile+" Completed\n")
                                                        pidpp=commands.getoutput("tail -20 "+log_file3)
                                                        #subprocess.call(["/usr/local/bin/sendEmail -t utkarsh.srivastava@timesgroup.com -f utkarsh.srivastava@timesgroupe.com -l /var/log/sendEmail -u 'Process Completed' -m 'Hi Sir ,\n\n\nProcess "+modfile+" completed for date "+datelog[modfile]+". This will restart for next shedule date, Please verify. \n\n\n\n "+pidpp+"\n\n\n\n Regards,\nUtkarsh Srivastava'"], shell=True)
							if currentsystime == datelog[modfile]:
								pass
							else:
								if any(c in modfile for c in ("Reminder","CVStage1","PlatinumCandDaily","PlatinumCandWeekly")):
									if int(time.strftime('%H')) in range(01, 23):
										subprocess.call(["sed -i '/"+modfile+"/d' /opt/JOBAlert_New/utk/files/cycle.txt"], shell=True)
                                                                                subprocess.call(["sed -i '/"+modfile+"/d' /opt/JOBAlert_New/utk/files/logfille"], shell=True)
										subprocess.call(['cd /opt/JOBAlert_New/; nohup '+script_name+' '+modfile+' '+currentsystime+' &'], shell=True)
                                                                                logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Process "+modfile+" Started\n")
										whiteinfine()
								elif any (c in modfile for c in ("Guest")):
									if (time.strftime('%H')=='11' and datetime.datetime.today().weekday()=='0'):
										subprocess.call(["sed -i '/"+modfile+"/d' /opt/JOBAlert_New/utk/files/cycle.txt"], shell=True)
                                                                                subprocess.call(["sed -i '/"+modfile+"/d' /opt/JOBAlert_New/utk/files/logfille"], shell=True)
										subprocess.call(['cd /opt/JOBAlert_New/; nohup '+script_name+' '+modfile+' '+currentsystime+' &'], shell=True)
                                                                                logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Process "+modfile+" Started\n")
										whiteinfine()
								elif any (c in modfile for c in ("Reminder36*")):
									if (time.strftime('%d')=='01'):
										subprocess.call(["sed -i '/"+modfile+"/d' /opt/JOBAlert_New/utk/files/cycle.txt"], shell=True)
                                                                                subprocess.call(["sed -i '/"+modfile+"/d' /opt/JOBAlert_New/utk/files/logfille"], shell=True)
										subprocess.call(['cd /opt/JOBAlert_New/; nohup '+script_name+' '+modfile+' '+currentsystime+' &'], shell=True)
                                                                                logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Process "+modfile+" Started\n")
										whiteinfine()
								elif any (c in modfile for c in ("widget")):
									if (time.strftime('%d')=='15'):
										subprocess.call(["sed -i '/"+modfile+"/d' /opt/JOBAlert_New/utk/files/cycle.txt"], shell=True)
                                                                                subprocess.call(["sed -i '/"+modfile+"/d' /opt/JOBAlert_New/utk/files/logfille"], shell=True)
										subprocess.call(['cd /opt/JOBAlert_New/; nohup '+script_name+' '+modfile+' '+currentsystime+' &'], shell=True)
                                                                                logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Process "+modfile+" Started\n")
										whiteinfine()
								else:
									subprocess.call(["sed -i '/"+modfile+"/d' /opt/JOBAlert_New/utk/files/cycle.txt"], shell=True)
        	                                                        subprocess.call(["sed -i '/"+modfile+"/d' /opt/JOBAlert_New/utk/files/logfille"], shell=True)
									subprocess.call(['cd /opt/JOBAlert_New/; nohup '+script_name+' '+modfile+' '+currentsystime+' &'], shell=True)
                                                                        logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Process "+modfile+" Started\n")
									whiteinfine()
						else:
                                                        logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Error in Process "+modfile+"\n")
							#pidp=commands.getoutput("ps aux | grep "+modfile+" | grep -v 'grep' | grep sh | awk '{print $2}'")
							if process_id != '':
								subprocess.call(['kill -9 '+process_id+'; kill -9 '+process_id], shell=True)
							subprocess.call(['cd /opt/JOBAlert_New/;'+line], shell=True)
                                                        subprocess.call(["sed -i '/"+modfile+"/d' /opt/JOBAlert_New/utk/files/logfille"], shell=True)
							pidpp=commands.getoutput("tail -30 "+log_file3)
							subprocess.call(["/usr/local/bin/sendEmail -t utkarsh.srivastava@timesgroup.com -f utkarsh.srivastava@timesgroupe.com -l /var/log/sendEmail -u 'Utkarsh Srivastava' -m 'Hi Sir ,\n\n\nThere is error in "+line+"\n\n\n Process have restarted, please find error details \n\n\n\n "+pidpp+"\n\n\n\n Regards,\nUtkarsh Srivastava'"], shell=True)
                                                        logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Error in Process "+modfile+"\n")
							whiteinfine()
					else:
                                        	logfile_for_process.write(time.strftime('%d-%m-%y %H:%M')+" Process "+modfile+" Running\n")
                                else:
                                        pass
pidp=commands.getoutput("ps aux | grep java | grep -v 'grep' | awk '{print $2}'")
if pidp != '':
	whiteinfine()
	processoncycle()
else:
	pass
