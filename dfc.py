import os
os.system('clear')
tempic = "------------------------------------------------------------\n| Script Deface Creator By Anon555    |\n------------------------------------------------------------"
print tempic
title = raw_input('Judul Script Deface: ')
sib = raw_input('Link Gambar Shortcut Icon: ')
des = raw_input('Kata Kata Buat Description: ')
gmbr = raw_input('Link Gambar : ')
hekedby = raw_input("kata kata Heked Bey cnth heked bey '/Mine7 : ")
kata = raw_input('kata kata (G usah panjang panjang :v): ')
thnk = raw_input('Thanks To (Cnth - nama heker - nama mamak - nama bapak -) :')
fo = open('ScAnonnn.html', 'w')
script1 = '<html>\n<head>\n<title>'
script2 = title
script3 = '</title>'
script4 = '\n<link rel="icon" type="image/x-icon" href='
script5 = sib
script6 = '>\n<meta name="description" content='
script7 = des
script8 = '>\n<link href="https://fonts.googleapis.com/css?family=Iceland" rel="stylesheet" type="text/css">\n<style>\n html, body\n{\nbackground-color: black;\nheight: 100vh;\nmargin: 0;\n}\n .full-height\n{\nheight: 100vh;\n }\n.flex-center\n {\nalign-items: center;\n display: flex;\njustify-content: center;\n}\n .position-ref\n{\n position: relative;\n}\n.content\n{\n text-align: center;\n}\n.title\n{\nfont-size: 36px; padding: 20px;\n }\n</style>\n </head> \n<body align="center" oncontextmenu="return false">\n<div class="flex-center position-ref full-height">\n<center><code><img src='
script9 = gmbr
script10 = ' style="width:350px">\n<br>\n<b><font size="6"><font color="white" font face="Iceland">'
script11 = hekedby
script12 = '\n<font color="white" size="4">\n<br><b>{'
script13 = kata
script14 = '}</b></font>\n<br><b><br>\n<font size="3">'
script15 = thnk
script16 = '<br><br>\n<font color="red" size="4">#Indonesian Hacker Rulez </b>\n</body>\n</html>'
fo.write(script1)
fo.write(script2)
fo.write(script3)
fo.write(script4)
fo.write(script5)
fo.write(script6)
fo.write(script7)
fo.write(script8)
fo.write(script9)
fo.write(script10)
fo.write(script11)
fo.write(script12)
fo.write(script13)
fo.write(script14)
fo.write(script15)
fo.write(script16)
print
print 'Done Cuk Nama Script ScAnonnn.html'
print 'untuk memindahkan script ke internal masukan comand berikut (mv ScAnonnn.html /sdcard)'
fo.close()
