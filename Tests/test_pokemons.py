import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = 'ec9f26a2ecba91b34ddc23d165264dc8'

def test_status_code():
    response = requests.get(f'{host}/trainers', params={trainer_id: 4432})
    assert response.status_code == 200

def test_part_of_answer ():
    response = requests.get(f'{host}/trainers', params={trainer_id: 4432})
    assert response.text.json() ['trainer_name'] == 'Берни'
    assert response.text.json() ['city'] == 'Москва'


    @pytest.mark.parametrize('key, value', [('city', 'Москва'), 
                                            ('trainer_name', 'Берни'), 
                                            ('battles', 0)])
    
    def test_part_of_answer(key, value): 
        response = requests.get(f'{host}/pokemons', params = {'trainer_id': 4432})
        assert response.json()[0][key] == value