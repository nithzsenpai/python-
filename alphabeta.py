def alpha_beta(node, depth, alpha, beta, maximizing_player, path):

    if isinstance(node, int):
        return node, path

    if maximizing_player:  
        value = float('-inf')
        best_path = None

        for i, child in enumerate(node):
            child_value, child_path = alpha_beta(
                child, depth + 1, alpha, beta, False, path + [i]
            )

            if child_value > value:
                value = child_value
                best_path = child_path

            alpha = max(alpha, value)

            if alpha >= beta:
                print(f"MAX (depth {depth}): alpha={alpha}, beta={beta}")
                break

        return value, best_path

    else:                  
        value = float('inf')
        best_path = None

        for i, child in enumerate(node):
            child_value, child_path = alpha_beta(
                child, depth + 1, alpha, beta, True, path + [i]
            )

            if child_value < value:
                value = child_value
                best_path = child_path

            beta = min(beta, value)

            if beta <= alpha:
                print(f"MIN (depth {depth}): alpha={alpha}, beta={beta}")
                break

        return value, best_path

tree = [
    [
        [  
            [10, 11],      
            [9, 12]      
        ],
        [  
            [14, 15],      
            [13, 14]        
        ],
    ],
    [  
        [  
            [5, 2],      
            [4, 1]
        ],
        [  
            [3, 22],    
            [20, 21]      
        ],
    ]
]

value, best_path = alpha_beta(tree, 0, float('-inf'), float('inf'), True, [])

print("\nFINAL MINIMAX VALUE AT ROOT =", value)
#print("BEST PATH FROM ROOT =", best_path)
