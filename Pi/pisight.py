import sys
import os


def snap():
    fname = 'test.png'
    ext = 'png'
    # Snap Image
    os.system('raspistill -t 1 -vf -hf -rot 90 -o ' + fname + ' -e ' + ext)


def transfer():
    fname = 'test.png'
    set_psswd = 'echo "Enter Password for Remote Host:"; read $password'
    tx_cmd = 'lftp sftp://pi:$password@192.168.1.217 -e "get ' + fname + ';bye"'
    os.system(set_psswd)


if '-snap' in sys.argv:
    snap()

if '-transfer' in sys.argv:
    transfer()
