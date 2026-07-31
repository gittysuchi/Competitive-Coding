def largestRectangleArea(heights):
    stack = []
    max_area = 0
    n = len(heights)

    for i in range(n + 1):
        current = 0 if i == n else heights[i]

        while stack and heights[stack[-1]] > current:
            h = heights[stack.pop()]

            if stack:
                width = i - stack[-1] - 1
            else:
                width = i

            area = h * width
            if area > max_area:
                max_area = area

        stack.append(i)

    return max_area

heights = list(map(int, input("Enter histogram heights: ").split()))
print("Largest Rectangle Area:", largestRectangleArea(heights))