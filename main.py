import wmi

dns_dict ={
    "google" : ["8.8.8.8", "8.8.4.4"],
    "Open-dns" : ["208.67.222.222", "208.67.220.220"],
    "Cloudflare" : ["1.1.1.1", "1.0.0.1"],
    "Quad9" : ["9.9.9.9", "149.112.112.112"],
    "Adguard" : ["94.140.14.14", "94.140.15.15"],
    "Shecan" : ["178.22.122.100", "185.51.200.2"],
    "Begzar" : ["185.55.226.26", "185.55.225.25"],
    "" : ["", ""],
}

c = wmi.WMI()

adapters = c.Win32_NetworkAdapterConfiguration(IPEnabled=True)

def main():

    for adapter in adapters:
        print(adapter.DNSServerSearchOrder)


if __name__=="__main__":
    main()