import numpy as np
import time
import sys

# Ορισμός χρωμάτων (έξω από τις συναρτήσεις για να είναι καθολικά)
CYAN = '\033[96m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'

def get_safe_int(prompt):
    """Συνάρτηση που σιγουρεύει ότι ο χρήστης έδωσε αριθμό χωρίς να κρασάρει"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(f"{RED}⚠️ Παρακαλώ δώστε μόνο αριθμό!{END}")

def main():
    print(f"\n{CYAN}{'='*40}{END}")
    print(f"{CYAN}{BOLD}          ✨ STARCALATOR ✨          {END}")
    print(f"{CYAN}{'='*40}{END}")
    
    print(f"{YELLOW}[1]{END} Προχώρησε στο επόμενο βήμα")
    print(f"{YELLOW}[0]{END} Πληροφορίες εφαρμογής")
    print(f"{RED}[2]{END} Έξοδος")
    print(f"{CYAN}{'-'*40}{END}")
    
    inp = get_safe_int(f"{BOLD}Επιλογή: {END}")
    
    if inp == 0:
        info()
    elif inp == 1:
        tupologio()
    elif inp == 2:
        feugw()
    else:
        print(f"{RED}Λάθος επιλογή, προσπάθησε ξανά.{END}")
        time.sleep(1)
        main()

def info():
    print(f"\n{GREEN}--- Πληροφορίες Εφαρμογής ---{END}")
    print("Αυτή η εφαρμογή βοηθάει στους υπολογισμούς αστρονομίας.")
    print(f"{CYAN}{'-'*30}{END}")
    
    inp = get_safe_int(f"{BOLD}Για επιστροφή πατήστε [7]: {END}")
    if inp == 7:
        main()

def tupologio():
    print(f"\n{GREEN}{'='*68}{END}")
    print(f"{GREEN}{BOLD}                     🔭 ΤΥΠΟΛΟΓΙΟ 🔭                     {END}")
    print(f"{GREEN}{'='*68}{END}\n")
    print(f" {YELLOW}[1]{END} {CYAN}{'Νόμος του Stefan-Boltzmann':<34}{END} {BOLD}F = σ · T_eff⁴{END}")
    print(f" {YELLOW}[2]{END} {CYAN}{'Νόμος μετατόπισης του Wien':<34}{END} {BOLD}λ_max · T_eff = 2.9 × 10⁻³ m·K{END}")
    print(f" {YELLOW}[3]{END} {CYAN}{'Τύπος της φωτεινότητας':<34}{END} {BOLD}L = 4π · R² · σ · T⁴{END}")
    print(f" {YELLOW}[4]{END} {CYAN}{'Φαινόμενη λαμπρότητα':<34}{END} {BOLD}l = L / (4π · r²){END}")
    print(f" {YELLOW}[5]{END} {CYAN}{'Πίεση ακτινοβολίας':<34}{END} {BOLD}P_rad = (4σ · T⁴) / 3c = u / 3{END}")
    print(f" {YELLOW}[6]{END} {CYAN}{'Πυκνότητα ενέργειας ακτινοβολίας':<34}{END} {BOLD}u = (4σ · T⁴) / c{END}")    
    print(f"\n{GREEN}{'-'*68}{END}")

    inp = get_safe_int(f"{BOLD}Για επιστροφή πατήστε [7]: {END}")
    if inp == 7:
        main()

def StefanBoltzman():
    print("a")

def Wien():
    print("s")

def fwtinotita():
    print("f")

def lamprotita():
    print("lama")

def aktinobolia():
    print("aktin")

def piknotita():
    print("piknot")



def feugw():
    print(f"\n{BOLD}{YELLOW}Ευχαριστούμε που χρησιμοποιήσατε το STARCALATOR!{END}")
    print(f"{RED}Κλείσιμο σε 2 δευτερόλεπτα...{END}")
    time.sleep(2)
    sys.exit() # Πιο κομψός τρόπος για έξοδο

if __name__ == "__main__":
    main()