import numpy as np
import random
import pygame
from collections import deque

# 动作映射
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

ACTION_MAP = {
    UP: (0, -1),
    DOWN: (0, 1),
    LEFT: (-1, 0),
    RIGHT: (1, 0)
}

class SnakeGame:
    def __init__(self, grid_size=20, render_mode=False):
        self.grid_size = grid_size
        self.cell_size = 20
        self.width = self.grid_size * self.cell_size
        self.height = self.grid_size * self.cell_size
        self.render_mode = render_mode
        self.reset()

        if self.render_mode:
            pygame.init()
            pygame.font.init()
            self.font = pygame.font.SysFont('Arial', 14)
            self.window = pygame.display.set_mode((self.width, self.height))
            pygame.display.set_caption('RL Snake')

    def reset(self):
        self.snake = [(self.grid_size // 2, self.grid_size // 2)]
        self.direction = RIGHT
        self._place_food()
        self.done = False
        self.score = 0
        return self.get_observation()

    def step(self, action):
        if self.done:
            return -1.0, True

        self._update_direction(action)
        new_head = (
        self.snake[0][0] + ACTION_MAP[self.direction][0],
        self.snake[0][1] + ACTION_MAP[self.direction][1]
        )

  
        if self._is_collision(new_head):
            self.done = True
            return -1.0, True

        old_dist = abs(self.snake[0][0] - self.food[0]) + abs(self.snake[0][1] - self.food[1])
        self.snake.insert(0, new_head)
        new_dist = abs(new_head[0] - self.food[0]) + abs(new_head[1] - self.food[1])

        reward = 0.0

    
        if new_head == self.food:
            self.score += 1
            self._place_food()
            reward += 5.0
            return reward, False

    
        self.snake.pop()

    
        if new_dist < old_dist:
            reward += 0.1  
        else:
            reward -= 0.05  


        

    
        body_distances = [abs(new_head[0] - x) + abs(new_head[1] - y) for x, y in self.snake[1:]]
        if body_distances:
            min_body_dist = min(body_distances)
            reward += 0.01 * min_body_dist  

        return reward, False

    def _update_direction(self, action):
        if (action == UP and self.direction != DOWN):
            self.direction = UP
        elif (action == DOWN and self.direction != UP):
            self.direction = DOWN
        elif (action == LEFT and self.direction != RIGHT):
            self.direction = LEFT
        elif (action == RIGHT and self.direction != LEFT):
            self.direction = RIGHT

    def _place_food(self):
        empty = [(x, y) for x in range(self.grid_size) for y in range(self.grid_size)
                 if (x, y) not in self.snake]
        self.food = random.choice(empty)

    def _is_collision(self, pos):
        x, y = pos
        return (
            x < 0 or x >= self.grid_size or
            y < 0 or y >= self.grid_size or
            pos in self.snake
        )

    def get_observation(self):
        
        obs = []

    
        fx, fy = self.food
        hx, hy = self.snake[0]
        dx = (fx - hx) / self.grid_size
        dy = (fy - hy) / self.grid_size
        obs.extend([dx, dy])

    
        direction_map = {
        UP: [1, 0, 0, 0],
        DOWN: [0, 1, 0, 0],
        LEFT: [0, 0, 1, 0],
        RIGHT: [0, 0, 0, 1]
        }
        obs.extend(direction_map[self.direction])

    
        def danger_in_direction(direction):
            dx, dy = ACTION_MAP[direction]
            nx, ny = hx + dx, hy + dy
            return (
                nx < 0 or nx >= self.grid_size or
                ny < 0 or ny >= self.grid_size or
                (nx, ny) in self.snake
            )

    
        direction_order = {
            UP:    [LEFT, UP, RIGHT],
            DOWN:  [RIGHT, DOWN, LEFT],
            LEFT:  [DOWN, LEFT, UP],
            RIGHT: [UP, RIGHT, DOWN]
        }

        for dir in direction_order[self.direction]:
            obs.append(1.0 if danger_in_direction(dir) else 0.0)

       
        obs.append(len(self.snake) / (self.grid_size ** 2))

        obs.append(self._flood_fill_free_ratio(self.snake[0]))

        return np.array(obs, dtype=np.float32)
    def _flood_fill_free_ratio(self, start_pos):
        visited = set(self.snake)
        q = deque()
        q.append(start_pos)    
        reachable = 0

        while q:
            x, y = q.popleft()
            for dx, dy in ACTION_MAP.values():
                nx, ny = x + dx, y + dy
                if (0 <= nx < self.grid_size and
                    0 <= ny < self.grid_size and
                    (nx, ny) not in visited):
                    visited.add((nx, ny))
                    q.append((nx, ny))
                    reachable += 1

        total = self.grid_size * self.grid_size
        return reachable / total

    def render(self):
        if not self.render_mode:
            return

        self.window.fill((0, 0, 0))
        for x, y in self.snake:
            pygame.draw.rect(self.window, (0, 255, 0),
                             pygame.Rect(x * self.cell_size, y * self.cell_size,
                                         self.cell_size, self.cell_size))
        fx, fy = self.food
        pygame.draw.rect(self.window, (255, 0, 0),
                         pygame.Rect(fx * self.cell_size, fy * self.cell_size,
                                     self.cell_size, self.cell_size))
        score_text = self.font.render(f"Score: {len(self.snake)}", True, (200, 200, 200))
        text_rect = score_text.get_rect(topright=(self.width - 5, 5))
        self.window.blit(score_text, text_rect)
        pygame.display.flip()
    def close(self):
        if self.render_mode:
            pygame.quit()