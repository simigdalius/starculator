import numpy as np
import time
import sys
import os  # <--- ΠΡΟΣΘΕΣΕ ΑΥΤΟ

# Αυτή η γραμμή "ξυπνάει" το terminal των Windows για να δείχνει χρώματα!
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
    print(f"{CYAN}{BOLD}          ✨ STARCULATOR ✨          {END}")
    print(f"{CYAN}{'='*40}{END}")
    
    print(f"{YELLOW}[1]{END} Προχώρησε στο επόμενο βήμα")
    print(f"{YELLOW}[0]{END} Πληροφορίες εφαρμογής")
    print(f"{RED}[2]{END} Έξοδος")
    print(f"{CYAN}{'-'*40}{END}")
    
    inp = get_safe_int(f"{BOLD}Επιλογή: {END}")
    while inp>2:
        print(f"{RED}{BOLD}η επιλογη σου ειναι μη εγκυρη διαλεξε μεταξυ 0-2.: {END}")
        inp = get_safe_int(f"{BOLD}Επιλογή: {END}")
    
    if inp == 0:
        info()
    elif inp == 1:
        kefalaia()
    elif inp == 2:
        feugw()
    else:
        print(f"{RED}Λάθος επιλογή, προσπάθησε ξανά.{END}")
        time.sleep(1)
        main()

def kefalaia():
    print(f"\n{CYAN}{'='*40}{END}")
    print(f"{CYAN}{BOLD}          ✨ Επελεξε κεφαλαιο ✨          {END}")
    print(f"{CYAN}{'='*40}{END}")
    print(f" {YELLOW}[0]{END} {CYAN}{'Μετατροπές':<34}{END}")
    print(f" {YELLOW}[1]{END} {CYAN}{'Ουρανια σφαίρα':<34}{END}")
    print(f" {YELLOW}[2]{END} {CYAN}{'Ακτινοβολία':<34}{END}")
    print(f"{BOLD}Για επιλογη κεφαλαίου πατήστε 0-6: {END}")
    print(f"{RED}{BOLD}Για επιστροφή πατήστε [3]: {END}")
    inp = get_safe_int(f"{BOLD}Επιλογή: {END}")
    while inp>3:
        print(f"{RED}{BOLD}η επιλογη σου ειναι μη εγκυρη διαλεξε μεταξυ 0-3.: {END}")
        inp = get_safe_int(f"{BOLD}Επιλογή: {END}")
    if inp == 2:
        tupologiok2()
    elif inp == 0:
        metatropes()
    elif inp == 3:
        main()
    elif inp == 1:
        ourania()

def ourania():
    print(f"\n{GREEN}{'='*68}{END}")
    print(f"{GREEN}{BOLD}                     🔭 ΤΥΠΟΛΟΓΙΟ ΟΥΡΑΝΙΑΣ ΣΦΑΙΡΑΣ 🔭                     {END}")
    print(f"{GREEN}{'='*68}{END}\n")
    print(f" {YELLOW}[1]{END} {CYAN}{'Τροχια αστερα':<34}{END}" )
 
    print(f"\n{GREEN}{'-'*75}{END}")
    print(f"{BOLD}Για επιλογη τυπου πατα 1-4: {END}")
    print(f"{RED}{BOLD}Για επιστροφή πατήστε [7]: {END}")
    inp = get_safe_int(f"{BOLD}Επιλογή: {END}")
    while inp>2:
        print(f"{RED}{BOLD}η επιλογη σου ειναι μη εγκυρη διαλεξε μεταξυ 1-2.: {END}")
        inp = get_safe_int(f"{BOLD}Επιλογή: {END}")
    if inp==1:
        star_tracker()
    elif inp==2:
        main()
        
