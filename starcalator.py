import numpy as np
import time
import sys
import os  
os.system("color")

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

def get_safe_float(prompt):
    """Ίδια με την get_safe_int, αλλά επιτρέπει δεκαδικούς αριθμούς (floats)"""
    while True:
        try:
            # Χρησιμοποιούμε float() αντί για int() γιατί η θερμοκρασία μπορεί να έχει δεκαδικά
            return float(input(prompt))
        except ValueError:
            print(f"{RED}⚠️ Παρακαλώ δώστε έναν έγκυρο αριθμό!{END}")

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
    print(f"\n{GREEN}{'='*68}{END}")
    print(f"{GREEN}{BOLD}                  ℹ️ ΠΛΗΡΟΦΟΡΙΕΣ ΕΦΑΡΜΟΓΗΣ ℹ️                   {END}")
    print(f"{GREEN}{'='*68}{END}\n")
    
    print(f"{CYAN}Καλώς ήρθατε στο STARCALATOR! 🌌{END}\n")
    print("Το STARCALATOR είναι μια διαδραστική εφαρμογή τερματικού (CLI)")
    print("σχεδιασμένη για να κάνει τους υπολογισμούς της Αστροφυσικής")
    print("γρήγορους, εύκολους και ακριβείς. Αποτελεί το ιδανικό εργαλείο")
    print("για φοιτητές, ερασιτέχνες αστρονόμους και λάτρεις του διαστήματος.\n")
    
    print(f"{YELLOW}Βασικές Δυνατότητες:{END}")
    print(f" {BOLD}*{END} Εφαρμογή θεμελιωδών νόμων (Stefan-Boltzmann, Wien).")
    print(f" {BOLD}*{END} Υπολογισμός Φωτεινότητας (L) & Φαινόμενης Λαμπρότητας (l).")
    print(f" {BOLD}*{END} Εύρεση Πίεσης (P_rad) & Πυκνότητας Ενέργειας Ακτινοβολίας (u).")
    
    print(f"\n{CYAN}Τεχνικά Χαρακτηριστικά:{END}")
    print(" - Ενσωματωμένες σταθερές ακριβείας (όπως c, σ, π).")
    print(" - Προστασία (Safe Input) για αποφυγή «κρασαρίσματος» από λάθη.")
    print(" - Έξοδος αποτελεσμάτων σε επιστημονική μορφή (π.χ. 6.30e+07).\n")
    
    print(f"{GREEN}{'-'*68}{END}")
    input(f"{BOLD}Πάτα Enter για επιστροφή...{END}")
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
    print(f"{BOLD}Για επιλογη τυπου πατα 1-6: {END}")
    print(f"{RED}{BOLD}Για επιστροφή πατήστε [7]: {END}")
    inp = get_safe_int(f"{BOLD}Επιλογή: {END}")
    if inp==1:
        StefanBoltzman()
    elif inp==2:
        Wien()
    elif inp==3:
        fwtinotita()
    elif inp==4:
        lamprotita()
    elif inp==5:
        aktinobolia()
    elif inp==6:
        piknotita()
    elif inp==7:
        main()

def StefanBoltzman():
    print(f"\n{GREEN}{'='*50}{END}")
    print(f"{CYAN}{BOLD} Υπολογισμός: Νόμος του Stefan-Boltzmann {END}")
    print(f"{GREEN}{'='*50}{END}")
    
    print(f"{CYAN}Τύπος:{END} {BOLD}F = σ · T_eff⁴{END}")
    print(f"Όπου σ = 5.6704 × 10⁻⁸ W/(m²·K⁴)\n")
    t_eff = get_safe_float(f"{BOLD}Δώσε την ενεργό θερμοκρασία T_eff (σε Kelvin): {END}")
    sigma = 5.6704e-8 
    f = sigma * (t_eff ** 4)
    print(f"\n{YELLOW}▶ Αποτέλεσμα:{END}")
    # Το :.2e εμφανίζει το αποτέλεσμα σε επιστημονική μορφή με 2 δεκαδικά
    print(f"{BOLD}Ροή Ακτινοβολίας (F) = {f:.2e} W/m²{END}") 
    print(f"\n{CYAN}{'-'*50}{END}")
    input(f"{BOLD}Πάτα Enter για επιστροφή...{END}")
    tupologio() 


def Wien():
    print(f"\n{GREEN}{'='*68}{END}")
    print(f"{GREEN}{BOLD}                     Υπολογισμός: Νόμος μετατόπισης του Wien                     {END}")
    print(f"{GREEN}{'='*68}{END}\n")
    print(f"{CYAN}Τύπος:{END} {BOLD}λ_max = (2.9 × 10⁻³) / T_eff{END}")
    t_eff = get_safe_float(f"{BOLD}Δώσε την ενεργό θερμοκρασία T_eff (σε Kelvin): {END}")
    # Αποφυγή διαίρεσης με το μηδέν
    if t_eff <= 0:
        print(f"{RED}Η θερμοκρασία πρέπει να είναι μεγαλύτερη από το μηδέν!{END}")
    else:
        l_max = 2.9e-3 / t_eff
        print(f"\n{YELLOW}▶ Αποτέλεσμα:{END}")
        print(f"{BOLD}Μέγιστο Μήκος Κύματος (λ_max) = {l_max:.2e} m{END}")

    print(f"\n{GREEN}{'-'*68}{END}")  
    input(f"{BOLD}Πάτα Enter για επιστροφή...{END}")
    tupologio() 

