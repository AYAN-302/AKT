import os,platform
os.system('git pull')
aktxd=platform.architecture()[0]
if aktxd=="32bit":exit(" Coming Soon 32 bit ")
elif aktxd=="64bit":__import__("akt_enc")