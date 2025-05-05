MAX_PLAYER = 'X'
MIN_PLAYER = 'O'
EMPTY = ' '


class Move:
    def __init__(self, player, coord_row, coord_col):
        self.player = player
        self.coord_row = coord_row
        self.coord_col = coord_col
    
    def __str__(self):
        return "(player=%s, row=%d, column=%d)"% (self.player, self.coord_row, self.coord_col)


class Board:
    def __init__(self):
        self.grid = [[EMPTY for _ in range(3)] for _ in range(3)]
    
    def make_move(self, move):
        if self.is_valid_move(move):
            self.grid[move.coord_row][move.coord_col] = move.player
            return True
        return False
    
    def undo_move(self, move):
        self.grid[move.coord_row][move.coord_col] = EMPTY
    
    def is_valid_move(self, move):
        return (
            0 <= move.coord_row < 3 and 
            0 <= move.coord_col < 3 and 
            self.grid[move.coord_row][move.coord_col] == EMPTY
        )
    
    def get_valid_moves(self, player):
        valid_moves = []

        for i in range(3):
            for j in range(3):
                move = Move(player, i, j)
                if self.is_valid_move(move):
                    valid_moves.append(move)

        return valid_moves
    
    def is_full(self):
        return all(cell != EMPTY for row in self.grid for cell in row)
    
    def check_winner(self):
        lines = []
        lines.extend(self.grid)
        lines.extend([[self.grid[i][j] for i in range(3)] for j in range(3)])
        lines.append([self.grid[i][i] for i in range(3)])
        lines.append([self.grid[i][2 - i] for i in range(3)])
        
        for line in lines:
            if line[0] == line[1] == line[2] != EMPTY:
                return line[0]
        return None
    
    def game_over(self):
        return self.check_winner() is not None or self.is_full()
    
    def __str__(self):
        board_str = ""
        for row in self.grid:
            board_str += "|" + "|".join(row) + "|\n"
        return board_str


def evaluate_board(board: Board) -> int:
    winner = board.check_winner()
    if winner == MAX_PLAYER:  # 'X' 胜利
        return float('inf')   # 极大值（MAX玩家获胜）
    elif winner == MIN_PLAYER:  # 'O' 胜利
        return float('-inf')    # 极小值（MIN玩家获胜）
    elif board.is_full():       # 平局
        return 0

    # 初始化 X2, X1, O2, O1
    X2 = 0  # 恰好 2 个 X 且无 O 的线数
    X1 = 0  # 恰好 1 个 X 且无 O 的线数
    O2 = 0  # 恰好 2 个 O 且无 X 的线数
    O1 = 0  # 恰好 1 个 O 且无 X 的线数
 
    # 收集所有可能的线（3行 + 3列 + 2对角线）
    lines = []
    # 添加所有行
    for row in board.grid:
        lines.append(row)
    # 添加所有列
    for col in range(3):
        column = [board.grid[row][col] for row in range(3)]
        lines.append(column)
    # 添加两条对角线
    diag1 = [board.grid[i][i] for i in range(3)]
    diag2 = [board.grid[i][2 - i] for i in range(3)]
    lines.append(diag1)
    lines.append(diag2)

    # 遍历所有线，计算 X2, X1, O2, O1
    for line in lines:
        x_count = line.count(MAX_PLAYER)  # 'X' 的数量
        o_count = line.count(MIN_PLAYER)  # 'O' 的数量
        empty = line.count(EMPTY)         # 空格数量

        # 忽略既有 X 又有 O 的线（无法形成威胁）
        if x_count > 0 and o_count > 0:
            continue

        # 统计 X2, X1
        if x_count == 2 and empty == 1:
            X2 += 1
        elif x_count == 1 and empty == 2:
            X1 += 1

        # 统计 O2, O1
        if o_count == 2 and empty == 1:
            O2 += 1
        elif o_count == 1 and empty == 2:
            O1 += 1

    # 计算评估值
    evaluation = 3 * X2 + X1 - (3 * O2 + O1)
    return evaluation

    
def eval_minimax(board: Board, remaining_depth: int, is_maximizing_player: bool) -> int:
    # 达到深度限制或最终局时为base case 返回评估值（胜利回合将返回正无穷或负无穷）
    if remaining_depth == 0 or board.game_over():
        return evaluate_board(board)


    if is_maximizing_player:
        max_eval = float("-inf")
        for move in board.get_valid_moves(MAX_PLAYER):
            board.make_move(move)
            eval = eval_minimax(board, remaining_depth - 1, False)
            board.undo_move(move)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for move in board.get_valid_moves(MIN_PLAYER):
            board.make_move(move)
            eval = eval_minimax(board, remaining_depth - 1, True)
            board.undo_move(move)
            min_eval = min(min_eval, eval)
        return min_eval


def find_best_move(board: Board) -> Move:
    best_eval = float("-inf")
    best_move = None

    for move in board.get_valid_moves(MAX_PLAYER):
        board.make_move(move)  # 假设AI是Max玩家（"X"）
        eval = eval_minimax(board, remaining_depth=3, is_maximizing_player=False)  # 限制深度
        board.undo_move(move)
        if eval > best_eval:
            best_eval = eval
            best_move = move

    return best_move


def human_move(board: Board) -> Move:
    while True:
        try:
            row = int(input("输入行号 (0-2): "))
            col = int(input("输入列号 (0-2): "))
            move = Move(MIN_PLAYER, row, col)
            if board.is_valid_move(move):
                return move
            print("无效移动，请重试")
        except ValueError:
            print("请输入数字")

def play_game():
    board = Board()
    print("欢迎来到井字棋游戏!")
    print("选择先手:")
    print("1. 人类先手 (O)")
    print("2. AI先手 (X)")
    
    while True:
        choice = input("请输入选择 (1/2): ")
        if choice in ['1', '2']:
            human_first = (choice == '1')
            break
        print("无效输入")

    current_player = MIN_PLAYER if human_first else MAX_PLAYER
    
    while not board.game_over():
        print(board)
        if current_player == MIN_PLAYER:
            print("你的回合 (O)")
            move = human_move(board)
        else:
            print("AI思考中...")
            move = find_best_move(board)
        
        board.make_move(move)
        current_player = MAX_PLAYER if current_player == MIN_PLAYER else MIN_PLAYER
    
    print(board)
    winner = board.check_winner()
    if winner == MIN_PLAYER:
        print("恭喜你赢了!")
    elif winner == MAX_PLAYER:
        print("AI赢了!")
    else:
        print("平局!")

if __name__ == "__main__":
    play_game()