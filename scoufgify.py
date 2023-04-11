import sys
import csv
def main():
    args_check()
    rewrite()

def args_check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Too many command-line arguments")

def rewrite():
        try:
            with open(sys.argv[1], "r") as file:
                 reader = csv.DictReader(file)
                 templist = []
                 for row in reader:
                     templist.append(row)

            with open(sys.argv[2], "w") as file:
                writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
                writer.writeheader()
                for i in templist:
                    last,first = i["name"].split(", ")
                    house = i['house']
                    writer.writerow({"first":first,"last":last,"house":house})

        except (FileNotFoundError, PermissionError, ValueError, UnicodeDecodeError, csv.Error) as e:
            sys.exit(f"Could not read {sys.argv[1]} {e}")

if __name__=="__main__":
    main()