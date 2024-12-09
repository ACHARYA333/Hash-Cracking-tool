import sys
import os
import time
import hashlib

def Crack_PASS(WL, Given_hash, ALGO):
    All_pass = sum(1 for wordlist in WL for _ in open(wordlist))
    use_pass = 0

    for WP in WL:
        try:
            with open(WP, 'r') as file:
                for line in file:
                    password = line.strip()
                    if ALGO == 'sha1':
                        HASH_Data = hashlib.sha1(password.encode())
                    elif ALGO == 'md5':
                        HASH_Data = hashlib.md5(password.encode())
                    elif ALGO == 'sha256':
                        HASH_Data = hashlib.sha256(password.encode())
                    elif ALGO == 'sha512':
                        HASH_Data = hashlib.sha512(password.encode())
                    else:
                        print(f"Hashing algorithm '{ALGO}' not supported.")
                        return None

                    crack_hash = HASH_Data.hexdigest()
                    use_pass += 1
                    progress = (use_pass / All_pass) * 100
                    print(f"\rProgress: {progress:.2f}%", end='', flush=True)

                    if crack_hash == Given_hash:
                        return password
        except FileNotFoundError:
            print(f"Wordlist file '{WP}' not found try again.")
            sys.exit()
        except Exception as e:
            print(f"Error reading wordlist file '{WP}': {str(e)}")
            sys.exit()
    return None
    
def main():
   
    while True:               
            print("\n  >>> PASS HASH CRACK TOOL <<<  \n")
            ALGO = input(" Enter type Hash Algo (sha1,md5,sha256,sha512) >>> ").lower()
            if ALGO not in ['sha1','md5', 'sha256', 'sha512']:
                print(" Invalid hash algo")
                continue
            num_WL = input(" Number Wordlists used >>>  ")
            if not num_WL.isdigit() or int(num_WL) <= 0:
                print(" Invalid number ")
                continue
            num_WL = int(num_WL)
            WL = []
            for i in range(num_WL):
                WP = input(f" Enter Location for wordlist {i+1}: ")
                if not os.path.exists(WP):
                    print(f" Wordlist file '{WP}' not found try again.")
                    sys.exit()
                WL.append(WP)
            Given_hash = input(" Enter Hash Value >>>  ")

            start_time = time.time()
            cracked_password = Crack_PASS(WL, Given_hash, ALGO)
            end_time = time.time()
            if cracked_password:
                print(f"\n\n >>>>>  Found Password: >>>>>  {cracked_password} <<<<< \n")
            else:
                print("\n >>>>  Password not found in the wordlist. <<<< \n")

            print(f" Time taken: {end_time - start_time:.2f} seconds")
            sys.exit()


if __name__ == "__main__":
    main()
