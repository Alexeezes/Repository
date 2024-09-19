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
