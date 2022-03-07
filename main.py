import requests as rsp
import art

def track_by_ip(ip='127.0.0.1'):
    try:
        resp = rsp.get(url=f"http://ip-api.com/json/{ip}").json()
        
        result = {
             '[IP]': resp.get('query'),
             '[Country]': resp.get('country'),
             '[Region]': resp.get('regionName'),
             '[City]': resp.get('city'),
             '[Provider]': resp.get('isp'),
             '[Lat]': resp.get('lat'),
             '[Lon]': resp.get('lon'),
        }
        for i, j in result.items():
            print(f"{i} : {j}")
        
        print("[GMap Link] : ", end='')
        print(f"https://maps.google.com/?q={result.get('[Lat]')},{result.get('[Lon]')}")

    except rsp.exceptions.ConnectionError:
        print("[!] Connection error!")


def main():
    art.tprint("IP_TRACKER", font="cybermedium")

    ip = input("Enter target IP: ")
    track_by_ip(ip)

if __name__ == "__main__":
    main()
