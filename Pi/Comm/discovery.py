import socket
import psutil


def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        psutil.os.remove(fname)
    return data


def which_sys():
    is_windows = False
    is_linux = False
    if psutil.os.name == 'nt':
        is_windows = True
    else:
        is_linux = True
    os_info = {'Windows': is_windows,
            'Linux': is_linux}
    return os_info


def process_ifcon(raw_dat):
    # TODO: Which interfaces are up?
    data = list()
    for line in raw_dat:
        try:
            ip = line.split('inet ')[1].split(' ')[0]
            data.append(ip)
        except KeyError:
            pass
        except IndexError:
            pass
    return data


def run_linux():
    network_info = {}
    psutil.os.system('ifconfig >> nx.txt')
    psutil.os.system('hostname >> hname.txt')
    psutil.os.system('echo $(GET https://ipinfo.io/$(GET https://api.ipify.org)) >> geoip.txt')
    nx_raw = process_ifcon(swap('nx.txt', True))
    hostname = swap('hname.txt', True)
    geo_ip = swap('geoip.txt', True)
    network_info['local_data'] = nx_raw
    network_info['name'] = hostname
    network_info['ext_data'] = geo_ip
    return network_info


def main():
    os_type = which_sys()
    if os_type['Linux']:
       nx_info = run_linux()


if __name__ == '__main__':
    main()
