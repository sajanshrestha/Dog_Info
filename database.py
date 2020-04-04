import sqlite3
import scrape

connector = sqlite3.connect('site.db')

cursor = connector.cursor()

try:
    cursor.execute('CREATE TABLE breeds (id INTEGER PRIMARY KEY, name VARCHAR(20), size VARCHAR(10), height VARCHAR(100), weight VARCHAR(100), coat VARCHAR(20), energy VARCHAR(100), activities TEXT)')
except:
    pass


def save_breeds():
    list_of_links = (scrape.get_all_links(f'{scrape.base_url}/dogs/dog-breeds?page={i}')
                     for i in range(16))

    for links in list_of_links:
        for link in links:
            dog_info = scrape.get_info(scrape.base_url + link)

            name = dog_info.get('name', None)
            size = dog_info.get('Size', None)
            height = dog_info.get('Height', None)
            weight = dog_info.get('Weight', None)
            coat = dog_info.get('Coat', None)
            energy = dog_info.get('Energy', None)
            activities = dog_info.get('Activities', None)

            cursor.execute('INSERT INTO breeds VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)',
                           (name, size, height, weight, coat, energy, activities))
            connector.commit()
    connector.close()
