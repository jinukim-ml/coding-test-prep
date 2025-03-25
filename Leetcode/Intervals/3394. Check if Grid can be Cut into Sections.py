class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        x_coords = []
        y_coords = []
        for start_x, start_y, end_x, end_y in rectangles:
            x_coords.append([start_x, end_x])
            y_coords.append([start_y, end_y])
        
        def is_possible(arr: list[int, int]) -> bool:
            arr.sort()
            maxval = arr[0][1]
            cuts = 0
            for start, end in arr:
                if maxval <= start:
                    cuts += 1
                if cuts == 2:
                    return True
                maxval = max(maxval, end)
            return False
        
        return is_possible(x_coords) or is_possible(y_coords)