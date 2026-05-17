class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, speed) for pos, speed in zip(position, speed)] #  [(0, 4), (2, 2), (4, 1)]
        cars.sort() # [(0, 4), (2, 2), (4, 1)]
        stack = [] # [96]
        for pos, speed in cars[::-1]: # pos = 0, speed = 4
            time = (target - pos) / speed # time = (100 - 0) / 4 = 100 / 4 = 25
            if stack and stack[-1] >= time: # 96 > 25
                continue
            stack.append(time)
        return len(stack)

        