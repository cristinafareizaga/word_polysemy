import word_polysemy.top_ten as to
import word_polysemy.average as av

def test_top_ten(number=10, input_file="data/palabras_polysemy.csv", print_top=True):
    result = to.calculate_top(number, input_file, print_top)
    assert len(result) == number
    assert result[-1][0] == 'good'
    assert result[-1][1] == 32

def test_metrics(file="data/palabras_polysemy.csv", print_average=True, print_suma=True):
    average, suma = av.calculate_metrics(file,print_average,print_suma)
    assert average == 15.48
    assert suma == 1548



