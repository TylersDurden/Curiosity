import sys
import os


if '-snap' in sys.argv:
    fname = 'test.png'
    ext = 'png'
    # Snap Image
    snap_cmd = 'raspistill -t 1 -vf -hf -rot 90 -o ' + fname + ' -e ' + ext
    os.system(snap_cmd)

if '-transfer' in sys.argv:
    fname = 'test.png'
    set_psswd = 'echo "Enter Password for Remote Host:"; read $password'
    tx_cmd = 'lftp sftp://pi:$password@192.168.1.217 -e "get '+fname+';bye"'
    os.system(set_psswd)
