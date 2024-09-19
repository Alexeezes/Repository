import pytest
import libtcodpy as libtcod
from components.fighter import Fighter
from components.inventory import Inventory
from entity import Entity
from map_objects.game_map import GameMap
from game_states import GameStates
from render_functions import RenderOrder
from game_messages import Message


# Фикстура для создания игрока
@pytest.fixture
def player():
    fighter_component = Fighter(hp=30, defense=2, power=5)
    inventory_component = Inventory(26)
    return Entity(0, 0, '@', libtcod.white, 'Player', blocks=True,
                  render_order=RenderOrder.ACTOR, fighter=fighter_component,
                  inventory=inventory_component)


# Фикстура для создания игровой карты
@pytest.fixture
def game_map():
    game_map = GameMap(80, 43)
    return game_map


# Фикстура для создания врага
@pytest.fixture
def enemy():
    fighter_component = Fighter(hp=10, defense=1, power=2)
    return Entity(1, 1, 'g', libtcod.desaturated_green, 'Goblin', blocks=True,
                  render_order=RenderOrder.ACTOR, fighter=fighter_component)


# Фикстура для создания предмета
@pytest.fixture
def item():
    return Entity(1, 1, '!', libtcod.violet, 'Healing Potion', item=True)


# Тест на передвижение игрока
def test_player_movement(player, game_map):
    initial_x = player.x
    initial_y = player.y

    # Симулируем движение игрока на одну клетку вправо
    dx, dy = 1, 0
    if not game_map.is_blocked(initial_x + dx, initial_y + dy):
        player.move(dx, dy)

    assert player.x == initial_x + dx
    assert player.y == initial_y + dy


# Тест на подбор предметов игроком
def test_pick_up_item(player, item):
    # Убеждаемся, что инвентарь пуст
    assert len(player.inventory.items) == 0

    # Помещаем игрока на ту же клетку, что и предмет
    item.x = player.x
    item.y = player.y

    # Симулируем подбор предмета
    pickup_results = player.inventory.add_item(item)

    # Проверяем, что предмет попал в инвентарь
    assert len(player.inventory.items) == 1
    assert item in player.inventory.items

    # Проверяем наличие сообщения
    message = pickup_results[0].get('message')
    assert isinstance(message, Message)
    assert 'picked up' in message.text


# Тест на атаку игроком врага
def test_player_attack(player, enemy):
    # Симулируем атаку игрока на врага
    attack_results = player.fighter.attack(enemy)

    # Проверяем, что атака привела к сообщению
    assert len(attack_results) > 0
    message = attack_results[0].get('message')
    assert isinstance(message, Message)
    assert 'attacks' in message.text

    # Проверяем, что здоровье врага уменьшилось
    assert enemy.fighter.hp < 10
