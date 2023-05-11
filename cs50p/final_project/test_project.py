import pytest
from project import validate_file, cleaning_date, get_origins

def test_cleaning_date():
    assert cleaning_date("any_email@gmail.com,Lead,"",1,2022-11-28 21:26:26 -0300,Busca Paga | google") == "2022-11-28"
    assert cleaning_date("2022-11-28 21:26:26 -0300") == "2022-11-28"
    assert cleaning_date("2022-11-28") == "2022-11-28"
    assert cleaning_date("2022/11/28") == "--"
    assert cleaning_date("Lead") == "--"

def test_get_origins():
    assert get_origins([{"name":"test","origem":"origem"}]) == ['origem']
    assert get_origins([{"origem":"origem_1"}, {"name":"test","origem":"origem_2"}]) == ['origem_1', 'origem_2']
    assert get_origins([{"origem":""}]) == ['']
    assert get_origins([]) == []
    with pytest.raises(KeyError):
        get_origins([{"name":"test"}])

def test_validate_file():
    with pytest.raises(SystemExit):
        validate_file(['project.py'],[])
    with pytest.raises(SystemExit):
        validate_file(['project.py', 'arg_1', 'arg_2'],[])
    with pytest.raises(SystemExit):
        validate_file(['project.py', 'file.py'],[])
    with pytest.raises(SystemExit):
        validate_file(['project.py', 'no_file.csv'],[])