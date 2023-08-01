import requests

token = 'ec9f26a2ecba91b34ddc23d165264dc8'  
host = 'https://api.pokemonbattle.me:9104' # хост для покемонов 

'''response = requests.post('https://api.pokemonbattle.me:9104/trainers/reg', json={
    "trainer_token": token,
    "email": "malevinagalina@qastudio.me",
    "password": "Iloveqa1"
}, headers={'Content-Type' : 'application/json'}) '''



'''if response.status_code == 200:
    print('Ok!')
else:
    print('Not Ok!')

response_activation = requests.post(f'{host}/trainers/confirm_email', json= {'trainer_token': token}, headers={'Content-Type': 'application/json'})

print(response_activation.text)
'''

'''response_change_trainer = requests.put(f'{host}/trainers/confirm_email', json= {
    "name": "Берни",
    "city": "Москва "
}, headers={'Content-Type': 'application/json', 'trainer_token': token })'''

'''print(response_change_trainer.text)'''

response_add_pokemon = requests.post(f'{host}/pokemons', json={ "name": "Монти",
    "photo": "https://dolnikov.ru/pokemons/albums/037.png"}, headers={'Content-Type': 'application/json', 'trainer_token': token })

print(response_add_pokemon.text)