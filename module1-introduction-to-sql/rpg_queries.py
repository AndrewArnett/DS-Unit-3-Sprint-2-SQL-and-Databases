import sqlite3


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

TOTAL_CHARACTERS = 'SELECT * FROM charactercreator_character;'
TOTAL_CLERIC = 'SELECT * FROM charactercreator_cleric;'
TOTAL_FIGHTER = 'SELECT * FROM charactercreator_fighter;'
TOTAL_MAGE = 'SELECT * FROM charactercreator_mage;'
TOTAL_NECROMANCER = 'SELECT * FROM charactercreator_necromancer;'
TOTAL_THIEF = 'SELECT * FROM charactercreator_thief;'
TOTAL_ITEMS = 'SELECT * FROM armory_item;'
TOTAL_WEAPONS = 'SELECT * FROM armory_weapon;'
ITEM_PER_CHAR = """SELECT item_id FROM armory_item, 
charactercreator_character_inventory WHERE item_id = name and 
character_id BETWEEN 1 and 20;"""

if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()
    results = execute_query(curs, TOTAL_CHARACTERS)
    print("Total Characters:" + str(len(results)))
    results_cleric = execute_query(curs, TOTAL_CLERIC)
    print("Total Clerics:" + str(len(results_cleric)))
    results_fighter = execute_query(curs, TOTAL_FIGHTER)
    print("Total Fighters:" + str(len(results_fighter))) 
    results_mage = execute_query(curs, TOTAL_MAGE)
    print("Total Fighters:" + str(len(results_mage))) 
    results_necromancer = execute_query(curs, TOTAL_NECROMANCER)
    print("Total Fighters:" + str(len(results_necromancer))) 
    results_thief = execute_query(curs, TOTAL_THIEF)
    print("Total Fighters:" + str(len(results_thief)))
    results_items = execute_query(curs, TOTAL_ITEMS)
    print("Total Items:" + str(len(results_items)))
    results_weapons = execute_query(curs, TOTAL_WEAPONS)
    print("Amount of Items that are weapons:" + 
        str(len(results_weapons)) + ", 137 are not")
    results_item_per = execute_query(curs, ITEM_PER_CHAR)
   