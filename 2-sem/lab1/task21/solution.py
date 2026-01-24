"""
Задача 21: Игра в дурака
Жадный алгоритм для определения, можно ли отбить карты.
"""

def get_rank_value(rank):
    """Возвращает числовое значение ранга карты."""
    ranks = {'6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 
             'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return ranks[rank]

def can_beat(attacking_card, defending_card, trump):
    """
    Проверяет, может ли defending_card покрыть attacking_card.
    """
    att_rank, att_suit = attacking_card[0], attacking_card[1]
    def_rank, def_suit = defending_card[0], defending_card[1]
    
    # Если защищающая карта - козырь, а атакующая - нет
    if def_suit == trump and att_suit != trump:
        return True
    
    # Если обе карты козыри
    if def_suit == trump and att_suit == trump:
        return get_rank_value(def_rank) > get_rank_value(att_rank)
    
    # Если защищающая карта той же масти и старше
    if def_suit == att_suit:
        return get_rank_value(def_rank) > get_rank_value(att_rank)
    
    return False

def solve(n, m, trump, player_cards, attacking_cards):
    """
    Определяет, можно ли отбить все атакующие карты.
    """
    # Жадный алгоритм: для каждой атакующей карты выбираем
    # минимальную карту, которая может её покрыть
    
    used = [False] * n
    attacking = attacking_cards[:]
    
    # Сортируем атакующие карты по сложности отбития
    # (сначала некозырные, потом козыри)
    attacking_sorted = []
    for i, card in enumerate(attacking):
        rank, suit = card[0], card[1]
        is_trump = (suit == trump)
        attacking_sorted.append((is_trump, get_rank_value(rank), i, card))
    attacking_sorted.sort()
    
    # Пытаемся отбить каждую карту
    for is_trump, rank_val, orig_idx, att_card in attacking_sorted:
        found = False
        
        # Ищем минимальную карту, которая может покрыть
        best_def_idx = -1
        best_def_card = None
        
        for i in range(n):
            if used[i]:
                continue
            
            def_card = player_cards[i]
            if can_beat(att_card, def_card, trump):
                # Выбираем минимальную подходящую карту
                def_rank, def_suit = def_card[0], def_card[1]
                def_is_trump = (def_suit == trump)
                def_rank_val = get_rank_value(def_rank)
                
                if best_def_idx == -1:
                    best_def_idx = i
                    best_def_card = def_card
                else:
                    # Предпочитаем некозырные карты, если возможно
                    best_is_trump = (best_def_card[1] == trump)
                    if not def_is_trump and best_is_trump:
                        best_def_idx = i
                        best_def_card = def_card
                    elif def_is_trump == best_is_trump:
                        # Одинаковый тип, выбираем меньшую
                        if def_rank_val < get_rank_value(best_def_card[0]):
                            best_def_idx = i
                            best_def_card = def_card
        
        if best_def_idx != -1:
            used[best_def_idx] = True
            found = True
        
        if not found:
            return False
    
    return True

def main():
    # Чтение входных данных
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        first_line = lines[0].strip().split()
        n = int(first_line[0])
        m = int(first_line[1])
        trump = first_line[2]
        player_cards = lines[1].strip().split()
        attacking_cards = lines[2].strip().split()
    
    # Решение задачи
    result = solve(n, m, trump, player_cards, attacking_cards)
    
    # Запись результата
    with open('output.txt', 'w') as f:
        f.write('YES\n' if result else 'NO\n')
    
    # Вывод для отчета
    print(f"Input: n = {n}, m = {m}, trump = '{trump}'")
    print(f"Player cards: {player_cards}")
    print(f"Attacking cards: {attacking_cards}")
    print(f"Result: {'YES' if result else 'NO'}")

if __name__ == '__main__':
    main()
