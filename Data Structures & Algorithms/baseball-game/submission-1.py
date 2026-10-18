class Solution:
    def calPoints(self, operations: List[str]) -> int:
        final_scores = []
        for op in operations:
            if op == '+':
                final_scores.append(final_scores[-1] + final_scores[-2])
            elif op == 'D':
                final_scores.append(final_scores[-1] * 2)
            elif op == 'C':
                final_scores.pop()
            else:
                final_scores.append(int(op))

        return sum(final_scores)        