def fwtinotita():
    print(f"\n{GREEN}{'='*68}{END}")
    print(f"{CYAN}{BOLD}                     Υπολογισμός: Τύπος της φωτεινότητας                      {END}")
    print(f"{GREEN}{'='*68}{END}\n")
    print(f"{CYAN}Τύπος:{END} {BOLD}L = 4π · R² · σ · T⁴{END}") 
    r_star = get_safe_float(f"{BOLD}Δώσε την ακτίνα του αστέρα R (σε μέτρα): {END}")
    t_eff = get_safe_float(f"{BOLD}Δώσε τη θερμοκρασία T (σε Kelvin): {END}")
    sigma = 5.6704e-8
    # np.pi για το π (3.14159...)
    lum = 4 * np.pi * (r_star**2) * sigma * (t_eff**4)
    print(f"\n{YELLOW}▶ Αποτέλεσμα:{END}")
    print(f"{BOLD}Φωτεινότητα (L) = {lum:.2e} W{END}")
    print(f"\n{GREEN}{'-'*68}{END}") 
    input(f"{BOLD}Πάτα Enter για επιστροφή...{END}")
    tupologio() 

def lamprotita():
    print(f"\n{GREEN}{'='*68}{END}")
    print(f"{CYAN}{BOLD}    Υπολογισμός: Φαινόμενη λαμπρότητα                      {END}")
    print(f"{GREEN}{'='*68}{END}\n")   
    print(f"{CYAN}Τύπος:{END} {BOLD}l = L / (4π · r²){END}")
    l_star = get_safe_float(f"{BOLD}Δώσε τη Φωτεινότητα L (σε Watt): {END}")
    r_dist = get_safe_float(f"{BOLD}Δώσε την απόσταση r (σε μέτρα): {END}")  
    if r_dist <= 0:
        print(f"{RED}Η απόσταση πρέπει να είναι θετικός αριθμός!{END}")
    else:
        app_bright = l_star / (4 * np.pi * (r_dist**2))
        print(f"\n{YELLOW}▶ Αποτέλεσμα:{END}")
        print(f"{BOLD}Φαινόμενη Λαμπρότητα (l) = {app_bright:.2e} W/m²{END}")

    print(f"\n{GREEN}{'-'*68}{END}")             
    input(f"{BOLD}Πάτα Enter για επιστροφή...{END}")
    tupologio() 

def aktinobolia():
    print(f"\n{GREEN}{'='*68}{END}")
    print(f"{CYAN}{BOLD}                     Υπολογισμός: Πίεση ακτινοβολίας                      {END}")
    print(f"{GREEN}{'='*68}{END}\n")
    print(f"{CYAN}Τύπος:{END} {BOLD}P_rad = (4σ · T⁴) / 3c{END}")
    
    t_eff = get_safe_float(f"{BOLD}Δώσε τη θερμοκρασία T (σε Kelvin): {END}")
    
    sigma = 5.6704e-8
    c = 3e8
    p_rad = (4 * sigma * (t_eff**4)) / (3 * c)
    print(f"\n{YELLOW}▶ Αποτέλεσμα:{END}")
    print(f"{BOLD}Πίεση Ακτινοβολίας (P_rad) = {p_rad:.2e} Pa (N/m²){END}")
    print(f"\n{GREEN}{'-'*68}{END}")
    input(f"{BOLD}Πάτα Enter για επιστροφή...{END}")
    tupologio() 

def piknotita():
    print(f"\n{GREEN}{'='*68}{END}")
    print(f"{CYAN}{BOLD}                     Υπολογισμός: Πυκνότητα ενέργειας ακτινοβολίας                      {END}")
    print(f"{GREEN}{'='*68}{END}\n")
    print(f"{CYAN}Τύπος:{END} {BOLD}u = (4σ · T⁴) / c{END}")
    t_eff = get_safe_float(f"{BOLD}Δώσε τη θερμοκρασία T (σε Kelvin): {END}")
    
    sigma = 5.6704e-8
    c = 3e8
    u = (4 * sigma * (t_eff**4)) / c
    
    print(f"\n{YELLOW}▶ Αποτέλεσμα:{END}")
    print(f"{BOLD}Πυκνότητα Ενέργειας Ακτινοβολίας (u) = {u:.2e} J/m³{END}")

    print(f"\n{GREEN}{'-'*68}{END}")
    input(f"{BOLD}Πάτα Enter για επιστροφή...{END}")
    tupologio() 



def feugw():
    print(f"\n{BOLD}{YELLOW}Ευχαριστούμε που χρησιμοποιήσατε το STARCALATOR!{END}")
    print(f"{RED}Κλείσιμο σε 2 δευτερόλεπτα...{END}")
    time.sleep(2)
    sys.exit() # Πιο κομψός τρόπος για έξοδο

if __name__ == "__main__":
    main()

