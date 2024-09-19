# Диаграммы состояний и последовательности

## Состояния игры (State Machine Diagram)

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


stateDiagram
    [*] --> Idle
    Idle --> Attack: Игрок в зоне видимости
    Attack --> MoveToPlayer: Игрок далеко
    MoveToPlayer --> Attack: Подошёл к игроку
    Attack --> Idle: Игрок вышел из зоны видимости
    Attack --> Dead: Враг погибает


stateDiagram
    [*] --> Closed
    Closed --> Open: Игрок открыл инвентарь
    Open --> UseItem: Использование предмета
    UseItem --> Open: Возврат к инвентарю
    Open --> DropItem: Выбрасывание предмета
    DropItem --> Open: Возврат к инвентарю
    Open --> Closed: Закрытие инвентаря


sequenceDiagram
    participant Player
    participant GameMap
    participant Enemy
    participant MessageLog

    Player->>GameMap: Проверяет наличие врага на клетке
    GameMap-->>Player: Возвращает врага
    Player->>Enemy: Атакует врага
    Enemy-->>Player: Получает урон
    Player->>MessageLog: Отправляет сообщение о нападении
    MessageLog-->>Player: Записывает сообщение
    Enemy->>Player: В ответ атакует (если жив)
    Player->>MessageLog: Сообщение о контратаке
