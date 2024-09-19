# Объединённая диаграмма состояний и последовательности

## 1. Объединённая диаграмма состояний

```mermaid
stateDiagram
    [*] --> PlayersTurn
    PlayersTurn --> EnemyTurn: Игрок сделал ход
    EnemyTurn --> PlayersTurn: Ход врага завершён
    PlayersTurn --> ShowInventory: Игрок открывает инвентарь
    ShowInventory --> PlayersTurn: Закрыть инвентарь
    PlayersTurn --> DropInventory: Игрок выбрал предмет для выброса
    DropInventory --> PlayersTurn: Предмет выброшен
    PlayersTurn --> PlayerDead: Игрок погиб
    EnemyTurn --> PlayerDead: Враг убивает игрока
    
    state EnemyState {
        [*] --> Idle
        Idle --> Attack: Игрок в зоне видимости
        Attack --> MoveToPlayer: Игрок далеко
        MoveToPlayer --> Attack: Подошёл к игроку
        Attack --> Idle: Игрок вышел из зоны видимости
        Attack --> Dead: Враг погибает
    }
    
    state InventoryState {
        [*] --> Closed
        Closed --> Open: Игрок открыл инвентарь
        Open --> UseItem: Использование предмета
        UseItem --> Open: Возврат к инвентарю
        Open --> DropItem: Выбрасывание предмета
        DropItem --> Open: Возврат к инвентарю
        Open --> Closed: Закрытие инвентаря
    }

