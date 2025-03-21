class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        cookbook = {recipe: i for i, recipe in enumerate(recipes)}
        supplies = set(supplies)
        res = []
        visited = set()
        def dfs(i: int) -> None:
            if i in visited:
                return
            visited.add(i)
            for item in ingredients[i]:
                if item not in supplies and item in cookbook:
                    dfs(cookbook[item])
                if item not in supplies:
                    break
            else:
                supplies.add(recipes[i])
                res.append(recipes[i])
        
        for i in range(len(recipes)):
            dfs(i)
        return res