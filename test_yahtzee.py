from yahtzee import YahtzeeMainClass
from die import Die
import pytest
 
def test_is_yahtzee_when_all_dice_matches():
    # Skapa en lista med fem tärningar
    dice = [Die(), Die(), Die(), Die(), Die()]
    # Sätt alla tärningars värde till 6
    for tärning in tärningar:
        tärning.value = 6
    # Skapa en instans av Yahtzee-spelet med tärningarna
    yahtzee_spel = YahtzeeMainClass()
    yahtzee_spel.tärningar = tärningar  # Sätt tärningarna direkt
    # Kontrollera om det är Yahtzee
    assert yahtzee_spel.är_yahtzee() == True, "Bör vara Yahtzee när alla tärningar matchar"
 
def test_is_not_yahtzee_when_all_dice_not_matching_each_other():
    # Skapa en lista med fem tärningar
    tärningar = [Die(), Die(), Die(), Die(), Die()]
    # Sätt fyra tärningars värde till 6 och en tärnings värde till 2
    for tärning in tärningar:
        tärning.value = 6
    tärningar[0].value = 2
    # Skapa en instans av Yahtzee-spelet med tärningarna
    yahtzee_spel = YahtzeeMainClass()
    yahtzee_spel.tärningar = tärningar  # Sätt tärningarna direkt
    # Kontrollera om det inte är Yahtzee
    assert yahtzee_spel.är_yahtzee() == False, "Bör inte vara Yahtzee när inte alla tärningar matchar"
 
if __name__ == '__main__':
    pytest.main()
