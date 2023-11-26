import wmi
import argparse

dns_dict ={
    "google" : ["8.8.8.8", "8.8.4.4"],
    "Open-dns" : ["208.67.222.222", "208.67.220.220"],
    "Cloudflare" : ["1.1.1.1", "1.0.0.1"],
    "Quad9" : ["9.9.9.9", "149.112.112.112"],
    "Adguard" : ["94.140.14.14", "94.140.15.15"],
    "ControlD" : ["76.76.2.0", "76.76.10.0"],
    "Shecan" : ["178.22.122.100", "185.51.200.2"],
    "Begzar" : ["185.55.226.26", "185.55.225.25"],
    "Comodo" : ["8.26.56.26", "8.20.247.20"],
#    "" : ["", ""],
}


def main():
    parser = argparse.ArgumentParser("Shows DNS settings for a given internet interface in Windows. Can also set DNS.") 
    parser.add_argument("-li","--list_interfaces" , help = "List available interfaces and their current DNS settings.", action="store_true")
    parser.add_argument("-ld","--list_dns" , help = "List available DNS providers.", action="store_true")
    parser.add_argument("--verbose" , help = "Shows more information.", action="store_true")

    #parser.add_argument("")

    args = parser.parse_args()
    c = wmi.WMI()

    adapters = c.Win32_NetworkAdapterConfiguration(IPEnabled=True)

    if args.list_dns :
        #print(dns_dict)
        print(f"Available DNS providers are as follows:\n")
        for i in dns_dict.keys():
            print(f"{i} : {dns_dict[i]}\n")

    if args.list_interfaces :
        print(f"Available interfaces and their DNSs are as follows:\n")
        for adapter in adapters:
            print(f"{adapter.Description} : {adapter.DNSServerSearchOrder}")


if __name__=="__main__":
    main()