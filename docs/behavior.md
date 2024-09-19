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
    [*] --> PlayersTurn
    PlayersTurn --> EnemyTurn: Игрок сделал ход
    EnemyTurn --> PlayersTurn: Ход врага завершён
    PlayersTurn --> ShowInventory: Игрок открывает инвентарь
    ShowInventory --> PlayersTurn: Закрыть инвентарь
    PlayersTurn --> DropInventory: Игрок выбрал предмет для выброса
    DropInventory --> PlayersTurn: Предмет выброшен
    PlayersTurn --> PlayerDead: Игрок погиб
    EnemyTurn --> PlayerDead: Враг убивает игрока