def star_tracker():
    print(f"\n{GREEN}{'='*68}{END}")
    print(f"{CYAN}{BOLD}               Υπολογισμός: Θέση & Τροχιά Αστέρα               {END}")
    print(f"{GREEN}{'='*68}{END}\n")
    
    print("Μετατροπή Ισημερινών σε Οριζόντιες Συντεταγμένες (Τρίγωνο Θέσης)\n")
    
    delta = get_safe_float(f"{BOLD}Δώσε την απόκλιση του αστέρα δ (σε μοίρες): {END}")
    phi = get_safe_float(f"{BOLD}Δώσε το γεωγραφικό πλάτος του παρατηρητή φ (σε μοίρες): {END}")
    omega = get_safe_float(f"{BOLD}Δώσε την ωριαία γωνία ω (σε μοίρες): {END}")
    
    # Μετατροπή σε ακτίνια (radians) για τη numpy
    d_rad, p_rad, w_rad = np.radians(delta), np.radians(phi), np.radians(omega)
    
    # 1. Υπολογισμός Ύψους (v)
    # Από τον Νόμο Συνημιτόνων στο τρίγωνο θέσης: sin(v) = sin(δ)sin(φ) + cos(δ)cos(φ)cos(ω)
    sin_v = np.sin(d_rad) * np.sin(p_rad) + np.cos(d_rad) * np.cos(p_rad) * np.cos(w_rad)
    v_rad = np.arcsin(sin_v)
    v = np.degrees(v_rad)
    
    # 2. Υπολογισμός Αζιμουθίου (A)
    # cos(A) = (sin(δ) - sin(v)sin(φ)) / (cos(v)cos(φ))
    cos_A = (np.sin(d_rad) - np.sin(v_rad) * np.sin(p_rad)) / (np.cos(v_rad) * np.cos(p_rad))
    # Περιορισμός του cos_A αυστηρά μεταξύ -1 και 1 για αποφυγή σφαλμάτων στρογγυλοποίησης
    cos_A = max(-1.0, min(1.0, cos_A)) 
    A = np.degrees(np.arccos(cos_A))
    
    # Διόρθωση Αζιμουθίου (Η σύμβαση μετράει από τον Νότο: 0=Νότος, 90=Δύση, 180=Βορράς, 270=Ανατολή)
    if np.sin(w_rad) > 0:
        # Αν sin(ω) > 0 ο αστέρας βρίσκεται στο δυτικό ημισφαίριο (δύει)
        A = 360 - A
        
    print(f"\n{YELLOW}▶ Αποτέλεσμα:{END}")
    if v < 0:
        print(f"{RED}Ο αστέρας βρίσκεται {-v:.2f}° κάτω από τον ορίζοντα (Αόρατος).{END}")
    else:
        print(f"{GREEN}Ο αστέρας είναι ορατός πάνω από τον ορίζοντα!{END}")
        
    print(f"{BOLD}Ύψος (v) = {v:.2f}°{END}")
    print(f"{BOLD}Αζιμούθιο (A) = {A:.2f}° (Μετρούμενο από τον Νότο προς τη Δύση){END}")
    
    input(f"\n{BOLD}Πάτα Enter για επιστροφή...{END}")
    ourania()

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

def tupologiok2():
    print(f"\n{GREEN}{'='*68}{END}")
    print(f"{GREEN}{BOLD}                     🔭 ΤΥΠΟΛΟΓΙΟ ΑΚΤΙΝΟΒΟΛΙΑΣ 🔭                     {END}")
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
    while inp>7:
        print(f"{RED}{BOLD}η επιλογη σου ειναι μη εγκυρη διαλεξε μεταξυ 1-7.: {END}")
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
    tupologiok2()

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
    tupologiok2() 

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
    tupologiok2() 

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
    tupologiok2() 

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
    tupologiok2() 

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
    tupologiok2() 

def metatropes():
    print(f"\n{GREEN}{'='*68}{END}")
    print(f"{GREEN}{BOLD}                     🔭 ΜΕΤΑΤΡΟΠΕΣ 🔭                     {END}")
    print(f"{GREEN}{'='*68}{END}\n")
    print(f" {YELLOW}[1]{END} {CYAN}{'Μετατροπές από Παρσέκ (pc)':<34}{END} ")
    print(f" {YELLOW}[2]{END} {CYAN}{'Μετατροπές από Έτη Φωτός (l.y.)':<34}{END} ")
    print(f" {YELLOW}[3]{END} {CYAN}{'Μετατροπές από Αστρονιμικές Μονάδες (A.U.)':<34}{END} ")
    print(f"{BOLD}Για επιλογη τυπου πατα 1-3: {END}")
    print(f"{RED}{BOLD}Για επιστροφή πατήστε [4]: {END}")
    inp = get_safe_int(f"{BOLD}Επιλογή: {END}")
    while inp>4:
        print(f"{RED}{BOLD}η επιλογη σου ειναι μη εγκυρη διαλεξε μεταξυ 1-4.: {END}")
        inp = get_safe_int(f"{BOLD}Επιλογή: {END}")
    if inp==1:
        pc()
    elif inp==2:
        lightyears()
    elif inp==3:
        astronomicalunits()
    elif inp ==4:
        main()

