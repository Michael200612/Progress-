import requests
import sys

def main():
    try:
        if len(sys.argv) == 1:
            print("Missing command-line argument")
            sys.exit()

        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=8da0595df9e7e70135d1bee076159c6a2603b7dc10c944ae9a0907ae604353ce")
        data = response.json()
        x = float(data["data"]["priceUsd"]) * float(sys.argv[1])
        print(f"${x:,.4f}")

    except ValueError:
        print("Command-line argument is not a number")
        sys.exit()
main()