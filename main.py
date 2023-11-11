import wmi

dns_dict ={
    "google" : ["8.8.8.8", "8.8.4.4"],
    "open-dns" : ["208.67.222.222", "208.67.220.220"],
    "cloudflare" : ["1.1.1.1", "1.0.0.1"],
    "quad9" : ["9.9.9.9", "149.112.112.112"],
    "adguard" : ["94.140.14.14", "94.140.15.15"],
    "shecan" : ["178.22.122.100", "185.51.200.2"],
    "" : ["", ""],
}

c = wmi.WMI()

adapters = c.Win32_NetworkAdapterConfiguration(IPEnabled=True)

def main():

    for adapter in adapters:
        print(adapter.DNSServerSearchOrder)


if __name__=="__main__":
    main()