def pc():
    pctimh = get_safe_float(f"{BOLD}Δώσε την απόσταση (σε Παρσέκ): {END}")
    print(f" {YELLOW}[1]{END} {CYAN}{'Μετατροπή σε m':<34}{END} ")
    print(f" {YELLOW}[2]{END} {CYAN}{'Μετατροπή σε km':<34}{END} ")
    print(f" {YELLOW}[3]{END} {CYAN}{'Μετατροπή σε A.U.':<34}{END} ")
    print(f" {YELLOW}[4]{END} {CYAN}{'Μετατροπή σε l.y.':<34}{END} ")
    print(f"{BOLD}Για επιλογη τυπου πατα 1-4: {END}")
    print(f"{RED}{BOLD}Για επιστροφή πατήστε [5]: {END}")
    inp = get_safe_int(f"{BOLD}Επιλογή: {END}")
    while inp>5:
        print(f"{RED}{BOLD}η επιλογη σου ειναι μη εγκυρη διαλεξε μεταξυ 1-5.: {END}")
        inp = get_safe_int(f"{BOLD}Επιλογή: {END}")
    if inp==1:
        pctimh = pctimh * 3.086 * (10**16)
        print(f"\n{YELLOW}▶ Αποτέλεσμα:{END}")
        print(f"{BOLD}pc σε m = {pctimh:.4e} m{END}")
        input(f"{BOLD}Πάτα Enter για επιστροφή...{END}")
        metatropes()
    elif inp==2:
        pctimh = pctimh * 3.086 * (10^13)
        print(f"\n{YELLOW}▶ Αποτέλεσμα:{END}")
        print(f"{BOLD}pc σε km = {pctimh:.4e} km {END}")
        input(f"{BOLD}Πάτα Enter για επιστροφή...{END}")
        metatropes()
    elif inp==3:
        pctimh = pctimh * 206265
        print(f"\n{YELLOW}▶ Αποτέλεσμα:{END}")
        print(f"{BOLD}pc σε A.U. = {pctimh:.4e} A.U.{END}")
        input(f"{BOLD}Πάτα Enter για επιστροφή...{END}")
        metatropes()
    elif inp==4:
        pctimh = pctimh * 3.26
        print(f"\n{YELLOW}▶ Αποτέλεσμα:{END}")
        print(f"{BOLD}pc σε l.y. = {pctimh:.4e} l.y.{END}")
        input(f"{BOLD}Πάτα Enter για επιστροφή...{END}")
        metatropes()
    elif inp ==5:
        main()



def lightyears():
    lytimh = get_safe_float(f"{BOLD}Δώσε την απόσταση (σε έτη φωτός): {END}")
    print(f" {YELLOW}[1]{END} {CYAN}{'Μετατροπή σε m':<34}{END} ")
    print(f" {YELLOW}[2]{END} {CYAN}{'Μετατροπή σε km':<34}{END} ")
    print(f" {YELLOW}[3]{END} {CYAN}{'Μετατροπή σε A.U.':<34}{END} ")
    print(f" {YELLOW}[4]{END} {CYAN}{'Μετατροπή σε pc':<34}{END} ")
    print(f"{BOLD}Για επιλογη τυπου πατα 1-4: {END}")
    print(f"{RED}{BOLD}Για επιστροφή πατήστε [5]: {END}")
    inp = get_safe_int(f"{BOLD}Επιλογή: {END}")
    while inp>5:
        print(f"{RED}{BOLD}η επιλογη σου ειναι μη εγκυρη διαλεξε μεταξυ 1-5.: {END}")
        inp = get_safe_int(f"{BOLD}Επιλογή: {END}")
    if inp==1:
        lytimh = lytimh * 9.46 * (10^15)
        print(f"\n{YELLOW}▶ Αποτέλεσμα:{END}")
        print(f"{BOLD}l.y. σε m = {lytimh:.4e} m{END}")
        input(f"{BOLD}Πάτα Enter για επιστροφή...{END}")
        metatropes()
    elif inp==2:
        lytimh = lytimh * 39.46 * (10^12)
        print(f"\n{YELLOW}▶ Αποτέλεσμα:{END}")
        print(f"{BOLD}l.y. σε km = {lytimh:.4e} km {END}")
        input(f"{BOLD}Πάτα Enter για επιστροφή...{END}")
        metatropes()
    elif inp==3:
        lytimh = lytimh * 63241
        print(f"\n{YELLOW}▶ Αποτέλεσμα:{END}")
        print(f"{BOLD}l.y. σε A.U. = {lytimh:.4e} A.U.{END}")
        input(f"{BOLD}Πάτα Enter για επιστροφή...{END}")
        metatropes()
    elif inp==4:
        lytimh = lytimh * 0.30675
        print(f"\n{YELLOW}▶ Αποτέλεσμα:{END}")
        print(f"{BOLD}l.y. σε pc = {lytimh:.4e} pc{END}")
        input(f"{BOLD}Πάτα Enter για επιστροφή...{END}")
        metatropes()
    elif inp ==5:
        main()



