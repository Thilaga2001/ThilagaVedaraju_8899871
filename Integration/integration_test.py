
import checkFunctions
def test_integration_positive():
    # Test number positive or not
    assert checkFunctions.checkNegative(2) == "positive"

def test_integration_odd():
    # Test number odd or even
    assert checkFunctions.oddOrEven(5) == "even"