def astronomicalunits():
    AUtimh = get_safe_float(f"{BOLD}Δώσε την απόσταση (σε αστρονιμικές μονάδες): {END}")
    print(f" {YELLOW}[1]{END} {CYAN}{'Μετατροπή σε m':<34}{END} ")
    print(f" {YELLOW}[2]{END} {CYAN}{'Μετατροπή σε km':<34}{END} ")
    print(f" {YELLOW}[3]{END} {CYAN}{'Μετατροπή σε l.y.':<34}{END} ")
    print(f" {YELLOW}[4]{END} {CYAN}{'Μετατροπή σε pc':<34}{END} ")
    print(f"{BOLD}Για επιλογη τυπου πατα 1-4: {END}")
    print(f"{RED}{BOLD}Για επιστροφή πατήστε [5]: {END}")
    inp = get_safe_int(f"{BOLD}Επιλογή: {END}")
    while inp>5:
        print(f"{RED}{BOLD}η επιλογη σου ειναι μη εγκυρη διαλεξε μεταξυ 1-5.: {END}")
        inp = get_safe_int(f"{BOLD}Επιλογή: {END}")
    if inp==1:
        AUtimh = AUtimh * 1.496 * (10^11)
        print(f"\n{YELLOW}▶ Αποτέλεσμα:{END}")
        print(f"{BOLD}A.U. σε m = {AUtimh:.4e} m{END}")
        input(f"{BOLD}Πάτα Enter για επιστροφή...{END}")
        metatropes()
    elif inp==2:
        AUtimh = AUtimh * 1.496 * (10^8)
        print(f"\n{YELLOW}▶ Αποτέλεσμα:{END}")
        print(f"{BOLD}A.U. σε km = {AUtimh:.4e} km {END}")
        input(f"{BOLD}Πάτα Enter για επιστροφή...{END}")
        metatropes()
    elif inp==3:
        AUtimh = AUtimh * 1.581 * (10*(-5))
        print(f"\n{YELLOW}▶ Αποτέλεσμα:{END}")
        print(f"{BOLD}A.U. σε l.y. = {AUtimh:.4e} A.U.{END}")
        input(f"{BOLD}Πάτα Enter για επιστροφή...{END}")
        metatropes()
    elif inp==4:
        AUtimh = AUtimh * 4.84814 * (10^(-6))
        print(f"\n{YELLOW}▶ Αποτέλεσμα:{END}")
        print(f"{BOLD}l.y. σε pc = {AUtimh:.4e} pc{END}")
        input(f"{BOLD}Πάτα Enter για επιστροφή...{END}")
        metatropes()
    elif inp ==5:
        main()












def feugw():
    print(f"\n{BOLD}{YELLOW}Ευχαριστούμε που χρησιμοποιήσατε το STARCULATOR!{END}")
    print(f"{RED}Κλείσιμο σε 2 δευτερόλεπτα...{END}")
    time.sleep(2)
    sys.exit() # Πιο κομψός τρόπος για έξοδο

if __name__ == "__main__":
    main()